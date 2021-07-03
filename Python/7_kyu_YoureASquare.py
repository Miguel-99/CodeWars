"""
Task

Given an integral number, determine if it's a square number:

    In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.
Examples

-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
"""
def is_square(n):    
	if n<0: 
		return False
	return int(n**(1/2))**2 == n

""" 
test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
test.assert_equals(is_square( 0), True, "0 is a square number (0 * 0)")
test.assert_equals(is_square( 3), False, "3 is not a square number")
test.assert_equals(is_square( 4), True, "4 is a square number (2 * 2)")
test.assert_equals(is_square(25), True, "25 is a square number (5 * 5)")
test.assert_equals(is_square(26), False, "26 is not a square number")
"""
print(is_square(-1)) #False
print(is_square( 0)) #True
print(is_square( 3)) #False
print(is_square( 4)) #True
print(is_square(25)) #True
print(is_square(26)) #False