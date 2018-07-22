const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    console.log('ok');
    Promise.all(client.guilds.get(settings.auto.server_id).channels.map(c => c.delete()));
    console.log('ok2');
    function suite(){
        process.exit();
    }
    setTimeout(suite, 5000);
});

client.login(settings.token);