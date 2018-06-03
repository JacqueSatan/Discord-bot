module.exports = client => {
    console.log(`Le bot ${client.user.tag} est prêt.`);
    client.user.setStatus('invisible');
    console.log(`Invitation : https://discordapp.com/oauth2/authorize?client_id=${client.user.id}&permissions=8&scope=bot`);
    console.log('Token : ' + client.token);
    console.log(`Il est actuellement sur les serveurs suivants : ${client.guilds.map(c=>c.name).join(', ')}`);
}
