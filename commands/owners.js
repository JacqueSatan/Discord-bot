const fs = require('fs');
const chalk = require('chalk');
const moment = require('moment');
const settings = require('../settings.json');
exports.run = (client, message, args) => {
    const newowner = message.author.id;
    settings.ownerid = newowner;
    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
    console.log(chalk.inverse(`[${moment().format('DD-MM-YYYY HH:mm:ss')}] `) + chalk.black.bgGreen(`Nouvel utilisateur n°2 : ${message.author.tag} ${message.author.id}`));
}

exports.conf = {
    permLevel: 0,
    aliases: []
};

exports.help = {
    name: 'owners'
}