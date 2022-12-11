const fs = require('fs');

let lines = fs.readFileSync('./input2.txt', 'utf-8').split('\n')

class monkey {
    constructor(num, items, operation, division, numTrue, numFalse) {
        this.num = num;
        this.items = items;
        this.operation = operation;
        this.division = division;
        this.numTrue = numTrue;
        this.numFalse = numFalse;
    }
};

var monkeys = [];
var inspections = [0, 0, 0, 0, 0, 0, 0, 0]
var toRemove = [];

for (let i=0; i < lines.length; i+=7) {
    let line = lines[i].split(' ');
    if (line[0] == "Monkey") {
        let monkeyNum = parseInt(line[1][0]);
        let worries = [];
        line = lines[i+1].split(' ');
        
        for (let j=4; j < line.length; j++) {
            worries.push(parseInt(line[j]));
        }

        line = lines[i+2].split('= ');
        let operation = line[1];
        line = lines[i+3].split(' ');
        let division = parseInt(line[5]);
        line = lines[i+4].split(' ');
        let monkeyTrue = parseInt(line[9]);
        line = lines[i+5].split(' ');
        let monkeyFalse = parseInt(line[9]);

        let monk = new monkey(monkeyNum, worries, operation, division, monkeyTrue, monkeyFalse);
        monkeys.push(monk);
    }
}

for (let j=0; j < 20; j++) {
    for (let i=0; i < monkeys.length; i++) {
        for (let it=0; it < monkeys[i].items.length; it += 1) {
            inspections[i]++;

            let op = monkeys[i].operation.split(' ')
            let currentItem = monkeys[i].items[it];

            if (op[1] == "+") {
                if (op[2] == "old") {
                    currentItem = currentItem + currentItem;
                }
                else {
                    currentItem = currentItem + parseInt(op[2]);
                }
            }
            else if (op[1] == "*") {
                if (op[2] == "old") {
                    currentItem = currentItem * currentItem;
                }
                else {
                    currentItem = currentItem * parseInt(op[2]);
                }
            }

            currentItem = Math.floor(currentItem / 3);

            if (currentItem % monkeys[i].division === 0) {
                toRemove.push(it);
                monkeys[monkeys[i].numTrue].items.push(currentItem);
            }
            else {
                toRemove.push(it);
                monkeys[monkeys[i].numFalse].items.push(currentItem);
            }
        }
        
        monkeys[i].items = [];
    }
}

let highest = Math.max(...inspections);
inspections.splice(inspections.indexOf(Math.max(...inspections)),1);
console.log(inspections);
let highest2 = Math.max(...inspections);

console.log(highest * highest2);
