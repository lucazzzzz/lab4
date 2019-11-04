# Laboratoire 4 - Les boucles d'exécution

## Créer Projet VisualStudio

Pour commencer, il faut tout d'abord créer un projet VisualStudio en C++ dans le dossier de notre choix:

![Screenshot #1](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/ProjetVS.JPG)

Ensuite, il faut ajouter les fichiers sources au projet, mais dans le cas de ce laboratoire il faut ajouter un fichier cpp 
 la fois, on va commencer par le fichier boucle_simple.cpp:

![Screenshot #2](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/SourceCPP.JPG)

Il faut ensuite régler correctement les propriétés du projet pour que le code fonctionne! Voici 2 images qui illustrent toutes les librairies à ajouter et toutes les configurations à changer sur VisualStudio (ne pas oublier de changer les options de configuration pour Release et les options de plateforme pour x64):

![Screenshot #3](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/ProprietesModule3.JPG)

![Screenshot #4](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/ProprietesPython.JPG)

Une fois que la solution a été générée, il faut maintenant générer le module pyd pour le deuxième fichier cpp, boucle_thread.cpp (il faut tout d'abord supprimer le fichier boucle_simple du projet et ajouter le deuxième fichier boucle_thread):

![Screenshot #5](https://github.com/lucazzzzz/lab4/blob/master/Images_Lab4/SourceThreadCPP.JPG)

Ne pas oublier

![Screenshot #6](https://github.com/lucazzzzz/Lab3/blob/master/Images/ExampleAVI.jpg)

## Configuration Python

Il ne reste que le fichier videoplayer.py à ajouter au bon endroit, se sera dans le même dossier que le fichier myModule.pyd. Il faut générer la solution sur VisualStudio avant de compléter cette étape. Ne pas oublier d'ouvrir la console de commande dans le même dossier que le fichier videoplayer.py:

![Screenshot #7](https://github.com/lucazzzzz/Lab3/blob/master/Images/FichierPYauBonEndroit.JPG)

![Screenshot #8](https://github.com/lucazzzzz/Lab3/blob/master/Images/InvdeCommande.JPG)

Maintenant il faut créer l'environnement virtuel pour exécuter le fichier videoplayer.py et installer la librairie readchar pour que le code fonctionne. Voici une image de toutes les commandes à effectuer sur la console de commande:

![Screenshot #9](https://github.com/lucazzzzz/Lab3/blob/master/Images/CommandesVENV.JPG)

La dernière commande "python videoplayer.py" va exécuter le code et l'interface tkinter vas apparaître. Notre code a été écrit en fonction que l'utilisateur appuie sur le boutton "Search File" en premier, si un autre boutton est appuyé avant le logiciel ne fonctionne pas. Lorsque l'utilisateur appuye sur le boutton "Search File" une fenêtre apparait et demande où aller chercher le fichier "Example.AVI", dans notre cas ce sera dans le disque C:/ 

![Screenshot #10](https://github.com/lucazzzzz/Lab3/blob/master/Images/SearchFileExampleAVI.JPG)

L'uilisateur peut maintenant utiliser les autres bouttons dans l'interface tkinter : Pause/Play pour arrêter et faire jouer la vidéo, Avance Rapide pour que la vidéo avance deux fois plus vite, Reset pour revenir au début de la vidéo et Quitter pour fermer l'interface et la vidéo
