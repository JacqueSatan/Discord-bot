const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    function all() {
        client.guilds.get(settings.auto.server_id).createChannel('stop', 'text');
    }
    function suite() {
        client.guilds.get(settings.auto.server_id).channels.find('name', 'stop').send('stop');
    }
});

client.login(settings.token);