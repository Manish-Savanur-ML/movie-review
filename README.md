# movie-review
DataGlen Assigment:- Movie Review System
Django Project = movies
Django App = usereview
DB Name = Movies.db
Log file = movie_review.log

It allows user to perform following operations:-
1. Add Movie:-
    a. API:- http://127.0.0.1:9001/movie/add
    b. Method:- POST
    c. Request Body:- 
         {
	"name":"<movie name>"
         }


2. Add Reviews & comment:-
     a. API:- http://127.0.0.1:9001/movie/review
     b. Method:- POST
     c. Request Body:- 
         {
	"name":"Robot 2.0",
	"rate":"4",
	"comment":"<comments>/ Empty"
        }

3. Get Movie Info. This will provide total number of reviews, total number of comments, average rating, list of comments:-
    a. API:- http://127.0.0.1:9001/movie/info?movie_name=""   // Query parameter will be movie name.
    b. Method:- GET
    c. backend Response:-
          {
            "total_review": 2,
            "list_of_comments": [
                "Awsome Movie. Ranveer singh best performance"
              ],
           "name": "Gully boy",
           "average_rating": 5,
           "total_comments": 1
         }        
