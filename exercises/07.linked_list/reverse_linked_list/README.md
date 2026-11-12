# Inverser une linked list

**Pattern :** Linked list | **Difficulté :** Easy

## Problème

On te donne `head`, le premier node d'une singly linked list. Il vaut `None` si la liste est vide.

Inverse la liste **en changeant les liens entre les nodes**, puis retourne le nouveau premier node.

Tu dois garder les mêmes objets node :

- Ne crée pas de nouveaux nodes
- Ne modifie pas la `value` d'un node

## Fonction à écrire

```python
def reverse_list(head: ListNode | None) -> ListNode | None:
```

La classe `ListNode` est déjà écrite pour toi dans `solution.py`.

## Exemples

### Exemple 1 : plusieurs nodes

```
Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
```

La fonction retourne le node qui a la valeur `5`.

### Exemple 2 : deux nodes

```
Input:  1 -> 2 -> None
Output: 2 -> 1 -> None
```

### Exemple 3 : un seul node

```
Input:  7 -> None
Output: 7 -> None
```

### Exemple 4 : une liste vide

```
Input:  None
Output: None
```

### Exemple 5 : valeurs en double

```
Input:  1 -> 1 -> 2 -> None
Output: 2 -> 1 -> 1 -> None
```

## Contraintes

- `0 <= nombre de nodes <= 200000`
- `-1000 <= node.value <= 1000`
- Complexité visée : `O(n)` en temps et `O(1)` en espace supplémentaire
- Standard library uniquement

La liste peut être trop longue pour une solution récursive, car Python s'arrête par défaut à environ
1000 appels imbriqués. Utilise une boucle.

## Pourquoi une linked list est utile pour ce problème

Une **linked list** est une chaîne de nodes. Chaque node contient une valeur et un lien vers le node
suivant. La variable `head` ne te donne que le premier node : pour atteindre les autres, tu suis les
liens un par un.

```
head
 |
 v
[1 | next] --> [2 | next] --> [3 | next] --> None
```

Une `list` Python range ses éléments côte à côte, elle peut donc sauter directement à n'importe
quelle position. Une linked list ne peut pas sauter, mais elle peut insérer ou retirer un node en
changeant quelques liens, sans décaler tout le reste.

Ce problème enseigne la compétence principale du pattern : **changer des liens sans perdre le reste
de la chaîne**. Les nodes ne bougent pas. Seules les flèches changent de sens :

```
Avant :  1 -> 2 -> 3 -> None
Après :  None <- 1 <- 2 <- 3
```

Chaque node ne connaît que le node **après** lui. Rien ne peut te ramener au node précédent, et dès
que tu écrases un lien, tu risques de perdre tout ce qui venait après. C'est le vrai défi de cet
exercice.

**Cas d'usage réels :**

- **LRU cache pour une API REST :** une hash map plus une doubly linked list trouve une entrée en
  `O(1)`, et la déplace en tête en `O(1)`. Elle retire ensuite l'entrée utilisée le moins récemment
  quand le cache est plein.
- **Playlist musicale :** "suivant" et "précédent" suivent des liens, et ajouter un morceau à la file
  ne change que quelques liens.
- **Historique du navigateur :** chaque page est liée à la page d'avant et à la page d'après.
- **`collections.deque` en Python :** elle est construite sur une doubly linked list de blocs, c'est
  pourquoi elle ajoute et retire aux deux extrémités en `O(1)`.

**Comment reconnaître un problème de linked list :**

- L'input est un node `head`, ou le problème montre `1 -> 2 -> 3`. Ce pattern est généralement nommé
  dans l'énoncé, donc il est facile à reconnaître
- Les mots **node**, **next**, **head** ou **tail** apparaissent
- Tu dois **réordonner, insérer ou retirer** des nodes, et on te dit de ne pas copier les valeurs
  ailleurs
- Des éléments sont souvent ajoutés ou retirés au milieu, mais rarement lus par position

## Syntaxe Python utile

```python
# Un node est un objet ordinaire avec deux attributs
first = ListNode(1)
second = ListNode(2)
first.next = second         # 1 -> 2 -> None

first.value                 # 1
first.next                  # le node qui contient 2
first.next.value            # 2
second.next                 # None

# Parcourir une liste, du premier node au dernier
current = first
while current is not None:
    print(current.value)
    current = current.next

# Comparer avec None en utilisant "is", pas "=="
if current is None:
    ...

# Attention : suivre un lien depuis None lève une erreur
empty = None
empty.next                  # AttributeError

# Assigner plusieurs variables sur une ligne
x, y = 1, 2
x, y = y, x                 # swap : x vaut 2 et y vaut 1
```

**La distinction la plus importante de ce pattern :**

```python
current = current.next      # déplace la variable : la liste ne change pas
current.next = other        # change un lien : la liste est maintenant différente
```

Une variable n'est qu'une **étiquette** posée sur un node. Déplacer une étiquette ne change rien
dans la liste. Assigner à `.next` est la seule chose qui modifie la chaîne.

**Le coût des opérations courantes :**

| Opération | `list` Python | Linked list | Pourquoi |
|---|---|---|---|
| Lire l'élément à la position `i` | `O(1)` | `O(n)` | Une linked list doit suivre les liens depuis `head` |
| Insérer ou retirer au début | `O(n)` | `O(1)` | Une `list` décale chaque élément, une linked list change un lien |
| Insérer ou retirer après un node que tu as déjà | `O(n)` | `O(1)` | Seuls les liens autour de ce node changent |
| Chercher une valeur | `O(n)` | `O(n)` | Les deux doivent vérifier les éléments un par un |

## Avant de coder

Réponds à ces questions sur papier. Donne tes réponses à Claude si tu veux les vérifier.

1. Dessine `1 -> 2 -> 3 -> None`, puis dessine la liste inversée. Pour chaque node, vers quoi pointe
   `next` avant et après ? Que doit devenir le `next` du node `1` ?
2. Tu es sur le node `2`, et tu mets son `next` sur le node `1`. Comment peux-tu maintenant atteindre
   le node `3` ? Qu'aurais-tu dû faire avant de changer le lien ?
3. Le node `2` doit pointer en arrière vers le node `1`, mais un node ne connaît pas le node avant
   lui. Comment ton code peut-il quand même avoir cette information quand il arrive au node `2` ?
4. Quand ta boucle se termine, quel node est le nouveau premier node ? La variable que tu as
   utilisée pour parcourir la liste pointe-t-elle encore dessus ?
5. Déroule ton idée à la main sur une liste vide et sur un seul node. As-tu besoin d'un cas
   particulier pour eux ?

<details>
<summary>Indice : comment structurer ton code</summary>

À chaque étape, ton code doit connaître trois nodes : celui sur lequel tu es, celui d'avant et celui
d'après. Décide ce que vaut chacun d'eux **avant la première étape**. Puis écris les étapes dans un
ordre qui ne perd jamais le reste de la chaîne.

</details>

Si `pytest` ne se termine jamais, appuie sur `Ctrl+C` : ta boucle ne s'arrête probablement jamais,
par exemple parce que les liens forment maintenant un cercle ou que la variable de parcours ne
bouge jamais.

Bloqué ? Demande à Claude un code snippet de la partie qui te bloque.
