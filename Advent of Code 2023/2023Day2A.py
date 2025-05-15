with open("Day2Input") as f:
    lines = [line.rstrip() for line in f]
#print(lines)
list2 = []

for j in lines:
    ji = j.find(':')
    jj = int(ji) - 4
    jo = int(ji) - 3
    jp = int(ji) - 2
    jk = int(ji) - 1
    jl = (str(j[jj]) + str(j[jo]) + str(j[jp]) + str(j[jk]))
    jm = ''.join(c for c in jl if c.isdigit())
    jn = int(jm)

    list1 = j.split(';')

    for i in list1:
        #print(i)
        bi = i.find('blue')
        if bi <= 0:
            bn = 0
        else:
            bj = int(bi) - 3
            bk = int(bi) - 2
            bl = (str(i[bj]) + str(i[bk]))
            bn = int(bl)
        if bn > 14:
            list2.append(jn)
            break
        else:
            ri = i.find('red')
            if ri <= 0:
                rn = 0
            else:
                rj = int(ri) - 3
                rk = int(ri) - 2
                rl = (str(i[rj]) + str(i[rk]))
                rn = int(rl)
            if rn > 12:
                list2.append(jn)
                break
            else:
                gi = i.find('green')
                if gi <= 0:
                    gn = 0
                else:
                    gj = int(gi) - 3
                    gk = int(gi) - 2
                    gl = (str(i[gj]) + str(i[gk]))
                    gn = int(gl)
                if gn > 13:
                    list2.append(jn)
                    break

        print(jn,bn,rn,gn)
print(list2)
list3 = list(set(list2))
print(list3)
Ans = 5050 - sum(list3)
print(Ans)