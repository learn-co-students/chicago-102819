
# Module 2 Assessment

Welcome to your Mod 2 Assessment. You will be tested for your understanding of concepts and ability to solve problems that have been covered in class and in the curriculum.

Use any libraries you want to solve the problems in the assessment.

The sections of the assessment are:

- Accessing Data Through APIs
- Object Oriented Programming
- SQL and Relational Databases

In this assessment you will primarily be exploring a Pokemon dataset. Pokemon are fictional creatures from the [Nintendo franchise](https://en.wikipedia.org/wiki/Pok%C3%A9mon) of the same name.

Some Pokemon facts that might be useful:
* The word "pokemon" is both singular and plural. You may refer to "one pokemon" or "many pokemon".
* Pokemon have attributes such as a name, weight, and height.
* Pokemon have one or multiple "types". A type is something like "electric", "water", "ghost", or "normal" that indicates the abilities that pokemon may possess.
* The humans who collect pokemon are called "trainers".


```python
# import the necessary libraries
import requests
import json
import pandas as pd
import sqlite3
```

## Part 1: Accessing Data Through APIs [Suggested Time: 25 minutes]

In this section we'll be using PokeAPI to get data on Pokemon. 

[Consult the documentation here](https://pokeapi.co/docs/v2.html) for information on obtaining data from this API.

### 1. Get the "types"
We want to know the "types" of any particular pokemon given it's name. Complete the `get_pokemon_types` function below. It should return a `list` of all the names of the "types" that pokemon has

Make a request to `"https://pokeapi.co/api/v2/pokemon/<add-name-of-pokemon-here>"`. Inspect the API response and extract the names of the types. Here are the [docs for this specific API route](https://pokeapi.co/docs/v2.html/#pokemon).

```python
# Examples: 
get_pokemon_types("pikachu")   # returns ["electric"]
get_pokemon_types("bulbasaur") # returns ["poison", "grass"]
get_pokemon_types("snorlax")   # returns ["normal"]
get_pokemon_types("moltres")   # returns ["flying", "fire"]
```


```python
def get_pokemon_types(name):
    '''
    input: name - a string of the pokemon's name
    
    return: a list of strings of the one or more types belonging to the pokemon
    '''
    pass
```


```python
get_pokemon_types("bulbasaur")
```

## Part 2: Object Oriented Programming [Suggested Time: 20 minutes]

As a pokemon trainer we want to make sure our pokemon are performing at their peak. To measure this, we want to calculate a pokemon's Body Mass Index (or BMI). This is a statistic calculated using the pokemon's height and weight. 

To help with this task we we will create Pokemon objects that methods can be called on. 

You'll be working with following dictionaries to create the `Pokemon` objects


```python
# Use the following data
bulbasaur_data = {"name": 'bulbasaur', "weight": 69, "height": 7, "base_experience": 64, "types": ["grass", "poison"]}
charmander_data = {"name": 'charmander', "weight": 85, "height": 6, "base_experience": 62, "types": ["fire"]}
squirtle_data = {"name": 'squirtle', "weight": 90, "height": 5, "base_experience": 63, "types": ["water"]}
```

### 1. Creating a Class

Create a class called `Pokemon` with an `__init__` method. Every `Pokemon` instance should have the following attributes:
* `name`
* `weight`
* `height`


```python
# Create your class below with the correct syntax, including an __init__ method.
```

    
### 2. Instantiating Objects

Using the `bulbasaur_data`, `charmander_data` and `squirtle_data` variables, create the corresponding pokemon objects.


```python
# Your code here
bulbasaur = pass
charmander = pass
squirtle = pass
```


```python
# run this cell to test and check your code
# you may need to edit the attribute variable names if you named them differently!

def print_pokeinfo(pkmn):
    print('Name: ' + pkmn.name)
    print('Weight: ' + str(pkmn.weight))
    print('Height: ' + str(pkmn.height))
    print('\n')
    
print_pokeinfo(bulbasaur)
print_pokeinfo(ivysaur)
print_pokeinfo(venusaur)
```

### 3. Instance Methods

Write an instance method called `bmi` within the class `Pokemon` defined above to calculate the BMI of a Pokemon. 

BMI is defined by the formula: $\frac{weight}{height^{2}}$ 

The BMI should be calculated with weight in **kilograms** and height in **meters**. 


The height and weight data of Pokemon from the API is in **decimeters** and **hectograms** respectively. Here are the conversions:

```
1 decimeter = 0.1 meters
1 hectogram = 0.1 kilograms
```


```python
# run this cell to test and check your code

# After defining a new instance method on the class, 
# you will have to rerun the code instantiating your objects

print(bulbasaur.bmi()) # 14.08
print(charmander.bmi()) # 23.61
print(squirtle.bmi()) # 36.0
```

## Part 3: SQL and Relational Databases [Suggested Time: 30 minutes]

For this section, we've put the Pokemon data into SQL tables. You won't need to use your list of dictionaries or the JSON file for this section. The schema of `pokemon.db` is as follows:

<img src="data/pokemon_db.png" alt="db schema" style="width:500px;"/>

Assign your SQL queries as strings to the variables `q1`, `q2`, etc. and run the cells at the end of this section to print your results as Pandas DataFrames.

- q1: Find all the pokemon on the "pokemon" table. Display all columns.  

  
- q2: Find all the rows from the "pokemon_types" table where the type_id is 3.


- q3: Find all the rows from the "pokemon_types" table where the associated type is "water". Do so without hard-coding the id of the "water" type, using only the name.


- q4: Find the names of all pokemon that have the "psychic" type.


- q5: Find the average weight for each type. Order the results from highest weight to lowest weight. Display the type name next to the average weight.


- q6: Find the names and ids of all the pokemon that have more than 1 type.


- q7: Find the id of the type that has the most pokemon. Display type_id next to the number of pokemon having that type. 


**Important note on syntax**: use `double quotes ""` when quoting strings **within** your query and wrap the entire query in `single quotes ''`.


```python
cnx = sqlite3.connect('data/pokemon.db')
```


```python
# q1: Find all the pokemon on the "pokemon" table. Display all columns. 
q1 = ''
pd.read_sql(q1, cnx)
```


```python
# q2: Find all the rows from the "pokemon_types" table where the type_id is 3.
q2 = ''
pd.read_sql(q2, cnx)
```


```python
# q3: Find all the rows from the "pokemon_types" table where the associated type is "water". Do so without hard-coding the id of the "water" type, using only the name.
q3 = ''
pd.read_sql(q3, cnx)
```


```python
# q4: Find the names of all pokemon that have the "psychic" type.
q4 = ''
# pd.read_sql(q4, cnx)
```


```python
# q5: Find the average weight for each type. Order the results from highest weight to lowest weight. Display the type name next to the average weight.
q5 = ''
pd.read_sql(q5, cnx)
```


```python
# q6: Find the names and ids of all the pokemon that have more than 1 type. 
q6 = ''
pd.read_sql(q6, cnx)
```


```python
# q7: Find the id of the type that has the most pokemon. Display type_id next to the number of pokemon having that type. 
q7 = ''
pd.read_sql(q7, cnx)
```


## Section 4: Web Scraping

### Accessing Data Using BeautifulSoup

Use BeautifulSoup to get quotes, authors, and tags from [Quotes to Read](http://quotes.toscrape.com/).

Before answering these questions, go to the site and inspect the page. Make sure to look at what links there are and how the site is structured.

1. Get the first author and the path for the author's page as a tuple from the [homepage](http://quotes.toscrape.com/).


```python
# Make a get request to retrieve the page
html_page = requests.get('http://quotes.toscrape.com/') 
# Pass the page contents to beautiful soup for parsing
soup = BeautifulSoup(html_page.content, 'html.parser')

# Your code here

```

2. Write a function to get **all** the authors and href links for the authors from the [homepage](http://quotes.toscrape.com/)



```python
def authors(url):
    '''
    input: url
    
    return: a dictionary of of authors and their urls
            {'author_1':'url_of_author_1', 'author_2':'url_of_author_2' ...}
    '''
    pass
```


```python
# run this cell to test the function
print(authors('http://quotes.toscrape.com/'))
print('\n')
print(authors('http://quotes.toscrape.com/page/3'))
```
