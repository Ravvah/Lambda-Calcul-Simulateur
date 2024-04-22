# main.py
import lambda_parser
import synthax_checker
import reducer

def main():
    '''
    Fonction principale pour exécuter le simulateur de lambda-calcul.
    '''
    try:
        # Demander une expression lambda à l'utilisateur
        expr = input("Entrez une expression lambda (e.g., '\\x.x x'): ")
        synthax_checker.check_syntax(expr)
        parsed_expr = lambda_parser.parse_lambda_expression(expr)
        reduced_expr = reducer.beta_reduce(parsed_expr)
        print("Expression réduite:", reduced_expr)
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
