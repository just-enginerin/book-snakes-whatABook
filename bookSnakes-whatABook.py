"""
  Title: bookSnakes-whatABook.py
  Authors: Erin Brady, Yakut Ahmedin, Brett Grashorn
  Date: 13 May 2023
  Description: Assignment 9.2: WhatABook Delivery
"""

import pymongo
import bson

# Build a connection string to connect to WhatABook database.
client = pymongo.MongoClient("mongodb+srv://whatABook_user:s3cret@bellevueuniversity.nhzwaya.mongodb.net/WhatABookretryWrites=true&w=majority")

# Configure a variable to access WhatABook.
db = client['WhatABook']

# Query to display a wishlist by customer ID.
def displayCustomerWishlist(customerId):
    specified_customer = db.customers.find_one({'_id': bson.ObjectId(customerId)})

    # Check if the customer's wishlist has any items.
    if specified_customer['wishlistItems'] == []:
        # Error message: Wishlist is empty.
        print(specified_customer['firstName'] + ' ' + specified_customer['lastName'] + "'s wishlist is empty.")

    else:
        # Success Message: display all wishlist items.
        for item in specified_customer['wishlistItems']:
            print(specified_customer['firstName'] + ' ' + specified_customer['lastName'] + "'s wishlist:")
            print(item['title'] + ' by ' + item['author'])


# Query to add a book to a customer’s wishlist.
def addBookToCustomerWishlist(customerId, bookId):
    specified_customer = db.customers.find_one({'_id': bson.ObjectId(customerId)})
    newBook = db.books.find_one({'bookId': bookId})

    # Get the existing wishlist items or create an empty list
    wishlist_items = specified_customer.get('wishlistItems', [])

    # Check if the book already exists within the customer's wishlist.
    for item in wishlist_items:
        if item.get('bookId') == bookId:
            # Error Message: The book is already on the customer's wishlist.
            print(newBook['title'] + ' is already on ' + specified_customer['firstName'] + ' ' + specified_customer['lastName'] + "'s wishlist!")
            break
    else:
        # Append the new book to the wishlist
        wishlist_items.append(newBook)

        # Update the customer document with the new wishlist items
        db.customers.update_one({'_id': specified_customer['_id']}, {'$set': {'wishlistItems': wishlist_items}})

        # Success message
        print(newBook['title'] + ' successfully added to ' + specified_customer['firstName'] + ' ' + specified_customer['lastName'] + "'s wishlist!")


# Query to remove a book from a customer's wishlist.
def removeBookFromCustomerWishlist(customerId, bookId):
    specified_customer = db.customers.find_one({'_id': bson.ObjectId(customerId)})
    specified_book = db.books.find_one({'bookId': bookId})

    # Get the existing wishlist items or create an empty list
    wishlist_items = specified_customer.get('wishlistItems', [])

    # Check if the customer's wishlist has any items.
    if specified_customer['wishlistItems'] == []:
        # Error message: The book cannot be removed because the wishlist is empty.
        print('Cannot remove ' + specified_book['title'] + '. ' + specified_customer['firstName'] + ' ' + specified_customer['lastName'] + "'s wishlist is empty!")
    
    else:
        # Check if the book exists within the customer's wishlist.
        for item in wishlist_items:
            if item.get('bookId') == bookId:

                # Remove the book from the customer's wishlist items.
                wishlist_items.remove(specified_book)

                # Update the customer's wishlist with the updated list items.
                db.customers.update_one({'_id': specified_customer['_id']}, {'$set': {'wishlistItems': wishlist_items}})
                print(specified_book['title'] + ' has been successfully removed from ' + specified_customer['firstName'] + ' ' + specified_customer['lastName'] + "'s wishlist!")
                break
        else:
            # Error message: the book cannot be removed because it is not on the customer's wishlist.
            print(specified_book['title'] + ' is not on ' + specified_customer['firstName'] + ' ' + specified_customer['lastName'] + "'s wishlist!")


# Choose a specific customer and book to run these queries.
specified_customer_id = '645ffc94dbe34a2962b0542a'
specified_book_id = '978-1408855652'

print('Display a wishlist by customer ID:')
displayCustomerWishlist(specified_customer_id)
print('\n')

print('Add a book to a customer’s wishlist:')
addBookToCustomerWishlist(specified_customer_id, specified_book_id)
print('\n')

print('Remove a book from a customer’s wishlist:')
removeBookFromCustomerWishlist(specified_customer_id, specified_book_id)
print('\n')
