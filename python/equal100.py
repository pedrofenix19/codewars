#123456789 == 100

def is100(signos):
    expression = "1%s2%s3%s4%s5%s6%s7%s8%s9 == 100" % tuple(signos)
    if eval(expression):
        print(expression)
    return

def generate_expression(signos):
    if(len(signos) == 8):
        is100(signos)
        return
    
    generate_expression(signos + ["+"])
    generate_expression(signos + ["-"])
    generate_expression(signos + [""])
    return


if __name__ == "__main__":
    generate_expression([])