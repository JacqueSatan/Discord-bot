# Bot Anti Discord v1.3.0


##    Sommaire :

    1. Présentation
    2. Utilisation
        1. Pré-requis
        2. Création d'une application Discord
        3. Configuration
        4. Commandes

## 1.  Présentation

Bot Anti Discord est une application JavaScript créé par @Jacques#1258, @ρυяρℓєgυу#9807, et 
@AICHAQUENDISHA(SALMA)#0160. Cette application consiste, une fois intégrée à une application 
Discord, à détruire **votre** serveur. C'est donc ici que vous allez apprendre à les 
configurer. N'hésitez pas (nous vous y encourageons même) à nous faire part des erreurs que 
vous puissiez rencontrer lors de votre utilisation !

A venir dans la prochaîne version (v1.3.1) :

    Personnalisation des noms des commandes
    Fixs si nécéssaire (faîtes-m'en part !)

## 2. Utilisation

#### 1.Pré-requis

Avant de commencer, vous devez avoir installé sur votre ordinateur [ Node.js et Npm ]( https://nodejs.org/en/ "Installer Node.js et Npm" ), disponibles en cliquant sur leurs noms ci-dessus. Vous avez également besoin, bien entendu, d'un compte Discord. Il est très fortement recommandé d'utiliser [ Visual Studio Code ]( https://code.visualstudio.com/download "Installer Visual Studio Code" ) pour modifier les documents.

#### 2. Création d'une application Discord

Rendez-vous sur [ ce site ]( https://discordapp.com/developers/applications/me/create "Vos applications Discord" ) et créez une nouvelle application. Une fois créée, cliquez sur 
"Créer un utilisateur Bot". Vous avez créé votre application. Maintenant, si vous cliquez sur "Cliquer pour révéler" dans l'onglet "UTILISATEUR APP BOT", c'est le token de votre bot qui s'affiche. Gardez-le pour la suite.

#### 3. Configuration

Dans le fichier "settings.json" (A remplir de la façon suivante : "valeur": "vous écrivez ici",) : 
* "token": "le token de votre bot",
* "auto" : {
    * "enabled": "1 pour que le bot lance l'attaque tout seul dès son démarrage, 2 pour qu'il la lance dès qu'il arrive sur le serveur."
    * "server_id": "l'Identifiant du serveur à attaquer automatiquement",
    * "channel_id": "l'Identifiant d'un salon **ECRIT** du serveur à attaquer automatiquement",
    * "function": "1 pour l'attaque complète, 2 pour l'attaque spam uniquement"
* },
* "config": {
    * "ban": "1 pour bannir tous les utilisateurs bannissables",
    * "imgnom": "1 pour changer l'image et le nom du serveur",
    * "img": "chemin vers l'image",
    * "name": "nouveau nom du serveur",
    * "chnl_dlt": "1 pour supprimer tous les salons du serveur",
    * "admin": "1 pour mettre les autorisations administrateur au rôle @everyone",
    * "role_dlt": "1 pour supprimer tous les rôles supprimables",
    * "role_crt": "1 pour créer des rôles à l'infini",
    * "spam": "0 pour que le bot crée des salons textuels à l'infini, 1 pour que le bot spamme dans un nombre infini de salons, 2 pour que le bot crée des vocaux à l'infini, 3 pour que le bot crée des catégories à l'infini."
* }

Dans le dossier où se situent tous les fichiers du bot, effectuez un Clic droit tout en appuyant sur la touche Maj (Clic droit + Shift), puis sélectionnez "Ouvrir la fenêtre PowerShell ici". Dans la fenêtre PowerShell, vous écrirez chacune à son tour les commandes suivantes :
* npm i fs
* npm i discord.js
* npm i ms
* npm i moment
* npm i chalk

#### Commandes

Pour lancer le bot, lancez simplement le fichier 'start.bat'.

Pour utiliser le bot, il faut que le bot sache qui vous êtes. Pour celà, envoyez simplement dans un salon auquel le bot a accès, soit "owner", soit "owners", soit "ownerss". Enfin, il faut utiliser des commandes. Ces commandes, doivent se trouver 
en début de message sans préfixe, et collées à aucun autre caractère qu'un espace. 
Ces commandes, en voici la liste : 


    Nom       | Description                                                              | Utilisation
              |                                                                          |
    admin     | change les permissions du rôle @everyone, il devient administrateur.     | admin
    attack    | effectue des changements sur le serveur en fonction de settings.json.    | attack
    ban       | bannit l'utilisateur mentionné.                                          | ban <mention>
    bann      | bannit tous les utilisateurs bannissables du serveur, même vous.         | bann
    channel i | crée des salons à l'infini.                                              | channel i
    channel s | supprime tous les salons du serveur.                                     | channel s
    nom       | remplace le nom du serveur par la suite du message.                      | nom <nouveau nom>
    quit      | quitte le serveur                                                        | quit
    quit all  | quitte tous les serveurs                                                 | quit all
    role s    | supprime tous les rôles supprimables.                                    | role s  
    role c    | crée des rôles à l'infini.                                               | role c
    spam      | spamme dans une infinité salons créés pour l'occasion                    | spam 
