const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');

var count = 0;

function isVisible(x, y) {
    return visibleFromTop(x, y) || visibleFromBottom(x, y) || visibleFromRight(x, y) || visibleFromLeft(x, y);
}

function visibleFromRight(x, y) {
    let treeVal = lines[x][y];
    for(let i=0; i < x; i++) {
        if (lines[i][y] >= treeVal) {
            return false;
        }
    }
    return true;
}

function visibleFromLeft(x, y) {
    let treeVal = lines[x][y];
    for (let i=x+1; i < lines.length; i++) {
        if (lines[i][y] >= treeVal) {
            return false;
        }
    }
    return true;
}

function visibleFromTop(x, y) {
    let treeVal = lines[x][y];
    for (let i=0; i<y; i++) {
        if (lines[x][i] >= treeVal) {
            return false;
        }
    }
    return true;
}

function visibleFromBottom(x, y) {
    let treeVal = lines[x][y];
    for (let i=y+1; i < lines[0].length; i++) {
        if (lines[x][i] >= treeVal) {
            return false;
        }
    }
    return true;
}

function isEdgeTree(x, y) {
    return x === 0 || y === 0 || x === lines[0].length-1 || y === lines[0].length-1;
}

function runThroughForest() {
    for (let i=0; i < lines.length; i++) {
        for (let j=0; j < lines[i].length; j++) {
            if (isEdgeTree(i, j) || isVisible(i, j)) { count++; }
        }
    }
}

runThroughForest();
console.log(count);
