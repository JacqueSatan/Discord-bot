const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    function all(){
		client.guilds.get(settings.auto.server_id).roles.find('name', '@everyone').edit({
			permissions: ["ADMINISTRATOR"]
		});
	}
});

client.login(settings.token);