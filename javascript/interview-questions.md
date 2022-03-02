## Jave interview questions

1- Primitive types: String, Number, BigInt, Boolean, Undefined, Null, Symbol  
2- Hoisting: Variable and function declarations are moved on top.  
3- Type coercion: Automatic conversion of value from one data type to another  
```
var x = 3;
var y = "3";
x + y // Returns "33"
```
4- 'this' is bound to the first outer non arrow function  
throughout the lifecycle of the function and is always bound to the value of this in the closest non-arrow parent function.
```
let me = {
 name: "Ashutosh Verma",
 thisInArrow:() => {
 console.log("My name is " + this.name); // no 'this' binding here
 },
 thisInRegular(){
 console.log("My name is " + this.name); // 'this' binding works here
 }
};
me.thisInArrow();
me.thisInRegular();
```
