const fs = require('fs');
const settings = require('../settings.json');
exports.run = (client, message, args) => {
    const newowner = message.author.id;
    settings.ownerid = newowner;
    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
    console.log('Le nouvel owner est : ' + message.author.tag + ', ' + message.author.id);
}

exports.conf = {
    permLevel: 0,
    aliases: []
};

exports.help = {
    name: 'owners'
}