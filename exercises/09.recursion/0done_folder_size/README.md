# Folder Size

**Pattern:** Recursion | **Difficulté :** Easy

## Problème

Ton ordinateur manque d'espace, et tu veux savoir combien de place prend un dossier.

Un dossier est une liste. Chaque élément de cette liste est soit :

- un **fichier**, écrit comme un entier : sa taille
- un **sous-dossier**, écrit comme une liste qui suit les mêmes règles

Retourne la taille totale de tous les fichiers du dossier, y compris les fichiers dans ses
sous-dossiers, à n'importe quelle profondeur. Un dossier vide a une taille de `0`.

## Fonction à écrire

```python
def folder_size(folder: list) -> int:
```

## Exemples

### Exemple 1 : seulement des fichiers

```
folder = [10, 20, 5]
```

Output : `35`

### Exemple 2 : un sous-dossier

```
folder = [10, [20, 5], 2]
```

Output : `37`

Le sous-dossier a une taille de `20 + 5 = 25`, et `10 + 25 + 2 = 37`.

### Exemple 3 : plusieurs niveaux

```
folder = [10, [20, 5], [[3]], 2]
```

Output : `40`

### Exemple 4 : un dossier vide

```
folder = []
```

Output : `0`

### Exemple 5 : seulement des dossiers vides

```
folder = [[], [[]], []]
```

Output : `0`

## Contraintes

- Un dossier a au maximum `200` niveaux de sous-dossiers
- Un dossier et ses sous-dossiers contiennent au maximum `200 000` éléments au total
- `0 <= taille d'un fichier <= 10^9`
- Ne pas modifier l'input
- Complexité visée : `O(n)` en temps, où `n` est le nombre total d'éléments
- Standard library uniquement, et écris une fonction récursive : c'est ce que tu es venu
  apprendre

## Pourquoi la recursion est utile pour ce problème

Tu pourrais gérer un niveau de sous-dossiers avec deux boucles imbriquées, et deux niveaux
avec trois boucles. Mais le nombre de niveaux n'est connu qu'à l'exécution, donc tu ne
peux pas savoir combien de boucles écrire.

Regarde plutôt la forme des données. **Un sous-dossier est aussi un dossier.** Donc
« quelle est la taille de ce sous-dossier ? » est la même question que celle à laquelle
ta fonction répond déjà, sur un input plus petit. Ta fonction peut s'appeler elle-même.

Voici l'Exemple 3 sous forme d'arbre. Chaque dossier additionne seulement ce qui est
directement à l'intérieur :

```
folder                     10 + 25 + 3 + 2 = 40
|-- file 10
|-- folder                 20 + 5 = 25
|   |-- file 20
|   |-- file 5
|-- folder                 3
|   |-- folder             3
|       |-- file 3
|-- file 2
```

Le dossier du haut n'a pas besoin de savoir ce qui se passe dans ses sous-dossiers. Il
demande leur taille et reçoit un nombre. C'est l'astuce mentale de la recursion :
**quand tu écris l'appel récursif, fais confiance au fait qu'il retourne la bonne
réponse.** N'essaie pas de suivre chaque niveau dans ta tête. Vérifie un seul niveau.

**La recette pour toute fonction récursive :**

1. **Base case :** quel est le plus petit input, celui auquel tu peux répondre sans
   rappeler la fonction ?
2. **Problème plus petit :** quelle partie de l'input a la même forme que l'input entier ?
3. **Combiner :** une fois que tu reçois la réponse pour la partie plus petite, comment
   l'utilises-tu ?

Chaque appel récursif doit se rapprocher d'un base case. Sans ça, les appels ne
s'arrêtent jamais, et Python lève une `RecursionError`.

**Ce qui se passe dans la machine :** quand une fonction s'appelle elle-même, l'appel
courant attend sur une stack, avec ses propres variables locales. Quand l'appel interne
retourne, l'appel en attente reprend là où il s'était arrêté. Chaque appel a ses propres
variables, même si elles ont les mêmes noms.

**Comment reconnaître un problème de recursion :**

- Les données **contiennent des versions plus petites d'elles-mêmes** : dossiers, listes
  imbriquées, JSON, arbres, fils de commentaires
- La profondeur n'est **connue qu'à l'exécution**, donc tu ne peux pas écrire le bon
  nombre de boucles
- Tu peux décrire la réponse à partir de la réponse à une version plus petite du même
  problème

**Quand ne pas l'utiliser :** une simple boucle est meilleure pour une liste plate.
Python s'arrête à environ 1000 appels imbriqués, donc la recursion convient quand le
nombre de niveaux est petit, pas quand le nombre d'éléments est grand.

**La recursion et les autres patterns :** la recursion est plus un outil qu'un pattern,
et d'autres patterns sont construits dessus.

| Pattern | Ce qu'il ajoute à la recursion |
| --- | --- |
| DFS | Se souvient des endroits déjà visités |
| Backtracking | Fait un choix, explore, puis annule le choix |
| Dynamic programming | Sauvegarde les résultats, parce que les mêmes appels reviennent |

Ici, chaque sous-dossier est visité une seule fois, et il n'y a aucun choix à annuler :
c'est de la recursion simple.

## Pourquoi la complexité est `O(n)`

Chaque fichier et chaque sous-dossier est traité une fois, et chacun demande une quantité
de travail constante. La stack utilise aussi de la mémoire : `O(d)`, où `d` est le niveau
le plus profond, parce qu'un appel attend pour chaque niveau.

## Cas d'usage réels

- Outils d'utilisation du disque, comme la commande Linux `du` ou les propriétés d'un
  dossier sous Windows
- Chercher une valeur dans un document JSON de profondeur inconnue
- Compter les réponses d'un fil de commentaires, où les réponses peuvent avoir des
  réponses
- Compter les employés sous un manager dans l'arbre d'une entreprise
- Afficher le menu d'un site web avec des catégories imbriquées

## Syntaxe Python utile

```python
# Vérifier le type d'une valeur
isinstance(5, int)       # True
isinstance([1, 2], list) # True
isinstance(5, list)      # False

# Préfère isinstance à la comparaison avec type() : type(x) == list n'est pas pythonic

# Une fonction récursive, sur un autre problème : 4! = 4 * 3 * 2 * 1
def factorial(n: int) -> int:
    if n <= 1:                      # base case : la réponse est connue
        return 1
    return n * factorial(n - 1)     # problème plus petit + combiner

# Ce qui se passe quand tu appelles factorial(3) :
#
# factorial(3) attend factorial(2)
#     factorial(2) attend factorial(1)
#         factorial(1) retourne 1        <- base case : les appels s'arrêtent ici
#     factorial(2) retourne 2 * 1 = 2
# factorial(3) retourne 3 * 2 = 6

# Chaque appel a ses propres variables locales
def show_levels(level: int) -> None:
    label = f"level {level}"        # un label différent dans chaque appel
    if level < 2:
        show_levels(level + 1)
    print(label)                    # affiche level 2, puis level 1, puis level 0

show_levels(0)

# La limite d'appels imbriqués
import sys
sys.getrecursionlimit()  # généralement 1000
```

## Avant de coder

Réponds à ces questions sur papier, en utilisant l'Exemple 3 (`[10, [20, 5], [[3]], 2]`).
Donne tes réponses à Claude si tu veux les vérifier.

1. Calcule la taille à la main. La taille de quel dossier peux-tu calculer en premier, et
   pourquoi celui-là ?
2. Liste les appels de `folder_size` qui ont lieu, avec l'input de chacun. Combien y en
   a-t-il ?
3. Un élément peut être l'une de deux choses. Que fait ta fonction avec chacune d'elles ?
4. `factorial` a une ligne qui arrête clairement les appels. Qu'est-ce qui arrête les
   appels dans ce problème ? Que se passe-t-il avec `[]` ?
5. Pendant que `folder_size([20, 5])` s'exécute, l'appel du haut a déjà ajouté `10` à son
   total. Où est gardé ce `10` ? L'appel interne peut-il le modifier ?

<details>
<summary>Indice : si les fichiers après un sous-dossier ne sont pas comptés</summary>

Regarde l'Exemple 2. Quand l'appel pour `[20, 5]` se termine, le dossier du haut a encore
le fichier `2` à compter. Relis ton code et vérifie ce qui se passe juste après l'appel
récursif. Est-ce que l'appel du haut continue ?

</details>

<details>
<summary>Indice : si le gros dossier plat lève une RecursionError</summary>

Un dossier avec 100 000 fichiers n'a qu'un seul niveau. Demande-toi combien d'appels
imbriqués ton code fait pour lui. Il te faut un appel imbriqué par niveau de dossiers,
pas un par élément.

</details>

Bloqué ? Demande à Claude un code snippet de la partie qui te bloque.
