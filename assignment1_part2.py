class Book:
    def __init__(self):
        title= raw_input("What is the title of the book?:").strip()
        author = raw_input("Who is the author of the book?:").strip()
        print ("The Book Of The Year Is: {}, Written By: {}").format(title, author)


Book1= Book()

Book1

