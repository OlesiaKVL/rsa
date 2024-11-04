import datetime

def egcd(a, b): #znajdowanie najwiekszego wspolnego dzielnika (NWD)
    s = 0; old_s=1
    t = 1; old_t = 0
    r = b; old_r = a

    while r!=0:
        quotient = old_r //r #znajdowanie ilorazu
        old_r, r = r, old_r - quotient * r #stala rownowazaca r-wspolczynnik
        #Moglibysmy okreslic najwiekszy wspolny dzielnik tylko za pomoca r, ale poniewaz wykonujemy odwrotne podstawienie, bedziemy potrzebowac dwoch innych zmiennych
        #old_s, old_t, s, t - Te zmienne pozwola rzeczywiscie wykonac odwrotne podstawienie:
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    #return gcd, x, y
    return old_r, old_s, old_t

def modularInv(a, b): #Metoda Euklidesa
    gcd, x, y = egcd(a, b)

    if x<0:
        x+=b
    return x

enctime = datetime.datetime.now()
def encrypt(e, N, msg): #funkcja szyfrowania
    cipher = "" #cipher - string
    #przeanalizujemy kazda wartosc za pomoca petli
    for c in msg:
        m = ord(c) #ord(c) - zwraca wartosc dla znaku c z tabeli znakow Unicode
        #powtorzenie kazdego znaku, ktory chcemy uzyskac
        cipher += str(pow(m, e, N)) + " "
        #str - przeksztalca wynik znaki
        #pow(m, e, N) - (m^e) mod N
        #" " - spacja oddziela rozne elementy
    return cipher

enctime2 = datetime.datetime.now()
timeencr = str(enctime2 - enctime)

decrtime = datetime.datetime.now()
def decrypt(d, N, cipher): #funkcja deszyfrowania
    msg = ""
    #musimy podzielic wiadomosc na czesci za pomoca spacji, poniewa? szyfrowalismy kazdy znak osobno
    parts = cipher.split() #split - dzieli ciag na czesci za pomoca spacji
    #zainicjowalismy wiadomosc, a teraz przegladamy kazda czesc
    for part in parts:
        if part: #sprawdzamy, czy part ma jakies wartosc
            #wartosc szyfru rowna sie calkowitej wartosci czesci
            c = int(part) #przeksztalcamy tekst na liczbe
            msg+= chr(pow(c, d, N))
            #chr - zwraca znak na podstawie jego przedstawienia numerycznego
            #pow(c, d, N) - (c^d)modN
    return msg
decrtime2 = datetime.datetime.now()
timedecr = str(decrtime2-decrtime)

def main():
    print ()
    print("Algorithm RSA")

    p=7
    q=19
    N=p*q
    phiN=(p-1)*(q-1) #funkcja Eulera

    e=31
    print("values for p, q, e:")
    print("p:", p)
    print("q:", q)
    print("e:", e)
    d=modularInv(e, phiN)

    print("please enter a message:")
    msg = input()

    enc=encrypt(e, N, msg)
    dec=decrypt(d, N, enc)

    print()
    print (f"message: {msg}")
    print ()
    print("values for encryption keys:")
    print (f"e: {e}")
    print(f"d: {d}")
    print (f"N: {N}")
    print ()
    print(f"encrypted message: {enc}")
    print("time spent on encryption: ", timeencr)
    print ()
    print("public encryption key: (e, n) = (",e, ", ", N,")")
    print("private encryption key: (d, n) = (",d, ", ", N,")")
    print ()
    print(f"decrypted message: {dec}")
    print("time spent on decryption: ", timedecr)
    print ()
    input()

main()
