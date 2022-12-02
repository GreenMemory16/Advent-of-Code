const fs = require('fs');

const LOSS = "X";
const DRAW = "Y";
const WIN = "Z"; 
const _ROCK = "A";
const _PAPER = "B";
const _SCISSORS = "C";

var score = 0;

let lines = fs.readFileSync('./input.txt', 'utf-8').split('\n');

for (let i = 0; i < lines.length; i++) {
    var play = lines[i].split(' ');

    switch(play[0]) {
        case _ROCK:
            switch (play[1]) {
                case LOSS:
                    score += 3;
                    break;
                case DRAW:
                    score += 4;
                    break;
                case WIN:
                    score += 8;
                    break;
            }
            break;
        case _PAPER:
            switch (play[1]) {
                case LOSS:
                    score += 1;
                    break;
                case DRAW:
                    score += 5;
                    break;
                case WIN:
                    score += 9;
                    break;

            }
            break;
        case _SCISSORS:
            switch (play[1]) {
                case LOSS:
                    score += 2;
                    break;
                case DRAW:
                    score += 6;
                    break;
                case WIN:
                    score += 7;
                    break;

            }
            break;
    }
}

console.log(score);