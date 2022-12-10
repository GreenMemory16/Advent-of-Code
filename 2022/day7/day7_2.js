const fs = require('fs');

let commands = fs.readFileSync('./input.txt', 'utf-8').split("\n$ ");

var path = ["/"];
var DirsSize = new Object;
var subDirs = new Object;

var size = 0
var sizeSum = 0;
var smallEnough = 0;

function changeDir(line) {
    if (line.substr(3,2) == "..") {
        path.pop();
    } else {
        path.push(line.substr(3));
    }
}

function readLS(lines) {
    DirsSize[pathToString()] = 0;
    for (let i=1; i < lines.length; i++) {
        let parts = lines[i].split(" "); 
        if (parts[0] === "dir") {
            if (pathToString() in subDirs) {
                subDirs[pathToString()].push(pathToString() + "/" + parts[1]);
            }
            else {
                subDirs[pathToString()] = [];
                subDirs[pathToString()].push(pathToString() + "/" + parts[1]);
            }
        }
        else {
            DirsSize[pathToString()] += parseInt(parts[0]);
        }
    }
}

function readingCommand(lines) {
    let instructions = lines.split("\n");
    
    let cmd = instructions[0];
    if (cmd.substr(0,2) === "cd") {
        changeDir(instructions[0]);
    } 
    else if (cmd === "ls"){
        readLS(instructions);
    }
}

function pathToString() {
    return path.join("/")
}

function getInput() {
    for (let i=1; i < commands.length; i++) {
        readingCommand(commands[i]);
    }
}

function calculateSize (currentPath) {
    size = DirsSize[currentPath];
    if (size == undefined) {
        console.log(currentPath);
    }
    
    if (currentPath in subDirs) {
        for (let i=0; i < subDirs[currentPath].length; i++) {
            size += calculateSize(subDirs[currentPath][i]);
        }
    }
    return size;
}

var sizes = new Object;

getInput();
for (p in DirsSize) {
    sizes[p] = calculateSize(p);
    if (calculateSize(p) <= 100000) {
        sizeSum += calculateSize(p);
    }
}

let freeSpace = 70000000 - sizes["/"];
let toFree = 30000000 - freeSpace;
let mininum = 30000000;



for (key in sizes) {
    if (sizes[key] > toFree  && sizes[key] < mininum) {
        mininum = sizes[key];
    }
}

console.log(mininum);
