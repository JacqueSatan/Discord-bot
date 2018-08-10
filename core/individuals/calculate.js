const conf = require('./conf.json');
const fs = require('fs')

function all() {
    conf.verified = "false"

    if (conf.entry === 'je suce des bites') {
        console.log('code ok');
        if (conf.you === 'hariel' | 'Psyko') {
            console.log('user ok');
           conf.verified = "true";

        } else {
            console.log('user faux');
        }
    } else {
        console.log('code faux');
    }

    conf.fist = "false";
    fs.writeFileSync('./conf.json', JSON.stringify(conf), (err) => console.error);

    process.exit();
}
setTimeout(all, 1000);