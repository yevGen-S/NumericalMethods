#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#include<string.h>
#include <math.h>
#define n 10

#define eps 1e-10
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

void createRandomDiagonalPredominantMatrix(double A[n][n]){
    srand(time(NULL));

    double X;
    for(int i =0 ; i< n;i++){
        for(int j =0;j<n;j++){
            if(i==j){
               X = (double)rand()*100/(double)RAND_MAX+ 100;
               A[i][j] = X;
                continue;
            }
            A[i][j] = (float)rand()/((float)RAND_MAX/10);
        }
    }
}




void printVector(double matrix[n]) {
    printf("--------------------------\n");
    for (int i = 0; i < n; i++) {
        printf("%.16f\n", matrix[i]);
    }
}



void T(double L[n][n], double Lt[n][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Lt[i][j] = L[j][i];
        }
    }
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
    printf("successful reading of matrix");
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
    printf("successful reading of vector");
    return EXIT_SUCCESS;

}


// Getting norm of vector and matrix
double norm2Matrix(double matrix[n][n]){
    double norm2=0;
    for (int i =0 ;i<n; i ++){
        for(int j =0; j<n; j++){
            norm2 += matrix[i][j]*matrix[i][j];
        }
    }
    return sqrt(norm2);
}

double norm2Vector(double vector[n]){
    double norm2 = 0;
    for (int i =0; i < n; i ++) {
        norm2 += vector[i] * vector[i];
    }
    return sqrt(norm2);
}


double norm_oo_Vector(double vector[n]){
    double max = fabs(vector[0]);

    for (int i =0 ; i < n ; i++){
        if(fabs(vector[i])> max){
            max = fabs(vector[i]);
        }
    }
    return max;
}

double norm_oo_Matrix(double matrix[n][n]){
    double abs_sums[n]={0};
    for(int i =0 ;i< n;i++){
        for (int j =0;j <n; j++){
            abs_sums[i] += fabs(matrix[i][j]);
        }
    }
    double max = abs_sums[0];
    for (int i =0 ; i < n ; i++){
        if(abs_sums[i]>max){
            max = abs_sums[i];
        }
    }
    return max;
}

double getAlpha(double matrix[n][n]){
    return (norm_oo_Matrix(matrix) > 0 && norm_oo_Matrix(matrix) < 1)? norm_oo_Matrix(matrix) : 1;
}

double getUpperBoundOfAlpha(double A[n][n]){
    return 2 / norm_oo_Matrix(A);
}



char checktheDominanceOfDiagonalElements(double matrix[n][n]){
    double sum = 0;
    for(int i =0 ;i<n;i++){
        sum =0;
        for(int j = 0; j < n; j++){
            if( i ==j){
                continue;
            }
            sum += fabs(matrix[i][j]);
        }
        if(fabs(matrix[i][i])<sum){
            fprintf(stderr,"%s","Error, matrix doesn't have diagonal dominance");
            exit(0); // bad

        }
    }
    return 1; // good for us
}


void get_Cg(double C[n][n],double g[n],double A[n][n], double b[n]) {
    double alpha = getUpperBoundOfAlpha(A)/4;
//    double alpha = 1.0/101;
    printf("\nalpha = %f\n", alpha);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                C[i][j] = (1 - alpha * A[i][j]);
            }
            C[i][j] = -alpha * A[i][j];
            g[i] = alpha * b[i];
        }
    }
    double norm = norm_oo_Matrix(C);
    if(norm < 1){
        printf("||C|| = %lf\n", norm);
    }
    else
        perror("Violation of convergence conditions, find another alpha pls for getting fittable C matrix");
}



int fpi(double A[n][n],double b[n],double C[n][n], double g[n],double x0[n],double xk[n],double epsilon){
    int counter = 0;
    double checkX[n];
    double res;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                continue;
            }
            C[i][j] =  - A[i][j] / A[i][i];
            g[i] = b[i] / A[i][i];
        }

    }

    double C_norm = norm_oo_Matrix(C);
    printf("\n\nNorm of C matrix: %f\n\n", C_norm);
    if (C_norm >= 1){
        fprintf(stderr, "%s", "Error matrix C, method is not converege");
        exit(0);
    }

    while (1) {
        counter++;
        for (int i = 0; i < n; i++) {
            res = 0;
            for (int j = 0; j < n; j++) {
                res += C[i][j] * x0[j];
            }
            res += g[i];
            xk[i] = res;
        }
        for (int k = 0; k < n; k++) {
            checkX[k] = xk[k] - x0[k];
        }
        if (norm_oo_Vector(checkX) < ((1 - norm_oo_Matrix(C)) / norm_oo_Matrix(C) * epsilon)) {
            printf("vector X found\n");
            printVector(xk);
            printf("Number of iterations: %d\n\n", counter);

            return counter;
        }
        for (int i = 0; i < n; i++) {
            x0[i] = xk[i];
        }
    }
}

int error_of_iter_number(double A[n][n],double b[n],double C[n][n], double g[n],double x0[n],double xk[n],FILE* file ){
    int counter = 0;
    double checkX[n];
    double res;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                continue;
            }
            C[i][j] =  - A[i][j] / A[i][i];
            g[i] = b[i] / A[i][i];
        }

    }
    double C_norm = norm_oo_Matrix(C);
    printf("\n\nNorm of C matrix: %f\n\n", C_norm);
    if (C_norm >= 1){
        fprintf(stderr, "%s", "Error matrix C, method is not converege");
        exit(0);
    }
    while (1) {
        counter++;
        for (int i = 0; i < n; i++) {
            res = 0;
            for (int j = 0; j < n; j++) {
                res += C[i][j] * x0[j];
            }
            res += g[i];
            xk[i] = res;
        }
        for (int k = 0; k < n; k++) {
            checkX[k] = xk[k] - x0[k];
        }
        fprintf(file,"%.20lf;%i\n", norm_oo_Vector(checkX), counter);
        if (norm_oo_Vector(checkX) < ((1 - norm_oo_Matrix(C)) / norm_oo_Matrix(C) * eps)) {
            printf("vector X found\n");
            printVector(xk);
            printf("Number of iterations: %d", counter);

            return counter;
        }
        for (int i = 0; i < n; i++) {
            x0[i] = xk[i];
        }
    }
}


int iter_number_of_eps (double A[n][n],double b[n],double C[n][n], double g[n],double x0[n],double xk[n],double epsilon, FILE * file){
    int counter = 0;
    double checkX[n];
    double res;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                continue;
            }
            C[i][j] = - A[i][j] / A[i][i];
            g[i] = b[i] / A[i][i];
        }

    }
    double C_norm = norm_oo_Matrix(C);
    printf("\n\nNorm of C matrix: %f\n\n", C_norm);
    if (C_norm >= 1){
        fprintf(stderr, "%s", "Error matrix C, method doesn't converge");
        exit(0);
    }
    while (1) {
        counter++;
        for (int i = 0; i < n; i++) {
            res = 0;
            for (int j = 0; j < n; j++) {
                res += C[i][j] * x0[j];
            }
            res += g[i];
            xk[i] = res;
        }
        for (int k = 0; k < n; k++) {
            checkX[k] = xk[k] - x0[k];
        }
        if (norm_oo_Vector(checkX) < ((1 - norm_oo_Matrix(C)) / norm_oo_Matrix(C) * epsilon)) {
            printf("vector X found\n");
            printVector(xk);
            printf("Number of iterations: %d", counter);
            fprintf(file,"%.20lf;%i\n", epsilon, counter);
            return counter;

        }
        for (int i = 0; i < n; i++) {
            x0[i] = xk[i];
        }
    }
}

void copy_matrix(double matrix_where[n][n], double matrix_from[n][n]){
    for(int i=0;i<n; i++){
        for(int j =0;j<n;j++){
            matrix_where[i][j] = matrix_from[i][j];
        }
    }
}



int main(void) {
    double A[n][n] = {0};
    double b[n] = {0};
    double xk[n] = {0};
    double middle_calc[n] = {0};
//    FILE * A_file = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\A.csv","r");
//
//    if( A_file == NULL ){
//        perror("error of opening file");
//        exit(OPEN_FAILURE);
//    }
//
//    fileToMatrix(A,A_file);


    // matrix C and g for iteration process
    double C[n][n]={0};
    double g[n];

    //starting approximation

//    fpi(A,b,C,g,x0,xk);


//  error of iter number
//    FILE * file_err_of_iter = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\error_of_iter_number.txt","w");
//    if( file_err_of_iter == NULL){
//        fprintf(stderr, " %s"," Error of opening file");
//        exit(1);
//    }
//   error_of_iter_number(A, b, C, g, x0,xk, file_err_of_iter);


//  number of iterations of eps
//    FILE * file_iter_of_eps = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\iter_of_eps.txt","w+");
//    if( file_iter_of_eps == NULL) {
//        fprintf(stderr, " %s"," Error of opening file");
//        exit(1);
//    }
//    double epsilon = 1e-0;
//    for(int i = 0; i < 15; i++){
//
//        for (int k =0 ; k<n ;k++){
//            xk[k] = 0;
//            x0[k] = b[k] / A[k][k];
//        }
//        iter_number_of_eps(A,b,C,g,x0,xk,epsilon,file_iter_of_eps );
//        epsilon = epsilon/10.0;
//    }

    double x0[n] ;

//  number of iterations of eps with different cond number
    FILE * results = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results.txt","a");
    FILE * file_with_matrices_with_cond = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\matrix_with_cond.txt" ,"r");
    FILE* results2 = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results2.txt","a");
    fileToMatrix(A,file_with_matrices_with_cond);

    printMatrix(A);
    double epsilon = 1e-1;
    for(int i = 0; i < 15; i++){
        double B[n] = {0};
        for(int k = 0 ;k < n ;k++){
            for (int j =0;j<n; j++){
                B[k] += A[k][j];
            }
        }
        for (int k =0 ; k < n ;k++){
            x0[k] = b[k] / A[k][k];
        }
        iter_number_of_eps(A,B,C,g,x0,xk,epsilon,results );
        epsilon = epsilon / 10.0;
    }

    fclose(results);
    fclose(results2);



//  number of iterations of cond number
//    FILE* file_iter_of_cond = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\src\\iters_of_cond.csv", "r");
//    FILE * file_iter_of_cond_res = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\src\\iters_of_cond_res.txt","a");
//    int iter;
//
//    for (int i =0; i < 15; i++){
//        double B[n] = {0};
//        fileToMatrix(A,file_iter_of_cond);
//        for(int k = 0 ;k < n ;k++){
//            for (int j =0;j<n; j++){
//                B[k] += A[k][j];
//            }
//        }
//        printMatrix(A);
//        for (int k =0 ; k < n ;k++){
//            x0[k] = B[k] / A[k][k];
//        }
//        iter = fpi(A,B,C,g,x0,xk,1e-14);
//        if ( i == 14){
//            fprintf(file_iter_of_cond_res,"%i\n",iter);
//            return 0;
//        }
//        fprintf(file_iter_of_cond_res,"%i;",iter);
//
//    }
//
//
//
//
//
//
//
//    fclose(file_iter_of_cond);
    return 0;
}



