const fs = require('fs');

const ROCK = "X";
const PAPER = "Y";
const SCISSORS = "Z"; 
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
                case ROCK:
                    score += 4;
                    break;
                case PAPER:
                    score += 8;
                    break;
                case SCISSORS:
                    score += 3;
                    break;
            }
            break;
        case _PAPER:
            switch (play[1]) {
                case ROCK:
                    score += 1;
                    break;
                case PAPER:
                    score += 5;
                    break;
                case SCISSORS:
                    score += 9;
                    break;

            }
            break;
        case _SCISSORS:
            switch (play[1]) {
                case ROCK:
                    score += 7;
                    break;
                case PAPER:
                    score += 2;
                    break;
                case SCISSORS:
                    score += 6;
                    break;

            }
            break;
    }
}

console.log(score);
