#include <cstdlib>
#include <ctime>
#include <iostream>
#include "../../../ext_libs/Eigen/Sparse"
using namespace Eigen;

using namespace std;

long double compute_sparse_cost(long double a_sparsity, long double b_sparsity, long double c_sparsity, int a_rows, int b_rows, int b_cols) {

    long double tempA = a_sparsity * ((long double)(a_rows + b_rows));
    long double tempB = (((long double) a_rows * b_rows) * a_sparsity * b_cols) * b_sparsity;
    long double tempC = ((long double)(a_rows * b_cols)) * c_sparsity;

    return tempA + tempB + tempC;
}

long double compute_sparsity(long double a_sparsity, long double b_sparsity, int common_dim) {
//    cout << "\t\t" << a_sparsity << ", " << b_sparsity << " = " << (1 - pow(1 - a_sparsity * b_sparsity, common_dim)) << endl;
    return (1 - pow(1 - a_sparsity * b_sparsity, common_dim));
}

long double fRand(double fMin, double fMax)
{
    long double f = (long double)rand() / RAND_MAX;
    return fMin + f * (fMax - fMin);
}

long double getSparsity(long double nnz, int rows, int cols) {
    return (nnz / ((long double) cols * rows));
}

main() {

    srand((unsigned)time(0));

    int i, a_rows, a_cols_b_rows, b_cols;
    long double res_sparsity, a_sparsity, b_sparsity;

    for (i =0; i<10000; i++) {
        a_rows = (rand() % 100000) + 1000;
        a_cols_b_rows = (rand() % 100000) + 1000;
        b_cols = (rand() % 100000) + 1000;

        a_sparsity = fRand(0.0000, 0.1);
        b_sparsity = fRand(0.0000, 0.1);

        long double nnzA = ((long double)a_rows * a_cols_b_rows) * a_sparsity / 100.0;
        std::vector<Triplet<int>> tripletList;
        // cout << nnzA << endl;
        tripletList.reserve(nnzA);


        for (long double j=0; j<nnzA; j++){
            int row = (rand() % a_rows);
            int col = (rand() % a_cols_b_rows);

            tripletList.push_back(Triplet<int>(row, col, rand()));
        }

        SparseMatrix<int> *A = new SparseMatrix<int>(a_rows, a_cols_b_rows);
        A->setFromTriplets(tripletList.begin(), tripletList.end());

        long double nnzB =  ((long double)a_cols_b_rows * b_cols) * b_sparsity / 100.0;
        std::vector<Triplet<int>> tripletListB;
        //cout << nnzB << endl;
        tripletList.reserve(nnzB);

        for (int j=0; j<nnzB; j++){
            int row = (rand() % a_cols_b_rows);
            int col = (rand() % b_cols);

            tripletListB.push_back(Triplet<int>(row, col, rand()));
        }

        SparseMatrix<int> *B = new SparseMatrix<int>(a_cols_b_rows, b_cols);
        B->setFromTriplets(tripletListB.begin(), tripletListB.end());

        clock_t begin = clock();

        SparseMatrix<int> C = (*A) * (*B);
        double cur_time = double(clock() - begin) / CLOCKS_PER_SEC;

        a_sparsity = A->nonZeros() / ((long double) A->cols() * A->rows());

        b_sparsity = B->nonZeros() / ((long double) B->cols() * B->rows());

        long double c_sparsity = compute_sparsity(a_sparsity, b_sparsity, a_cols_b_rows);
        long double tempA = (a_sparsity * (long double)a_rows) * (long double)a_cols_b_rows;

        long double tempB = (((long double) a_rows * a_sparsity ) * (long double)a_cols_b_rows) * ((long double)b_cols * b_sparsity);

        long double tempC = (((long double)a_rows * c_sparsity)) * (long double) b_cols;

        cout << tempA << "\t" << tempB << "\t" << tempC << "\t" << cur_time << endl;
    }

}
