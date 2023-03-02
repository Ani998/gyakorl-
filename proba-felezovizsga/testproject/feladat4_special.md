## 4. Feladat: Speciális számok kiválasztása.

Nevezzük speciálisnak azokat a számokat, amelyek `11` többszörösei (másként fogalmazva oszthatók `11`-el) vagy pont `1`-el nagyobbak, mint `11` valamelyik többszöröse.

írj egy olyan Python függvényt, ami megkapja a tesztelendő számot paraméterként és visszaadja, hogy a kérdéses szám az speciális-e vagy nem. Ezt igaz/hamis formájában várjuk!

```Python
def special_eleven(x):
    pass # write your code here

special_eleven(22)
# >>> True
special_eleven(23)
# >>> True
special_eleven(24)
# >>> False
```

Hívd meg a függvényed az alábbi számokra:
```
23, 24, 122, 96
```

### Tanácsok a megoldáshoz:
* Fontos, hogy függvényt használj!
* Fontos, hogy legyen bekérés a felhasználótól a konzolon keresztül.
* Ne gondold túl!
* Nem kell ellenőrizni, hogy a bemenet csak egész szám legyen!
* Bármilyen megoldás ami a fenti tesztadatokra (és hasonló tesztadatokra) a helyes megoldást adja tökéletesen megfelel.
* Nincs pontlevonás ha `lehetne ezt egyszerűbben is`.
* Nincs plusz pont ha `kevesebb sorból oldod meg`.


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat4_special.py`
* a lokálisan kidolgozott megoldásodat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a legjobb szintaktikai praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne teljesen biztos, mert részpontokat ér a tárgyhoz kötődő mindennemű kód beadása
* a megoldás fájlba írjál kommenteket, amiben magyarázod a megírt kódodat (ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod)
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(