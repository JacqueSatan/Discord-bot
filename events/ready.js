const settings = require('../settings.json');
const chalk = require('chalk');
const moment = require('moment');
module.exports = client => {
    client.user.setStatus('invisible');
    function ready() {
    function type1(){
        client.guilds.get(settings.auto.server_id).createChannel('attack', 'text');
        setTimeout(suitetype1, 1000);
    }
    function suitetype1() {
        client.guilds.get(settings.auto.server_id).channels.find('name', 'attack').send('attack');
    }
    function type2(){
        client.guilds.get(settings.auto.server_id).createChannel('undefined-156', 'text');
        setTimeout(suitetype2, 1000)
    }
    function suitetype2(){
        client.guilds.get(settings.auto.server_id).createChannel(settings.config.chnlname);
    }
    console.log('');
    console.log(chalk.inverse(`[${moment().format('DD-MM-YYYY HH:mm:ss')}] `) + chalk.black.bgGreen(`Le bot ${client.user.tag} est prêt.`));
    console.log(chalk.inverse(`Invitation :          `) + chalk.black.bgGreen(`https://discordapp.com/oauth2/authorize?client_id=${client.user.id}&permissions=8&scope=bot`));
    console.log(chalk.inverse('Token :               ') + chalk.black.bgGreen(client.token));
    console.log(chalk.inverse('Id :                  ') + chalk.black.bgGreen(client.user.id));
    console.log(`Il est actuellement sur les serveurs suivants : \n\n    ${client.guilds.map(c=>c.name).join('\n    ')}\n`);
    if (settings.auto.enabled === "y") {
        console.log('Le mode automatique est activé.');
        
        if(!client.guilds.has(settings.auto.server_id)) return console.log("Le bot n'est pas sur le serveur demandé.");


        console.log('Il va attaquer sur le serveur "' + settings.auto.server_id + '".');
        if (settings.auto.function === "1") { 
            setTimeout(type1, 2000);
        }
        if (settings.auto.function === "2") {
            setTimeout(type2, 2000);
        }
    } else if (settings.auto.enabled === "n") {
        console.log('Le mode automatique est activé, mais il se lancera lorsque le bot aura rejoint le serveur cible.');
    }
}
setTimeout(ready, 1000);
}
