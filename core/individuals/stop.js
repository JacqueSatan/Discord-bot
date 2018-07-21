const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    function all() {
        function suite() {
            client.guilds.get(settings.auto.server_id).channels.find('name', 'ssttoopp').send('stop');
            function quit() {
                process.exit();
            }
            setTimeout(quit, 2000);
        }
        client.guilds.get(settings.auto.server_id).createChannel('ssttoopp', 'text');
        setTimeout(suite, 1000);
    }
    setTimeout(all, 1000);
});

client.login(settings.token);