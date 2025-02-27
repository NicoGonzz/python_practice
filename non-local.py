def outer_function():
    x = 'enclosing'
    def inner_function():
        nonlocal x
        x = 'modified_value'
        print(f'El valor modificado es {x}')
    inner_function()
    print(f'El valor de la variable es {x}')
outer_function()