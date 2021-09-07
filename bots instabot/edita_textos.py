coisas = ['oi','Bom dia','que dia lindo', 'muita paz']


#epilef = set(felipe.read())

def writedown(content):
    n=0
    felipe = open( 'C:/Users/Felilpe Lima/Desktop/ODE/OBAOBA.py', 'a')

    felipe.write("[")
    for x in content:
        felipe.write("'")
        felipe.write(coisas[n])
        felipe.write("'")
        if n!=len(content)-1:
            felipe.write(",")
        n+=1

    felipe.write("]")
    felipe.close()

writedown(coisas)

felipe = open('C:/Users/Felilpe Lima/Desktop/ODE/OBAOBA.py', 'r')
oi=felipe.read()


print(oi,len(oi))

