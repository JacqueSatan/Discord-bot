const fs = require('fs');
const settings = require('../settings.json');
const chalk = require('chalk');
const moment = require('moment');
exports.run = (client, message, args) => {
    const newfriendid1 = message.author.id;
    settings.friendid1 = newfriendid1;
    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
    console.log(chalk.inverse(`[${moment().format('DD-MM-YYYY HH:mm:ss')}] `) + chalk.black.bgGreen(`Nouvel utilisateur n°3 : ${message.author.tag} ${message.author.id}`));
}

exports.conf = {
    permLevel: 0,
    aliases: []
}

exports.help = {
    name: 'ownerss'
}