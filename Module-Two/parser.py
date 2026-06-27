"""
Simple Arithmetic Interpreter

Grammar Rules:
expression -> term (('+' | '-') term)*
term -> factor ('*' factor)*
factor -> number | '(' expression ')'
number -> digit digit*
digit -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

"""

class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Parser:
    def __init__(self, expression):
        self.expr = expression.replace(' ', '')
        self.pos = 0
        self.current_char = self.expr[0] if self.expr else None

    def advance(self):
        self.pos += 1
        self.current_char = self.expr[self.pos] if self.pos < len(self.expr) else None

    def parse_number(self):
        num = ""

        while self.current_char is not None and self.current_char.isdigit():
            num += self.current_char
            self.advance()

        return NumberNode(int(num))

    def parse_factor(self):
        if self.current_char == '(':
            self.advance()  # Skip '('
            node = self.parse_expression()
            if self.current_char != ')':
                raise Exception("Expected ')'")
            self.advance()  # Skip ')'
            return node
        elif self.current_char.isdigit():
            return self.parse_number()
        else:
            raise Exception(f"Unexpected character: {self.current_char}")

    def parse_term(self):
        node = self.parse_factor()

        while self.current_char == '*':
            op = self.current_char
            self.advance()
            node = BinaryOpNode(node, op, self.parse_factor())

        return node

    def parse_expression(self):
        node = self.parse_term()

        while self.current_char in ('+', '-'):
            op = self.current_char
            self.advance()
            node = BinaryOpNode(node, op, self.parse_term())

        return node

def evaluate(node):
    if isinstance(node, NumberNode):
        return node.value
    elif isinstance(node, BinaryOpNode):
        left_val = evaluate(node.left)
        right_val = evaluate(node.right)
        if node.op == '+':
            return left_val + right_val
        elif node.op == '-':
            return left_val - right_val
        elif node.op == '*':
            return left_val * right_val
        else:
            raise Exception(f"Unknown operator: {node.op}")
    else:
        raise Exception(f"Unknown node type: {type(node)}")

def interpret(expression):
    parser = Parser(expression)
    ast = parser.parse_expression()
    return evaluate(ast)

# Test cases
if __name__ == "__main__":
    test_expressions = [
        "42",
        "2 + 3",
        "10 - 4",
        "3 * 7",
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "1 + 2 + 3",
        "10 - 5 - 2",
        "((1 + 2) * 3) - 4"
    ]

    print("Brady Weber")
    print("Arithmetic Interpreter Test")
    for expr in test_expressions:
        try:
            result = interpret(expr)
            print(f"{expr} = {result}")
        except Exception as e:
            print(f"Error interpreting '{expr}': {e}")
