//    get_Cg(C,g,A,b);
//    printf("matrix C\n");
//    printMatrix(C);
//    printf("vector g\n");
//    printVector(g);
//    printf("starting approximation\n");
//    printVector(x0);
//    while(1) {
//        counter++;
//        for(int i = 0; i < n; i++){
//            res = 0;
//            for(int j = 0; j < n; j++){
//                res += C[i][j] * x0[j];
//            }
//            res += g[i];
//            xk[i] = res;
//        }
//        printf("iteration  = %i",counter);
//        printVector(xk);
//        for ( int k = 0; k < n; k++){
//            checkX[k] = xk[k] - x0[k];
//        }
//
//        if(norm_oo_Vector(checkX) < ((1 - norm_oo_Matrix(C))/ norm_oo_Matrix(C) * eps)){
//            printf("vector X found\n");
//            printVector(xk);
//            printf("Number of iterations: %d", counter);
//            return counter;
//        }
//        for(int i =0 ; i < n ; i++){
//            x0[i] = xk[i];
//        }
//    }