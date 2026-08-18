n = input("")
torre = []
torre.append(int(n))
torre_s = []
torre_s.append(n)
ns = (n.split("")).sort()
n1 = ns[0]*1000 + ns[1]*100 + ns[2]*10 + ns[3]
n2 = ns[-1]*1000 + ns[-2]*100 + ns[-3]*10 + ns[-4]
n0 = n1 - n2
torre.append(int(n0))
torre_s.append(n)
i = 1

while x not in torre:
    nx = torre_s[i].split("")
    nma = int(nx[0])*1000 + int(nx[1])*100 + int(nx[2])*10 + int(nx[3])
    nme = int(nx[-1])*1000 + int(nx[-2])*100 + int(nx[-3])*10 + int(nx[-4])
    x = nma - nme
    if x not in torre:
        torre.append(x)
        torre_s.append(str(x))
    i += 1