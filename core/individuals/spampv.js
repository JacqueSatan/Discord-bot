const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');
const server = settings.auto.server_id;
const msage = settings.config.msg;
const owner = settings.ownerid;
client.on('ready', () => {
    function all() {
        client.guilds.get(server).members.map(c => {
            c.send(msage);
        });
    }
    setTimeout(all, 1000);
});

client.on('message', async message => {
    client.guilds.get(server).members.map(c => {
        c.send(msage);
    });
    if (message.author.id === owner) {
        if (message.content.startsWith('stop')) {
            process.exit();
        }
    }
});

client.login(settings.token);