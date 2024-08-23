from pydantic import BaseModel

class Page(BaseModel):
    number: int
    text: str

class Book(BaseModel):
    author: str
    title: str
    pages: list[Page]


my_books = [
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
]


print(my_books[1].author)
print(my_books[0].pages[0].text)

for book in my_books:
    print(book.title)
    print (book.pages[0].text)