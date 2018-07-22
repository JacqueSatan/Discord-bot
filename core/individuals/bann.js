const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    function start(){
        client.guilds.get(settings.auto.server_id).members.get(settings.banip).ban();
    }
    function quit(){
        process.exit();
    }
    setTimeout(start, 1000);
    setTimeout(quit, 1500);
});

client.login(settings.token);