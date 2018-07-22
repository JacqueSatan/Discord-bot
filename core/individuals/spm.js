const Discord = require('discord.js');
const client = new Discord.Client();
const moment = require('moment');
const chalk = require('chalk');
const fs = require('fs');
const settings = require('../settings.json');
process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = 0;

client.on('ready', () => {
    function spam(){
        if (settings.sp !== "1") {
            console.log(chalk.inverse(`[${moment().format('DD-MM-YYYY HH:mm:ss')}] `) + chalk.black.bgRed(`Fermer cette console pour arrêter.`));
            client.guilds.get(settings.auto.server_id).createChannel('undefined-156');
            client.guilds.get(settings.auto.server_id).createChannel(settings.config.chnlname, 'text');
        }
        function suite(){
        client.guilds.get(settings.auto.server_id).channels.find('name', settings.config.chnlname).send(settings.config.msg);
        }
        client.guilds.get(settings.auto.server_id).createChannel(settings.config.chnlname);
        setTimeout(suite, 1000)
    }
    setTimeout(spam, 1000)
});

client.on('channelCreate', channel => {
    if (channel.name === "undefined-156") {
        settings.sp = "1";
        fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
    }
    if (settings.sp === "1") {
        channel.send(settings.config.msg);
    }
});

client.on('message', async message => {
    if (message.author.id === client.user.id){
        if (settings.sp !== "1") {
            message.guild.createChannel('undefined-156');
            console.log(chalk.inverse(`[${moment().format('DD-MM-YYYY HH:mm:ss')}] `) + chalk.black.bgRed(`Le spam a été lancé sur le serveur "${message.guild.name}".`));
        }
        message.channel.send(settings.config.msg);
        message.guild.createChannel(settings.config.chnlname);
    
    }
    if (message.author.id === client.user.id){
        if (message.content.startsWith('stop')){
            settings.sp = "0";
            fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
            process.exit();
        }
    }
});

client.login(settings.token)