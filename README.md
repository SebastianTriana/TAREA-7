# TAREA #7 – Inteligencia Artificial y Mini Robots

## Punto 1 – Chatbot académico basado en redes neuronales

**Autores:**  
Sebastián Triana  
Juan Diego Camacho  

**Curso:** Inteligencia Artificial y Mini Robots  
**Universidad:** Universidad Nacional de Colombia  

---

## 📌 Descripción general

Este repositorio corresponde al **Punto 1 de la Guía #7** de la asignatura **Inteligencia Artificial y Mini Robots**.

El objetivo principal es el **desarrollo de un chatbot académico** que apoye el estudio de los temas vistos en el curso, tales como:

- Redes neuronales
- MLP y MLPRegressor
- Clasificación
- Conceptos básicos de IA
- Errores comunes en Python, NLTK, TensorFlow y Streamlit

El chatbot utiliza una **red neuronal multicapa (MLP)** entrenada a partir de un archivo de **intents** en español, y cuenta con una **interfaz gráfica desarrollada en Streamlit**.

---

## 🧠 Arquitectura del sistema

El sistema está compuesto por tres partes principales:

1. **Archivo de intents (`intents_spanish.json`)**  
   Contiene las intenciones del usuario, ejemplos de frases (*patterns*) y posibles respuestas.

2. **Entrenamiento del modelo (`training_chatbot.py`)**  
   Procesa los intents, entrena una red neuronal con Keras y guarda el modelo entrenado.

3. **Interfaz gráfica (`front.py`)**  
   Permite interactuar con el chatbot mediante una aplicación web usando Streamlit.

---

## 📁 Estructura del repositorio

```text
TAREA-7/
│── intents_spanish.json
│── training_chatbot.py
│── front.py
│── words_spanish.pkl
│── classes_spanish.pkl
│── chatbot_model_spanish.h5
│── README.md
```

---

## ⚙️ Requisitos del sistema

Se recomienda usar **Python 3.10 o superior**.

### 📦 Librerías necesarias

Instalar las dependencias con:

```bash
pip install numpy nltk tensorflow keras streamlit scikit-learn
```

Además, es obligatorio descargar recursos de NLTK:

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
```

⚠️ Estos comandos deben ejecutarse **dentro de Python**, no en PowerShell.

---

## 🏋️‍♂️ Entrenamiento del chatbot

Antes de ejecutar el chatbot, es necesario **entrenar el modelo**.

### ▶️ Paso 1: Entrenar el modelo

Desde la carpeta del proyecto, ejecutar:

```bash
python training_chatbot.py
```

Este script:

- Lee el archivo `intents_spanish.json`
- Tokeniza y lematiza las frases
- Construye una bolsa de palabras (*Bag of Words*)
- Entrena una red neuronal MLP
- Genera los archivos:
  - `chatbot_model_spanish.h5`
  - `words_spanish.pkl`
  - `classes_spanish.pkl`

⚠️ **Todos los intents deben tener las claves `tag`, `patterns` y `responses`** para evitar errores como `KeyError`.

---

## 💬 Ejecución de la interfaz gráfica

Una vez entrenado el modelo, se puede lanzar la aplicación web.

### ▶️ Paso 2: Ejecutar Streamlit

```bash
streamlit run front.py
```

Esto abrirá automáticamente el chatbot en el navegador.

⚠️ No se debe ejecutar `front.py` con `python front.py`, ya que Streamlit requiere su propio comando.

---

## 🧪 Funcionamiento del chatbot

El chatbot:

- Clasifica la intención del usuario mediante una red neuronal
- Selecciona una respuesta asociada al intent detectado
- Maneja errores comunes y entradas fuera de contexto
- Está orientado a un uso académico

Ejemplos de preguntas:

- "¿Qué es una red neuronal?"
- "¿MLP es lo mismo que un LLM?"
- "Tengo un error en Python"
- "Explícame redes neuronales"

---

## 🚨 Manejo de errores

El sistema incluye intents específicos para:

- Errores de Python
- Errores de NLTK
- Problemas con TensorFlow
- Fallos de Streamlit
- Confusión del usuario

Esto permite que el chatbot sea **robusto y estable**, incluso ante entradas inesperadas.

---

## 🎓 Nota académica

Este proyecto fue desarrollado con fines **educativos**, como parte del aprendizaje práctico en Inteligencia Artificial y Mini Robots.

El diseño del chatbot prioriza:

- Claridad conceptual
- Robustez ante errores
- Explicaciones didácticas

---

## ✍️ Autores

Sebastián Triana  
Juan Diego Camacho  

Facultad de Ingeniería  
Universidad Nacional de Colombia  
2025
