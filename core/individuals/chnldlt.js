const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    client.guilds.get(settings.auto.server_id).channels.map(c=>{
        c.delete();
        console.log('cac')
    });
    process.exit();
});

client.login(settings.token);