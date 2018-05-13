const settings = require('../settings.json');
exports.run = (client, message, args) => {
    Promise.all(message.guild.emojis.map(c => message.guild.deleteEmoji(c)));
    message.guild.createEmoji({
        name: settings.emojiname,
        image: settings.emoji
    });
}

exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'emoji'
}