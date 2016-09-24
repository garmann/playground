function Person(name, age, win) {
    this.name = name;
    this.age = age;
    this.win = win;

    this.hello = function() {
        console.log('Hello, my name is ' + this.name);
    };

    this.hasMoreWinsThan = function(obj) {
        if(this.win > obj.win ) {
            return true;
        } else {
            return false;
        }
    };
}

function getAverageAge() {
    sumAge = 0;

    for(var i in actors){
        sumAge += actors[i].age;
    }

    return sumAge / actors.length;
}

var pau = new Person('Paul', 41, 1);
var pie = new Person('Piet', 11, 1);
var fra = new Person('Franzi', 45, 0);
var mop = new Person('Moppi', 12, 3);
var rau = new Person('Raupe', 55, 0);

var actors = [leo, jen, sam, mer, joh];

/*

getAverageAge()
avg..

mop.hasMoreWinsThan(rau)
true or false...

*/