exports.run = (client, message, args) => {
    message.guild.setVerificationLevel(4);
}

exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'verif'
}