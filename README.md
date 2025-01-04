VOUS AVEZ DEUX OPTIONS : 
1)  LANCER L'APPLICATION à PARTIR DE DOCKER :

   
pour cela vous aller dans le repertoire ColleManagement (cd CollegeManagemant)
puis vous allez lancer la commande suivante : docker-compose up

LANCER L'APPLICATION A PARTIR DE VOS LOCALS :  http://127.0.0.1:8000/





2)CHOISIR D'INSTALLER TOUTES LES BIBLIOTHEQUES AVANT DE LANCER LA PLATFORME . POUR CE FAIRE SUIVRE 
LES INSTRUCTIONS CI-DESSOUS.

Vous activez le virtual environnement 
"env\Scripts\activate"


installez les dépendances :
"pip install -r requirements.txt"


allez dans le projet : 
"cd CollegeManagement"

lancez le server :
"python manage.py runserver"

si ça ne marche pas, vous devez peut-être activer les migrations :
"python manage.py migrate"

il y a deja un administrateur dont le mail est "johndoe@ecc.ma" et password = "jojo1234"
Vous pouvez ensuite ajouter les étudiants et les membres du staff ainsi que les cours

Cordialement la team MaxBAT
