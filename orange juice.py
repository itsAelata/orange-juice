print('orange juice calories counter by Aelata')
try:
    amount = float(input('how much did u drink? (ml) -> '))
except ValueError:
    print('wrong input')
    exit()
conclusion = (amount * 45)/100
conclusion = round(conclusion, 1)
print(conclusion, 'calories')
answer = input('do u wanna know what part of daily limit it is? (yes or no) -> ')
answer.lower()
if answer == 'yes':
    result = (conclusion/2000) * 100
    result = round(result, 1)
    print(result,'%')
else:
    print('ok')


