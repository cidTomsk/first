import pyperclip


clas_v = [] #класс вычитов по модулю 256
for i in range(256):
    if i%2!=0:
        clas_v.append(i)





def AfinaCrypt(text, a, b):
    text2 = []
    s = len(text)
    for i in range(s):

        sym = ord(text[i])
        if sym<256:
            sym = (sym*a+b)%256
            text2.append(chr(sym))
        else:
            text2.append(chr(sym))
    text2 = ''.join(text2)
    return text2



def AfinaEncrypt(text, a, b):

    text2 = []
    s = len(text)
    for i in range(s):
        sym = ord(text[i])
        if sym<256:
            sym = ((sym -b)*a)%256  #нужно а^-1

            if sym<0:
                sym+=256
        text2.append(chr(sym))
    text2 = ''.join(text2)
    return text2


def f(a):
    for k in range(256):
        if (k*a)%256==1:
            return k



print('Введите коэфициенты альфа и бета')
f1=0 # флаги проверки
f2=0

while(f1!=1 or f2!=1):
    a = input()
    b = input()
    if a.isdigit():
        a=int(a)
        if a in clas_v:
            f1=1
        else:
            print('Ваше число не находится в классе вычитов по модулю 256')
    else:
        print('Вы ввели не число')
    if b.isdigit():
        b = int(b)
        if b < 255 and b >= 0:
            f2 = 1
        else:
            print('Ваше число не находится в диапазоне 0-255')
    else:
        print('Вы ввели не число')


s = pyperclip.paste()
s2 = AfinaCrypt(s, a, b)
print(s2)
s3 = AfinaEncrypt(s2, f(a), b)
print(s3)



