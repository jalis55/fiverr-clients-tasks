class Employee:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.email=self.first_name.lower()+self.last_name.lower()+'@company.com'

    def full_name(self):
        return '{} {}'.format(self.first_name.capitalize(),self.last_name.capitalize())



e1=Employee('jalis','tarif')

print(e1.full_name())