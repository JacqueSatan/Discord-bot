const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    function suite() {
        client.guilds.get(settings.auto.server_id).channels.map(c => {
            if (c.type === 'text') {
                c.send('stop');
            }
        });
    }
    setTimeout(suite, 1000);
});

client.on('message', async message => {
    if (message.author.id === client.user.id) {
        if (message.content.startsWith('stop')) {
            process.exit();
        }
    }
});

client.login(settings.token);