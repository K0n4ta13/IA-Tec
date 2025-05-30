# Detector de Emociones Faciales

Este proyecto tiene como objetivo detectar emociones humanas a partir de imágenes faciales. Las imágenes utilizadas representan expresiones emocionales clasificadas en siete categorías: `angry`, `disgust`, `fear`, `happy`, `neutral`, `sad` y `surprise`.

## Red neuronal

Se utilizó una red neuronal convolucional (CNN), ya que son altamente eficaces para tareas de clasificación de imágenes. Las CNN son capaces de capturar patrones espaciales jerárquicos mediante el uso de filtros convolucionales, lo que las hace ideales para reconocer características faciales que distinguen diferentes emociones. El modelo consta de múltiples capas convolucionales y de pooling, seguidas de capas densas totalmente conectadas que culminan en una capa softmax para clasificar entre las 7 emociones.

## Parámetros de entrenamiento

- **Tamaño de imagen**: 48x48 píxeles, escala de grises
- **Tamaño del lote**: 32
- **Épocas**: 15
- **Optimizador**: Adam
- **Función de pérdida**: Categorical Crossentropy
- **Métrica de evaluación**: Accuracy
- **Normalización**: Se normalizaron los valores de píxeles dividiéndolos entre 255

## Uso

### 1. Instalar dependencias

```bash
pip install .
```

### 2. Entrenar el modelo

```bash
python train_model.py
```
### 3. Probar el modelo

```bash
python predict_emotion.py /ruta/a/tu/imagen
```

## Evaluar modelo

El archivo `reporte_clasificacion.txt` incluye información sobre la precisión del modelo al momento de evaluar las emociones. La imagen `matriz_emociones.png` muestra un gráfico en el que se pueden ver la emoción real y las emociones predichas.

Para generar estos archivos, debes ejecutar el script `evaluate_model.py`, asegurándote de que el modelo ya se encuentre entrenado.
