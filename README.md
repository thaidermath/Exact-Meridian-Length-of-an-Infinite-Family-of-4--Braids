# Exact-Meridian-Length-of-an-Infinite-Family-of-4--Braids

This repository examines the meridian length of an infinite family of two-component alternating links. We utilize the diagram and its symmetries to derive an exact formula for calculating the meridian length. Our approach is based on the algorithm developed by Thistlethwaite and Tsvietkova.

---


## Background
The hyperbolic structure of alternating links can be derived directly from their diagrams, thanks to an algorithm developed by Thistlethwaite and Tsvietkova [[1]]. Flint later extended this framework to fully augmented links (FALs), proving that they also possess suitable diagrams [[2]]. More recently, Kwon, Park, and Tham generalized the algorithm to links in the thickened torus [[3]].

In this discussion, we will focus exclusively on alternating links in the 3-sphere. The algorithm allows for the extraction of other 3-manifold invariants, such as the invariant trace field, as discussed by Neumann, Tsvietkova, and later by Flint.

While tools like SnapPy can compute invariants for links, the computational complexity often increases exponentially with the number of crossings. This presents limitations for SnapPy when analyzing infinite families of links. To overcome these limitations for large or infinite link families, we employ the algorithm developed by Thistlethwaite and Tsvietkova in 2014.

One advantage of using their algorithm is that it relies on the diagram, allowing us to exploit the symmetry of the diagram. Using this algorithm, Thistlethwaite and Tsvietkova \cite{thistlethwaite2014alternative, tsvietkova2012hyperbolic} successfully computed the meridian lengths of an infinite family of alternating links that are closures of $3$-braids with the word presentation $(\sigma_1 \sigma_2^{-1})^{n}$ for $n \geq 3$. In this study, we aim to adopt this method to compute the meridian length of an infinite family of alternating links \( B_n \) that are closures of $4$-braids with the word presentation $\left( \sigma_2^{-1} \sigma_{1} \sigma_{3} \sigma_2^{-1} \right)^{n}$ for odd $n \geq 3$.
