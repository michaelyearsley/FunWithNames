my_name = input("Enter name: ")
blank_pos = my_name.find(' ')
name_len = len(my_name)-1
i= len(my_name)-1
x=0
y = my_name.find(' ')-1
z = "AaEeIiOoUu"
while i >= 0 :
    if i%2 != 0:
        u = my_name[i]
        u= u.upper()
        c = my_name[x]
        c = c.lower()
        m = my_name[y]
        m = m.lower()
    if i%2 == 0:
        u = my_name[i]
        u = u.lower()
        c = my_name[x]
        c = c.upper()
        m = my_name[y]
        m = m.lower()
    if my_name[i] in z:
        s = ":-)"
    else:
        s =my_name[i]
    if my_name[i] in z:
        v = my_name[i]
    else:
        v =":-)"
    print(my_name[i], my_name[x], my_name[y], u, c, m, s, v)
    if y == 0:
        y = blank_pos
    elif y < blank_pos:
        y -=1
    elif y == blank_pos:
        y = name_len
    else:
        y -= 1
    x+=1
    i-= 1
