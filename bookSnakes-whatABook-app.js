/*
============================================
; Title:  bookSnakes-whatABook-app.js
; Author: Erin Brady
; Date:   6 May 2023
; Description: Server setup file for WhatABook app by Team Book Snakes
;===========================================
*/

"use strict"

const express = require("express")
const http = require("http")
const swaggerUi = require("swagger-ui-express")
const swaggerJsDoc = require("swagger-jsdoc")
const mongoose = require("mongoose")
// const customerAPI = require('./routes/bookSnakes-whatABook-customer-routes')

const app = express()
app.set('port', process.env.PORT || 3000)
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

// MongoDB Atlas Connection
const conn = `mongodb+srv://whatABook_user:s3cret@bellevueuniversity.nhzwaya.mongodb.net/WhatABook`
mongoose.connect(conn, {
    promiseLibrary: require('bluebird'),
    useUnifiedTopology: true,
    useNewUrlParser: true
}).then(() => {
    console.log(`Connection to WhatABook database on MongoDB Atlas successful`)
}).catch(err => {
    console.log(`MongoDB Error: ${err.message}`)
})

const options = {
    definition: {
        openapi: "3.0.0",
        info: {
            title: "WEB 335: Introduction to NoSQL: WhatABook Project by Team Book Snakes",
            version: "1.0.0"
        },
    },
    apis: ['./docs/**/*.yaml', "./routes/*.js"] // files containing annotations for the OpenAPI Specification
}

const openApiSpecification = swaggerJsDoc(options)


app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(openApiSpecification))
// app.use('/api', bookAPI)

http.createServer(app).listen(app.get('port'), () => {
    console.log(`Application started and listening on port ${app.get('port')}`)
})
