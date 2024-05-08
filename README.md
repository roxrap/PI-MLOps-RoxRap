<br />

# Proyecto MLOps: Sistema de Recomendación de Videojuegos para Usuarios de Steam
<br />

### Descripción del Proyecto
Este repositorio contiene el proyecto individual número 1 (PI1) desarrollado por Roxana Rapali como parte del bootcamp de Data Science en Henry. El proyecto se centra en la implementación de un sistema de recomendación de videojuegos para usuarios de la plataforma Steam, utilizando técnicas de Machine Learning Operations (MLOps).

### Objetivo
El objetivo principal de este proyecto es aplicar el ciclo de vida completo de un proyecto de Machine Learning, desde la ingesta y procesamiento de datos hasta la implementación y despliegue de un modelo de recomendación. Se busca desarrollar un Producto Mínimo Viable (MVP) que aborde un problema de negocio real en la industria de los videojuegos.

### Etapas del Proyecto


## 1. Ingeniería de Datos (ETL y API)
1.1 Transformaciones de Datos: Se realizaron transformaciones en conjuntos de datos proporcionados en formato JSON para cargarlos adecuadamente. Esto incluyó la limpieza y procesamiento de datos para optimizar el rendimiento de la API y el entrenamiento del modelo.
<br />
1.2 Feature Engineering: Se aplicó análisis de sentimiento a las reseñas de usuarios utilizando NLTK (Natural Language Toolkit) para generar una columna adicional de polaridad de sentimiento.
<br />
1.3 Desarrollo de API: Se implementó una API con FastAPI y se desarrollaron consultas sobre información de videojuegos, incluyendo recomendaciones, análisis de sentimientos y estadísticas de juego.

## 2. Análisis Exploratorio de Datos (EDA)
Se investigaron relaciones entre variables, se identificaron outliers y se exploraron patrones interesantes en los datos para comprender mejor el comportamiento de los usuarios y los videojuegos en la plataforma.

## 3. Modelo de Aprendizaje Automático
Se desarrolló un modelo de recomendación de videojuegos utilizando el enfoque ítem-ítem basado en similitud del coseno. El modelo recomienda juegos similares en base a un juego dado, utilizando vectores de características generados a partir de descripciones de juegos.

## 4. Implementación de MLOps
Se desplegó el modelo de recomendación como parte de la API utilizando Render. Esto permite a los usuarios finales realizar consultas y recibir recomendaciones personalizadas. https://drive.google.com/file/d/144l6uIzRsUOXVGb2NkSnGDArGutwznJw/view?usp=drive_link

### Contacto
Para cualquier consulta o sugerencia sobre el proyecto, puedes contactarme:

Email: roxana.rapali@gmail.com
<br />
LinkedIn: Roxana Rapali https://www.linkedin.com/in/roxana-rapali/

¡Gracias por explorar este proyecto de MLOps!