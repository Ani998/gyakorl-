## 1. Feladat: Keressük a téglalap kerületét

Készíts egy python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a téglalap kerülete app-ot az [https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/teglalap_kerulet.html](https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/teglalap_kerulet.html) oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a téglalap kerülete appban:

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

* Helyes kitöltés esete:
    * a: 74
    * b: 32
    * Eredmény: 212

* Nem számokkal történő kitöltés:
    * a: kiskutya
    * b: 32
    * Eredmény: NaN

* Üres kitöltés:
    * a: <üres>
    * b: <üres>
    * Eredmény: NaN

### A megoldás beadása
* a megoldásodat a `testproject` mappába tedd, `feladat1_teglalap.py` néven
* a lokálisan kidolgozott megoldásodat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a legjobb szintaktikai praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne teljesen biztos, mert részpontokat ér a tárgyhoz kötődő mindennemű kód beadása
* a megoldás fájlba írjál kommenteket, amiben magyarázod a megírt kódodat (ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod)
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
