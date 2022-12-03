const fs = require('fs');

var stream1;
var stream2;
var sum = 0;

let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');


function getLetter(streams) {
    // Great complexity, I know
  
    for (let i=0; i < streams[0].length; i++) {
        for (let j=0; j < streams[1].length; j++) {
            for (let k=0; k < streams[2].length; k++) {
                if (streams[0].charAt(i) === streams[1].charAt(j) && 
                    streams[1].charAt(j) === streams[2].charAt(k) && 
                    streams[0].charAt(i) === streams[2].charAt(k)) {
                    return streams[0].charAt(i);
                }
            }
        }
    }

    return "ad"; 
}

function getLetterValue(letter) {
    if (letter.charCodeAt() < 97) {
        return letter.charCodeAt() - 38;
    }
    else {
        return letter.charCodeAt() - 96;
    }
}

for (let i=0; i < lines.length; i+=3) {
    stream1 = lines[i]
    stream2 = lines[i];
    sum += getLetterValue(getLetter([lines[i], lines[i+1], lines[i+2]]));
}

console.log(sum);