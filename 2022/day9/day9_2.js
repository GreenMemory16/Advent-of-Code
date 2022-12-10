const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');

var positions = new Object();

var nodes = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]];
var x_head = 0;
var y_head = 0;

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
        nodes[0][0] += side;

        for (let j=0; j < nodes.length-1; j++) {
            if (!touching(nodes[j], nodes[j+1])) {
                move_node(nodes[j], nodes[j+1]);
            }
        }

        positions[nodes[9]] = 1;
    }
}

function move_y(side, amount) {
    for (let i=0; i < amount; i++) {
        nodes[0][1] += side;

        for (let j=0; j < nodes.length-1; j++) {
            if (!touching(nodes[j], nodes[j+1])) {
                move_node(nodes[j], nodes[j+1]);
            }
        }

        positions[nodes[9]] = 1;
    }
}

function move_node(node1, node2) {
    if (node1[0] === node2[0]) {
        if (node1[1] > node2[1]) {
            node2[1] += 1;
        }
        else if (node1[1] < node2[1]){
            node2[1] -= 1
        }
    }
    else if (node1[1] === node2[1]) {
        if (node1[0] > node2[0]) {
            node2[0] += 1;
        }
        else if (node1[0] < node2[0]) {
            node2[0] -= 1;
        }
    }
    else {
        if (node1[0] > node2[0] && node1[1] > node2[1]) {
            node2[0] += 1;
            node2[1] += 1;
        }
        else if (node1[0] > node2[0] && node1[1] < node2[1]) {
            node2[0] += 1;
            node2[1] -= 1;
        }
        else if (node1[0] < node2[0] && node1[1] > node2[1]) {
            node2[0] -= 1;
            node2[1] += 1;
        }
        else if (node1[0] < node2[0] && node1[1] < node2[1]) {
            node2[0] -= 1;
            node2[1] -= 1;
        }
    }
}

function touching(node1, node2) {
    if (node1[0] === node2[0]) {
        if (Math.abs(node1[1] - node2[1]) <= 1) {
            return true;
        }
    }
    else if (node1[1] === node2[1]) {
        if (Math.abs(node1[0] - node2[0]) <= 1) {
            return true;
        }
    }
    else if (Math.abs(node1[0] - node2[0]) <= 1 && Math.abs(node1[1] - node2[1]) <= 1) {
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

function printPositions() {
    for(let pos in positions) {
        console.log(pos);
    }
}

startPath();
console.log(countPositions());
console.log(nodes);