#Sandpiles are a cool idea
#Made by Eli Thorpe
#Hey, note for people who understand how to control the size of ints in python (I don't):
    #A stable array can be written as (rows*cols) 2-bit ints, and I would say that 3 or 4 bits would be enough for the internal calculations
    #So if you are running out of space, and you are able to do that in Python, switch from basic ints to bitstrings of length 4

#Set this to where you want to save the output. In theory you can just set this to "output.txt", but for me that will just to "C:\Users\Eli\output.txt", which isn't what I want
output_dir="C:\\Users\\Eli\\Documents\\GitHub\\sandpiles\\output"
output_name="output1.csv"
debug=True #controls the main testing prints
def check(pile):
    #checks that the pile is fully settled, i.e. all cells are less than 3 (in a square setup, which is all this will be able to carry for awhile)
    for i in range(len(pile)):
        for j in range(len(pile[i])):
            if pile[i][j]>3:
                return False
    return True

def simple(val,rows,cols):
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
    sand=simple(0,len(pile),len(pile[0])) #sand is the new sandpile, pile is the old
    for i in range(len(pile)):
        for j in range(len(pile[i])):
            sand[i][j]+=pile[i][j]%4
            n=pile[i][j]/4
            if n>0:
                if i>0:
                    sand[i-1][j]+=n
                if j>0:
                    sand[i][j-1]+=n
                if i<len(pile)-1:
                    sand[i+1][j]+=n
                if j<len(pile[i])-1:
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
    sand=simple(0,len(pile1),len(pile1[0]))
    for i in range(len(pile1)):
        for j in range(len(pile1[i])):
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
                a.append(b)
                pos.append(a)
        return pos
def main(start, adds,show=debug,i_0=0):
    #Start is the thing that adds are piled onto, show=True means it prints the piles at internal steps while show=False just prints % done after every add,
    #i_0 is where it starts numbering the items
    ##assumes that everything will work, or that you will see what the errors are and tell me
    #f=open(output_dir+"\\"+output_name,"w")
    #f.write("ID,Addition,ar1c1,ar1c2,ar1c3,ar2c1,ar2c2,ar2c3,ar3c1,ar3c2,ar3c3,Result,rr1c1,rr1c2,rr1c3,rr2c1,rr2c2,rr2c3,rr3c1,rr3c2,rr3c3\n")
    #if debug:
        #f.write("Test,123456789,1,2,3,4,5,6,7,8,9,987654321,9,8,7,6,5,4,3,2,1\n")
    #Test looks like this:
    #1  2  3
    #4  5  6
    #7  8  9
    #And has result of this:
    #9  8  7
    #6  5  4
    #3  2  1
    out=[]
    for i,add in enumerate(adds):
        #f.write(str(i)+",")
        #s1=""
        #s2=""
        #for j in range(len(add)):
        #    for k in range(len(add[j])):
        #        s1+=str(add[j][k])
        #        s2+=","+str(add[j][k])
        #f.write(s1+s2+",")
        p=add_piles(start,add)
        if show:
            print p
        else:
            print str((100*i)/len(adds))+"%"#Because this takes awhile, shows that it hasn't hung
        p=settle(p,show=show)
        out.append([i+i_0,add,p])
        #s1=""
        #s2=""
        #for j in range(len(p)):
        #    for k in range(len(p[j])):
        #        s1+=str(p[j][k])
        #        s2+=","+str(p[j][k])
        #f.write(s1+s2+"\n")
    #f.close()
    return out
def write_pile_list(piles_list,loc=(output_dir+output_name)):
    #meant to intake the output of main, outputs it to a .csv or .txt
    f=open(loc,"w")
    for l in piles_list:
        s1=str(l[0])+","
        s2=""
        s3=""
        for r in l[1]:
            for c in r:
                s2+=str(c)
                s3+=","+str(c)
        f.write(s1+s2+s3+",")
        s2=""
        s3=""
        for r in l[2]:
            for c in r:
                s2+=str(c)
                s3+=","+str(c)
        f.write(s2+s3+"\n")
    f.close()
def filter_unique_outs(outs):
    #Originally was recursive, but it was getting close to the memory limit on a 2X2 pile
    out=[]
    a=outs[:]
    while len(a)!=0:
        b=a.pop(0)
        out.append(b)
        def not_unique(c):
            if c[-1]==b[-1]:
                return False
            return True
        a=filter(not_unique,a)
    #print a
    return out
       
#f=open("C:\Users\Eli\Documents\GitHub\sandpiles\output.txt","w")
#f.write("Test")
#f.close()