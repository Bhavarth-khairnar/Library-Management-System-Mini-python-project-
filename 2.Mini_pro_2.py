books_data={ 1: {"title": "Python Basics", "author": "John", "quantity": 5},
    2: {"title": "Data Science", "author": "Jane", "quantity": 3},}

def add_book():
    book_id = max(books_data.keys()) + 1
    titel=input("Enter book title: ")    
    author=input("Enter the author of book:")
    quantity=int(input("Enter the quantity of books:"))   
    books_data[book_id]={"titel":titel,"author":author,"quantity":quantity}
    print(books_data)
    main_menu() 
    
def update_book ():
    get_id=int(input("Enter the book ID :"))
    if get_id in books_data:
        title=input("Enter the title:")
        quantity=int(input("Enetr the quantity:"))
        books_data[book_id]["title"]=title
        books_data[book_id]["quantity"]=quantity
    else:
        print("Book not found")    
    main_menu() 
        
def delete_book ():
    get_id=int(input("Enetr the book Id:")) 
    if get_id in books_data:
        books_data.pop(get_id)
        print("Book deleted succesfully..")     
    else:
        print("Book are not found..")   
    main_menu()   
     
def search_book ():
    get_title = input("Enter book title or ID: ") 
    found=False
    for book_id, book in books_data.items(): 
        if get_title.lower() in book["title"].lower():
            print(f"Book found: {book_id}. {book['title']} by {book['author']} - {book['quantity']} copies")
            found=True
            break  
    if not found:
        print("Book not found in the library.") 
    main_menu() 
    
def borrow_book():
    get_id = int(input("Enter the book ID to borrow: "))
    if get_id in books_data:
        if books_data[get_id]["quantity"] > 0:
            books_data[get_id]["quantity"] -= 1
            print(f"You have borrowed '{books_data[get_id]['title']}'. Please return it on time.")
        else:
            print("Sorry, this book is currently not available.")
    else:
        print("Book not found.")
    main_menu() 

def return_book():
    get_id = int(input("Enter the book ID to return: "))
    if get_id in books_data:
        books_data[get_id]["quantity"] += 1
        print(f"Thank you for returning '{books_data[get_id]['title']}'.")
    else:
        print("Invalid book ID. This book does not belong to our library.") 
    main_menu()                 
def view_book ():
    print("\n Available Books:")
    for book_id, book in books_data.items():
        print(f"{book_id}. {book['title']} by {book['author']} - {book['quantity']} copies")
    main_menu() 
    
        
        
def main_menu():
    print("Menu:\n1. Add Book \n2. Update Book \n3. Delete Book \n4. View Books \n5. Search Book \n6. Borrow Book \n7. Return Book")   
    option=int(input("Enter the your choice:")) 
    if option==1:
        add_book()
    elif option == 2:
        update_book() 
    elif option == 3:
        delete_book ()      
    elif option == 4:
        view_book()  
    elif option == 5:
        search_book()
    elif option == 6:
        borrow_book()  
    elif option == 7:
        return_book()       
              
if __name__ == "__main__":
    main_menu()
        
        