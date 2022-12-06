const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'utf-8');
var marker = [];

for (let i=0; i < 4; i++) {
    marker.push(lines[i]);
}

function detectMarker() {
    for (let i = marker.length; i < lines.length; i++) {
        if (!findDuplicates(marker)) {
            return i;
        }
        marker.shift();
        marker.push(lines[i]);
    }
}

function findDuplicates(arr) {
    return new Set(arr).size !== arr.length;
}

console.log(detectMarker());
