def calculate_square_area(side: int = 1) -> int: 
    return side * side

area = calculate_square_area()

print(f"The area of the square is {area}")

def build_ferrari(color = "red"):
    print(f"Built a {color} Ferrari")

build_ferrari("blue")