const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');

var positions = new Object();

var x_head = 0;
var y_head = 0;
var x_tail = 0;
var y_tail = 0;

function move(move) {
    let data = move.split(" ");
    let side = 0
    switch (data[0]) {    
        case "U":
            side = 1;
            move_y(side, data[1]);
            break;
        case "D":
            side = -1;
            move_y(side, data[1]);
            break;
        case "R":
            side = 1;
            move_x(side, data[1]);
            break;
        case "L":
            side = -1;
            move_x(side, data[1]);
            break;
    }
    
}

function move_x(side, amount) {
    for (let i=0; i < amount; i++) {
        x_head += side;
        if (!tailTouching()) {
            move_tail(side);
        }
        positions[[x_tail, y_tail]] = 1;
    }
}

function move_y(side, amount) {
    for (let i=0; i < amount; i++) {
        y_head += side;
        if (!tailTouching()) {
            move_tail(side);
        }
        positions[[x_tail, y_tail]] = 1;
    }
}

function move_tail(side) {
    if (x_head === x_tail) {
        y_tail += side;
    }
    else if (y_head === y_tail) {
        x_tail += side;
    }
    else {
        if (x_head > x_tail && y_head > y_tail) {
            x_tail += 1;
            y_tail += 1;
        }
        else if (x_head > x_tail && y_head < y_tail) {
            x_tail += 1;
            y_tail -= 1;
        }
        else if (x_head < x_tail && y_head > y_tail) {
            x_tail -= 1;
            y_tail += 1;
        }
        else if (x_head < x_tail && y_head < y_tail) {
            x_tail -= 1;
            y_tail -= 1;
        }
    }
}

function tailTouching() {
    if (x_tail === x_head) {
        if (Math.abs(y_head - y_tail) <= 1) {
            return true;
        }
    }
    else if (y_head === y_tail) {
        if (Math.abs(x_head - x_tail) <= 1) {
            return true;
        }
    }
    else if (Math.abs(x_head - x_tail) <= 1 && Math.abs(y_head - y_tail) <= 1) {
        return true;
    }

    return false;
}

function countPositions() {
    let sum = 0;
    for (key in positions) {
        sum++;
    }

    return sum;
}

function startPath() {
    for (let i=0; i < lines.length; i++) {
        move(lines[i]);
    }
}

startPath();
console.log(countPositions());
