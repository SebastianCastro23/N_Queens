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
  
<br> Se podrán ver implementaciones de distintos algoritmos para la resolución del problema anteriormente planteado en busca de exponer eficiencia y complejidad, se podra ver documentación que data distintas formas de resolución de este problema como implementaciones con Fireflies y algoritmos geneticos, sin embargo nos centraremos en revisar a profundidad los siguientes algoritmos:
* Hill climbing y dos variantes
* Backtracking y variante usando metodo de optimizacion Branch and Bound
* Algoritmo de busqueda eficiente de Sosic y Jun Gu
  
   
## Navegacion y reproducción del proyecto:
El proyecto esta hecho en su totalidad en python tanto la interfaz grafica como los algoritmos implementados, aunque no se requiere mucho para la ejecución igualmente cabe nombrar lo siguiente.<br>
Para la ejecución de los algoritmos (Backtracking.py,Hill_Climbing.py,Uniform_Cos-Search.py y Sisoc_JunGu_Algorithm.py) tengase en cuenta la presencia de las siguientes librerias utilizadas de python: 
  - globals
  - copy
  - random
  - memory_profiler 
  - heapq.
## Especificaciones para acceso a recursos pedidos en la entrega:
 Visualización edición del reporte del proyecto final: [Acercamiento e implementación de algoritmos para la resolución del problema de las N-reinas](https://www.overleaf.com/2218436297jnttdwfzsygd).<br>
 Visualización del video explicativo: [Video Presentación Proyecto final Inteligencia artificial](https://youtu.be/RV19d8TX-ag).<br>
 Para la visualización del Notebook, <b>Véase el archivo marcado N-queens problem-Notebook.ipynb</b><br>
  
[^1]: View of complexity of n-queens completion. (s/f). Jair.org. Recuperado el 28 de noviembre de 2022, de https://jair.org/index.php/jair/article/view/11079/26262
