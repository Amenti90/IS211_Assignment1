# class Book:
#     def __init__(self):
#         title= raw_input("What is the title of the book?:").strip()
#         author = raw_input("Who is the author of the book?:").strip()
#         print ("The Book Of The Year Is: {}, Written By: {}").format(title, author)
#
#
# Book1= Book()
#
# Book1
#

class Book:
    title =  ""
    author = ""
    def display (self):
        desc = " %s is the title of the book written by %s ." % (self.title, self.author)
        print desc

book1= Book()
book1.title = "Of Mice & Men"
book1.author = "John Steinbeck"
book1.display()

book2= Book()
book2.title = "To Kill A Mockingbird"
book2.author = "Harper Lee"
book2.display()





