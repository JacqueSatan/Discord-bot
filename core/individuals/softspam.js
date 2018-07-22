const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    function all() {
        client.guilds.map(g => {
            g.channels.map(c => {
                c.send(settings.config.msg)
            })
        })
    }
    setTimeout(all, 1000);
});

client.on('message', async message => {
    if (message.author.id === client.user.id) {
        if (message.content.startsWith('stop')) {
            process.exit();
        }
    }
    message.channel.send(settings.config.msg);
});

client.login(settings.token);