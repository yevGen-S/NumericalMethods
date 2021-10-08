#include <stdio.h>
#include <stdlib.h>
#define n 3
#define swap(a, b){double tmp = a; a = b; b = tmp; }


void printMatrix(double matrix[n][n]) {
	printf(" ------------------\n");
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%f ", matrix[i][j]);
		}
		putchar('\n');
	}
}

void printVector(double matrix[n]) {
	printf("--------------------------\n");
	for (int i = 0; i < n; i++) {
		printf("%f\n", matrix[i]);
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
			}
			else
				L[i][j] = sum / D[j][j];
		}
	}

}


void ldltSolve(double  L[n][n],double D[n][n],double Lt[n][n], double B[n], double X[n]) {
	double z[n];
	double y[n];
	// Lz=B
	for (int i = 0; i < n; i++) {
		double alpha = B[i];
		for (int j = 0; j < i; j++)
			alpha -= L[i][j] * z[j];
		z[i] = alpha / L[i][i];
	}
	printVector(z);
	// Dy=z
	for (int i = 0; i < n; i++) {
		y[i] = z[i] / D[i][i];
	}
	printVector(y);
	// Ltz = x
	for (int i = n - 1; i >= 0; i--) {
		double alpha =y[i];
		for (int j = n - 1; j > i; j--)
			alpha -= Lt[i][j] * X[j];
		X[i] = alpha / Lt[i][i];
	}
	printVector(X);
}


int main(void) {
	double A[n][n] = { {3,2,1 }, {2,4,2}, {1,2,5} };
	double L[n][n] = { 0 };
	double D[n][n] = { 0 };
	double Lt[n][n];
	double b[n] = { 5, 1, 2 };
	double x[n];
	printMatrix(A);
	//solving ldlt

	printVector(b);
	ld(A, L, D);
	T(L, Lt);
	printMatrix(Lt);
	ldltSolve(L, D,Lt, b, x);
	printVector(x);


	return 0;
}