
/*setTimeout(reminder, 1000)*/

// задание 1

/*i= 25;
x=(i*9/5)+32;
function reminder (){
      alert(x)
}*/

// задание 2 

/*let a= 32;
let b= 23;

setTimeout(three, 2000)


function three() {
    let a=36; let by=10; 
    if (a>0|b>0)
        console.log(a-b);
    else if (a<0|b<0)
        console.log(a*b);
    else (a<0,b>0)|(a>0,b<0)
        console.log(a+b);
}
three()
*/





// задание 3

/*$a = 15;
	switch ($a) {
		case 1:
			echo "1";
		case 2:
			echo "2";
		case 3:
			echo "3";
		case 4:
			echo "4";
		case 5:
			echo "5";
		case 6:
			echo "6";
		case 7:
			echo "7";
		case 8:
			echo "8";
        case 9:
			echo "9";
        case 10:
			echo "10";
        case 11:
			echo "11";
        case 12:
			echo "12";
        case 13:
			echo "13";
        case 14:
			echo "14";
        case 15:
			echo "15";
		break;
	
		}*/

	// задание 4	
/*function sum($arg1, $arg2) {
	return $arg1 + $arg2;
	}
		
function subtraction($arg1, $arg2) {
	return $arg1 - $arg2;
	}
		
function multiply($arg1, $arg2) {
	return $arg1 * $arg2;
	}
function divide($arg1, $arg2) {
	return ($arg2 === 0) ? "invalid arg2 value (=0)" : $arg1 / $arg2;
	}	*/


// задание 5

/*function mathOperation($arg1, $arg2, $operation) {
	switch ($operation) {
		case "sum": 
			return $arg1 + $arg2;
		case "subtraction":
			return $arg1 - $arg2;
		case "multiply":
			return $arg1 * $arg2; 
		case "divide":
			if ($arg2 === 0) {
				echo "invalid arg2 value (=0)";
				break;
			}
			return $arg1 / $arg2;
		}
	}
	echo mathOperation(10, 0, divide);
	*/


// задание 6

/*function power($val, $pow) {
		return ($pow == 1) ? $val : $val * power($val, $pow - 1);
	}
	echo power(5, 3);
	*/


	// задание 7


function fibonacci (n, prev1, prev2) {
	var current = prev1 + prev2;
	var fibonacci_string = current + " ";
	if (n>1)
		fibonacci_string += fibonacci (n-1, current, prev1);
}
