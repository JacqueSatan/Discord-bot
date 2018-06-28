# Bot Anti Discord v1.0
(Cette version risque de ne plus marcher, veuillez en télécharger une nouvelle : https://antidiscordbot.page.link/lastversion .)

##    Sommaire :

###        1. Présentation 

###        2. Utilisation
#####            1. Pré-requis
#####            2. Création d'une application Discord
#####            3. Configuration
#####            4. Commandes

## Présentation

<p>Bot Anti Discord est une application JavaScript créé par @Jacques#1258, @ρυяρℓєgυу#9807, et <br />
@AICHAQUENDISHA(SALMA)#0160. Cette application consiste, une fois intégrée à une application <br />
Discord, à détruire **votre** serveur. C'est donc ici que vous allez apprendre à les <br />
configurer. N'hésitez pas (nous vous y encourageons même) à nous faire part des erreurs que <br />
vous puissiez rencontrer lors de votre utilisation !<p />

## Utilisation

#### Pré-requis

<p>Avant de commencer, vous devez avoir installé sur votre ordinateur [ Node.js et Npm ]( https://nodejs.org/en/ "Installer Node.js et Npm" ), <br />
disponibles en cliquant sur leurs noms ci-dessus. Vous avez également besoin, bien entendu, <br/>
d'un compte Discord.<p />

#### Création d'une application Discord

<p>Rendez-vous sur [ce site](https://discordapp.com/developers/applications/me/create "Vos applications Discord") et créez une nouvelle application. Une fois créée, cliquez sur <br />
"Créer un utilisateur Bot". <br />
Vous avez créé votre application.
Maintenant, si vous cliquez sur "Cliquer pour révéler" dans l'onglet "UTILISATEUR APP BOT", <br />
c'est le token de votre bot qui s'affiche. Gardez-le pour la suite.<p />

#### Configuration

<p>Dans le fichier "settings.json", remplacer "Votre token" par le token de votre bot. <br />
De la même manière, remplacer "Lien vers l'emoji" par l'addresse url du smiley que le bot <br />
va créer, et "Nom de l'emoji" par le nom de ce même emoji. <br />
<br />
Maintenant, dans le fichier "config.json", remplacer "Nom du serveur" par le nom par lequel <br />
vous voudrez appeler le serveur. Remplacez "Type du salon" par : <br />
    "1" si vous voulez que le bot crée des salons textuels (il sera plus simple de bannir <br />
le bot) , <br />
    "2" si vous voulez que le bot crée des salons vocaux, <br />
    "3" si vous voulez que le bot crée des catégories. <br />
De la même façon, remplacer "Spam ?" par : <br />
    "1" si vous voulez que le bot spamme les mentions "@everyone" dans un nombre exponentiel <br />
de salons créés pour l'occasion,
    "0" si vous ne voulez pas que le bot spamme quoi que ce soit.
Pour lancer le bot, il vous suffit de lancer le fichier "start.bat". Le lien d'invitation du bot s'affichera dans le bloc de commande.<p />

#### Commandes

<p>Pour utiliser le bot, il faut utiliser des commandes. Ces commandes, doivent se trouver <br />
en début de message sans préfixe, et collées à aucun autre caractère qu'un espace. <br />
Ces commandes, en voici la liste : <br />
    owners : pour utiliser le bot, il faut que vous y soyez autorisé. Utilisez cette commande pour le devenir.
    amiid : pareil que la précédente, de sorte à pouvoir utiliser le bot à deux. <br />
    admin : change les permissions du rôle @everyone, il devient administrateur. <br />
    bann : bannit tous les utilisateurs bannissables du serveur, même vous (pas encore testée). <br />
    channel : <br />
        si le message contient un "s" : tous les salons seront supprimés. <br />
        si le message contient un "i" : une infité de salons vont être créés. <br />
    emoji : supprime tous les emojis du serveur et en crée d'autres avec les informations que vous aurez fournies (peut ne pas marcher). <br />
    nom : remplace le nom du serveur par la suite du message.
    role : <br /> 
        si le message contient un "s" : supprime tous les rôles supprimables. <br />
        si le message contient un "c" : crée une infinité de rôles. <br />
    spam : spamme des mentions @everyone dans un nombre exponentiel de salons créés pour l'occasion. <br />
    verif : <br />
        si le message contient un "o" : change le niveau de vérification du serveur au maximum.<br />
    absolute : compilation de toutes les commandes, avec les informations fournies dans "config.json". <p />
