const fs = require('fs');
const settings = require('../settings.json');
exports.run = (client, message, args) => {
    const newfriendid = message.author.id;
    settings.friendid = newfriendid;
    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
    console.log('Le nouvel utilisateur secondaire est : ' + message.author.tag + ', ' + message.author.id);
}

exports.conf = {
    permLevel: 0,
    aliases: []
}

exports.help = {
    name: 'owner'
}