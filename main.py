from add import add
from sub import sub
from mul import mul

print("Welcome to the Git Calculator")

if __name__ == "__main__":
    a = 10
    b = 5

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {sub(a, b)}")
    print(f"Multiplication: {mul(a, b)}")