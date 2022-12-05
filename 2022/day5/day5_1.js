const fs = require('fs');

var from = 0;
var quantity = 0;
var column = 0;

let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');

var crates =  [ ['Z', 'J', 'G'],
                ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],
                ['F', 'P', 'M', 'C', 'L', 'G', 'R'],
                ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
                ['G', 'C', 'F', 'S', 'V', 'Q'],
                ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
                ['H', 'F', 'S', 'B', 'V'],
                ['F', 'J', 'Z', 'S'],
                ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']];
    
for (let i=0; i < lines.length; i++) {
    lines[i] = lines[i].split(' ');
    quantity = lines[i][1];
    from = lines[i][3];
    column = lines[i][5];
    move(quantity, from, column);
}

function move(q, f, c) {
    for (let i=0; i < q; i++) {
        crates[c-1].push((crates[f-1].pop()));
    }
}

function printCrates() {
    let l = "";
    for (let i=0; i < crates.length; i++) {
        l = i+1 + ":  ";
        for (let j=0; j < crates[i].length; j++) {
            l += crates[i][j]; + ' ';
        }
        console.log(l);
        l = ' ';
    }
}

printCrates();
