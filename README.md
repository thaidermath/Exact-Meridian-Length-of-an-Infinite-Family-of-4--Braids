# Exact-Meridian-Length-of-an-Infinite-Family-of-4--Braids

This repository examines the meridian length of an infinite family of two-component alternating links. We utilize the diagram and its symmetries to derive an exact formula for calculating the meridian length. Our approach is based on the algorithm developed by Thistlethwaite and Tsvietkova.

---


## Background
The hyperbolic structure of alternating links can be derived directly from their diagrams, thanks to an algorithm developed by Thistlethwaite and Tsvietkova [[1]]. Flint later prove that fully augmented links (FALs) also possess suitable diagrams [[2]]. More recently, Kwon, Park, and Tham generalized the algorithm to links in the thickened torus [[3]].

In this discussion, we will focus exclusively on alternating links in the 3-sphere. The algorithm allows for the extraction of other 3-manifold invariants, such as the invariant trace field, as discussed by Neumann, Tsvietkova, and later by Flint.

While tools like SnapPy can compute invariants for links, the computational complexity often increases exponentially with the number of crossings. This presents limitations for SnapPy when analyzing infinite families of links. To overcome these limitations for large or infinite link families, we employ the algorithm developed by Thistlethwaite and Tsvietkova in 2014.

One advantage of using their algorithm is that it relies on the diagram, allowing us to exploit the symmetry of the diagram. Using this algorithm, Thistlethwaite and Tsvietkova \cite{thistlethwaite2014alternative, tsvietkova2012hyperbolic} successfully computed the meridian lengths of an infinite family of alternating links that are closures of $3$-braids with the word presentation $(\sigma_1 \sigma_2^{-1})^{n}$ for $n \geq 3$. In this study, we aim to adopt this method to compute the meridian length of an infinite family of alternating links $B_n$ that are closures of $4$-braids with the word presentation 
$( \sigma_2^{-1} \sigma_{1} \sigma_{3} \sigma_2^{-1})^{n}$ for odd $n \geq 3$.

## Main Result
Refer to the thesis for the main theorem (Will provide a link once it is available online). We also compute the numerical values for the meridian length using the code mentioned in the code.py file and compare these values with those obtained from SnapPy.

| n   | SnapPy Values | Our Code Values |
| --- | ------------- | --------------- |
| 3   | 1.76095258    | 1.760953        |
| 5   | 1.96289334    | 1.962893        |
| 7   | 2.02454571    | 2.024546        |
| 9   | 2.0511218     | 2.051122        |
| 11  | 2.06489810    | 2.064898        |
| 13  | 2.0729294     | 2.072929        |
| 15  | 2.07801089    | 2.078011        |
| 17  | 2.08142571    | 2.081426        |
| 19  | 2.083829311   | 2.083829        |
| 21  | 2.08558431    | 2.085584        |
| 23  | 2.086904440   | 2.086904        |
| 25  | 2.08792219    | 2.087922        |
| 27  | 2.08872326    | 2.088723        |
| 29  | 2.08936499    | 2.089365        |

## 🛠 Tools

- Thistlethwaite–Tsvietkova algorithm
    
- SnapPy (for numerical comparison)
    
---

## References


1. Thistlethwaite, M., & Tsvietkova, A. (2014). _An alternative approach to hyperbolic structures on link complements_. Algebraic & Geometric Topology, 14(3), 1307–1337. [DOI:10.2140/agt.2014.14.1307](https://doi.org/10.2140/agt.2014.14.1307)
    
2. Flint, R. (2017). _Intercusp Geodesic and Cusp Shapes of Fully Augmented Links_. PhD Thesis, City University of New York (CUNY). [Link to thesis](https://academicworks.cuny.edu/gc_etds/2139)
    
3. Kwon, A., Park, B., & Tham, Y. (2023). _Generalization of Thistlethwaite–Tsvietkova Method_. arXiv:2309.01282. (https://arxiv.org/abs/2309.01282)
    
4. Neumann, W., & Tsvietkova, A. (2016). _Intercusp geodesics and the invariant trace field of hyperbolic 3-manifolds_. Proceedings of the American Mathematical Society, 144(2), 887–896. 


---
