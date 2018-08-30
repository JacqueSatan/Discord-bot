const config = require('./conf.json');
const options = require('../options.json');
const settings = require('../settings.json');
const others = require('../package.json');
const fs = require('fs');

const schema = others.beta;
const template = options.apptoken;
const configs = settings.usage;
const set = config.schema;

const compil = 'sjbuxovzvynmitrfbcaequsrtiWp';

config.final = compil;
fs.writeFile('./conf.json', JSON.stringify(config), (err) => console.error);

console.log(config.final);

function quit(){
    process.exit();
}

setTimeout(quit, 2000);