## NYT Spelling Bee Cheat "code"

[New York Times' Spelling Bee Game](https://www.nytimes.com/puzzles/spelling-bee)

The letters for a recent game are "lmexgap." The challenge is to fine as many word
words as possible that use those letters. The "L" must be included  in all words. 

For bonus points, find "pangrams" that use all of the letters in a single word.

# Example Usage

```python
import spelling_bee as sb
words = sb.word_finder("lmexgap")

# print pangrams
print(sb.find_pangrams(words))
# print all words
print(sorted(words, key=len, reverse=True))

```

```python
['megaplex']

['appellee', 'expellee', 'lamellae', 'malaxage', 'megaplex', 'pellmell', 'allegge', 'amalgam', 'example', 'exempla', 'exemple', 'lamella', 'lappage', 'palamae', 'agleam', 'alegge', 'allege', 'allele', 'appall', 'appeal', 'empale', 'gaggle', 'galage', 'galeae', 'lappel', 'lexeme', 'mallam', 'mallee', 'malmag', 'mammal', 'paella', 'palama', 'palapa', 'paleae', 'paleal', 'pallae', 'palpal', 'pelage', 'plagal', 'plexal', 'aglee', 'alaap', 'alapa', 'algae', 'algal', 'allee', 'allel', 'ample', 'appal', 'appel', 'apple', 'eagle', 'elpee', 'expel', 'galax', 'galea', 'gelee', 'gemel', 'gleam', 'lapel', 'legal', 'legge', 'lemel', 'lemma', 'llama', 'malax', 'maple', 'melee', 'pagle', 'palea', 'palla', 'papal', 'pelma', 'pepla', 'plage', 'alae', 'alap', 'alee', 'alga', 'alma', 'alme', 'amla', 'axal', 'axel', 'axle', 'eale', 'egal', 'gala', 'gale', 'gall', 'geal', 'glam', 'glee', 'gleg', 'lall', 'lama', 'lame', 'lamp', 
'leal', 'leam', 'leap', 'leep', 'leme', 'male', 'mall', 'malm', 'meal', 'mela', 'mell', 'pale', 'pall', 'palm', 'palp', 'peal', 'peel', 'pela', 'pele', 'pell', 'plap', 'plea']
```
