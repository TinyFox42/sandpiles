#Sandpiles are a cool idea
#Made by Eli Thorpe
#Hey, note for people who understand how to control the size of ints in python (I don't):
    #A stable array can be written as (rows*cols) 2-bit ints, and I would say that 3 or 4 bits would be enough for the internal calculations
    #So if you are running out of space, and you are able to do that in Python, switch from basic ints to bitstrings of length 4
rows=3
cols=3
debug=True #controls the main testing prints
def check(pile):
    #checks that the pile is fully settled, i.e. all cells are less than 3 (in a square setup, which is all this will be able to carry for awhile)
    #Please make sure that the dimensions of this are correct, I'm not planning on covering that up
    for i in range(rows):
        for j in range(cols):
            if pile[i][j]>3:
                return False
    return True

def simple(val):
    #makes a pile where all of the cells have the same value
    pile=[]
    for i in range(rows):
        r=[]
        for j in range(cols):
            r.append(val)
        pile.append(r)
    return pile
    
def settle(pile, show=debug):
    #goes through one iteration of settling the sandpile, then recurses. 
    #Show is a debugging option that you may want, prints the pile after every iteration
    sand=simple(0) #sand is the new sandpile, pile is the old
    for i in range(rows):
        for j in range(cols):
            sand[i][j]+=pile[i][j]%4
            n=pile[i][j]/4
            if n>0:
                if i>0:
                    sand[i-1][j]+=n
                if j>0:
                    sand[i][j-1]+=n
                if i<rows-1:
                    sand[i+1][j]+=n
                if j<cols-1:
                    sand[i][j+1]+=n
    if show:
        print sand
        print "\n"
    if check(sand):
        return sand
    else:
        return settle(sand,show)
def add_piles(pile1, pile2):
    #adds the two together, returns the resulting pile without settling, doesn't touch the input arrays
    sand=simple(0)
    for i in range(rows):
        for j in range(cols):
            sand[i][j]+=pile1[i][j]
            sand[i][j]+=pile2[i][j]
    return sand
#ok, I'm going to make a method that works for a 3x3 right now, and then try to make a general one later. Probably going to be a bit recursive
def all_3x3():
    #makes a very large list, with 262,144 members, each which is a 3x3 matrix. Fun!
    #the members are [[a,b,c],[d,e,f],[g,h,i]]
    piles=[]
    #x=0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        for f in range(4):
                            for g in range(4):
                                for h in range(4):
                                    for i in range(4):
                                        #oh god, what have I done?
                                        piles.append([[a,b,c],[d,e,f],[g,h,i]])
    return piles



#Ok, recursive formation of all arrays in the current dimensions
def all_rows(rs):
    if rs==1:
        return [[0],[1],[2],[3]]#Returns the 4 base lists
    else:
        smalls=all_rows(rs-1)
        pos=[]
        for r in smalls:
            for i in range(4):
                a=r[:]
                a.append(i)
                pos.append(a)
        return pos
def all_arrs(cs, rs):
    #Warning, at best this runs proportional to 4^(cs*rs), and this isn't the best case program
    if cs==1:
        pos=[]
        r=all_rows(rs)
        for a in r:
            pos.append([a])
        return pos
    if cs>1:
        pos=[]
        arrs=all_arrs(cs-1,rs)
        r=all_rows(rs)
        for arr in arrs:
            for row in r:
                a=arr[:]
                b=row[:]
                a.append([b])
                pos.append(a)
        return pos