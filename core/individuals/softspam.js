const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings');

client.on('ready', () => {
    function all() {
        client.guilds.get(settings.auto.server_id).channels.map(c => {
            if (c.type === 'text') {
                c.send(settings.config.msg);
            }
        });
    }
    setTimeout(all, 1000);
});

client.on('message', async message => {
    if (message.author.id === settings.ownerid) {
        if (message.content.startsWith('stop')) {
            process.exit();
        }
    }
    message.channel.send(settings.config.msg);
});

client.login(settings.token);