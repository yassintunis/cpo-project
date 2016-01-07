# CPO #
Projet d'application de contrôle parental open source.


## Principes généraux ##
  * application en mode connecté: si pas de connexion internet, limitation maximale (contrainte considérée comme acceptable)
  * serveur hébergeant les données de paramétrage d'utilisateurs reliés en réseau social
  * client minimal (service, pas d'IHM; les IHM sont gérées sur le serveur)
  * limitation par plages horaires et par durée
  * contrôle de l'exécution d'applications non connectées, et de l'accès réseau

## Maquette préliminaire ##
  * client windows et linux
  * on met pas l'accent sur une sécurisation sévère; les enfants sont considérés comme n'ayant pas de connaissance système
  * serveur développé avec django (d'où intérêt de réaliser le client en python, éventuellement django, avec une base sqlite en mémoire)

## Tâches en cours ##
  * Création de quelques modèles de données django