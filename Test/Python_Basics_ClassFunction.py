class MyNFT:
    name = "NexaForge Technologies - Wales.." #Its a property of my nft class

    def __init__(self, name, age): #Buildin function in class and passing two arguments like Name, Age
        self.name = name
        self.age = age


    def sum(myself, a, b):
        print(a + b)


x = MyNFT("NFT Wales", 2) # its a veriable pass function of class
print(x.name)
x.sum(1, 2)
print(x.age)