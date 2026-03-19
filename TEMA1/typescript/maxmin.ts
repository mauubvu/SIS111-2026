import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });

function maxmin(a: number, b: number, c: number, mayor: number = 0, menor: number = 0): string {
    if (a >= b && a >= c) { mayor = a;
    } else if (b >= a && b >= c) { mayor = b;
    } else { mayor = c;
    } if (a <= b && a <= c) { menor = a;
    } else if (b <= a && b <= c) { menor = b;
    } else { menor = c;
    }
    return `Mayor:${mayor} Menor:${menor}`;
}

const a = Number(await rl.question("Introduzca el primer numero: "));
const b = Number(await rl.question("Introduzca el segundo numero: "));
const c = Number(await rl.question("Introduzca el tercer numero: "));
console.log(maxmin(a,b,c));
rl.close();