# Application de suivi de Fitness
**API REST** pour gérer les exercices, les programmes d'entrainement et les progrès des utilisateurs avec django.

## Les étapes d'installation de l'application :
- Ouvrer un terminal puis cloner le lien github de l'application : 
```bash
 git clone https://github.com/Ivanyao2002/Fitness_tracking_api.git
 ```
- Créer un environnement virtuel dans le repertoire 
```bash
 python -m venv venv ou env ( Pour windows )
 python3 -m venv venv ou env ( Pour Unix ) 
 ```
- Naviguer vers le fichier activate.bat soit dans scripts ou bin, puis activer l'environnement 
```bash
 source activate ( Pour Unix ) 
 activate ( Pour windows) 
 ```
- Revener au repertoire de votre projet puis installer les dépendances de l'application à partir du fichier requirements.txt
```bash
 pip install -r requirements.txt ( Pour windows ) 
 pip3 install -r requirements.txt ( Pour Unix )
 ```
- Installez et configurez une base de données Postgresql 'forum_db' configurer les accès dans le fichier settings.py
- Naviguez vers le repertoire source (src) puis créer et appliquer les migrations 
```bash
 python manage.py makemigrations 
 python manage.py migrate
 ``` 
 
## Les instructions de démarrage :
- Naviguez vers le repertoire source (src) puis lancer le server
```bash
 python manage.py runserver 
 ``` 
- Vous pouvez tester avec le navigateur ou avec Postman 
- Lien vers l'api : http://127.0.0.1:8000/api/
- Lien vers la documentation : 
  
## Description des fonctionnalités principales de l'application :
