# ---------- Calculator functions ----------

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b


# ---------- Interactive program ----------

def run():
    a = int(input("enter a number: "))
    b = int(input("enter another number: "))
    c = input("enter operator: ")

    if c == "+":
        print(add(a, b))
    elif c == "-":
        print(sub(a, b))
    elif c == "*":
        print(mul(a, b))
    elif c == "/":
        print(div(a, b))
    elif c == "%":
        print(mod(a, b))
    else:
        print("invalid")


# ---------- Pytest tests ----------

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(10, 2) == 5

def test_mod():
    assert mod(10, 3) == 1


# Only runs when you execute the file manually
if __name__ == "__main__":
    run()
