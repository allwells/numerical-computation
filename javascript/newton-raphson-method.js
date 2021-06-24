// Formula: Xn+1 = Xn + C/Xn

let X0 = 2;
let C = 5;

console.log("Formula: Xn+1 = Xn + C/Xn\n");
console.log("X0: " + X0);

for (let n = 1; n < 11; n++) {
  let Xn = (X0 + C / X0) / 2;
  if (Xn == X0) {
    break;
  } else {
    console.log("X" + n + ": " + Xn.toFixed(6));
    X0 = Xn;
  }
}
