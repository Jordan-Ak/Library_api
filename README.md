# Library_api
This is a library loaning api made using the django rest framework.
This is the first project I am doing entirely on my own using all the knowledge I have learned about django rest framework so far.
This api is to allow users to borrow books from the library and return before the due date.
The library stores all the books it contains in its database, which can be filtered by Author, Genre, Publisher.
It also keeps a record of the Total quantity of each book, how many books have be loaned out and the available quantity that can be loaned.
It has constraints such as not allowing users to borrow more than a certain number of books per time, not allowing users to borrow multiple numbers of the same book, and also only loaning books out that are still available.



Database: Postgresql
Access Control: Third-party packages used, "dj-rest-auth", "allauth",'django-rest-password-reset'

