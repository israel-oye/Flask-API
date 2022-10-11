# This is a simple RESTful API created with Flask-RESTFUL
###### The API is based on a model of a relationship betwixt a store(s) and an item(s). A user of the API can create items and add the store id of an existing Store.
**These are the endpoints and a guide**

**POST /auth**

## POST /register
>this is the endpoint to register a new user to have access to the resources.
```
Request Headers: 
Content-Type: application/json
Body(json): json
            {
                "username": "<new username>",
                "password": "<new user's password>"
            }
```

## POST /auth
>this is the endpoint to authenticate a registered user on the system. It returns a JWT access token if successful.
```
Request Headers:
Content-Type: application/json
Body(json): json
            {
                "username": "<username>",
                "password": "<user's password>"
            }

Response(json): json 
            {
                "access_token": "accessToken123"
            }  

Fail response(json)
        {
            "description": "Invalid credentials",
            "error": "Bad Request",
            "status_code": 401
        }         
```

## GET /item/<name>
>the endpoint to get an item by its name **Requires authentication**
```
Request Headers:
Content-Type: application/json
Authorization: JWT <access_token> #In a script, parse it as JWT access_token variable. JWT, a single white space and the token in string or a variable containing the string. e.g JWT eyj0xyz
Body(json): None #parse the item name in the url route e.g /item/foo_item
Response(json): json 
            {
                "name": "<NewItemName>",
                "price": <NewItemPrice>,
                "store": "Store name"
            }        
```

## POST /item/<name>
>the endpoint to create a new, unique item which belongs to a store. Will not allow duplicate item entry. **Requires authentication** Creating an Item with a store that does not exist may not work. It is advised to create a store first.
```
Request Headers:
Content-Type: application/json
Authorization: JWT <access_token> #In a script, parse it as JWT access_token variable. JWT, a single white space and the token in string or a variable containing the string. e.g JWT eyj0123
Body(json): json
            {
                "name": "<ItemName>",
                "price": <ItemPrice> #type: double,
                "store_id": <Store Id of new item> #type:integer
             }

Response(json): json 
            {
                "name": "<NewItemName>",
                "price": <NewItemPrice>,
                "store": "Store name"
            }        
```

## PUT /item/<name>
>the endpoint to edit an existing item which belongs to a store. If item with given parameters does not exist, it creates new one. **Requires authentication** 
```
Request Headers:
Content-Type: application/json
Authorization: JWT <access_token> #In a script, parse it as JWT access_token variable. JWT, a single white space and the token in string or a variable containing the string.
Body(json): json
            {
                "name": "<NewItemName>",
                "price": <NewItemPrice> #type: double,
                "store_id": <NewStoreId of item> #type:integer
             }

Response(json): json 
            {
                "name": "<NewItemName>",
                "price": <NewItemPrice>,
                "store": "Store name"
            }        
```

## DELETE /item/<name>
>the endpoint to delete an item by its name **Requires authentication** 
```
Request Headers:
Content-Type: application/json
Authorization: JWT <access_token> #In a script, parse it as JWT access_token variable. JWT, a single white space and the token in string or a variable containing the string.
Body(json): None #parse the item name in the url route e.g DELETE /item/foo
Response(json): json 
            {
                "message": "Item deleted"
            }    

Fail response(json): json
            {
                "message": "Item not found."
            }    
```

## GET /store/<name>
>the endpoint to get an item by its name **Requires authentication** 
```
Request Headers:
Content-Type: application/json
Authorization: JWT <access_token> #In a script, parse it as JWT access_token variable. JWT, a single white space and the token in string or a variable containing the string.
Body(json): json
            {
                "name": "<StoreName>"
            }
Response(json): json 
            {
                "items": [listOfItems],
                "name": <StoreName>,
                "store_id": <StoreID>
            }        
```

## POST /store/<name>
>the endpoint to create a new, unique store. Will not allow duplicate store entry. **Requires authentication** 
```
Request Headers:
Content-Type: application/json
Authorization: JWT <access_token> #In a script, parse it JWT acess_token variable. JWT, a single white space and the token in string
Body(json): json
            {
                "name": "New store name"
            }

Response(json): json 
            {
                "items": [listOfItems],
                "name": "New store name",
                "store_id":
            }        
```

## DELETE /store/<name>
>the endpoint to delete a store by its name **Requires authentication** 
```
Request Headers:
Content-Type: application/json
Authorization: JWT <access_token> #In a script, parse it as JWT access_token variable. JWT, a single white space and the token in string or a variable containing the string.
Body(json): None #parse the item name in the url route e.g DELETE /item/foo
Response(json): json 
            {
                "message": "Store deleted"
            }    

Fail response(json): json
            {
                "message": "Item not found."
            }    
```

## GET /items
>the endpoint to get a list of all items 
```
Request Headers:
Content-Type: application/json
Body(json): None
Response(json): json 
            {
                "items": [ListOfItems]
            }        
```

## GET /store
>the endpoint to get a list of all stores 
```
Request Headers:
Content-Type: application/json
Body(json): None
Response(json): json 
            {
                "stores": [ListOfStores]
            }        
```
