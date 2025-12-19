from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException #, Body
from pydantic import BaseModel, Field
from starlette import status

"""
What is Pydantics?
- Python Library that is used for data modelling, data parsing and has efficient error handling
- Pydantics is commonly used as a resource for data validation and how to handle data coming to our FastAPI application
"""

"""
Status Codes
- 1xx - Information Response: Request Processing
- 2xx - Success: Request Successfully complete
- 3xx - Redirection: Furrther action must be complete
- 4xx - Client errors: An error was caused by the client
- 5xx - Server errors: An error occurred on the server 

2xx Successful Status Codes:
200: OK - Standard Response for a Successful Reuqest. Commonly used for successful GET requests when data is being returned
201: Create - The request has been successful, creating a new resource. Used when a POST creates an entity
204: No Content - The request has been successful, did not create an entity nor return anything. Commonly used with PUT requests.

4xx Client Errors Status Codes:
400: Bad Request - Cannot process request due to client error. Commonly used for invalid request methods.
401: Unauthorized - Client does not have valid authentication for target resource
404: Not Found - The clients requested resource cannot be found
422: Unprocessable Entity - Semantic Errors in Client Request

5xx Server Status Codes:
500: Internal Server Error - Generic Error Message, when an unexpected issue on the server happened.

"""

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Book Author",
                "description": "A new description of a book.",
                "rating": 5,
                "published_date": 2025
            }
        }
    }

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2012),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2015),
    Book(3, 'Master Endpoints', 'codingwithroby', 'An awesome book', 5, 2020),
    Book(4, 'HP1', 'Author 1', 'Book description', 2, 2023),
    Book(5, 'HP2', 'Author 2', 'Book description', 3, 2023),
    Book(6, 'HP3', 'Author 3', 'Book description', 1, 2025),
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

#Assignment request
@app.get("/books/publish/}", status_code=status.HTTP_200_OK)
async def read_book_by_published_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


# @app.post("/create-book")
# async def create_book(book_request = Body()):
#     BOOKS.append(book_request)

# adding validation to create_book
@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

# this function updates the id of the book so that it doesn't clash with Books of the same id already stored.
def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put("/books/update-book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True

    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")

