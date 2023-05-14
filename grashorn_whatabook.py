"""
  Title: bookSnakes-whatABook.py
  Authors: Erin Brady, Yakut Ahmedin, Brett Grashorn
  Date: 13 May 2023
  Description: Assignment 9.2: WhatABook Delivery
"""
# Query to add a book to a customer's wishlist.


import pymongo
import bson

# Build a connection string to connect to WhatABook database.
client = pymongo.MongoClient(
    "mongodb+srv://whatABook_user:s3cret@bellevueuniversity.nhzwaya.mongodb.net/WhatABookretryWrites=true&w=majority")

# Configure a variable to access WhatABook.
db = client['WhatABook']


def addBookToCustomerWishlist(customerId, bookId):
    specified_customer = db.customers.find_one(
        {'_id': bson.ObjectId(customerId)})
    newBook = db.books.find_one({'bookId': bookId})

    # Gets already existing wishlist/creates empty list.
    wishlist_items = specified_customer.get('wishlistItems', [])

    # Check customers wishlist to see if book already exists.
    for item in wishlist_items:
        if item.get('bookId') == bookId:
            # Displays Error Message: The book is already on the customer's wishlist.
            print(newBook['title'] + ' is already on ' + specified_customer['firstName'] +
                  ' ' + specified_customer['lastName'] + "'s wishlist!")
            break
    else:
        # Appends new book to the wishlist.
        wishlist_items.append(newBook)

        # Updates customer document with new items
        db.customers.update_one({'_id': specified_customer['_id']}, {
                                '$set': {'wishlistItems': wishlist_items}})

        # Displays Success message
        print(newBook['title'] + ' successfully added to ' + specified_customer['firstName'] +
              ' ' + specified_customer['lastName'] + "'s wishlist!")


# Choose a specific customer and book to run these queries.
specified_customer_id = '645ffc94dbe34a2962b0542a'
specified_book_id = '978-1408855652'

print('Add a book to a customer’s wishlist:')
addBookToCustomerWishlist(specified_customer_id, specified_book_id)
print('\n')
