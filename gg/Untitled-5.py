#зробити програму яка відсортовує текст і виводить їх в алфавітному порядку і викидає слова які повторються.
a = input('text:')
b = sorted(set(a.split(' ')))
    
g = str(input('''
Порахувати текст: - 
Вивести слова: +
= '''))

if g == "-":
    for i in b:
        if len(b) >= 4:
            a += i
    print(int(len(a)/2))
    
elif g == "+":
    for i in b:
        if len(i) >= 4:
            print(i)

        
    
        

