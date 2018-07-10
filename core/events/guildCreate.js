const settings = require('../settings.json');
module.exports = (guild, client) => {
    console.log('Le serveur "' + guild + '" a été rejoint.');
    function ready() {
        function type1(){
            client.guilds.get(settings.auto.server_id).channels.get(settings.auto.channel_id).send('attack');
        }
        function type2(){
            client.guilds.get(settings.auto.server_id).channels.get(settings.auto.channel_id).send('spam');
        }
        if (settings.auto.enabled === 0) {
            console.log('Le mode automatique est activé.');
            console.log('Il va attaquer sur le serveur "' + settings.auto.server_id + '" sur le salon "' + settings.auto.channel_id + '".');
            if (settings.auto.function === "1") { 
                setTimeout(type1, 2000);
            }
            if (settings.auto.function === "2") {
                setTimeout(type2, 2000);
            }
        }
    }
    setTimeout(ready, 1000);
}
