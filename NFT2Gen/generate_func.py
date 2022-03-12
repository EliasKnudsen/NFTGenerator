import random
def generate_function(depth):

    funcs = [
        {
            "name": "push_rand",
            "num_params": 0,
        },
        {
            "name": "push",
            "num_params": 0,
        },
        { 
            "name": "sin",
            "num_params": 1, 
        },
        {
            "name": "cos",
            "num_params": 1,
        },
        {
            "name": "tan",
            "num_params": 1,
        },
        {
            "name": "abs",
            "num_params": 1,
        },
        {
            "name": "log",
            "num_params": 1,
            "requires_abs": True,
        },
        {
            "name": "sqrt",
            "num_params": 1,
            "requires_abs": True,
        },
        {
            "name": "pow",
            "num_params": 2
        },
        {
            "name": "div",
            "num_params": 2,
            "sym": "/",
        },
        {
            "name": "add",
            "num_params": 2,
            "sym": " + ",
        },
        {
            "name": "sub",
            "num_params": 2,
            "sym": " - ",
        },
        {
            "name": "mul",
            "num_params": 2,
            "sym": " * "
        },
    ]
    assert depth > 0, "Must pass positive depth in generate"

    stack = []

    def push_two(func):
        name, num_params = func["name"], func["num_params"]


        if "sym" in func:
            sym = func["sym"]
            name = "" 
        else:
            sym = ", "

        params = []

        for _ in range(num_params):
            el = stack.pop()
            params.append(el)

        params.reverse()

        to_push = name + "("

        for i, e in enumerate(params):
            to_push += e
            if i == len(params)-1:
                to_push += ")"
            else:
                to_push += sym

        stack.append(to_push)

    for i in range(depth):
        lst = [x for x in funcs if x["num_params"] <= len(stack)]
        func = random.choice(lst)
        stack.append("x")
        stack.append("y")
        name, num_params = func["name"], func["num_params"]

        if num_params == 0:
            if name == "push":
                var = random.choice(["x", "y"])
                stack.append(var)
            elif name == "push_rand":
                var = str(random.randint(-500, 501))
            elif name == "push_uniform":
                var = "random.randint(-10000,10000)"
            else:
                assert False, "Exhaustive name handling when num_params is 0"

            stack.append(var)
            continue


        if num_params == 1:
            el = stack.pop()
            
            if "requires_abs" in func:
                el = f"abs({el})"


            stack.append(f"{name}({el})")
        else: 
            push_two(func)


    while len(stack) > 1:
        lst = [x for x in funcs if x["num_params"] >= 2]
        func = random.choice(lst)

        push_two(func)

    return stack[0]

