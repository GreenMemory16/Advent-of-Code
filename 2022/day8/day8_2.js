const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');

var highest = 0;

function calculateScore(x, y) {
    return fromRight(x, y) *  fromLeft(x, y) * fromTop(x, y) * fromBottom(x, y);
}

function fromRight(x, y) {
    let treeVal = lines[x][y];
    for(let i=x-1; i>=0; i--) {
        if (lines[i][y] >= treeVal) {
            return x-i;
        }
    }
    return x;
}

function fromLeft(x, y) {
    let treeVal = lines[x][y];
    for (let i=x+1; i < lines.length; i++) {
        if (lines[i][y] >= treeVal) {
            return i-x;
        }
    }
    return lines[0].length - 1 - x;
}

function fromTop(x, y) {
    let treeVal = lines[x][y];
    for (let i=y-1; i>=0; i--) {
        if (lines[x][i] >= treeVal) {
            return y-i;
        }
    }
    return y;
}

function fromBottom(x, y) {
    let treeVal = lines[x][y];
    for (let i=y+1; i < lines[0].length; i++) {
        if (lines[x][i] >= treeVal) {
            return i-y;
        }
    }
    return lines.length - 1 - y;
}

function runThroughForest() {
    for (let i=0; i < lines.length; i++) {
        for (let j=0; j < lines[i].length; j++) {
            let score = calculateScore(i, j);
            if (score > highest) {
                highest = score;
            }
        }
    }
}

runThroughForest();
console.log(highest);