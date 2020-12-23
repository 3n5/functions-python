"""
Pythonコードをきれいに書く
https://www.youtube.com/watch?v=C-gEQdGVXbk
"""
#Ternary Conditionals：条件式　
#Trueなら1を、Falseなら0を返すコード
condition = True
x = 1 if condition else 0
#print(x)


#Enumerate:enumerate関数
names = ['Mirai','Tech','Denshi']
for index, name in enumerate(names,start=1):
    print(index, name)

#Zip:zip関数
names = ['Peter Parker','Clark Kent','Bruce Wayne']
heros = ['Spiderman','Superman','Batman']
for name, hero in zip (names, heros):
    print(f'{name} is actually {hero}')#フォーマット済み文字列リテラル

#小数点以下の桁数、有効桁（有効数字）
f = 12.3456
print(f'digit(decimal): {f:.3f}')
print(f'digit(all)    : {f:.3g}')
# digit(decimal): 12.346
# digit(all)    : 12.3