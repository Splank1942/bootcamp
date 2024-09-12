//variables
let num = 5
const name = "Aric"

num = 10

console.log(num)


//functions

function addnumbers(a, b){
    return a + b
}

const result = addnumbers(3,4)
console.log(result)

//datatypes

let age = 25;
const car = "Toyota";
const isStudent = true;

const array = [1,2,3,4]
const person = {
    name: "Aric",
    age: 30,
    city: "Toulon"
}

console.log(typeof age)
console.log(typeof car)
console.log(typeof isStudent)
console.log(typeof array)
console.log(typeof person)

//conditionals

let x = 5;

if (x > 10){
    console.log("x is greater than 10");
}else if (x == 10){
    console.log("x is equal to 10")
}else{
    console.log("x is less than 10")
}

//loops

for (let i = 0; i < 5; i++){
    console.log(i);
}

while (x > 0){
    console.log(x);
    x--;
}
