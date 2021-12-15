#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#pragma warning(disable : 4996)

#define eps1 1e-10
#define DIMENSION 10



void printMatrix(double** A, int N, int M)
{
    printf("\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            printf("%*.5lf ", 6, A[i][j]);
        }
        printf("\n");
    }
}

// creates n x m matrix
double** createMatrix(int n) { // c is length of column, r is length of row
    double** A = (double**)malloc(n * sizeof(double*));
    for (int i = 0; i < n; i++) {
        A[i] = (double*)malloc(n * sizeof(double));
    }
    return A;
}

double* createVector(int c) {
    return (double*)malloc(c * sizeof(double));
}

double** readMatrix(FILE* file, int rang) {
    double** matrix = createMatrix(rang);
    for (int i = 0; i < rang; i++) {
        for (int j = 0; j < rang; j++) {
            fscanf(file, "%lf; ", &matrix[i][j]);
        }
    }
    return matrix;
}

void freeMatrix(double** A, int n) { // there's n for sure
    for (int i = 0; i < n; i++) {
        free(A[i]);
    }
    free(A);
}

double** T(double** a, int n) { // transpose matrix
    double** a_t = createMatrix(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            a_t[j][i] = a[i][j];
        }
    }
    return a_t;
}

double** create_E(int n) {
    double** A = (double**)malloc(sizeof(double*)* n);
    for(int i =0; i < n; i++) {
        A[i] = (double*)calloc(n,sizeof(double));
        A[i][i] =1 ;
    }
    return A;
}


double vectorNorm_2(double* A, int n) {
    double norm = 0;
    for (int i = 0; i < n; i++) {
        norm += A[i] * A[i];
    }
    return sqrt(norm);
}



double** multiplyMatrix(int n, double** H, double** A) {
    double** A1 = createMatrix(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            A1[i][j] = 0;
            for (int k = 0; k <n; k++) {
                A1[i][j] += H[i][k] * A[k][j];
            }
        }
    }
    return A1;
}


double** hessenberg(double** A, int n) {
    double** B = A;
    double summa;
    double s ;
    int sign;
    double m;
    for (int i = 0; i < n - 2; i++) {
        summa = 0;

        for (int j = i+1;j<n;j++) {
            summa += B[j][i] * B[j][i];
        }
        if(-B[i + 1][i] > 0){
            sign = 1;
        }
        else{
            sign = -1;
        }
        s = sign * sqrt(summa);

        m = 1 / sqrt(2 * s * (s - B[i + 1][i]));

        double* w = createVector(n);
        for (int j = 0; j < n; j++) {
            if (j < i) {
                w[j] = 0;
            }
        }

        w[i+1] = m * (B[i+1][i] - s);

        for (int p = i + 2; p< n; p++) {
            w[p] = m * B[p][i];
        }

        double** P = create_E(n);
        for (int v = 0; v < n; v++) {
            for (int k = 0; k < n; k++) {
                P[v][k] -= 2 * w[v] * w[k];
            }
        }

        B = multiplyMatrix(n, P, B);
        B = multiplyMatrix(n, B, P);

        }
    return B;
}






void givens(double** B, double*** Q, double*** R, int n) {
    double t;
    double cos;
    double sin;
    for (int j = 0; j < n - 1; j++) {
        t = B[j][j] / B[j + 1][j];
        cos = 1 / sqrt(1 + t * t);
        sin = t * cos;
        double** G = create_E(n);
        G[j][j] = sin;
        G[j + 1][j] = -cos;
        G[j + 1][j + 1] = sin;
        G[j][j + 1] = cos;
        B = multiplyMatrix(n, G, B);
        if (j == 0) {
            (*Q) = T(G,n);
        }
        else {
            double** G_t = T(G, n);
            double** Q1 = multiplyMatrix(n, (*Q), G_t);
            freeMatrix((*Q), n);
            freeMatrix(G_t, n);
            freeMatrix(G, n);
            (*Q) = Q1;
        }
    }
    (*R) = B;
}


double find_max_underdiagonal_element(double** matrix, int n ) {
    double max =0;
    for(int j =0;j < (n-1); j++){
        for(int i =(j+1) ;  i< n ; i++){
            if(fabs(matrix[i][j]>max))
                max = fabs(matrix[i][j]);
        }
    }
    return max;
}

char stop_criteria(double** matrix,int n, double eps) {
    if (find_max_underdiagonal_element(matrix,n) < eps)
        return 1;
    return 0;
}



double* qr(double** A, int n, double eps) {
    double** Q = createMatrix(n);
    double** R = createMatrix(n);
    double** A1;
    int iter = 0;
    double** B = hessenberg(A, n);
    do {
        givens(B, &Q, &R, n);
        A1 = multiplyMatrix(n, R, Q);
        B = A1;
        iter++;
    } while (!stop_criteria(B, n, eps));
    FILE* file_iter = fopen("iterations.csv", "a");
    fprintf(file_iter, "%i;", iter);
    fclose(file_iter);

    double* solution = (double*)malloc(n * sizeof(double));
    for (int i = 0; i < n; i++) {
        solution[i] = B[i][i];
    }
    printf("number of iters qr with no shift: %i", iter);
    printf("\n");
    return solution;
}

void matrix_defference(double*** matrix1, double** matrix2,int n ){
    for (int i = 0; i < n; i++){
        (* matrix1)[i][i] -= matrix2[i][i];
    }
}
void matrix_sum (double*** matrix1, double** matrix2, int n){
    for (int i = 0; i < n; i++){
        (* matrix1)[i][i] += matrix2[i][i];
    }
}

double* qr_shift(double** A, int n, double eps) {
    double** Q = createMatrix(n);
    double** R = createMatrix(n);
    double** A1;
    int iter = 0;
    double** B = hessenberg(A, n);

    do {
        double** E = create_E(n);
        for(int i=0;i<n;i++){
            E[i][i] = B[n-1][n-1];
        }
        matrix_defference(&B,E,n);
        givens(B, &Q, &R, n);
        A1 = multiplyMatrix(n, R, Q);
        B = A1;
        matrix_sum(&B,E,n);
        iter++;
    } while (!stop_criteria(B, n, eps));
    FILE* file_iter = fopen("iterations.csv", "a");
    fprintf(file_iter, "%i;", iter);
    fclose(file_iter);

    double* solution = (double*)malloc(n * sizeof(double));
    for (int i = 0; i < n; i++) {
        solution[i] = B[i][i];
    }
    printf("number of iters qr with shift: %i", iter);
    printf("\n");
    return solution;
}


int fileToMatrix(double*** A, FILE* file, int n) {
    char* token;
    double number;
    char row[300];
    for(int i =0 ; i < n; i++){
        fgets(row,sizeof(row),file);
        token = strtok(row,";");
        for(int j = 0; j < n; j++){
            number = atof(token);
            (*A)[i][j] = number;
            token =  strtok(NULL,";");
        }
    }
    fgets(row,sizeof(row),file);
    printf("successful reading of matrix");
    return EXIT_SUCCESS;

}

int main(void) {


    double** m = createMatrix(DIMENSION);
    FILE* file = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab4\\src\\graphics\\matrix.csv", "r");
    fileToMatrix(&m,file,DIMENSION);
    double** m2 = m;


    printMatrix(m, DIMENSION, DIMENSION);
    double* solution = qr(m2, DIMENSION , eps1);
    for(int i=0;i<DIMENSION;i++){
        printf("%lf ",solution[i]);
    }

    double* solution2 = qr_shift(m, DIMENSION , eps1);
    for(int i=0;i<DIMENSION;i++){
        printf("%lf ",solution2[i]);
    }


}