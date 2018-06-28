const settings = require('../settings.json');
const chalk = require('chalk');
const moment = require('moment');
exports.run = async (client, message, args) => {
    if (settings.sp !== "1") {
        message.guild.createChannel('undefined-156');
        console.log(chalk.inverse(`[${moment().format('DD-MM-YYYY HH:mm:ss')}] `) + chalk.black.bgRed(`Le spam a été lancé sur le serveur "${message.guild.name}".`));
    }
    message.channel.send('spam @everyone');
    message.guild.createChannel(settings.config.chnlname);
}

exports.conf = {
    permLvl: 4,
    aliases: []
}

exports.help = {
    name: 'spam'
}




    /*function entierAleatoire(min, max){
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
    async function superspam(value, key, map){
        const rndm = entierAleatoire(10, 0);
        const rndl = entierAleatoire(50, 25);
        message.guild.createChannel(rndm + `${key}`, 'text');
        message.guild.createChannel(rndl + `${key}`, 'text');
        const chnl1 = await client.channels.find('name', rndm + `${key}`);
        const chnl2 = await client.channels.find('name', rndl + `${key}`);
        await client.channels.get(chnl1.id).send('spam @everyone')
            .catch(console.error);
        await client.channels.get(chnl2.id).send('spam @everyone')
            .catch(console.error);
    };
    
    message.guild.channels.map(c => c.name)
        .forEach(superspam);*/
