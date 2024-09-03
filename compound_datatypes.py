

fruits = ["apple", "banana", "cherry", "date"]

fruits.append("elderberry")

fruits.remove("banana")

fruits.sort()

print(fruits)

student = {
    "name": "John Doe",
    "age": "26",
    "major": "Computer Science"
}

student.update({"major": "Electrical Engineering"})

student.update({"year": "Senior"})

print(student.keys())

print(student.values())


#"Horus Rising","Dan Abnett", 2006
#"False Gods", "Graham McNeill", 2006
#"The Flight of the Eisensten", "James Swallow", 2007

booklist = {
    "book1": {"title": " ", "author": " ", "year": " "}, 
    "book2": {"title": " ", "author": "", "year": " "}, 
    "book3": {"title": " ", "author": " ", "year": " "}
    }

booklist["book1"]["title"] = "Horus Rising"
booklist["book1"]["author"] = "Dan Abnett"
booklist["book1"]["year"] = 2006

booklist["book2"]["title"] = "False Gods"
booklist["book2"]["author"] = "Graham McNeill"
booklist["book2"]["year"] = 2006

booklist["book3"]["title"] = "The Flight of the Eisenstein"
booklist["book3"]["author"] = "James Swallow"
booklist["book3"]["year"] = 2007


first_title = booklist["book1"]["title"]
first_author = booklist["book1"]["author"]
second_title = booklist["book2"]["title"]
second_author = booklist["book2"]["author"]
third_title = booklist["book3"]["title"]
third_author = booklist["book3"]["author"]
third_pub = booklist["book3"]["year"]


print(f"The Second Title is: ", second_title)

print(f"The Third Book's Year of Publication is:", third_pub)

print(f"The first book's title is:",first_title)
print("The first book's author is:",first_author)

print(f"The second book's title is:",second_title)
print("The second book's author is:",second_author)

print(f"The third book's title is:",third_title)
print("The third book's author is:",third_author)


course = {
    "math": (["Dick", "Philip", "Elvis", "Ryan"]),
    "history": (["Dick", "Philip", "Elvis", "Ryan"]),
    "chemistry": (["Dick", "Philip", "Elvis", "Ryan"])
}

course["math"].extend(["Harry", "Sally", "John", "Jane", "Jack"])

course["history"].pop(1)

chem_st = course["chemistry"]

course.update({"physics": ["Tom", "Mark", "Jeremy", "Don"]})

print(course)
print(chem_st)