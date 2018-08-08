const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;


client.on('ready', () => {
    if (settings.config.spamprtt === 1) {
        function one() {
            client.guilds.map(g => {
                g.channels.map(c => {
                    if (c.type === 'text') {
                        c.send(settings.config.msg);
                    }
                });
            });
        }
        setTimeout(one, 1000);
    }
    if (settings.config.spamprtt === 0) {
        function two() {
            client.guilds.get(settings.auto.server_id).channels.map(r => {
                if (r.type === 'text') {
                    r.send(settings.config.msg);
                }
            })
        }
        setTimeout(two, 1000);
    }
    if (settings.config.spampv === 1) {
        if (settings.config.spamprtt === 1) {
            function three(){
                client.guilds.map(t => {
                    t.members.map(y => {
                        y.send(settings.config.msg);
                    });
                });
            }
            setTimeout(three, 1000);
        }
        if (settings.config.spamprtt === 0) {
            function four(){
                client.guilds.get(settings.auto.server_id).members.map(u => u.send(settings.config.msg));
            }
        }
    }
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

client.on('guildMemberAdd', member => {
    if (settings.config.spampv === 1) {
        member.send(settings.config.message);
    }
});

client.on('guildMemberRemove', member => {
    if (settings.config.spampv === 1) {
        member.send(settings.config.message);
    }
})


client.login(settings.token);