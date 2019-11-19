#Sandpiles are a cool idea
#Made by Eli Thorpe
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