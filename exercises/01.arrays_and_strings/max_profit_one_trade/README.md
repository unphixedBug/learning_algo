# Max Profit From One Trade

**Pattern :** Arrays and strings (single-pass scan, "best so far") | **Difficulté :** Easy

## Problème

On te donne le prix d'un article pour chaque jour, dans l'ordre. Tu peux **acheter un article un jour**
et **le revendre un jour ultérieur**.

Retourne le plus grand profit possible. Si aucune transaction ne rapporte d'argent, retourne `0`.

## Fonction à écrire

```python
def max_profit(prices: list[int]) -> int:
```

## Exemples

### Exemple 1

```
prices = [8, 2, 6, 4, 9, 3]
```

Sortie : `7` (achat à `2`, vente à `9`)

### Exemple 2 : le prix le plus bas arrive après le prix le plus haut

```
prices = [5, 9, 1, 3]
```

Sortie : `4` (achat à `5`, vente à `9`)

`9 - 1 = 8` n'est pas autorisé, car on ne peut pas vendre avant d'acheter.

### Exemple 3 : le prix ne fait que baisser

```
prices = [9, 7, 4, 1]
```

Sortie : `0` (le meilleur choix est de ne pas faire de transaction)

### Exemple 4 : une liste vide

```
prices = []
```

Sortie : `0`

## Contraintes

- `0 <= len(prices) <= 400000`
- `0 <= prices[i] <= 10000`
- Tu dois vendre un jour **strictement postérieur** au jour d'achat
- `prices` ne doit pas être modifiée
- Complexité visée : `O(n)` en temps et `O(1)` en espace supplémentaire
- Standard library uniquement

## Pourquoi un single-pass scan est utile pour ce problème

L'approche directe consiste à essayer chaque paire de jours. Ça fonctionne, mais avec 400 000 jours,
ça fait environ 80 milliards de paires.

Un scan évite ça, car la plupart de ces paires ne peuvent jamais être la meilleure réponse. Quand tu
arrives à un jour, tu n'as pas besoin de te souvenir de **tous** les prix précédents. Un petit résumé
du passé suffit pour connaître le meilleur profit possible en vendant aujourd'hui.

C'est la forme "best so far" du scan. Dans `run_length_encoding`, ce que tu retenais concernait le
**groupe courant**. Ici, ça concerne **tout ce que tu as lu jusqu'à présent**.

**Cas d'usage réels :**

- **Finance :** trouver le plus grand gain dans un historique de prix, où l'achat doit précéder la vente.
- **Météo :** trouver la plus forte hausse de température sur une période, où le minimum doit précéder le maximum.
- **Monitoring :** suivre la plus forte augmentation de l'utilisation mémoire d'un serveur à partir d'un flux de mesures, sans toutes les stocker.

**Comment reconnaître cette forme de scan :**

- La réponse dépend d'une paire d'éléments, et leur **ordre** compte (l'un doit venir avant l'autre)
- Les mots **best**, **largest**, **smallest** ou **so far** (meilleur, plus grand, plus petit, jusqu'ici) apparaissent
- La solution directe compare chaque paire, ce qui est `O(n²)`
- À chaque élément, un petit résumé du passé suffit pour prendre une décision

## Syntaxe Python utile

```python
# Boucler sur les valeurs
for price in prices:
    ...

# Sauter le premier élément sans copier la liste
for i in range(1, len(prices)):
    price = prices[i]

# Comparer deux valeurs
min(3, 7)                   # 3
max(3, 7)                   # 7

# Vérifier si une liste est vide
if not prices:
    ...

# Donner une valeur de départ que n'importe quel nombre réel peut battre
float("inf")                # plus grand que n'importe quel nombre
```

**Le coût des opérations courantes :**

| Opération | Coût | Pourquoi |
|---|---|---|
| `min(a, b)` | `O(1)` | Compare deux valeurs |
| `min(prices)` | `O(n)` | Lit toute la liste |
| `prices[i:]` | `O(n - i)` | Un slice **copie** les éléments |
| `max(prices[i:])` dans une boucle | `O(n²)` au total | Le coût ci-dessus, répété pour chaque élément |

## Avant de coder

Réponds à ces questions sur papier, avec `[5, 9, 1, 3]`. Donne tes réponses à Claude si tu veux les vérifier.

1. Pourquoi `max(prices) - min(prices)` est-il une mauvaise réponse ici ? Quelle règle est enfreinte ?
2. Imagine que tu es au dernier jour, au prix `3`, et que tu décides de vendre. Quel prix précédent
   (un seul) veux-tu connaître ? As-tu besoin des autres prix précédents ?
3. Donc, en lisant de gauche à droite, quelles **deux informations** dois-tu retenir à chaque instant ?
4. Pour chaque jour, tu peux d'abord mettre à jour ce que tu retiens, ou d'abord calculer le profit.
   Essaie les deux ordres sur `[9, 7, 4, 1]`. L'ordre change-t-il la réponse ? Pourquoi ?
5. Dans `run_length_encoding`, des nested loops restaient `O(n)`. Pourquoi une nested loop qui essaie
   chaque paire de jours serait-elle `O(n²)` ici ?

<details>
<summary>Indice : comment structurer ton code</summary>

Utilise les quatre questions de `exercises/01.arrays_and_strings/summary.md` : qu'est-ce que je retiens,
quel événement le modifie, que fais-je quand il se produit, et reste-t-il quelque chose après la boucle ?

</details>

Bloqué ? Demande à Claude un code snippet pour la partie qui te bloque.
