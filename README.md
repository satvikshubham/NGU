# Ipopt (Interior Point OPTimizer)
## Overview
It is an open source software package for large-scale non-linear optimization. It can be used to solve general nonlinear programming problems of the form:
<br>
$min_{x \in R^n} f(x)$
<br>
Such that

$g^L \leq g(x) \leq g^U$
and
$x^L \leq x \leq x^U$
Where $x\in R^n$ are the optimization variables possibly with lower and upper bounds, $x^L \in (R \; U \; \{-\infty \})^n$ and $x^U \in (R \; U \; \{+\infty \})^n$ 
With $x^L \leq x^U$, $ f:R^𝑛→R$ is the objective function, and 𝑔:ℝ𝑛→ℝ𝑚 are the general nonlinear constraints. 
The functions $𝑓(𝑥)$ and $𝑔(𝑥)$ can be linear or nonlinear and convex or non-convex (but should be twice continuously differentiable). 
The constraint functions, $𝑔(𝑥)$, have lower and upper bounds, $g^L \in (R \; U \; \{-\infty \})^m$ and $g^U \in (R \; U \; \{+\infty \})^m$  with $g^L \leq g^U$.

It is designed to exploit 1st and 2nd Hessian transformations, if provided otherwise it approximates using quasi-Newton methods, specifically a [BFGS update](https://en.wikipedia.org/wiki/Broyden–Fletcher–Goldfarb–Shanno_algorithm)

## Availability

The Ipopt package is available from COIN-OR under the EPL (Eclipse Public License) open-source license and includes the source code for Ipopt. This means, it is available free of charge, also for commercial purposes. 

## How to use
Requirements are:
- Gekko
- Sympy
### Setup
Install requirements 
```
pip install -r requirements.txt
```
Write your equations in _Equations.txt file and execute the code_runner.py file.

To execute code runner file
```
python code_runner.py
```
You can expect the answer now in _Answer.txt file.
## References
[Github - Ipopt](https://coin-or.github.io/Ipopt/)  
[Gekko library](https://gekko.readthedocs.io)