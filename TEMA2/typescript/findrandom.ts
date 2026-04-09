import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });
const { floor, random } = Math;

function rand(n: number): number[] {
    const r: number[] = [];
    for (let i = 0; i < n; i++) {
        r.push(floor(random() * 100) + 1);
    }
    return r;
}

function find(x: number, n: number): string {
    const randNum = rand(n);
    let nx = 0;
    for (const i of randNum) {
        if (i === x) nx++;
    }
    return `La lista de numeros es ${randNum}\nEl numero ${x} sale ${nx} veces`;
}

const n = Number(await rl.question("Introduzca el limite: "));
const x = Number(await rl.question("Introduzca el numero a encontrar: "));
console.log(find(x, n));

rl.close();