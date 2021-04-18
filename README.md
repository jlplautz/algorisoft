# cursoDjango3
Projeto baseado no site Algorisoft - Python com Django

## Como verificar a estrutura dos diretorio no projeto
  ### abrir o python console
  - >>> import os
  - >>> BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  - >>> BASE_DIR
      - '/home/plautz/PycharmProjects' 
        
  - >>> os.path.join(BASE_DIR, 'templates')

      - '/home/plautz/PycharmProjects/templates'

|[] (https://github.com/jlplautz/algorisoft/blob/main/asserts/images/dbase.png)





Django 3.0.4
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


Django 3.2
Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent