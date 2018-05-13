const fs = require('fs');
const settings = require('../settings.json');
exports.run = (client, message, args) => {
    const newowner = message.author.id;
    settings.ownerid = newowner;
    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
    console.log('Le nouvel owner est : ' + message.author.tag + ', ' + message.author.id);
}

exports.conf = {
    enabled: true,
    guildOnly: true,
    aliases: [],
    permLevel: 0
};

exports.help = {
    name: 'owners'
}