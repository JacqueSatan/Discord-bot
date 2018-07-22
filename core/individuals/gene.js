const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json')
const fs = require('fs')
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    function all() {
        settings.id = client.user.id;
        fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
    }
    function exit() {
        process.exit();
    }
    setTimeout(all, 1000);
    setTimeout(exit, 2000);
});

client.login(settings.token);