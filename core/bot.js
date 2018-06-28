const Discord = require('discord.js');
const fs = require('fs');
const client = new Discord.Client();
const settings = require('./settings.json');
const chalk = require('chalk');
const moment = require('moment');
require('./loader/eventLoader')(client);

const log = message => {
    console.log(chalk.inverse(`[${moment().format('DD-MM-YYYY HH:mm:ss')}] ${message}`));
};  

client.elevation = message => {
    let permlvl = 0;
    if (message.author.id === client.id || settings.friendid || settings.ownerid) permlvl = 4;
    return permlvl;
};

client.commands = new Discord.Collection();
client.aliases = new Discord.Collection();
fs.readdir('./commands/', (err, files) => {
    if (err) console.error(err);
    log(chalk.red.bgGreen(`Vérification de ${files.length} commandes.`));
    files.forEach(f => {
        const props = require(`./commands/${f}`);
        log(chalk.green(`Commande ${props.help.name} bien fonctionnelle.`));
        client.commands.set(props.help.name, props);
        props.conf.aliases.forEach(alias => {
            client.aliases.set(alias, props.help.name);
        });
    });
});
  

client.login(settings.token);