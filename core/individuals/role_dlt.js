const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    function all(){
    Promise.all(client.guilds.get(settings.auto.server_id).roles.map(c=>c.delete()));
    }
    setTimeout(all, 1000)
});

client.on('message', async message => {
    if (message.author.id === client.user.id) {
        if (message.content.startsWith('stop')) {
            process.exit();
        }
    }
})


client.login(settings.token);