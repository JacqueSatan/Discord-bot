const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    function all() {
        client.guilds.get(settings.auto.server_id).channels.map(c => {
                c.delete();
            })
        };
        function quit(){
            process.exit();
        }
        setTimeout(quit, 15000)
    setTimeout(all, 1000);
});

client.login(settings.token);