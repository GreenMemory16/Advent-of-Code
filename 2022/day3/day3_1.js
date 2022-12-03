const fs = require('fs');

var stream1;
var stream2;
var sum = 0;

let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');


function getLetter(stream1, stream2) {
    for (let i=0; i < stream1.length; i++) {
        for (let j=0; j < stream2.length; j++) {
            if (stream1.charAt(i) === stream2.charAt(j)) {
                return stream1.charAt(i);
            }
        }
    }

    return ""; 
}

function getLetterValue(letter) {
    if (letter.charCodeAt() < 97) {
        return letter.charCodeAt() - 38;
    }
    else {
        return letter.charCodeAt() - 96;
    }
}

for (let i=0; i < lines.length; i++) {
    stream1 = lines[i].substr(0, lines[i].length/2);
    stream2 = lines[i].substr(lines[i].length/2);
    sum += getLetterValue(getLetter(stream1, stream2));
}

console.log(sum);
