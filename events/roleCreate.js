module.exports = message => {
    const role = message.guild.roles.find('name', 'undefined-1');
    if (role) {
        message.guild.createRole({
            name: 'undefined-1'
        });
    }
}