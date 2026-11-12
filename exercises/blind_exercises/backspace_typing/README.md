# Backspace Typing

**Pattern :** ??? (à toi de le trouver) | **Difficulty :** Easy | **Level :** -1 | **Temps visé :** 5 minutes

## Problème

Un clavier enregistre toutes les touches tapées dans une string `keys`.
Le caractère `#` représente la touche **Backspace** : elle efface le dernier caractère encore
présent à l'écran. Si l'écran est vide, `#` ne fait rien.

Retourne le **texte final** affiché à l'écran.

## Fonction à écrire

```python
def typed_text(keys: str) -> str:
```

## Exemples

### Exemple 1

```
keys = "ab#c"
```

Output : `"ac"` (on tape `a`, `b`, on efface `b`, on tape `c`)

### Exemple 2

```
keys = "abc##"
```

Output : `"a"` (deux Backspace effacent `c` puis `b`)

### Exemple 3 : Backspace sur un écran vide

```
keys = "#a"
```

Output : `"a"` (le premier `#` ne fait rien)

### Exemple 4 : on efface tout puis on retape

```
keys = "a##b"
```

Output : `"b"`

### Exemple 5 : string vide

```
keys = ""
```

Output : `""`

## Contraintes

- `0 <= len(keys) <= 200000`
- `keys` contient des lettres minuscules et `#`
- Complexité visée : `O(n)` en temps
- Standard library uniquement

## Méthode pour un blind exercise (on y va pas à pas)

1. **Reformule le problème en une phrase simple.**
   Quand on tape `#`, **quel** caractère est effacé ? Le premier ? Un au hasard ? Lequel ?
2. **Trouve la solution naïve.**
   Comment tu le ferais avec une string qu'on modifie au fur et à mesure ? Combien coûte
   l'effacement d'un caractère dans une string Python ?
3. **Cherche le pattern.**
   « On ajoute à la fin, on retire à la fin. » Ça te rappelle quelle structure de données ?

Tu peux me donner tes réponses dans le chat avant de coder.

<details>
<summary>Indice 1 : la reformulation</summary>

`#` efface toujours le **dernier** caractère ajouté encore présent.
Le dernier entré est le premier sorti : c'est du **LIFO** (Last In, First Out).

</details>

<details>
<summary>Indice 2 : la solution naïve et son problème</summary>

Solution naïve : garder une string `screen` et faire `screen = screen[:-1]` à chaque `#`.

Problème : les strings Python sont **immutables**. `screen[:-1]` crée une **nouvelle** string
en copiant tous les caractères, donc `O(n)` par Backspace, et `O(n²)` au total. Le test de
performance va échouer.

</details>

<details>
<summary>Indice 3 : le pattern</summary>

LIFO → **stack**. En Python, une `list` sert de stack :

- `append()` ajoute à la fin en `O(1)`
- `pop()` retire à la fin en `O(1)`

</details>

<details>
<summary>Indice 4 : la structure du code</summary>

1. Crée une `list` vide : c'est l'écran.
2. Parcours `keys`. Pour chaque caractère :
   - si c'est `#` **et** que l'écran n'est pas vide → retire le dernier caractère
   - si c'est `#` et que l'écran est vide → ne fais rien
   - sinon → ajoute le caractère
3. À la fin, transforme la `list` en string.

</details>

<details>
<summary>Syntaxe Python utile</summary>

```python
stack = []
stack.append("a")     # ["a"], O(1)
stack.append("b")     # ["a", "b"]
stack.pop()           # retourne "b", stack == ["a"], O(1)

if stack:             # True si la list n'est pas vide
    ...

"".join(["a", "c"])   # "ac" : list de caractères -> string, O(n)
```

**Piège :** `stack.pop()` sur une `list` vide lève une `IndexError`.

</details>

Bloqué ? Demande-moi un code snippet de la partie qui te bloque.
