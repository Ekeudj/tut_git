class Animal():
    def __init__(self,breed,age,owner,name):
        self.breed = breed
        self.age = 0
        self.owner = owner
        self.name = name

    def gen_description(self):
        credential = print("My name is "+self.owner+" I own a "+self.breed+".")
        return credential

    def specify(self):
        specific = print("My "+self.breed+" pet is "+str(self.age)+" years old.")
        return specific

    def update_age(self,new_age):
        if new_age >= self.age:
            age = new_age
        else:
            print("Changed swii.")

