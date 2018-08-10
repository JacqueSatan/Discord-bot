const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    function all() {
        client.guilds.get(settings.auto.server_id).channels.map(c => {
            if (settings.config.chnlsuppr.text === 1) {
                if (c.type === 'text') {
                    c.delete();
                }
            }
            if (settings.config.chnlsuppr.vocal === 1) {
                if (c.type === 'voice') {
                    c.delete();
                }
            }
            if (settings.config.chnlsuppr.text === 1) {
                if (c.type === 'category') {
                    c.delete();
                }
            }
        });
        function quit(){
            process.exit();
        }
        setTimeout(quit, 15000)
    }
    setTimeout(all, 1000);
});

client.login(settings.token);