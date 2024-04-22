# utils.py
def log_reduction(step, description, expression, result=None):
    header = f"--- Étape {step}: {description} ---"
    print("=" * len(header))
    print(header)
    print("Expression Initiale: ", expression)
    if result is not None:
        print("Résultat: ", result)
    print("=" * len(header) + "\n")

