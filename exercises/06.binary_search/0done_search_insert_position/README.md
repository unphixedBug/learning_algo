# Search Insert Position

**Pattern :** Recherche binaire (binary search) | **Difficulté :** Facile

C'est la suite directe de `find_in_sorted_list`. Le code va être presque le même. La différence
est dans le cas « pas trouvé » : au lieu de renvoyer `-1`, tu renvoies **l'endroit où la cible
devrait être**.

## Problème

On te donne une liste d'entiers `nums`, **triée par ordre croissant**, **sans doublons**, et un
entier `target`.

- Si `target` est dans `nums`, renvoie son **index**.
- Sinon, renvoie l'**index où il faudrait l'insérer** pour que la liste reste triée.

## Fonction à écrire

```python
def search_insert(nums: list[int], target: int) -> int:
```

## Exemples

### Exemple 1 : la cible existe

```
nums = [1, 3, 5, 6], target = 5
```

Sortie : `2` (`nums[2] == 5`)

### Exemple 2 : la cible manque, au milieu

```
nums = [1, 3, 5, 6], target = 2
```

Sortie : `1`. Si on insère `2` à l'index `1`, on obtient `[1, 2, 3, 5, 6]`, toujours trié.

### Exemple 3 : la cible est plus grande que tout

```
nums = [1, 3, 5, 6], target = 7
```

Sortie : `4`. Ça correspond à `len(nums)`, c'est-à-dire la toute fin de la liste.

### Exemple 4 : la cible est plus petite que tout

```
nums = [1, 3, 5, 6], target = 0
```

Sortie : `0`

### Exemple 5 : liste vide

```
nums = [], target = 4
```

Sortie : `0`

## Contraintes

- `0 <= len(nums) <= 1000000`
- `nums` est trié par ordre croissant, sans doublons
- `-10^9 <= nums[i], target <= 10^9`
- Complexité visée : `O(log n)` en temps, `O(1)` en mémoire
- Bibliothèque standard uniquement, **mais sans le module `bisect`** : il fait exactement ce
  problème à ta place (on en parle à la fin)

## Pourquoi la recherche binaire est utile pour ce problème

### Ce qui change par rapport à `find_in_sorted_list`

Dans `find_in_sorted_list`, quand la zone devenait vide, tu renvoyais `-1` : « pas trouvé, rien
d'autre à dire ». Pourtant, à ce moment-là, la boucle **sait** quelque chose d'utile. Regarde où
s'arrêtent `left` et `right` :

```
nums = [1, 3, 5, 6], target = 2, convention "right exclu" : zone = [left, right)

left = 0, right = 4   middle = 2, nums[2] = 5 > 2  -> right = 2
left = 0, right = 2   middle = 1, nums[1] = 3 > 2  -> right = 1
left = 0, right = 1   middle = 0, nums[0] = 1 < 2  -> left = 1
left = 1, right = 1   zone vide, fin de la boucle
```

La boucle s'arrête avec `left == right == 1`, et `1` est justement la bonne position d'insertion.
Ce n'est pas un hasard.

### Pourquoi `left` tombe toujours au bon endroit

Regarde ce que chaque mise à jour **garantit** :

- `left = middle + 1` n'arrive que si `nums[middle] < target`. Comme la liste est triée, **tout
  ce qui est à gauche de `left` est plus petit que `target`**.
- `right = middle` n'arrive que si `nums[middle] > target`. Donc **tout ce qui est à partir de
  `right` est plus grand que `target`**.

Ces deux phrases restent vraies du début à la fin de la boucle. On appelle ça un **invariant** :
une propriété que chaque tour de boucle préserve.

```
           left            right
             |               |
  [ < target | zone inconnue | > target ]
```

Quand la zone inconnue devient vide, `left == right`, et il ne reste que deux blocs : les valeurs
plus petites, puis les valeurs plus grandes. La place de `target` est **pile entre les deux**,
c'est-à-dire à l'index `left`.

### L'idée importante du pattern

Une recherche binaire ne sert pas seulement à répondre « oui ou non, est-ce que c'est là ? ». Elle
peut répondre à **« où est la frontière ? »** : la frontière entre les valeurs `< target` et les
valeurs `>= target`. Beaucoup de problèmes de niveau moyen se ramènent à trouver une frontière
comme celle-là.

## Cas d'usage réels

- **Garder une liste triée à jour :** un classement de scores, un agenda trié par heure. Pour
  ajouter un élément, on cherche sa place en `O(log n)` au lieu de tout retrier.
- **Tranches et barèmes :** dans quelle tranche d'impôt tombe un revenu ? Quelle note (A, B, C...)
  correspond à 73 points ? On cherche où la valeur s'insère dans la liste des seuils.
- **Index de base de données :** pour trouver toutes les commandes entre deux dates, la base
  cherche la position de la première date, puis lit à partir de là.
- **Autocomplétion :** dans une liste de mots triée, la position d'insertion de `"pro"` est
  l'endroit où commencent tous les mots qui démarrent par `"pro"`.

## Syntaxe Python utile

```python
nums = [1, 3, 5, 6]

left, right = 0, len(nums)     # affectation multiple : left = 0, right = 4
middle = (left + right) // 2   # division entière, arrondie vers le bas : 2

nums.insert(1, 2)              # insère 2 à l'index 1 : [1, 2, 3, 5, 6]
                               # (juste pour vérifier tes réponses à la main : c'est O(n))

# Dans une boucle while, tu peux "return" au milieu,
# ET renvoyer autre chose après la boucle si elle se termine normalement
while left < right:
    ...
    if found:
        return middle
return ...                     # que renvoyer ici ? C'est toute la question
```

**Coût des opérations courantes :**

| Opération | Coût | Pourquoi |
|---|---|---|
| `nums[i]` | `O(1)` | Accès direct à la position |
| `x in nums`, `nums.index(x)` | `O(n)` | Parcourt la liste élément par élément |
| `nums.insert(i, x)` | `O(n)` | Décale tous les éléments après `i` |
| `nums[a:b]` | `O(b - a)` | Copie les éléments |

## Avant de coder

Réponds à ces questions sur papier. Donne tes réponses à Claude si tu veux les vérifier.

1. Déroule `nums = [1, 3, 5, 6]`, `target = 7` avec ta boucle de `find_in_sorted_list`, en
   écrivant `left`, `right` et `middle` à chaque tour. Où s'arrêtent `left` et `right` ? Est-ce la
   bonne réponse ?
2. Même chose avec `target = 0`.
3. Avec `nums = []`, la boucle tourne-t-elle au moins une fois ? Que vaut `left` à la fin ?
4. Avec la convention « `right` exclu », pourquoi `right = middle` (et pas `middle - 1`) ne perd
   aucune position d'insertion possible ?
5. Combien de lignes de `find_in_sorted_list` faut-il changer pour résoudre ce problème ?

<details>
<summary>Indice 1 : par où commencer</summary>

Pars de ta solution de `find_in_sorted_list`. Le cas « trouvé » ne change pas. Seul ce qui se
passe **après** la boucle change.

</details>

<details>
<summary>Indice 2 : que renvoyer après la boucle</summary>

Relis la section « Pourquoi `left` tombe toujours au bon endroit ». Quand la boucle se termine,
`left` et `right` ont la même valeur.

</details>

Bloqué ? Demande à Claude un extrait de code pour la partie qui te bloque.

## Pour aller plus loin (après avoir réussi)

- **Le module `bisect` :** `bisect.bisect_left(nums, target)` fait exactement cet exercice. Une
  fois que tu as écrit ta version, tu as le droit de l'utiliser en entretien, à condition de
  savoir expliquer ce qu'il fait.
- **Et avec des doublons ?** Avec `nums = [1, 3, 3, 3, 5]` et `target = 3`, quelle position faut-il
  renvoyer pour avoir le **premier** `3` ? Est-ce que ta boucle la trouve ? Que faudrait-il changer
  ? (C'est l'idée du prochain exercice.)
