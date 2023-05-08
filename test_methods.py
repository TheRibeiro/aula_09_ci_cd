import methods
 
def test_areaRectangle():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeterRectangle():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

# ------------- THE BASIC OPERATIONS ------------

def test_sum():
    # given two numbers 
    num1 = 31
    num2 = 10

    # when we calculate the sum
    output = methods.math_sum(num1, num2)
    
    # then the sum should be 41
    assert output == 41

def test_subtraction():
    # given two numbers 
    num1 = 45
    num2 = 5

    # when we calculate the subtraction
    output = methods.math_subtraction(num1, num2)
    
    # then the subtraction should be 40
    assert output == 40

def test_multiplication():
    # given two numbers 
    num1 = 4
    num2 = 6

    # when we calculate the multiplication
    output = methods.math_multiplication(num1, num2)
    
    # then the multiplication should be 24
    assert output == 24

def test_division():
    # given two numbers 
    num1 = 25
    num2 = 5

    # when we calculate the division
    output = methods.math_division(num1, num2)
    
    # then the division should be 5
    assert output == 5


# --------------------------------------------------------


# Operations for test

def test_raised():
    # given two numbers 
    num1 = 3
    num2 = 2

    # when we calculate the raise
    output = methods.math_raised(num1, num2)
    
    # then the raise should be 9
    assert output == 9

def test_squareRoot():
    # given the number you want to take the square root 
    num = 25
    

    # when we calculate the Square Root
    output = methods.math_squareRoot(num)
    
    # then the squareRoot should be 5
    assert output == 5


def test_areaSquare():
    # given the side of the Square  
    side = 2

    # when we calculate the area
    output = methods.area_of_square(side)

    # then the area should be 4
    assert output == 4
 
def test_perimeterSquare():
    # given the side of the Square  
    side = 2

    # when we calculate the perimeter
    output = methods.perimeter_of_square(side)
    
    # then the perimeter should be 8
    assert output == 8

def test_areaTriangle():
    # given a width of 4 and a height of 10
    width = 4
    height = 10

    # when we calculate the area
    output = methods.area_of_triangle(width, height)

    # then the area should be 20
    assert output == 20
 
def test_perimeterTriangle():
    # given the 3 sides
    side1 = 4
    side2 = 10
    side3 = 15

    # when we calculate the perimeter
    output = methods.perimeter_of_triangle(side1, side2, side3)
    
    # then the perimeter should be 29
    assert output == 29