# Handling of sparse matrix
https://caam37830.github.io/book/02_linear_algebra/sparse_linalg.html
A matrix is called sparse only if the number of non-zero elements is equal to the number or rows or columns

Hence sparsity is defined as $s = \frac{no\;of\;non-zero\;elements}{total\;number\;of\;elements}$

## Storage of sparse matrix
Not much of a concern since at max the number of variables would be 30 which is 30*30 matrix (Let's say we have an upper bound)
### Methods
- Dictionary of keys
- List of lists
- Coordinate list
- Compressed sparse row (CSR, CRS or Yale format)

## Solving sparse matrix
### Conjugate gradient method
Positive definite matrix
Let's say for a system,
$Ax = b$
A is symmetric, positive definite ($x^TAx>0$) for all non-zero vectors in R, and real, b is known as well, we denote the unique solution of the following system as $x_{*}$
This method is not useful since our A can be non-symmetric

### Generalized minimal residual method
$Ax =b$
The matrix A is assumed to be invertible of the size m by m.
Furthermore it is assumed that b is normalized i.e. $||b|| = 1$.
The nth Krylov subspace for this problem is:
$K_n = K_n (A, r_0) = span\{r_0, Ar_0,A^2r_0, ..., A^{n-1}r_0$
Where $r_0 = b - Ax_0$ is the initial error given an initial guess such that $x_0 \ne 0$

GMRES approximates the exact solution of $Ax =b$ by the vector $x_n \in K_n$ that minimizes the euclidean norm of the residual $r_n = b-Ax_n$.
