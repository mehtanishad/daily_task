class programmer:
    company = "microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getinfo(self):
        print(f"The name is the {self.company} programmer is {self.name} and product is {self.product} ")

nimisha = programmer("nimisha", "skype")
ram = programmer ("ram", "github")
nimisha.getinfo()
ram.getinfo()
