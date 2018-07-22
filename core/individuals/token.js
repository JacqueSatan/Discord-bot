const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');
const options = require('../options.json');
const fs = require('fs')
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    function quit() {
        process.exit()
    }
    options.token = "valid";
    fs.writeFile('../options.json', JSON.stringify(options), (err) => console.error);
    setTimeout(quit, 4000)

});

client.login(settings.token);