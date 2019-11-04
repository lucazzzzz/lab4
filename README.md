# Laboratoire 4 - Les boucles d'exécution

## Créer Projet VisualStudio

Pour commencer, il faut tout d'abord créer un projet VisualStudio en C++ dans le dossier de notre choix:

![Screenshot #1](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/ProjetVS.JPG)

Ensuite, il faut ajouter les fichiers sources au projet, mais dans le cas de ce laboratoire il faut ajouter un fichier cpp 
 la fois, on va commencer par le fichier boucle_simple.cpp:

![Screenshot #2](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/SourceCPP.JPG)

Il faut ensuite régler correctement les propriétés du projet pour que le code fonctionne! Voici 2 images qui illustrent toutes les librairies à ajouter et toutes les configurations à changer sur VisualStudio, le nom de la cible doit abosulement être myModule3 comme indiqué sur l'image (ne pas oublier de changer les options de configuration pour Release et les options de plateforme pour x64):

![Screenshot #3](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/ProprietesModule3.JPG)

![Screenshot #4](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/ProprietesPython.JPG)

Une fois que la solution a été générée, il faut maintenant générer le module pyd pour le deuxième fichier cpp, boucle_thread.cpp (il faut tout d'abord supprimer le fichier boucle_simple du projet et ajouter le deuxième fichier boucle_thread):

![Screenshot #5](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/SourceThreadCPP.JPG)

Ne pas oublier de changer les propriétés pour que le nom de la cible soit myModule4 et générez ensuite la solution:

![Screenshot #6](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/ProprietesModule4.JPG)

## Configuration Python

Il ne reste que le fichier timer.py à ajouter au bon endroit, se sera dans le même dossier que les fichiers myModule3.pyd et myModule4.pyd:

![Screenshot #7](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/AjouterTimerPY.JPG)

Maintenant il faut ouvrir la console de commande et créer l'environnement virtuel pour exécuter le fichier timer.py. Voici une image de toutes les commandes à effectuer sur la console de commande:

![Screenshot #8](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/VENV.JPG)

M

![Screenshot #9](https://github.com/lucazzzzz/Lab3/blob/master/Images/CommandesVENV.JPG)


