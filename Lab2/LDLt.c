#include <stdio.h>
#include <stdlib.h>
#define n 3



void printMatrix(float matrix[][n]) {
	printf("--------- matrix--------\n");
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%f ", matrix[i][j]);
		}
		putchar('\n');
	}
}

int main(void) {
	float A[n][n] = { {3,2,1 }, {2,4,2}, {1,2,5} };
	float L[n][n] = { 0 };
	float D[n][n] = { 0 };

	printMatrix(A);
	float sum = 0;
	D[0][0] = A[0][0];
	//method LDLt factorization
	for (int j = 0; j < n; j++) {
		for (int i = j; i < n; i++) {
			sum = A[i][j];
			for (int k = 0; k < i; k++) {
				sum = sum - L[i][k] * L[j][k] * D[k][k];
			}
			if (i == j) {
				D[j][j] = sum;
				L[i][j] = 1;
			}
			else 
				L[i][j] = sum / D[j][j];

		}
	}
	printMatrix(L);
	printMatrix(D);

	


	return 0;
}