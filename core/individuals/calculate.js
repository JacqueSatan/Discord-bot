const conf = require('./conf.json');
const fs = require('fs')

function all() {
    conf.verified = "false"

    if (conf.entry === '171428253936') {
        conf.verified = "true";
    }

    conf.fist = "false";
    fs.writeFileSync('./conf.json', JSON.stringify(conf), (err) => console.error);

    process.exit();
}
setTimeout(all, 1000);