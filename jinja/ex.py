import jinja2

env = jinja2.Environment()
template = env.from_string("Hi {{ their_name }}, my name is {{ my_name }}.")
print(template.render(their_name="John", my_name="Mary"))


class Page:
    def __init__(self, number, text):
        self.number = number
        self.text = text

class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages



env = jinja2.Environment()
template = env.from_string("""
My favorite fruits are:
{% for fruit in fruits -%}
 {{ fruit }}
{% endfor %}
""")
print(template.render(fruits=["apples", "oranges","bannana","watermelon"]))

env = jinja2.Environment()
template = env.from_string("""
Title of the books are:
{% for book in my_books -%}
- {{ book.title }}
{% endfor %}
""")

print(template.render(my_books=[
         Book(
		    author="J. K. Rowling",
		    title="Harry Potter and the Philosopher's stone",
		    pages=[
		        Page(
		            number=1,
		            text="There once was a boy...",
		        ),
		        Page(
		            number=2,
		            text="He went to magic school...",
		        )
		    ]
		),
		Book(
		    author="Roger Zelazny",
		    title="Lord of Light",
		    pages=[
		        Page(
		            number=1,
		            text="It is said that fifty-three years ago...",
		        )
		    ]
		),
		Book(
            author="D.r Alemayehu wase",
		    title="Zigora",
		    pages=[
		        Page(
		            number=1,
                    text="The morning sun was shinning the cold breeze of the the wind gives chills through the body....."
                )
            ]
        )
]) )

