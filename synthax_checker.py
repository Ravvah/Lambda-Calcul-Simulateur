# syntax_checker.py
def check_syntax(expr):
    '''
    Vérifie la syntaxe de l'expression lambda.

    Args:
    expr (str): Expression lambda en notation textuelle.

    Raises:
    ValueError: Si une erreur de syntaxe est détectée.
    '''
    if expr.count('(') != expr.count(')'):
        raise ValueError("Erreur de syntaxe : parenthèses non équilibrées.")
    if not any(c in expr for c in '\\.'):
        raise ValueError("Erreur de syntaxe : expression lambda incomplète.")

