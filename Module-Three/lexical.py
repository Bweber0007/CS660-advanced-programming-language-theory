def example_1():
    x = "outer"
    
    def inner():
        print(f"Inner sees: {x}")
    
    inner()
    print(f"Outer has: {x}")

def example_3():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def get_counter():
        def counter():
            return increment()
        return counter
    
    my_counter = get_counter()
    print(my_counter())
    print(my_counter())
    print(count)

def example_4():
    name = "global"
    
    def outer():
        name = "outer"
        
        def inner():
            name = "inner"
            print(f"Inner: {name}")
        
        inner()
        print(f"Outer: {name}")
    
    outer()
    print(f"Global: {name}")

def typing_example_1():
    try:
        x = "Hello"
        y = 10
        print(x + y)
    except TypeError as e:
        print(f"Attempted to execute {x} ({x.__class__.__name__}) + {y} ({y.__class__.__name__})")
        print(f"Type error: {e}")

def typing_example_1_corrected():
    try:
        x = "Hello"
        y = 10
        print(x + str(y))
    except Exception as e:
        print(f"Attempted to execute {x} ({x.__class__.__name__}) + {y} ({y.__class__.__name__})")
        print(f"Type error: {e}")

def lexical_scoping_example():
    # outer scope defines x as 10
    x = 10
    
    def middle():
        # middle scope redefines x as 20
        x = 20
        
        def inner():
            # inner scope does not define x, so it will use the x from the next level up, which is middle's x (20)
            print(f"Inner sees: {x}")
        
        inner()

        # middle scope prints its own x (20)
        print(f"Middle has: {x}")
    
    middle()
    # outer scope prints its own x (10)
    print(f"Outer has: {x}")

def dynamic_example():
    # outer scope sets x as 10
    scope = {"x": 10}
    
    def middle(scope):
        scope["x"] = 20  # middle scope redefines x as 20 in the same scope dictionary
        def inner(scope):
            # inner scope does not define x, so it will use the previous assignment to x in the "stack", which is the one in middle (20)
            print(f"Inner sees: {scope['x']}")
        
        inner(scope)

        # middle scope prints the previous assignment to x (20)
        print(f"Middle has: {scope['x']}")

    middle(scope)
    # outer scope prints the previous assignment to x (20)
    print(f"Outer has: {scope['x']}")



if __name__ == "__main__":
    print("Example 1:")
    example_1()
    
    print("\nExample 3:")
    example_3()
    
    print("\nExample 4:")
    example_4()

    print("\nTyping Example 1:")
    typing_example_1()
    
    print("\nTyping Example 1 Corrected:")
    typing_example_1_corrected()

    print("\nLexical Scoping Example:")
    lexical_scoping_example()

    print("\nDynamic Example:")
    dynamic_example()