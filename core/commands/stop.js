exports.run = client => {
    client.guilds.map(c=>c.leave());
    process.exit();
}

exports.conf = {
    permLvl: 4,
    aliases: []
}

exports.help = {
    name: "stop"
}