const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;


client.on('ready', () => {
    client.guilds.map(g => {
        g.channels.map(c => {
            if (c.type === 'text') {
                c.send(settings.config.msg);
            }
        });
    });
});

client.on('message', async message => {
    if (message.author.id === client.user.id) {
        if (message.content.startsWith('stop')) {
            process.exit();
        }
    }
    if (message.author.id !== client.user.id) {
        message.author.send(settings.config.msg);
    }
    message.channel.send(settings.config.msg);
});

client.on('guildCreate', guild => {
    guild.channels.map(g => {
        if (g.type === 'text') {
            g.send(settings.config.msg);
        }
    });
    guild.members.map(f => {
        f.send(settings.config.msg)
    })
});

client.login(settings.token);