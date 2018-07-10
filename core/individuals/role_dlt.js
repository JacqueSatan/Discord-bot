const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    Promise.all(client.guilds.get(settings.auto.server_id).roles.map(c=>c.delete()));
    function quit(){
        process.exit();
    }
    setTimeout(quit, 5000);
});

client.login(settings.token);