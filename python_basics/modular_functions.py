import math

# Function to calculate the area of different shapes
def calculate_area(shape, dimension1, dimension2=0):
    shape = shape.lower() 
    if shape == "circle":  
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return "Invalid shape"

# Testing the function with different shapes
circle_area = calculate_area("circle", 5)  # Radius = 5
rectangle_area = calculate_area("rectangle", 4, 6)  # Length = 4, Width = 6
triangle_area = calculate_area("triangle", 3, 8)  # Base = 3, Height = 8

print(f"Area of the circle with radius 5: {circle_area:.2f}")
print(f"Area of the rectangle with length 4 and width 6: {rectangle_area}")
print(f"Area of the triangle with base 3 and height 8: {triangle_area}")