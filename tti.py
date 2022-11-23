testtomeg:int = int(input('hány Kg vagy? '))
testmagassag:float = int(input('hány cm magas vagy? ')) / 100

tti:float = testtomeg / (testmagassag ** 2)

if   tti < 16:   tso:str = 'súlyos soványság'
elif tti < 17:   tso:str = 'mérsékelt soványság'
elif tti < 18.5: tso:str = 'mérsékelt soványság'
elif tti < 25:   tso:str = 'normális testsúly '
elif tti < 30:   tso:str = 'túlsúlyos'
elif tti < 35:   tso:str = 'I. fokú elhízás'
elif tti < 40:   tso:str = 'II. fokú elhízás'
else:            tso:str = 'III. fokú (súlyos) elhízás'

print(f'tti = {round(tti, 2)}; testsúlyosztályod: {tso}')