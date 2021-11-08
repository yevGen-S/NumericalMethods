#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#include<string.h>
#define n 10
#define swap(a, b){double tmp = a; a = b; b = tmp; }
typedef enum ERROR_t{
    OPEN_FAILURE,
}error;

void printMatrix(double matrix[n][n]) {
    printf(" ------------------\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%.16f ", matrix[i][j]);
        }
        putchar('\n');
    }
}


void printVector(double matrix[n]) {
    printf("--------------------------\n");
    for (int i = 0; i < n; i++) {
        printf("%.10f\n", matrix[i]);
    }
}


//transporance of matrix
//void T(double matrix[][n]) {
//	for (int j = 0; j < n; j++) {
//		for (int i = 0; i <= j; i++) {
//			if (i == j) {
//				continue;
//			}
//			swap(matrix[i][j], matrix[j][i]);
//		}
//	}
//}


void T(double L[n][n], double Lt[n][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Lt[i][j] = L[j][i];
        }
    }
}


void ld(double A[n][n],double L[n][n],double D[n][n]) {// LDLt factorization
    double sum;
    for (int j = 0; j < n; j++) {
        for (int i = j; i < n; i++) {
            sum = A[i][j];
            for (int k = 0; k < i; k++) {
                sum -= L[i][k] * L[j][k] * D[k][k];
            }
            if (i == j) {
                D[j][j] = sum;
                L[i][j] = 1;
            } else
                L[i][j] = sum / D[j][j];
        }
    }
}


void ldltSolve(double A[n][n], double B[n], double X[n]) {
    double L[n][n] = { 0 };
    double D[n][n] = { 0 };
    double Lt[n][n];
    ld(A, L, D);
    T(L, Lt);
    double z[n];
    double y[n];
    // Lz=B
    for (int i = 0; i < n; i++) {
        double sum = B[i];
        for (int j = 0; j < i; j++)
            sum -= L[i][j] * z[j];
        z[i] = sum / L[i][i];
    }
    printVector(z);
    // Dy=z
    for (int i = 0; i < n; i++) {
        y[i] = z[i] / D[i][i];
    }
    printVector(y);
    // Ltz = x
    for (int i = n - 1; i >= 0; i--) {
        double sum =y[i];
        for (int j = n - 1; j > i; j--)
            sum -= Lt[i][j] * X[j];
        X[i] = sum / Lt[i][i];
    }
    printf("-----------X");
    printVector(X);
}


void random_symetric_matrix(double matrix[n][n]) {
    double X = ((double)rand() / (double)RAND_MAX);
    // create random matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            X = (double)rand()*100/(double)RAND_MAX;
            matrix[i][j] = X;
        }
    }
    // symetric matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            matrix[j][i] = matrix[i][j];
        }
    }
}


int fileToMatrix(double A[][n],FILE* file){
    char* token;
    double number;
    char row[300];
    for(int i =0 ; i<n;i++){
        fgets(row,sizeof(row),file);
        token = strtok(row,";");
        for(int j = 0; j < n; j++){
            number = atof(token);
            A[i][j] = number;
            token =  strtok(NULL,";");
        }
    }
    fgets(row,sizeof(row),file);
    printf("success");
    return EXIT_SUCCESS;

}


int fileToVector(double b[n], FILE* file){
    char* token;
    double number;
    char row[300];
    fgets(row,sizeof(row),file);
    token = strtok(row,";");
    for(int j = 0; j < n; j++){
        number = atof(token);
        b[j] = number;
        token =  strtok(NULL,";");

    }
    fgets(row,sizeof(row),file);
    printf("success");
    return EXIT_SUCCESS;

}





int main(void) {
    //write to file
    FILE* list_of_A  = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab2\\A.csv","r");
    FILE* list_of_b = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab2\\b.csv", "r");
    if (list_of_A == NULL|| list_of_b == NULL) {
        perror("error of opening file");
        exit(OPEN_FAILURE);
    }

    double A[n][n];
    double b[n] ;
    double x[n];

    FILE* X = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab2\\Xv2.csv", "w");
    if (X == NULL){
        perror("error of opening file");
        exit(OPEN_FAILURE);
    }

    for (int i = 0; i < 16; i++){
        fileToMatrix(A,list_of_A);
        printMatrix(A);
        fileToVector(b,list_of_b);
        ldltSolve(A, b, x);
        for(int k = 0; k < n; k++){
            fprintf(X,"%.16lf;",x[k]);
        }
        fprintf(X,"\n");
    }

    fclose(list_of_A);
    fclose(list_of_b);


    return 0;
}