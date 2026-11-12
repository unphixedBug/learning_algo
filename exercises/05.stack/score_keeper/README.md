# Score Keeper

**Pattern :** Stack (pile) | **Difficulté :** Facile

## Problème

Tu tiens le score d'une partie, une manche à la fois. On te donne une liste
d'**opérations**, appliquées dans l'ordre à un **registre** (record) des scores des manches :

- Une chaîne qui ressemble à un nombre, par ex. `"5"` ou `"-2"` : le score de cette manche
  est ce nombre. Ajoute-le au registre.
- `"+"` : le score de cette manche est la **somme des deux derniers scores** du registre.
  Ajoute-le au registre (les deux scores précédents restent aussi dans le registre).
- `"D"` : le score de cette manche est le **double du dernier score** du registre. Ajoute-le
  au registre.
- `"C"` : **annule** le dernier score du registre : supprime-le. Cette opération n'ajoute rien.

Renvoie la **somme de tous les scores restant dans le registre** une fois toutes les
opérations appliquées.

## Fonction à écrire

```python
def final_score(operations: list[str]) -> int:
```

## Exemples

### Exemple 1

```
operations = ["5", "2", "C", "D", "+"]
```

Déroulé pas à pas :

| Opération | Registre après |
|---|---|
| `"5"` | `[5]` |
| `"2"` | `[5, 2]` |
| `"C"` | `[5]` (le `2` est annulé) |
| `"D"` | `[5, 10]` (double de `5`) |
| `"+"` | `[5, 10, 15]` (somme de `5` et `10`) |

Sortie : `30` (`5 + 10 + 15`)

### Exemple 2

```
operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
```

Sortie : `27`

### Exemple 3 : une seule manche

```
operations = ["1"]
```

Sortie : `1`

### Exemple 4 : aucune opération

```
operations = []
```

Sortie : `0`

## Contraintes

- `0 <= len(operations) <= 100000`
- Chaque opération est `"+"`, `"D"`, `"C"`, ou une chaîne représentant un entier dans
  `[-30000, 30000]`
- L'entrée est toujours **valide** : `"+"` n'apparaît jamais quand le registre contient moins
  de deux scores, et `"D"` ou `"C"` n'apparaissent jamais quand le registre est vide
- Complexité visée : `O(n)` en temps
- Bibliothèque standard uniquement

## Pourquoi une pile est utile pour ce problème

Trois des quatre opérations ne s'intéressent qu'aux scores **ajoutés le plus récemment** :
`"D"` lit le dernier, `"+"` lit les deux derniers, et `"C"` supprime le dernier. Aucune ne
touche jamais un score plus ancien. C'est encore la règle LIFO : **le dernier score entré est
le premier que ces opérations regardent ou retirent**.

Un simple total cumulé ne suffit pas ici. Une fois qu'un score est ajouté à un total, le total
ne se souvient plus de ce score individuellement — donc quand `"C"` dit « annule la dernière
manche », il n'y a plus rien à soustraire. Il te faut le véritable **historique**, dans
l'ordre, pas seulement sa somme. Une pile est exactement cet historique, avec la manche la
plus récente toujours au sommet, à portée de main.

**Cas d'usage réels :**

- **Annuler / rétablir :** un éditeur de texte ou un logiciel de dessin empile chaque action.
  Ctrl+Z dépile la plus récente, exactement comme `"C"` ici.
- **Gestion de versions :** `git revert` ou `git reset --soft HEAD~1` annule d'abord le commit
  le plus récent, jamais un commit au milieu de l'historique.
- **Calculatrices et tableurs :** certaines opérations (comme `"D"` et `"+"` ci-dessus)
  combinent les résultats les plus récents au lieu de te demander de les ressaisir.
- **Pile d'appels :** quand une fonction se termine, le contrôle revient à la fonction qui l'a
  appelée le plus récemment, pas à une plus ancienne.

**Comment reconnaître un problème de pile :**

- Une opération ne lit ou ne retire que le(s) élément(s) **le(s) plus récent(s)**, jamais un
  plus ancien
- Le problème parle explicitement d'**annuler**, de **supprimer** ou de **rejouer** un historique
- Tu as besoin des vraies valeurs passées, pas seulement d'un total cumulé, parce qu'une étape
  ultérieure peut revenir en arrière et modifier ce qui précède

## Syntaxe Python utile

```python
record = []
record.append(5)        # empiler (push) : [5]
record.append(-2)       # empiler (push) : [5, -2]

record[-1]              # regarder le sommet : -2 (ne le retire pas)
record[-2]              # regarder juste sous le sommet : 5 (ne le retire pas non plus)

record.pop()            # dépiler (pop) : renvoie -2, record vaut maintenant [5]

# Distinguer un nombre d'un symbole d'opération
op = "-2"
op in ("+", "D", "C")   # False -> op est un nombre, pas un symbole
int(op)                  # -2 (int() gère correctement le "-" initial)

sum(record)              # additionne tous les éléments actuellement dans la pile
```

**Coût des opérations courantes :**

| Opération | Coût | Pourquoi |
|---|---|---|
| `record.append(x)` | `O(1)` en moyenne | Ajoute à la fin d'une liste |
| `record.pop()` | `O(1)` | Retire à la fin, rien d'autre ne bouge |
| `record[-1]`, `record[-2]` | `O(1)` | Accès direct à la position |
| `sum(record)` | `O(n)` | Doit additionner chaque élément une fois |

## Avant de coder

Réponds à ces questions sur papier. Donne tes réponses à Claude si tu veux les vérifier.

1. Pour chaque type d'opération (`"5"`, `"+"`, `"D"`, `"C"`), est-ce qu'elle empile dans le
   registre, dépile, les deux, ou aucun des deux ?
2. Pour `"+"`, le registre passe de deux scores à trois, pas de deux à un. Quels scores
   existants restent, et lequel est nouveau ?
3. Déroule `operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]` à la main, en dessinant le
   registre après chaque opération. Quel est le registre final, et quelle est sa somme ?
4. Si tu gardais un seul total cumulé au lieu d'une liste, quelle information précise te
   manquerait au moment où `"C"` doit annuler la dernière manche ?
5. Que doit renvoyer la fonction quand `operations` est vide ?

<details>
<summary>Indice : comment structurer ton code</summary>

Chaque opération a besoin d'exactement un cas : une chaîne-nombre empile `int(op)` ; `"+"`
empile la somme des deux derniers éléments ; `"D"` empile le double du dernier élément ; `"C"`
dépile. Une fois la boucle terminée, la réponse n'est qu'à un appel de fonction intégrée
(built-in) du registre.

</details>

Bloqué ? Demande à Claude un extrait de code pour la partie qui te bloque.
