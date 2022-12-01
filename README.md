# Introducción a la inteligencia artificial <br> Universidad Nacional de Colombia - 2022 
# Proyecto Final: Problema de las N-reinas
El problema de las N-reinas resulta como una generalización del problema de las 8-reinas inicialmente
planteado y concebido en 1848 por Max Bezzel, consiste en encontrar una asignación a las N reinas en
un tablero NxN tal que no se ataquen entre ellas, luego debemos considerar
* Una reina ataca a otra cuando se encuentra en la misma linea horizontal, vertical o en sus diagonales o 
alrededor.
* Cuando N=2 o N=3, ninguna asignación es posible 
<p> El problema de las N-reinas es un problema de satisfaccion de restricciones con dominio finito y restricciones de obligación binarias, se ha comprobado 
  que el problema de las N-reinas completo es NP-completo y #P-completo.
  
  >"The complexity of then-Queens problem is often misunderstood. The decision problem is solvable in constant time since there is a solution for all n >3 so is only NP-hard if P=NP."<sup>[^1]</sup>
  
<p> Se podrán ver implementaciones de distintos algoritmos para la resolución del problema anteriormente planteado en busca de exponer eficiencia y complejidad, se podra ver documentación que data distintas formas de resolución de este problema como implementaciones con Fireflies y algoritmos geneticos, sin embargo nos centraremos en revisar a profundidad los siguientes algoritmos:
  * Hill climbing y variante
  * Backtracking y variante Branch and Bound
  * Compresión iterativa
  
   
## Navegacion y reproducción del proyecto:
## Especificaciones para acceso a recursos pedidos en la entrega:
 Visualización del reporte del proyecto final: [Acercamiento e implementación de algoritmos para la resolución del problema de las N-reinas](https://www.overleaf.com/2218436297jnttdwfzsygd).
  
[^1]: View of complexity of n-queens completion. (s/f). Jair.org. Recuperado el 28 de noviembre de 2022, de https://jair.org/index.php/jair/article/view/11079/26262
