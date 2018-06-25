const settings = require('../settings.json');
module.exports = client => {
    function ready() {
    function type1(){
        client.guilds.get(settings.auto.server_id).channels.get(settings.auto.channel_id).send('attack');
    }
    function type2(){
        client.guilds.get(settings.auto.server_id).channels.get(settings.auto.channel_id).send('spam');
    }
    console.log('')
    const settings = require('../settings.json');
    console.log(`Le bot "${client.user.tag}" est prêt.`);
    client.user.setStatus('invisible');
    console.log(`Invitation : https://discordapp.com/oauth2/authorize?client_id=${client.user.id}&permissions=8&scope=bot`);
    console.log('Token : ' + client.token);
    console.log('Id : ' + client.user.id);
    console.log(`Il est actuellement sur les serveurs suivants : ${client.guilds.map(c=>c.name).join(', ')}`);
    if (settings.auto.enabled === "1") {
        console.log('Le mode automatique a été activé.');
        
        if(!client.guilds.has(settings.auto.server_id)) return console.log("Server not found");
        if(!client.channels.has(settings.auto.channel_id)) return console.log("Channel not found");


        console.log('Il va attaquer sur le serveur "' + settings.auto.server_id + '" sur le salon "' + settings.auto.channel_id + '".');
        if (settings.auto.function === "1") { 
            setTimeout(type1, 2000);
        }
        if (settings.auto.function === "2") {
            setTimeout(type2, 2000);
        }
    } else if (settings.auto.enabled === "2") {
        console.log('Le mode automatique est activé, mais il se lancera lorsque le bot aura rejoint le serveur cible.');
    } else {
        console.log('Le mode automatique est désactivé.');
    }
}
setTimeout(ready, 1000);
}
