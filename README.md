
## Nashville Sell and Trade API

Nashville Sell and Trade is an app where users in Nashville can post what they want to sell or trade.It can be from items you no longer need to produce from a garden that you want to sell. 







    
## Tech Stack

**Client:** JavaScript, React, React-Bootstrap

**Server:** Django, Python


## Run Locally

Clone the project

```bash
  git clone git@github.com:bdleon/nashville-sell-and-trade.git
```

Go to the project directory

```bash
  cd nashville-sell-and-trade
```

Install dependencies

```bash
  `pipenv shell`
```
```bash
  `pipenv install`
```
```bash
  python3 manage.py makemigrations nashville_sell_and_trade_api
```
```bash
  python3 manage.py migrate
```
```bash
  #this is seeding the database

  python3 manage.py loaddata {table name}  
```

Loaddata table names

```bash
  1.users
  2.tokens
  3.nash_users
  4.categories
  5.products
  6.save_posts
  
```

Start the server

```bash
  python3 manage.py runserver
```


## Documentation

- create a new user and you will be directed the the homepage.
- In the homepage all users posts will be displayed and a button on each post for more details
- The user can filter the post by categores and by key term in search bar
- When the authenticated user click the button a detailed page of the post will render with the ability to message the user who created the post
- As a user in the nav bar you have the ability to sell and create a post in the nav bar (`+product`)
- The authenticated user can see all the products posted by the user in `my products` in nav bar with the ability to edit or delete the post
- The user is able to see any messages regarding the post in `my messages`link in nav bar



## ERD Link

https://dbdiagram.io/d/61a7e9fb8c901501c0dc356f