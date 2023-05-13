/**
	Title: bookSnakes-whatABook-createCustomers.js
    Authors: Erin Brady, Yakut Ahmedin, Brett Grashorn
    Date: 6 May 2023
    Description: MongoDB Shell Scripts for the books collection.
*/

/**
 * NOTE: Connect to the database in mongosh using the following command: mongosh "mongodb+srv://bellevueuniversity.nhzwaya.mongodb.net/WhatABook" --username whatABook_user
 * password: s3cret
*/

// Delete any books collections.
db.books.drop()

// Create the books collection using Document Validation.
db.createCollection("books", {
	validator: { $jsonSchema: {
		bsonType: "object",
		properties: {
			bookId: {
				bsonType: "string"
			},
			title: {
				bsonType: "string"
			},
			author: {
				bsonType: "string"
			},
			genre: {
				bsonType: "string"
			}
		}
	}}
})

// Insert the Book documents.
db.books.insertMany([
    {
        "bookId": "978-0142424179",
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "genre": "Young Adult Fiction"
    },
    {
        "bookId": "978-1408855652",
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy"
    },
    {
        "bookId": "978-0316278013",
        "title": "Ready Player Two",
        "author": "Ernest Cline",
        "genre": "Science Fiction"
    },
    {
        "bookId": "978-0345391803",
        "title": "Jurassic Park",
        "author": "Michael Crichton",
        "genre": "Science Fiction"
    },
    {
        "bookId": "978-0743273565",
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "genre": "Fiction"
    },
	{
        "bookId": "978-1401309706",
        "title": "Bossypants",
        "author": "Tina Fey",
        "genre": "Autobiography"
    },
    {
        "bookId": "978-0385517255",
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "genre": "Mystery"
    },
    {
        "bookId": "978-0062699787",
        "title": "Becoming",
        "author": "Michelle Obama",
        "genre": "Autobiography"
    },
    {
        "bookId": "978-0062315007",
        "title": "Yes Please",
        "author": "Amy Poehler",
        "genre": "Humor"
    },
	{
        "bookId": "978-0547928227",
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "genre": "Young Adult Fiction"
    },
    {
        "bookId": "978-1594489501",
        "title": "A Thousand Splendid Suns",
        "author": "Khaled Hosseini",
        "genre": "Fiction"
    }
])

// Display a list of books.
db.books.find()

// Display a list of books by genre.
db.books.find({genre: "Autobiography"}).toArray()

// Display a list of book by author.
db.books.find({author: "Khaled Hosseini"}).toArray()

// Display a book by bookId.
db.books.find({bookId: "978-0316278013"}).toArray()
