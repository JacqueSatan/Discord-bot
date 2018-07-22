const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    client.guilds.get(settings.auto.server_id).setIcon(settings.config.img);
    process.exit();
});

client.login(settings.token);