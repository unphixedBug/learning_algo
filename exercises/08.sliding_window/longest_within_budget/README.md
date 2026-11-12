# La plus longue série dans le budget

**Pattern :** Sliding window (taille variable) | **Difficulté :** Facile

## Problème

Tu as une liste `costs` : `costs[i]` est ce que tu as dépensé le jour `i`. Tu as aussi un entier
`budget`.

Trouve le **plus grand nombre de jours consécutifs** dont le total des dépenses est
**inférieur ou égal** à `budget`.

Si aucun jour ne rentre dans le budget (ou si la liste est vide), retourne `0`.

## Fonction à écrire

```python
def longest_within_budget(costs: list[int], budget: int) -> int:
```

## Exemples

### Exemple 1

```
costs  = [3, 1, 2, 7, 1, 1]
budget = 6
```

Résultat : `3`

```
[3, 1, 2] 7  1  1     total = 6   <- 3 jours, ok
 3  1  2 [7] 1  1     total = 7   <- trop cher, même seul
 3  1  2  7 [1, 1]    total = 2   <- 2 jours seulement
```

### Exemple 2 : tout rentre

```
costs  = [1, 2, 1]
budget = 10
```

Résultat : `3`

### Exemple 3 : rien ne rentre

```
costs  = [8, 9, 12]
budget = 5
```

Résultat : `0`

### Exemple 4 : la meilleure série est à la fin

```
costs  = [5, 5, 1, 1, 1, 1]
budget = 4
```

Résultat : `4`

### Exemple 5 : liste vide

```
costs  = []
budget = 3
```

Résultat : `0`

## Contraintes

- `0 <= len(costs) <= 200000`
- `1 <= costs[i] <= 10000` (toujours **strictement positif**, c'est important !)
- `0 <= budget <= 10**9`
- `costs` ne doit pas être modifiée
- Complexité visée : `O(n)` en temps, `O(1)` en mémoire supplémentaire
- Bibliothèque standard uniquement

## Ce qui change par rapport à `max_sum_window`

Dans l'exercice précédent, la fenêtre avait **une taille fixe `k`** : les deux bords avançaient
ensemble, toujours à `k` d'écart.

Ici, **personne ne te donne la taille**. C'est justement ce qu'on cherche. Alors la fenêtre doit
**grandir** et **rétrécir** toute seule, selon une **règle** :

- **Le bord droit** avance à chaque tour : il essaie d'**ajouter** un jour.
- **Le bord gauche** avance **seulement quand la fenêtre n'est plus valide** (total > budget) :
  il **retire** des jours jusqu'à ce que la fenêtre redevienne valide.

```
budget = 6

 left
  v
 [3]  1   2   7   1   1        total = 3   ok   -> longueur 1
 [3,  1]  2   7   1   1        total = 4   ok   -> longueur 2
 [3,  1,  2]  7   1   1        total = 6   ok   -> longueur 3  (meilleur)
 [3,  1,  2,  7]  1   1        total = 13  trop ! on retire à gauche...
  3  [1,  2,  7]  1   1        total = 10  encore trop...
  3   1  [2,  7]  1   1        total = 9   encore trop...
  3   1   2  [7]  1   1        total = 7   encore trop...
  3   1   2   7  []   1   1    total = 0   ok (fenêtre vide)
  ...
```

## Pourquoi une fenêtre glissante est utile ici

La solution évidente : tester **chaque point de départ**, et pour chacun, ajouter des jours
jusqu'à dépasser le budget. C'est `O(n²)` dans le pire cas : avec 200 000 jours, ça fait
des dizaines de milliards d'opérations.

L'idée clé : **si une fenêtre dépasse le budget, toute fenêtre plus grande qui la contient
dépasse aussi** (car les coûts sont positifs). Donc quand ça dépasse, ça ne sert à rien de
continuer à agrandir depuis le même départ : il faut avancer le départ.

Et quand on avance le départ, **on ne recommence pas de zéro** : on retire juste le jour qui sort
du total. Chaque jour **entre une fois** (bord droit) et **sort au plus une fois** (bord gauche).
Les deux bords ne reculent jamais, donc au total : `O(n)`.

> Pourquoi « strictement positif » est important : avec des nombres négatifs, ajouter un jour
> pourrait **faire baisser** le total. Alors une fenêtre trop chère pourrait redevenir valide en
> grandissant, et la règle « je retire à gauche dès que ça dépasse » ne marcherait plus.

**Le problème que ça résout :** trouver la plus longue (ou la plus courte) suite d'éléments
consécutifs qui respecte une **condition**, quand cette condition est « monotone » (plus de
contenu = plus difficile à respecter).

**Cas d'usage réels :**

- **Streaming vidéo :** la plus longue séquence de segments qu'on peut précharger sans dépasser
  la taille du buffer.
- **Forfait mobile :** la plus longue période d'affilée où ta consommation de données est restée
  sous la limite.
- **Logs serveur :** la plus longue période sans plus de N erreurs.
- **Texte :** la plus longue sous-chaîne sans caractère répété (un grand classique d'entretien,
  ce sera probablement ton prochain exercice de ce type).

**Comment reconnaître une fenêtre de taille variable :**

- Les mots **consécutif**, **sous-tableau**, **sous-chaîne**, **d'affilée**
- On cherche **la plus longue** ou **la plus courte**, et **la taille n'est pas donnée**
- Il y a une **condition** (« au plus », « au moins », « sans répétition », « dans le budget »)
- Si une fenêtre **casse** la condition, l'agrandir ne la répare pas

## Syntaxe Python utile

```python
costs = [3, 1, 2, 7]

# Parcourir avec l'index ET la valeur
for right, cost in enumerate(costs):
    print(right, cost)           # 0 3, puis 1 1, puis 2 2, puis 3 7

# Une boucle while : se répète TANT QUE la condition est vraie
total = 13
left = 0
while total > 6:
    total -= costs[left]
    left += 1
# Question : que valent total et left à la fin ? Déroule-le à la main.

# Longueur d'une fenêtre qui va de left à right (les deux inclus)
left, right = 2, 4
length = right - left + 1        # 3  (les index 2, 3 et 4)

# Fenêtre vide : left = right + 1
left, right = 5, 4
right - left + 1                 # 0

# Garder le maximum
best = 0
best = max(best, 3)              # 3
```

**`if` ou `while` pour rétrécir ?** Un `if` retire **un seul** jour. Un `while` retire **autant
de jours qu'il faut**. Regarde le schéma plus haut : quand `7` entre, combien de jours faut-il
retirer ?

## Avant de coder

Réponds sur papier avec `costs = [3, 1, 2, 7, 1, 1]` et `budget = 6`. Donne tes réponses à Claude
si tu veux les vérifier.

1. Quel est **l'état** de la fenêtre que tu dois connaître à chaque instant ? (Dans
   `max_sum_window`, c'était la somme.) Quelles variables te faut-il en plus ?
2. Quand le bord droit avance à l'index `right`, comment mets-tu l'état à jour ?
3. Quand la fenêtre n'est plus valide, que fais-tu exactement ? Quand t'arrêtes-tu ?
4. À quel moment du tour de boucle peux-tu **mettre à jour la meilleure longueur** : avant ou
   après avoir rétréci ? Pourquoi ?
5. Termine le tableau du schéma : qu'est-ce qui se passe quand les deux `1` de la fin entrent ?
6. Que se passe-t-il pour un jour qui coûte plus que le budget à lui seul ? La fenêtre devient
   vide : est-ce que ton code le gère sans cas spécial ?

<details>
<summary>Indice : la structure du code</summary>

1. Initialise le bord gauche, le total de la fenêtre et la meilleure longueur.
2. Boucle sur le bord droit, un jour à la fois :
   - ajoute le jour qui entre au total ;
   - **tant que** la fenêtre est trop chère, retire le jour de gauche et avance le bord gauche ;
   - maintenant la fenêtre est valide : compare sa longueur à la meilleure.
3. Retourne la meilleure longueur.

</details>

Bloqué ? Demande à Claude un bout de code pour la partie qui te bloque.
