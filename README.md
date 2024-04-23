# Simulateur de Lambda-Calcul

Le lambda-calcul est un système formel en logique mathématique et en informatique théorique qui joue un rôle clé dans la compréhension des fonctions et leur application. Il sert de fondement aux langages de programmation fonctionnels et à l'étude des systèmes de preuve. Le lambda-calcul est particulièrement utile pour modéliser des fonctions et des calculs, sans recourir à des états ou des variables muables.

## À propos du Lambda-Calcul

Le lambda-calcul a été introduit par Alonzo Church dans les années 1930 comme partie de la recherche en fondements des mathématiques. Le concept central repose sur la fonction anonyme, ses règles de création (abstraction) et d'application. En lambda-calcul, toute fonction est anonyme, c'est-à-dire sans nom, et est souvent représentée comme suit :

- **Abstraction** : `λx.M`, où `x` est un paramètre et `M` est le corps de la fonction.
- **Application** : `F x`, applique la fonction `F` à l'argument `x`.

### Réduction Beta en Lambda-Calcul

La réduction beta est l'opération de base du lambda-calcul qui permet de simplifier les expressions en appliquant des fonctions à leurs arguments. La forme générale de la réduction beta est exprimée comme suit :

- **Formule Générale** : `(λx.M) N → M[x := N]`

Où `λx.M` représente une fonction lambda qui prend `x` comme paramètre et `M` comme corps de la fonction. `N` est l'argument appliqué à la fonction. La réduction beta consiste à remplacer toutes les occurrences de `x` dans `M` par `N`.

#### Exemple Simplifié

Supposons que nous avons la fonction suivante et que nous l'appliquons à un argument :

- **Expression** : `(λx.x + x) 5`

La réduction de cette expression consiste à remplacer `x` par `5` dans le corps de la fonction, ce qui nous donne :

- **Après Réduction** : `5 + 5`

Ce qui simplifie ensuite à `10`. Cet exemple montre comment une fonction peut être appliquée et simplifiée en utilisant la réduction beta.

Cette opération est essentielle pour le calcul des expressions en lambda-calcul et est fondamentale pour comprendre comment les fonctions sont traitées dans les langages de programmation fonctionnels.


## Intérêt et Utilisation
Le lambda-calcul est essentiel pour :
- Concevoir et analyser des systèmes informatiques et des langages de programmation.
- Développer des preuves en logique.
- Comprendre les transformations de fonctions et les calculs formels.

Les opérations de réduction, notamment la *réduction beta*, qui substitue un argument à toutes les instances de son paramètre correspondant dans le corps d'une fonction, permettent de simplifier les expressions de fonction.

## Structure du Projet

Ce projet de simulateur de lambda-calcul est structuré en plusieurs fichiers principaux qui facilitent la compréhension et l'interaction avec le système :

### Fichiers du Projet

- **main.py** : Le point d'entrée du simulateur. Il gère l'interaction avec l'utilisateur et orchestre les opérations de réduction des expressions lambda.
- **parser.py** : Contient les fonctions nécessaires pour analyser les expressions lambda saisies par l'utilisateur, les transformant en structures de données internes manipulables par le simulateur.
- **reducer.py** : Implémente les mécanismes de réduction, y compris la réduction beta, essentiels pour évaluer les expressions lambda.
- **utils.py** : Fournit des outils et fonctions utilitaires qui supportent les autres modules, notamment pour les opérations de substitution et de formatage des logs.
- **syntax_checker.py** : Vérifie la syntaxe des expressions lambda pour s'assurer qu'elles sont bien formées avant d'essayer de les réduire.

### Utilisation

Pour utiliser ce simulateur, naviguez vers le répertoire du projet et exécutez `main.py` via votre terminal ou invite de commande :
```bash
python main.py
```
