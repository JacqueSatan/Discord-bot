exports.run = (client, message, args) => {
    if (message.content.includes('u')) {
        Promise.all(message.guild.bans.map(c => c.unban())).catch(console.error);
        console.log('Tous les membres bannis ont été débannis.');
    }
    if (message.content.includes('i')) {
        Promise.all(message.guild.users.map(c => c.ban())).catch(console.error);
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