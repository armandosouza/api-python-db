from fastapi import FastAPI
from typing import Union

app = FastAPI()
persons = [
	{
		"number": 1,
		"name": "Mahesh",
		"age": 25,
		"city": "Bangalore",
		"country": "India"
	},
	{
		"number": 2,
		"name": "Alex",
		"age": 26,
		"city": "London",
		"country": "UK"
	},
	{
		"number": 3,
		"name": "David",
		"age": 27,
		"city": "San Francisco",
		"country": "USA"
	},
	{
		"number": 4,
		"name": "John",
		"age": 28,
		"city": "Toronto",
		"country": "Canada"
	},
	{
		"number": 5,
		"name": "Chris",
		"age": 29,
		"city": "Paris",
		"country": "France"
	},
]

@app.get("/index")
def read_root():
	return {"Hello": "World"}


@app.get("/persons/{person_id}")
def read_item(person_id: int, q: Union[str, None]=None):
	return persons[person_id]