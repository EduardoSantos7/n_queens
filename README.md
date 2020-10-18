# N queens
-----------------

[![Build Status](https://api.travis-ci.org/EduardoSantos7/n_queens.svg?branch=main)](https://travis-ci.org/EduardoSantos7/n_queens)

N queens is an app that gets each possible solution of the famous N queens problem for a given N. This app is built-in `Python 3` and uses `SQLAlchemy` and `Postgres` to save each solution in a table named `solutions`. `Pytest` is used to verify that the core function is still working after each commit and `Travis CI` is used to automate the tests. 

# Features!
-----------------

  - Find all the possible boards for a given `N` and return the number of boards
  - Save each board in `Postgres` for future searches
  - Data persist
  - Dockerized 
  - Tests

### Tech
-----------------

N queens uses a number of open source projects to work properly:

* [Python 3] - algorithms, DB connection and tests!
* [SQLAlchemy] - ORM
* [Postgres] - relational database.
* [Pytest] - framework for test
* [Travis CI] - automate tests
* [Docker] - containers

The algorithm used can be found in this [video], but this solution only give the number of the solutions, so extra modifications were needed to save the boards.

The table in the database has 3 columns (`id`, `queens (the N)` and `bt_solution (the board)`) and looks like this:

![Alt text](solutions_table.png?raw=true "Solution table example")

### Installation
-----------------

1) Clone the repository (`.env` and `database.env` files are exposed for demonstration purposes, that said, this doesn't represent security leaks)

2) Build the containers

    ```sh
    $ docker-compose up
    ```
    After this step you should see a message from the DB container like this: `database system is ready to accept connections`
3) In other terminal run: 
    ```sh
    $ docker exec -it n_queens_n_queens_1 bash
    ```
4) Now you can run test using the next command:

    ```python
    pytest test_queen_algorithms.py
    ```
    
    ![Alt text](test_results.png?raw=true "After run the test")
    
5) You can get the solutions for a given N running the next command:

    ```python
    python main.py
    ```
    
    ![Alt text](run_examples.png?raw=true "After get the solutions for some Ns")


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [Python 3]: <https://www.python.org/>
   [SQLAlchemy]: <https://www.sqlalchemy.org/>
   [Postgres]: <https://www.postgresql.org/>
   [Pytest]: <https://pytest.org/>
   [Travis CI]: <https://travis-ci.org/>
   [Docker]: <https://www.docker.com/>
   [video]: <https://www.youtube.com/watch?v=u6viVC1fJ9g&t=1134s>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
