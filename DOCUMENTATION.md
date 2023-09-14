CREATE OBJECT

POST request with the following data
name: string (required)
state: string (not required)
area: string (not required)
house_no:string (not required)
height: string (not required)
weight:string (not required)
complexion:string (not required)
NOTE: an object can be created with just the name field
example:
REQUEST:
POST: localhost:8000/api/
BODY(JSON)--> {"name":"Joyin"}
RESPONSE:
{
  "name": "Joyin",
  "email": null,
  "physique": {
    "height": null,
    "weight": null,
    "complexion": null
  },
  "address": {
    "area": null,
    "state": null,
    "house_no": null
  }
}


UPDATE object
PATCH request to the endpoint api/user_id with the field whose data is to be updated
example:
REQUEST:
PATCH: localhost:8000/api/1
BODY--> {
 "name":"dami",
  "email":"dami+4@gmail.com",
  "physique":{
    "weight":"50kg",
    "height":"5'11",
    "complexion":"dark"
    
  }
}

RESPONSE:
{
  "name": "dami",
  "email": "dami+8@gmail.com",
  "physique": {
    "height": "5'11",
    "weight": "50kg",
    "complexion": "dark"
  },
  "address": {
    "area": null,
    "state": null,
    "house_no": null
  }
}

DELETE object 
DELETE request to the endpoint api/user_id with the id whose data is to be deleted
example:
REQUEST:
DELETE: localhost:8000/api/1
RESPONSE:
{'message':'Deleted Successfully'}


RETRIEVE object
GET request to the endpoint api/user_id with the id whose data is to be deleted
example:
REQUEST:
GET: localhost:8000/api/1
RESPONSE:
{
  "name": "dami",
  "email": "dami+8@gmail.com",
  "physique": {
    "height": "5'11",
    "weight": "50kg",
    "complexion": "dark"
  },
  "address": {
    "area": null,
    "state": null,
    "house_no": null
  }
}
}
