i = 1

while i == 19 or 22:
    if i == 1:
        print('''Te vagy az iskola rosszfiúja. Késve érkezel a suli elé, még elszívod a cigidet, aztán…
2. elnyomod a csikket az igazgatónő bringájának kerekébe.
3. felrúgod a bejárat melletti szemeteskukát és mellé pöccinted a csikket. 
4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire. ''')

        v = int(input('Mit választasz? Írj be a számot: '))
if v == 2 or v == 3 or v == 4:
    i = v

    if i == 2:
        print('''észreveszi az éppen érkező töri tanárod, mit tettél és…
5. azonnal felrángat az igazgatói irodába. Te hőzöngve tiltakozol végig a folyosón.
6. gratulál neked, hisz szerinte is egy nagyképű szipirtyó a nő. 
7. szó nélkül tovább sétál, mivel eléggé parázik tőled.
''')
        v = int(input('Mit választasz? Írj be a számot: '))
if v == 5 or v == 6 or v == 7:
    i = v

