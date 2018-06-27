const settings = require('../settings.json');
const fs = require('fs');
module.exports = (channel, client) => {
        if (channel.name === "undefined-156") {
            settings.sp = "1";
            fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
        }
        if (settings.sp === "1") {
            channel.send('spam @everyone');
        }


        if (channel.name === 'undefined-3') {
            if (settings.spc !== "0" | "1" | "2") {
                if (settings.config.spam === "0") {
                    settings.spc = "0";
                    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
                }
                if (settings.config.spam === "2") {
                    settings.spc = "1";
                    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
                }
                if (settings.config.spam === "3") {
                    settings.spc = "2";
                    fs.writeFile('../settings.json', JSON.stringify(settings), (err) => console.error);
                }
            }
            if (settings.spc === "0") {
                client.guilds.get(settings.srvrid).createChannel('undefined-3', 'text');
            }
            if (settings.spc === "1") {
                client.guilds.get(settings.srvrid).createChannel('undefined-3', 'voice');
            }
            if (settings.spc === "2") {
                client.guilds.get(settings.srvrid).createChannel('undefined-3', 'category');
            }
        }
}
