#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#include<string.h>
#include <windows.h>
#include <math.h>
#define n 10



#define eps 1e-10
#define swap(a, b){double tmp = a; a = b; b = tmp; }
typedef enum ERROR_t{
    OPEN_FAILURE,
}error;


#define INIT_TIMER \
    LARGE_INTEGER frequency; \
    LARGE_INTEGER start,end; \
    double result; \
    QueryPerformanceFrequency(&frequency);

#define TIMER_START QueryPerformanceCounter(&start);

#define TIMER_STOP \
    QueryPerformanceCounter(&end); \
    result =(float)(end.QuadPart-start.QuadPart)/frequency.QuadPart; \




int dimension;









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


void T(double L[n][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            L[i][j] = L[j][i];
        }
    }
}


void ld(double A[n][n],double L[n][n],double D[n]) {// LDLt factorization
    double sum;
    for (int j = 0; j < n; j++) {
        for (int i = j; i < n; i++) {
            sum = A[i][j];
            for (int k = 0; k < i; k++) {
                sum -= L[i][k] * L[j][k] * D[k];
            }
            if (i == j) {
                D[j] = sum;
                L[i][j] = 1;
            } else
                L[i][j] = sum / D[j];
        }
    }
}


void ldltSolve(double A[n][n], double B[n], double X[n]) {
    double L[n][n] = { 0 };
    double D[n] = { 0 };
    ld(A, L, D);

    double z[n];
    double y[n];
    // Lz=B
    for (int i = 0; i < n; i++) {
        double sum = B[i];
        for (int j = 0; j < i; j++)
            sum -= L[i][j] * z[j];
        z[i] = sum / L[i][i];
    }
    // Dy=z
    for (int i = 0; i < n; i++) {
        y[i] = z[i] / D[i];
    }
    // Ltz = x
    T(L);
    for (int i = n - 1; i >= 0; i--) {
        double sum =y[i];
        for (int j = n - 1; j > i; j--)
            sum -= L[i][j] * X[j];
        X[i] = sum / L[i][i];
    }
    printf("-----------X   from ldlt Method");
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


int fileToMatrix(double A[][n],FILE* file) {
    char* token;
    double number;
    char row[300];
    for(int i =0 ; i < n; i++){
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
    checktheDominanceOfDiagonalElements(A);
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
            printf("vector X found from fpi\n");
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

    double xk_fpi[n] = {0};
    double xk_ldlt[n] = {0};

    double x0[n] ;
    double middle_calc[n] = {0};
    double C[n][n]={0};
    double g[n];


//    FILE * A_file = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\A.csv","r");
//    if( A_file == NULL ){
//        perror("error of opening file");
//        exit(OPEN_FAILURE);
//    }
//    fileToMatrix(A,A_file);
    // matrix C and g for iteration process
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







//  number of iterations of eps with different cond number
//    FILE * results = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results.txt","a");
//    FILE * file_with_matrices_with_cond = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\matrix_with_cond.txt" ,"r");
//    FILE* results2 = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\results2.txt","a");
//    fileToMatrix(A,file_with_matrices_with_cond);
//
//    printMatrix(A);
//    double epsilon = 1e-1;
//    for(int i = 0; i < 15; i++){
//        double B[n] = {0};
//        for(int k = 0 ;k < n ;k++){
//            for (int j =0;j<n; j++){
//                B[k] += A[k][j];
//            }
//        }
//        for (int k =0 ; k < n ;k++){
//            x0[k] = b[k] / A[k][k];
//        }
//        iter_number_of_eps(A,B,C,g,x0,xk,epsilon,results );
//        epsilon = epsilon / 10.0;
//    }
//
//    fclose(results);
//    fclose(results2);






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
//    fclose(file_iter_of_cond);







    /*** Comparing direct and iterative methods  **/



//    FILE * file_matrix_with_cond = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\src\\iters_of_cond2.csv", "r");
//    FILE* file_compare_direct = fopen("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\src\\comparing_direct.txt","w");
//    FILE* file_compare_iterative = fopen ("D:\\Coding\\NumericalMethods\\NumericalMethods\\Lab3\\src\\comparing_iterative.txt","w" );
//
//    if( file_matrix_with_cond == NULL || file_compare_direct==NULL || file_compare_iterative == NULL){
//        fprintf(stderr,"%s","error of opening file" );
//        exit(OPEN_FAILURE);
//    }
//    double x_exact = 1.000000000000 ;
//    double new_eps;
//    INIT_TIMER
//    double sum =0;
//    for (int i =0 ; i < 10 ; i++){
//        fileToMatrix(A,file_matrix_with_cond);
//        printMatrix(A);
//        double B[n]= {0};
//        for (int j =0 ; j < n ; j++ ){
//            for (int k =0 ; k< n; k++){
//                B[j] += A[j][k];
//            }
//        }
//        for (int j = 0 ; j < n ; j++){
//            x0[j] = b[j]/A[j][j];
//            xk_fpi[j] = 0;
//            xk_ldlt[j] = 0;
//        }
//        TIMER_START
//            ldltSolve(A,B,xk_ldlt);
//
//        sum =0;
//        for(int j =0;j<n;j++){
//            sum +=xk_ldlt[j];
//        }
//        new_eps = fabs(sum/n - x_exact);
////        double degree =0;
////        while (new_eps < 1) {
////            degree++;
////            new_eps *= 10;
////        }
////        new_eps = pow(10,-degree);
//
//        printf("eps_from_f : %.20lf\n", new_eps);
//        fprintf(file_compare_direct,"%.20lf;", result);
//
//
//        TIMER_START
//            fpi(A,B,C,g,x0,xk_fpi,new_eps);
//        TIMER_STOP
//        fprintf(file_compare_iterative,"%.20lf;", result);
//
//    }





    return 0;
}



