# Double Badge

**Pattern :** ??? (à toi de le trouver) | **Difficulty :** Easy | **Level :** -1 | **Temps visé :** 5 minutes

## Problème

À l'entrée d'un bâtiment, chaque employé doit badger **une seule fois** par jour.
Le système enregistre les IDs des badges dans une `list`, dans l'ordre de passage.

Écris une fonction qui retourne `True` si **au moins un badge a été utilisé plus d'une fois**,
et `False` sinon.

## Fonction à écrire

```python
def has_double_badge(badges: list[int]) -> bool:
```

## Exemples

### Exemple 1

```
badges = [12, 7, 33, 7]
```

Output : `True` (le badge `7` est passé deux fois)

### Exemple 2

```
badges = [1, 2, 3, 4]
```

Output : `False` (tous les badges sont différents)

### Exemple 3 : liste vide

```
badges = []
```

Output : `False` (personne n'est passé, donc aucun doublon)

### Exemple 4 : un seul badge

```
badges = [42]
```

Output : `False`

### Exemple 5 : le doublon est tout au début

```
badges = [5, 5, 8, 9, 10]
```

Output : `True`

## Contraintes

- `0 <= len(badges) <= 100000`
- `badges` contient des entiers (positifs ou négatifs)
- Complexité visée : `O(n)` en temps
- Standard library uniquement

## Méthode pour un blind exercise (on y va pas à pas)

Dans un blind exercise, le plus important n'est pas le code : c'est **reconnaître le pattern**.
Fais ces 3 étapes dans l'ordre, sur papier ou dans ta tête :

1. **Reformule le problème en une phrase simple.**
   Sans parler de badges ni de bâtiment : qu'est-ce qu'on cherche vraiment dans cette `list` ?
2. **Trouve la solution naïve.**
   Comment tu ferais à la main, sans réfléchir à la performance ? Quelle est sa complexité ?
3. **Cherche ce qui coûte cher dans la solution naïve.**
   Quelle question est-ce que tu te poses encore et encore ? Est-ce qu'un outil que tu connais
   peut répondre à cette question en `O(1)` ?

Tu peux me donner tes réponses dans le chat avant de coder.

<details>
<summary>Indice 1 : la reformulation</summary>

"Est-ce qu'un élément apparaît **plus d'une fois** ?"

Pour chaque badge, la vraie question est : **"est-ce que j'ai déjà vu ce badge avant ?"**

</details>

<details>
<summary>Indice 2 : la solution naïve et son problème</summary>

Solution naïve : pour chaque badge, comparer avec **tous les autres** badges (deux boucles
imbriquées). Ça marche, mais c'est `O(n²)` : avec 100 000 badges, ça fait ~5 milliards de
comparaisons. Le test de performance va échouer.

Le problème : à chaque badge, tu re-parcours la liste pour savoir "est-ce que je l'ai déjà vu ?".

</details>

<details>
<summary>Indice 3 : le pattern</summary>

Quand la question est **"est-ce que j'ai déjà vu X ?"**, l'outil est un **hash set**.

- On n'a pas besoin de savoir **combien de fois** (sinon ce serait un hash map / `dict`)
- On veut juste savoir **oui ou non**, en `O(1)` → `set`

</details>

<details>
<summary>Indice 4 : la structure du code</summary>

1. Crée un `set` vide : ce sont les badges "déjà vus".
2. Parcours `badges`. Pour chaque badge :
   - s'il est déjà dans le `set` → tu as trouvé un doublon, tu peux arrêter tout de suite
   - sinon → ajoute-le au `set`
3. Si la boucle se termine sans rien trouver → aucun doublon.

</details>

<details>
<summary>Syntaxe Python utile</summary>

```python
seen = set()          # set vide (attention : {} crée un dict, pas un set !)
seen.add(7)           # ajoute 7, O(1)
7 in seen             # True, O(1)
3 in seen             # False, O(1)

# Comparaison de coût :
7 in [1, 2, 7]        # O(n) : parcourt la list
7 in {1, 2, 7}        # O(1) : lookup direct
```

</details>

Bloqué ? Demande-moi un code snippet de la partie qui te bloque.
