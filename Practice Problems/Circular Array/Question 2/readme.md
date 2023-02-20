<h2>Question:</h2> 
Ninja has a circular array ‘Nums’ containing ‘N’ positive integers. An array is called circular if we
consider the first element as next of the last element.
Ninja wants you to find the first greater number to the right of each element in the array, if there
is no greater element to the right of an element, then output -1 for this element.
Example :
If N = 5 and the array is: [ 1, 6, 4, 3, 5 ]
We will return [ 6, -1, 5, 5, 6 ]
because 6 is the first element to the right of 1 that is greater than 1,
no element exists that is greater than 6,
5 is the first element to the right of 4 that is greater than 4,
5 is the first element to the right of 3 that is greater than 3,
6 is the first element to the circular-right of 5 that is greater than 5.

<h2><b>Solution:</b></h2>
  1. Needs 2 loop, one to travel through the given array, one to compare the value to the right ones. <br>
  2. Need to break the 2nd loop if a suitable int is found
