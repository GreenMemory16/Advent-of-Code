const fs = require('fs');

let count = 0;
let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');
let pairs = [];

function isOverlaped(pair1, pair2) {
    console.log(pair1 + "  " + pair2)
    if ((parseInt(pair1[0]) >= parseInt(pair2[0]) && parseInt(pair1[1]) <= parseInt(pair2[1])) || (parseInt(pair2[0]) >= parseInt(pair1[0]) && parseInt(pair2[1]) <= parseInt(pair1[1]))) {
        count ++;
    }
}

for (let i=0; i < lines.length; i++) {
    pairs = lines[i].split(',');
    isOverlaped(pairs[0].split('-'), pairs[1].split('-'));
}

console.log(count);