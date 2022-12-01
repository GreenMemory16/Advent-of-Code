const fs = require('fs');

var sum = 0;
var elfs = [];

let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');

for (let i = 0; i < lines.length; i++) {
    if(lines[i] == "") {
        elfs.push(sum);
        sum = 0;
    }
    else {
        sum += parseInt(lines[i]);
    }
}

console.log(Math.max.apply(Math, elfs));