const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'utf-8').split("\n");
let cycle = 1;
let X = 1;
let signalStrength = [];


function exeADDX(value) {
    // ADDX begins to execute
    cycle++;
    if (signalReady()) {
        registerSignal();
    }

    cycle++;
    X += parseInt(value);
    if (signalReady()) {
        registerSignal();
    }
}

function exeNOOP() {
    cycle++;
    if (signalReady()) {
        registerSignal();
    }
}

function signalReady() {
    if (cycle === 20 || cycle % 40 === 20) {
        return true;
    }

    return false;
}

function registerSignal() {
    signalStrength.push(cycle * X);
}

function countSingals() {
    let sum = 0;
    for (let i=0; i < signalStrength.length; i++) {
        sum += signalStrength[i];
    }

    return sum;
}

for (let i=0; i < lines.length; i++) {
    action = lines[i].split(" ");

    if (action[0] == "noop") {
        exeNOOP();
    }
    else if (action[0] == "addx") {
        exeADDX(action[1]);
    }
}

console.log(countSingals());
