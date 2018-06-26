exports.run = (client, message, args) => {
    if (message.guild.me.hasPermission("ADMINISTRATOR")) return console.log('Le bot est bien administrateur.');
    console.log('Le bot n\'est pas administrateur.');
}

exports.conf = {
    "permLevel": 4,
    "aliases": []
}

exports.help = {
    name: 'ver'
}