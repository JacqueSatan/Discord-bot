# Bot Anti Discord v1.3.5


##    Sommaire :

    1. Présentation
    2. Utilisation
        1. Pré-requis
        2. Création d'une application Discord
        3. Configuration
        4. Commandes

## 1.  Présentation

Bot Anti Discord est une application JavaScript créé par "@Jacques#1258", "@ρυяρℓєgυу#9807", et 
"@(SALMA) AICHAQUENDISHA#0160". Cette application consiste, une fois intégrée à une application 
Discord, à faciliter certaines modifications de masse sur serveur. C'est donc ici que vous allez apprendre à les 
configurer. N'hésitez pas (nous vous y encourageons même) à nous faire part des erreurs que 
vous puissiez rencontrer lors de votre utilisation !

Me contacter : 

    Discord : J͋ͣá̝c̥̩ͭͤͮ͟q̍u̧͂ͬͯ͒̊ͨ̆eͣ̎š#5823
    E-mail  : dsicrod@gmail.com
    Twitter : @AntiDiscord

[ Serveur de support ]( https://discord.gg/ngrdmkN "Serveur de support" )<br />
[ Lien vers le Github ]( https://antidiscordbot.page.link/lastversion "Lien vers cette page" )

Nouveautés :
    
    Fixs
    Interface GUI optimisée :
        Ajout de boutons manquants
        Refonte de la mise en page
        

A venir dans les prochaines versions (ordre approximatif) :

    Fixs si nécéssaire (faîtes-m'en part !)
    Personnalisation des messages spammés
    Spammer tous les membres du serveur en message privé

## 2. Utilisation

#### 1.Pré-requis

Avant de commencer, vous devez avoir installé sur votre ordinateur [ Node.js et Npm ]( https://nodejs.org/en/ "Installer Node.js et Npm" ), disponibles en cliquant sur leurs noms ci-dessus. Vous avez également besoin, bien entendu, d'un compte Discord. Il est très fortement recommandé d'utiliser [ Visual Studio Code ]( https://code.visualstudio.com/download "Installer Visual Studio Code" ) pour modifier les documents. Il est également nécéssaire d'installer [ Python 3 ]( https://www.python.org/downloads/ "Installer Python 3" ), sauf si vous relevez le défi de tout configurer à la main. Pendant l'installation de Python, veillez à ce que l'extension Tkinter soit cochée. Il est maintenant nécéssaire d'avoir installer [ l'application Discord ]( https://discordapp.com/ "Page d'accueil de Discord" ).

#### 2. Création d'une application Discord

Rendez-vous sur [ ce site ]( https://discordapp.com/developers/applications/me/create "Vos applications Discord" ) et créez une nouvelle application. Une fois créée, cliquez sur 
"Créer un utilisateur Bot". Vous avez créé votre application. Maintenant, si vous cliquez sur "Cliquer pour révéler" dans l'onglet "UTILISATEUR APP BOT", c'est le token de votre bot qui s'affiche. Gardez-le pour la suite. Cochez aussi "Bot public", sinon personne ne pourra ajouter votre bot.

#### 3. Configuration

Pour configurer et lancer le bot, lancez le fichier "launcher.pyw".

Pour installer les dépendences, il vous suffit maintenant simplement de cliquer sur 'Installer les dépendences', dans l'onglet Fichier.

Pour changer le nom d'une commande, il suffit simplement d'aller dans le fichier de la commande (dans core/commande/nomdelacommande), puis de rajouter, entre guillemets, le nouveau nom de la commande entre les crochets au bas du fichier. 

Exemple :

    exports.conf => {
        permLvl: 4,
        aliases: ["nouveau nom"]
    }
