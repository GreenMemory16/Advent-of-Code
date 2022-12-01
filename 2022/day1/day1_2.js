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

elfs.push(sum);

var index = 0;
sum = 0;

for (let i = 0; i < 3; i++) {
    index = elfs.indexOf(Math.max.apply(Math, elfs));
    sum += elfs[index];
    elfs.splice(index, 1);
}

console.log(sum);