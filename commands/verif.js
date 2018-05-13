exports.run = (client, message, args) => {
    if (message.content.includes('o')) {
        message.guild.setVerificationLevel(4);
    }
}

exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'verif'
}
