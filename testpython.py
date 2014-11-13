
message = "Hello how are you?"
for word in message.split():
    print (word)

words = ('ccol','powerful','readable')
for i in range(0,len(words)):
    print(i,words[i])

#d = {'a':1, 'b':1.2, 'c':1j}
#for key, val in d.iteritems():
#    print("key: %s has value %s" %(key,val))
    
def diskArea(radius=3):
    return 3.14*radius*radius
print(diskArea(1.5))
print(diskArea())

def slicer(seq, start=None, stop=None,step=None):
    return seq[start:stop:step]

rhyme = 'one fish, two fish, red fish, blue fish'.split()
print(rhyme)
print(slicer(rhyme))
print(slicer(rhyme,step=2))
print(slicer(rhyme,1,step=2))
print(slicer(rhyme,1,4,2))

def tryToModify(x,y,z):
    x=23
    y.append(42)
    z=[99]
    print(x)
    print(y)
    print(z)

a = 77
b = [99]
c = [28]
tryToModify(a,b,c)
print(a)
print(b)        #b is now [99, 42]
print(c)

