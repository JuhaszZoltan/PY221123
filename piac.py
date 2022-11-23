arlista:str = '''
======= árlista =======
alma          500 Ft/Kg
banán        1160 Ft/Kg
kígyóuborka   340 Ft/Kg
paradicsom   1990 Ft/Kg
'''
print(arlista)

ossz_ar:int = 0
print('Jó napot kívánok!')
kerdes:str = 'Szeretne valamit vásárolni? '
while input(kerdes) == 'igen':
    termek:str = input('Mit szeretne vásárolni? ')
    if termek in ['alma', 'banán', 'kígyóuborka', 'paradicsom']:
        mennyiseg:float = float(input(f'hány Kg {termek}-t kér? '))
        if   termek == 'alma':        ossz_ar +=  500 * mennyiseg
        elif termek == 'banán':       ossz_ar += 1160 * mennyiseg
        elif termek == 'kígyóuborka': ossz_ar +=  350 * mennyiseg
        elif termek == 'paradicsom':  ossz_ar += 1990 * mennyiseg
    else: print(f'Sajnálom {termek} jelenleg nincs raktáron :(')
    kerdes = 'Szeretne még valamit vásárolni? '
print(f'Rendben van, összesen {round(ossz_ar)} Ft-ot kérek!')
print('viszont látásra!')