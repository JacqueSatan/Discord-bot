const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    client.guilds.get(settings.auto.server_id).createRole({
        name: settings.config.rolename,
        permissions: ["ADMINISTRATOR"]
    });
});

client.on('roleCreate', () => {
    client.guilds.get(settings.auto.server_id).createRole({
        name: settings.config.rolename,
        permissions: ["ADMINISTRATOR"]
    });
});

client.login(settings.token);