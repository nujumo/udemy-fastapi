from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "maths"},
    {"title": "Title Five", "author": "Author Five", "category": "maths"},
    {"title": "Title Six", "author": "Author Two", "category": "maths"},
]

@app.get("/books")
# async in not needed in FastAPI
# but it wil be used explicitly here in every function that is an api endpoint that we create
async def read_all_books():
    return BOOKS

"""
What are Path Parameters?

- Path Parameters are request parameters that have been attached to the URL
- Path Parameters are usually defined as a way to find information based on location
- Think of a computer file system:
    - You can identify the specific resources based on the file you are in 
    e.g. /Users/nuamonag/desktop
- NB Order matters when declaring path parameters - always have the smallest/static functions higher in the order

Dynamic Path Parameters
#######################
e.g. 127.0.0.1:8000/books/title_four
"""

# Assignment
# Query parameter
@app.get("/books/byauthor/")
async def read_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

# this function needs to be above the dynamic_param function to prevent a clash
# @app.get("/books/mybook")
# async def read_all_books():
#     return {'book_title': 'My favourite book!'}

@app.get("/books/{book_title}")
# async in not needed in FastAPI
# but it wil be used explicitly here in every function that is an api endpoint that we create
async def read_book(book_title: str):
    # return {'dynamic_param': book_title}
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return None

"""
What are Query Parameters?
- Query Parameters are request parameters that have been attached after a "?"
- Query Parameters have name=value pairs e.g. 127.0.0.1:8000/books/?category=science
- Query Parameters can be used with Path Parameters e.g. 127.0.0.1:8000/books/author%20four/?category=science
"""

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category") == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (book.get("author").casefold() == book_author.casefold() and
                book.get("category") == category.casefold()):
            books_to_return.append(book)

    return books_to_return

@app.post("/books/create_book/")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book/")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

# Assignment
# Path parameter
@app.get("/books/byauthor/{author}")
async def read_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return
