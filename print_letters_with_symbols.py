print("\n")
---------------------------------------------------------------------------
Print K with % using for loop 1
h = 8
w = 9
x = 0
v = w

for i in range(h):
    for j in range(w):
        if j == 0 or (j == x and i >= h // 2) or j == v:
            print("%", end="")
            v -= 1
        else:
            print(" ", end="")
    x += 1
    print()


print("\n")
-----------------------------------------------------------------------------
Print Kl with % using for loop
h = 8
w = 9
x = 0
v = w

for i in range(h):
    for j in range(w):
        if j == 0 or (j == x and i >= h // 2) or j == v:
            print("%", end="")
            v -= 1
        else:
            print(" ", end="")
    x += 1
    print("   %")


print("\n")
----------------------------------------------------------------
Print A with % using for loop
h = 7
w = 13
x = 0

for i in range(h):
    for j in range(w):
        if (j == w // 2 and i == 0) or (j == (w // 2) - x  and i > 0) or (j == (w // 2) + x and i > 0) or (i == h // 2 and ((j == w // 2) or (j == (w // 2) - 2) or (j == (w // 2) + 2))):
            print("%", end="")
        else:
            print(" ", end="")
    x += 1
    print()


print("\n")
-----------------------------------------------------------
Print H with @ using for loop 1
h=8
for i in range(h):
    if i ==  h//2:
        print("@"*7)
    else:
        print("@     @")



print("\n")
-------------------------------------------------------------
Print H with @ using for loop 2
h = 7
w = 9
for i in range(h):
    for j in range(w):
        if j == 0 or j == w - 1 or i == h // 2:
            print("@", end="")
        else:
            print(" ", end="")
    print()



print("\n")
-------------------------------------------------------------
Print |\ with $ using for loop

h = 7
w = 7
x = 0

for i in range(h):
    for j in range(w):
        if j == 0 or j == x:
            print("$", end="")
        else:
            print(" ", end="")
    x += 1
    print()



print("\n")
------------------------------------------------------------
Print K with % using for loop
h = 8
w = 10
x = 0
v = w

for i in range(h):
    for j in range(w):
        if (j == 0) or (i >= h // 2 and j == x + 1) or (i <= h // 2 and j == v - 1):
            print("%", end="")
            v -= 1
        else:
            print(" ", end="")
    x += 1
    print()



print("\n")
-----------------------------------------------------------------
Print N with % using for loop

h = 7
w = 7
x = 0

for i in range(h):
    for j in range(w):
        if j == 0 or j == x:
            print("%", end="")
        else:
            print(" ", end="")
    x += 1
    print("%")


print("\n")
--------------------------------------------------------------------
