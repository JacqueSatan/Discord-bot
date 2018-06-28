exports.run = (client, message, args) => {
    //const settings = require('../settings.json');
    message.guild.roles.find('name', '@everyone').members.map(m=>m.ban());
    //async function map(value){
    //    if (!value === settings.ownerid | settings.friendid) {
    //        message.author.send(value);
    //    }
    //}
    //message.guild.roles.find('name', '@everyone').members.map(c=>c.id).forEach(map);
    //console.log('Tous les membres bannissables ont été bannis sauf vous.');
    //client.fetchUser;
    //const filterthis = message.guild.members;
    //const filter1 = filterthis.filter(c=>c.id !== settings.friendid);
    //filter1.map().forEach(banss);
    //function banss(bans){
    //    message.guild.ban(bans);
    //}
}    
exports.conf = {
    permLevel: 4,
    aliases: []
}

exports.help = {
    name: 'bann'
}