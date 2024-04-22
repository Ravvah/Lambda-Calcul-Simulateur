import utils

def beta_reduce(expr, depth=0):
    """
    Réduit récursivement une expression lambda en appliquant des réductions beta.

    Args:
        expr (dict): L'expression lambda à réduire, représentée sous forme de dictionnaire.
        depth (int): La profondeur de récursion actuelle, utilisée pour le logging.

    Returns:
        dict: L'expression lambda après application des réductions nécessaires.
    """
    if depth == 0:
        utils.log_reduction(1, "Début de la Réduction", expr)
    
    if isinstance(expr, dict) and 'type' in expr and expr['type'] == 'application':
        function = expr['function']
        argument = expr['argument']
        
        if function['type'] == 'lambda':
            # Remplace la tête de la lambda par l'argument dans le corps
            new_expr = substitute(function['body'], function['head'], argument)
            utils.log_reduction(depth + 1, "Réduction Beta", expr, new_expr)
            return beta_reduce(new_expr, depth + 1)
        else:
            # Réduit récursivement la fonction et l'argument si la fonction n'est pas une lambda
            reduced_function = beta_reduce(function, depth + 1)
            reduced_argument = beta_reduce(argument, depth + 1)
            result_expr = {'type': 'application', 'function': reduced_function, 'argument': reduced_argument}
            utils.log_reduction(depth + 1, "Réduction de l'Application", expr, result_expr)
            return result_expr
    elif isinstance(expr, dict) and expr['type'] == 'lambda':
        # Réduit récursivement le corps de l'abstraction lambda
        reduced_body = beta_reduce(expr['body'], depth + 1)
        result_expr = {'type': 'lambda', 'head': expr['head'], 'body': reduced_body}
        utils.log_reduction(depth + 1, "Réduction du Corps de Lambda", expr, result_expr)
        return result_expr
    else:
        return expr

def substitute(body, var, value):
    """
    Substitue une variable par une valeur dans une expression lambda.

    Args:
        body (dict): Le corps de l'expression où la substitution doit être effectuée.
        var (str): Le nom de la variable à remplacer.
        value (dict): La valeur par laquelle remplacer la variable.

    Returns:
        dict: Nouveau corps de l'expression après substitution.
    """
    if body['type'] == 'variable':
        if body['name'] == var:
            return value
        else:
            return body
    elif body['type'] == 'lambda':
        if body['head'] == var:
            return body 
        else:
            return {'type': 'lambda', 'head': body['head'], 'body': substitute(body['body'], var, value)}
    elif body['type'] == 'application':
        new_function = substitute(body['function'], var, value)
        new_argument = substitute(body['argument'], var, value)
        return {'type': 'application', 'function': new_function, 'argument': new_argument}
