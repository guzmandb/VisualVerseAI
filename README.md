# VisualVerseAI



Artificial Intelligence final project for Alvaro Montenegro's class: Video generation from lyrics or text, Stable Diffusion model-based from keras_cv

Proyecto final para la clase de Inteligencia Artificial del profesor Alvaro Montenegro: Generador de video a partir de texto, utilizando el modelo Stable Diffusion de keras_cv

![Logo](https://github.com/guzmandb/VisualVerseAI/blob/b083a4df013be276b67ff2680c1d80b101246b4b/VisualVerseAI.png)

Para el correcto despliegue del aplicativo, descargue el archivo comprimido .zip con el entorno virtual, en el siguiente link:

Para MacOS o Unix:
https://drive.google.com/file/d/1xuELIf8s6XuYVNxHhLkQ1XWFjwYvFvzG/view?usp=drive_link

Para Windows:
https://drive.google.com/file/d/1f3pPaIIAcM2x8nquzUGaNl67HBB8DMhk/view?usp=drive_link

Posteriomente descomprima el archivo, se creará una carpeta myenvIA. Abra una terminal en la carpeta del proyecto y ejecute el siguiente comando:

Para MacOS o Unix:

`source myenvIA/bin/activate`

Para Windows

`myenvIA\Scripts\activate.bat`

Luego corra, el siguiente scriptm para ejecutar el programa

`python app.py`

El programa estará corriendo en la dirección: http://127.0.0.1:5000

Abra la dirección en el navegador y podra ver la interfaz de usuario

![Interfaz de usuario](https://raw.githubusercontent.com/guzmandb/VisualVerseAI/b083a4df013be276b67ff2680c1d80b101246b4b/UI.png)

Inserte el archivo letras.txt con el texto de la canción o poema o fragmento textual en el campo de Insertar Letra

Inserte el link de Youtube del que desea extraer el audio.

Espere a que se procese.

A continuación en la carpeta del proyecto dentro de la sub carpeta ./videos/ encontrará el video correspondiente.

##### Si encuentra algún error de ejecución surge, asegurese que tiene instalado Imagemagick

Para MacOS:

En la terminal, ejecute
`brew install imagemagick`

O siga la documentación:
https://imagemagick.org/index.php

Para Windows, descargue en:
https://imagemagick.org/script/download.php


