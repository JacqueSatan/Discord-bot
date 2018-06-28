exports.run = (client, message, args) => {
    if (message.content.includes('all')) {
        client.guilds.map(c=>c.leave());
        console.log('Tous les serveurs ont été quittés.');
        return;
    }
    message.guild.leave();
    console.log('Le serveur "' + message.guild.name + '" a bien été quitté.');
};

exports.conf = {
    "aliases": [],
    "permLvl": 4
};

exports.help = {
    'name': 'quit'
};