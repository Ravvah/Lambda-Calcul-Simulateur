# parser.py
def parse_lambda_expression(expr):
    '''
    Transforme une expression lambda sous forme de chaîne en structure de données.

    Args:
    expr (str): Expression lambda en notation textuelle.

    Returns:
    dict: Une structure de données représentant l'expression lambda.
    '''
    expr = expr.strip()
    if expr.startswith('(') and expr.endswith(')'):
        return parse_lambda_expression(expr[1:-1])

    if '.' in expr:
        head, body = expr.split('.', 1)
        variable = head.strip()[1:].strip()
        return {'type': 'lambda', 'head': variable, 'body': parse_lambda_expression(body)}
    elif ' ' in expr:
        parts = expr.split(' ')
        func = parse_lambda_expression(parts[0])
        arg = parse_lambda_expression(' '.join(parts[1:]))
        return {'type': 'application', 'function': func, 'argument': arg}
    else:
        return {'type': 'variable', 'name': expr}


def preprocess_expression(expr):
    # toute préparation nécessaire avant le parsing
    pass
