// Task 1
var dairy = ['cheese', 'sour cream', 'milk', 'yogurt', 'ice cream', 'milkshake']
function logDairy () {
    for(var items of dairy){
        console.log(items);
    }
}

logDairy();
// Task 2
const animal = {

canJump: true

};

const bird = Object.create(animal);

bird.canFly = true;

bird.hasFeathers = true

function birdCan() {
    for(var key of Object.keys(bird)){
        console.log(key+": "+bird[key]);

    }
}

birdCan();

// Task 3

function animalCan(){
    for(var key in bird){
        console.log(key+": "+bird[key]);
    }
}
animalCan();