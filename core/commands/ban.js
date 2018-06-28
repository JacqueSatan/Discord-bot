exports.run = (client, message, args) => {
    const user = message.mentions.users.first();
    message.guild.ban(user);
    console.log('Le membre ' + user.tag + ' a bien été banni.');
}

exports.conf = {
    aliases: []
}

exports.help = {
    name: "ban"
}