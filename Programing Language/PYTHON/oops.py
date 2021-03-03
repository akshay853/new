class Animal:
    def __init__(self,name,kilo):
        self.name = name
        self.kilo = kilo
        #print("hello"+self.name)


class Lion(Animal):
    def __init__(self):
        print("I am lion with ID : 234567382","I am a herbivorous",sep="\n")



if __name__ == '__main__':
    array = []

    array.append(Animal("Lion",200))
    array.append(An
    imal("Tiger",170))
    array.append(Animal("deer",120))

    for arr in array:
        print(arr.name,arr.kilo,sep="\t\t",end = "\n")
    
    l = Lion()

