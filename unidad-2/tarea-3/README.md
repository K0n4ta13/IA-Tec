# Clasificador de Emails

Este proyecto es un clasificador de emails que utiliza el dataset `spam_assassin.csv` para detectar correos electrónicos spam y no spam.

## Instalación

Para ejecutar este proyecto, sigue estos pasos:

1. Instalar las dependencias con:
   ```sh
   uv sync
   ```
   o:
   ```sh
   pip install .
   ```

2. Activar el entorno virtual:
   ```sh
   source .venv/bin/activate
   ```

## Entrenamiento del Modelo

Para entrenar el modelo, ejecuta:
```sh
uv run train_model.py
```
o:
```sh
python train_model.py
```

Para entrenar el modelo y evaluar su precisión, usa:
```sh
uv run train_test_model.py
```
o:
```sh
python train_test_model.py
```

## Uso del Modelo

Para ejecutar el modelo usa:

```sh
streamlit run app.py
```
Este comando iniciará una interfaz interactiva donde podrás ingresar emails y determinar si son spam o no.
