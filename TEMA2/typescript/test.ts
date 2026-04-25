import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });
const { floor, random } = Math;

let x : number = 4;
let y : string = "4";
console.log(typeof(x+y))

rl.close();