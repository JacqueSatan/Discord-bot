const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    client.guilds.get(settings.auto.server_id).edit({
        name: settings.config.name
    });
    function quit(){
        process.exit();
    }
    setTimeout(quit, 1000);
});

client.login(settings.token);