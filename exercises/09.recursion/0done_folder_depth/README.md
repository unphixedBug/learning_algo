# Folder Depth

**Pattern:** Recursion | **Difficulté :** Easy

## Problème

Ton backup refuse les dossiers trop imbriqués. Avant de le lancer, tu veux savoir combien de
niveaux de dossiers il y a au maximum.

Comme dans `folder_size`, un dossier est une liste. Chaque élément est soit :

- un **fichier**, écrit comme un entier : sa taille
- un **sous-dossier**, écrit comme une liste qui suit les mêmes règles

Retourne la **profondeur** du dossier : le nombre de dossiers sur le chemin le plus long,
en partant du dossier du haut. Le dossier du haut compte pour `1`. Les fichiers n'ajoutent
pas de profondeur.

## Fonction à écrire

```python
def folder_depth(folder: list) -> int:
```

## Exemples

### Exemple 1 : seulement des fichiers

```
folder = [10, 20, 5]
```

Output : `1`

Il n'y a qu'un dossier : celui du haut.

### Exemple 2 : un sous-dossier

```
folder = [10, [20, 5], 2]
```

Output : `2`

### Exemple 3 : plusieurs niveaux

```
folder = [10, [20, 5], [[3]], 2]
```

Output : `3`

Le chemin le plus long est : dossier du haut → `[[3]]` → `[3]`.

### Exemple 4 : un dossier vide

```
folder = []
```

Output : `1`

Un dossier vide reste un dossier.

### Exemple 5 : le plus profond n'est pas le premier

```
folder = [[1], [[[2]]], [3]]
```

Output : `4`

## Contraintes

- Un dossier a au maximum `200` niveaux de sous-dossiers
- Un dossier et ses sous-dossiers contiennent au maximum `200 000` éléments au total
- `0 <= taille d'un fichier <= 10^9`
- Ne pas modifier l'input
- Complexité visée : `O(n)` en temps, où `n` est le nombre total d'éléments
- Standard library uniquement, et écris une fonction récursive

## Pourquoi la recursion est utile pour ce problème

C'est la même forme de données que `folder_size` : **un sous-dossier est aussi un
dossier**. « Quelle est la profondeur de ce sous-dossier ? » est donc la même question que
celle de ta fonction, sur un input plus petit.

Ce qui change, c'est l'étape **Combiner**. Dans `folder_size`, chaque sous-dossier
apportait un nombre que tu **additionnais**. Ici, additionner les profondeurs n'a pas de
sens : deux sous-dossiers de profondeur 2 ne font pas une profondeur de 4. Ce qui compte,
c'est **le plus profond** des sous-dossiers.

Voici l'Exemple 3 sous forme d'arbre. Chaque dossier regarde seulement ses sous-dossiers
directs :

```
folder                     ? -> 3
|-- file 10
|-- folder                 1
|   |-- file 20
|   |-- file 5
|-- folder                 2
|   |-- folder             1
|       |-- file 3
|-- file 2
```

Regarde un seul niveau, celui du haut : ses sous-dossiers répondent `1` et `2`. Comment le
dossier du haut obtient-il `3` à partir de ces deux réponses ? C'est toute la question de
l'exercice.

**Rappel de la recette :**

1. **Base case :** quel input peux-tu traiter sans rappeler la fonction ?
2. **Problème plus petit :** quelle partie de l'input a la même forme que l'input entier ?
3. **Combiner :** avec les réponses des sous-dossiers, comment construis-tu la réponse du
   dossier courant ?

**Le piège classique de ce type de problème :** oublier que le dossier courant compte
lui-même pour un niveau. Les sous-dossiers te donnent leur profondeur à eux, pas la tienne.

## Pourquoi la complexité est `O(n)`

Chaque élément est visité une fois, avec un travail constant. La stack utilise `O(d)` en
mémoire, où `d` est la profondeur : c'est d'ailleurs exactement ce que tu calcules.

## Cas d'usage réels

- Limites de profondeur : certains outils de backup ou d'archive refusent les chemins trop
  longs
- Valider un JSON avant de le parser : refuser un document trop imbriqué protège le serveur
- Afficher un fil de commentaires : savoir jusqu'où l'indentation va aller
- Hauteur d'un arbre (tree height) : la même idée, très fréquente en entretien
- Nombre de niveaux hiérarchiques entre le CEO et l'employé le plus bas

## Syntaxe Python utile

```python
# Le plus grand de deux valeurs
max(3, 7)                # 7

# Garder le maximum au fil d'une boucle
best = 0
for value in [4, 9, 2]:
    best = max(best, value)
# best vaut 9

# Le plus grand élément d'une liste
max([4, 9, 2])           # 9

# Attention : max() sur une liste vide lève une erreur
max([])                  # ValueError
max([], default=0)       # 0, grâce à default

# Rappel : vérifier le type
isinstance([1, 2], list) # True
```

## Avant de coder

Réponds à ces questions sur papier, avec l'Exemple 5 (`[[1], [[[2]]], [3]]`). Donne tes
réponses à Claude si tu veux les vérifier.

1. Calcule la profondeur à la main. Quelle est la profondeur de chacun des trois
   sous-dossiers ?
2. Avec ces trois réponses, comment le dossier du haut calcule-t-il sa propre profondeur ?
   Écris le calcul.
3. Que doit retourner un dossier qui n'a **aucun** sous-dossier, comme `[1]` ou `[]` ?
   Est-ce que ta réponse à la question 2 donne aussi ce résultat ?
4. Dans `folder_size`, que faisait ta fonction avec un fichier ? Et ici ?
5. Dans `folder_size`, ta variable commençait à `0` et tu ajoutais avec `+=`. Ici, à quoi
   sert ta variable, à quelle valeur commence-t-elle, et comment la mets-tu à jour ?

<details>
<summary>Indice : si tes résultats ont 1 de moins que prévu</summary>

Regarde l'Exemple 1 : `[10, 20, 5]` doit donner `1`. Si ta fonction donne `0`, elle ne
compte pas le dossier courant. Où dans ton code ajoutes-tu le niveau du dossier que tu es
en train de traiter ?

</details>

<details>
<summary>Indice : si tes résultats sont trop grands</summary>

Prends `[[1], [2]]`, qui doit donner `2`. Si tu obtiens `3`, tu combines les sous-dossiers
comme dans `folder_size`. Deux sous-dossiers côte à côte ne s'empilent pas.

</details>

<details>
<summary>Indice : si l'Exemple 5 donne le mauvais résultat</summary>

Le plus profond est au milieu. Si ta fonction ne garde que la réponse du **dernier**
sous-dossier (ou du premier), elle perd les autres. Ta variable doit garder la meilleure
réponse vue jusqu'ici.

</details>

Bloqué ? Demande à Claude un code snippet de la partie qui te bloque.
