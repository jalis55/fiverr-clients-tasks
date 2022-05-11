class Book:
    def __init__(self,book_name,book_qty) -> None:
        self.book_name=book_name
        self.book_qty=book_qty
    def display(self):
        print(f"Book name:{self.book_name}..Available Books:{self.book_qty}")

lst=[]
lst.append(Book('java 1',2))
lst.append(Book('c programming',5))

for i in lst:
    i.display()

