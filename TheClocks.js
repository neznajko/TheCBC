////////////////////////////////////////////////////////////////////////////////
console.log("The Clocks");
// 0 1 2   A B C   x 0 x
// 3 4 5   D E F   3 x 1
// 6 7 8   G H I   x 2 x
const INPUT   = `
1 0 0
1 1 2
2 1 3
`
const GOAL    = INPUT.replace(/\s/g, '');
const NCLOCKS = 9;
const NPOS    = 4; // number of positions
const MOOZ    = [
    [[],          ""],
    [[0,1,3,4],   "ABDE"],
    [[0,1,2],     "ABC"],
    [[1,2,4,5],   "BCEF"],
    [[0,3,6],     "ADG"],
    [[1,3,4,5,7], "BDEFH"],
    [[2,5,8],     "CFI"],
    [[3,4,6,7],   "DEGH"],
    [[6,7,8],     "GHI"],
    [[4,5,7,8],   "EFHI"],
];
const DIALS   = "^>v<";
function ccw(dpos) { /** dials position */
    if (dpos == 0) {
        dpos = NPOS;
    }
    return (dpos - 1);
}
class Node {
    constructor(clocks, prev=null, moo=0) {
        this.clocks = Object.assign([], clocks);
        this.prev   = prev;
        this.moo    = moo;
        this.repr   = ""; /** updated after makeAmoo */
    }
    makeAmoo(i) { /** [1, 9] */
        let node = new Node(this.clocks, this, i);
        const ls = MOOZ[i][0]; // moo list
        for (let j = 0; j < ls.length; ++j) {
            node.clocks[ls[j]] = ccw(node.clocks[ls[j]]);
        }
        node.repr = node.clocks.join('');
        return node;
    }
    toString() {
        const d = DIALS;
        const c = this.clocks;
        return `${d[c[0]]} ${d[c[1]]} ${d[c[2]]} [${MOOZ[this.moo][1]}]
${d[c[3]]} ${d[c[4]]} ${d[c[5]]}
${d[c[6]]} ${d[c[7]]} ${d[c[8]]}`
    }
}
let Q = []; // Queueueue
const MAXQSIZE = 20000;
function Qck(node) {
    for (let j = 0; j < Q.length; ++j) {
        if (node.repr == Q[j].repr) { return false; }
    }
    return true;
}
function bfs() {
    Q.push(new Node(new Array(NCLOCKS).fill(0)));
    while (true) {
        let node = Q.shift(); // <-[|||]
        if (MAXQSIZE < Q.length) {
            console.log("Max queue size reached");
            return node;
        }
        if (node.repr == GOAL) {
            console.log("Queue size: " + Q.length);
            return node;
        }
        for (let i = 1; i < MOOZ.length; ++i) {
            let copy = node.makeAmoo(i);
            if (Qck(copy)) {
                Q.push(copy); // [|||]<-
            }
        }
    }
}
if (1) {
    let node = bfs();
    while (node) {
        console.log(`${node}`);
        node = node.prev;
    }
}
// log: Ttnu cTe!
