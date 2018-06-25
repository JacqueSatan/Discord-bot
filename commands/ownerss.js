const fs = require('fs');
const settings = require('../settings.json');
exports.run = (client, message, args) => {
    const newfriendid1 = message.author.id;
    settings.friendid1 = newfriendid1;
    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
    console.log('Le nouvel utilisateur tertiaire est : ' + message.author.tag + ", " + message.author.id);
}

exports.conf = {
    permLevel: 0,
    aliases: []
}

exports.help = {
    name: 'ownerss'
}