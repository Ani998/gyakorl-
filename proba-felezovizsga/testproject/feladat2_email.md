## 2. Feladat: Email mező

Készíts egy python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a email mező app-ot az [https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/email_validation.html](https://svtesztelovizsga.blob.core.windows.net/$web/proba-vizsga/email_validation.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel az email mező app tesztelését.

A cél az email validáció tesztelése:

* Helytelen kitöltés esete:
    * email: teszt@
    * Az alábbi hibaüzenet jelenik meg (a nyelv beállítás függvényében változik a megjelenített üzenet):
  Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes. (magyar beállítások esetén)
  Please enter a part following '@'. 'teszt@' is incomplete. (angol beállítások esetén)

* Üres:
    * email: <üres>
    * Az alábbi hibaüzenet jelenik meg (a nyelv beállítás függvényében változik a megjelenített üzenet):
  Kérjük, töltse ki ezt a mezőt. (magyar beállítások esetén)
  Please fill out this field. (angol beállítások esetén)

* Helyes kitöltés:
    * email: teszt@elek.hu
    * Nincs validációs hibazüzenet

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `feladat2_email.py`
* a lokálisan kidolgozott megoldásodat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a legjobb szintaktikai praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne teljesen biztos, mert részpontokat ér a tárgyhoz kötődő mindennemű kód beadása
* a megoldás fájlba írjál kommenteket, amiben magyarázod a megírt kódodat (ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod)
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
