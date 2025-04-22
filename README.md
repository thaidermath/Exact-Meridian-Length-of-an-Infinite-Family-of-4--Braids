# Exact-Meridian-Length-of-an-Infinite-Family-of-4--Braids

This repository examines the meridian length of an infinite family of two-component alternating links. We utilize the diagram and its symmetries to derive an exact formula for calculating the meridian length. Our approach is based on the algorithm developed by Thistlethwaite and Tsvietkova.

---


## Background
The hyperbolic structure of alternating links can be derived directly from their diagrams, thanks to an algorithm developed by Thistlethwaite and Tsvietkova [[1]]. Flint later extended this framework to fully augmented links (FALs), proving that they also possess suitable diagrams [[2]]. More recently, Kwon, Park, and Tham generalized the algorithm to links in the thickened torus [[3]].

In this discussion, we will focus exclusively on alternating links in the 3-sphere. The algorithm allows for the extraction of other 3-manifold invariants, such as the invariant trace field, as discussed by Neumann, Tsvietkova, and later by Flint.

While tools like SnapPy can compute invariants for links, the computational complexity often increases exponentially with the number of crossings. This presents limitations for SnapPy when analyzing infinite families of links. To overcome these limitations for large or infinite link families, we employ the algorithm developed by Thistlethwaite and Tsvietkova in 2014.

One advantage of using their algorithm is that it relies on the diagram, allowing us to exploit the symmetry of the diagram. Using this algorithm, Thistlethwaite and Tsvietkova \cite{thistlethwaite2014alternative, tsvietkova2012hyperbolic} successfully computed the meridian lengths of an infinite family of alternating links that are closures of $3$-braids with the word presentation $(\sigma_1 \sigma_2^{-1})^{n}$ for $n \geq 3$. In this study, we aim to adopt this method to compute the meridian length of an infinite family of alternating links \( B_n \) that are closures of $4$-braids with the word presentation $\left( \sigma_2^{-1} \sigma_{1} \sigma_{3} \sigma_2^{-1} \right)^{n}$ for odd $n \geq 3$.

## Main Result

\textbf{Theorem \ref{thm:length}.} 
Let \( B_{n} \) be the infinite family of alternating links with two components that is the closure of the braid \( \left( \sigma_2^{-1} \sigma_1 \sigma_3 \sigma_2^{-1} \right)^{n} \) for odd \( n \geq 3 \). 

\begin{enumerate}
    \item Meridian length of each braid can be computed as \( l = |w_1|^{-\frac{1}{2}} \), where \( w_1 \) is a root of the following polynomial equation:

\begin{equation*}\label{final_equation}
\begin{aligned}
    &\left(16 L^{4} - 8L^{2} + 1 \right) w_{1}^{4} 
    + \left( 16 L^{4} +3L^{2} - 2\right) w_{1}^{3} \\
    &+ \left(12 L^{4} - 2L^{2} + 1 \right) w_{1}^{2} 
    + \left(4 L^{4} - 2L^{2} \right) w_{1} 
    + L^{4} = 0,
\end{aligned}
\end{equation*}
with \( L = \frac{1}{2} \sec \left( \frac{\pi}{n} \right) \).
    
    \item As \( n \) approaches infinity, the meridian length \( l \) of the infinite family \(  B_{n} \) converges to an algebraic number given by:

\begin{equation*}
\dfrac{\sqrt{6} \sqrt[6]{x}}{\sqrt[4]{-880 \cdot y \sqrt[3]{x} - 330 \sqrt{33} - 726 + 12 \cdot 11^{\frac{2}{3}} x^{\frac{2}{3}} + 11 y x^{\frac{4}{3}} }}
\end{equation*}
 where 
\[
x = 3 \sqrt{33} + 77, \quad y = \sqrt[3]{11} \quad,
\]
which is approximately equal to \( 2.09355577138662 \).
