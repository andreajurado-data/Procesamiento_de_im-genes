# Procesamiento_de_imágenes
Detección y seguimiento de vasos en tiempo real con OpenCV y YOLOv8, incluyendo conteo dinámico y análisis por regiones.


# Detección y seguimiento de vasos en video

## Descripción
Este proyecto consiste en el procesamiento de un video casero en el que se detectan 10 vasos. Para cada uno de ellos se definieron áreas delimitadas, representadas por recuadros de color verde.

Cuando un vaso se encuentra dentro de su área correspondiente, se muestra un recuadro adicional de color azul indicando su presencia. En caso de que el vaso sea retirado, solo permanece visible el recuadro verde.

A lo largo del video, los vasos son retirados y colocados nuevamente, permitiendo observar el comportamiento dinámico del sistema de detección.

En la esquina superior izquierda se muestra en tiempo real la cantidad de vasos presentes dentro de las áreas delimitadas. Además, cada vaso está numerado:
- El número se muestra en color verde si el vaso está presente dentro de su área.
- El número cambia a color rojo si el vaso no se encuentra en su posición.

---

## Tecnologías utilizadas
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- Pandas

---

## Ejemplo
![Captura del video](https://github.com/andreajurado-data/Procesamiento_de_im-genes/blob/main/Procesamiento_de_im%C3%A1genes.png?raw=true)


