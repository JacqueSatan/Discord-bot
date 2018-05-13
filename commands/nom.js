exports.run = (client, message, args) => {
    const opt = args.splice(0, args.length).join(' ');
    message.guild.edit({
        name: opt
    })
}

exports.conf = {
    enabled: true,
    guildOnly: true,
    aliases: [],
    permLevel: 4
};

exports.help = {
    name: 'nom'
}