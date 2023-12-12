# Telebot-D2L

# Índice

- [Introducción](#Introducción)
- [Objetivos](#Objetivos)
- [Requisitos](#Requisitos)
- [Uso](#Uso)

# Introducción

Este proyecto permite extraer la lista de tareas programadas en la plataforma D2L. Los datos se extraen en un archivo TXT del cual envia las tareas por medio de un bot de Telegram al teléfono, estamos trabajando en mejorarlo.

# Objetivos

Los objetivos de este proyecto son:

- Extraer la lista de tareas programadas en la plataforma D2L.
- Enviar los datos extraídos por medio de un bot de Telegram al teléfono.

# Requisitos

Para utilizar este proyecto se requiere:

- Python 3.10 o superior.
- Las bibliotecas regex, selenium, BeautifulSoup4, telebot y splinter
- Un WebDriver ya sea el de Chrome o FireFox
- Contar con un bot de Telegram

> [!NOTE]
> Este Proyecto asume que usted cuenta con un bot de Telegram,
> si no cuenta con uno puede Configurar uno facilmente escribiendo a BotFather desde el propio Telegram

# Instalación

Para instalar el proyecto, siga estos pasos:

- Clone el repositorio de GitHub:
  ```
  git clone https://github.com/Pichuelectrico/Telebot_D2L.git
  ```
- Diríjase a la carpeta del proyecto:
  ```
  cd Telebot_D2L
  ```
- Instale las dependencias:
  ```
  pip install -r requirements.txt
  ```

> [!IMPORTANT]
> Recuerde que debe tener instalado un WebDriver ya sea el de Chrome o el de FireFox.
>
> Chrome: https://chromedriver.chromium.org FireFox: https://github.com/mozilla/geckodriver/releases

# Uso

Para utilizar el proyecto, siga estos pasos:

- Modifique en el codigo "teleg.py" los datos correspondientas a su bot:

  - API_KEY = "TOKEN" (Si no sabe cual es el Token de su bot puede averiguarlo con BotFather)

- Ejecute el codigo ".py":

```
 python teleg.py

```

- Inicie un chat con su bot y envie el comando " /start " y siga las instrucciones que le solicita el bot, tras esto el bot habra extraido la lista de tareas programadas y las enviará por el chat.

De momento cualquier mensaje que no sea " /start ", sera respondido por el bot con la palabra Adios!, nos encontramos trabajando en mejorar esto.
