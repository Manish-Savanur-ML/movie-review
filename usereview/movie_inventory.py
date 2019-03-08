"""
This module will contain movies information
"""
from models import Movies
from models import Usereview
import copy
import logging
LOGGER = logging.getLogger(__name__)
def add_movie(name):
    """
    This will add movie name to DB
    """
    try:
        movie_obj = Movies.objects.get(movie_name=name.lower())
        msg = "Movie "+name+" already added"
        return 403, {"sucess": msg}
    except BaseException as err:
        LOGGER.error("Movie details not found for "+name.lower()+" creating new entry")
        LOGGER.error(str(err))
    movie_obj = Movies()
    movie_obj.movie_name = name.lower()
    movie_obj.save()
    msg = "Movie "+name+" added successfully"
    return 201, {"sucess": msg}

def add_review(movie, rate, comment, found=False):
    """
    This method will add review
    """
    if found == True:
        review_obj = Usereview.objects.get(name=movie.lower())
        rate_list = review_obj.rating
        rate_list.append(rate)
        review_obj.rating = copy.copy(rate_list)
        review_obj.save()
        if comment != "":
            comment_list = review_obj.comments
            comment_list.append(comment)
            review_obj.comments = copy.copy(comment_list)
            review_obj.save()
    else:
        review_obj = Usereview()
        review_obj.name = movie.lower()
        rate_list = review_obj.rating
        rate_list.append(rate)
        review_obj.rating = copy.copy(rate_list)
        review_obj.save()
        if comment != "":
            comment_list = review_obj.comments
            comment_list.append(comment)
            review_obj.comments = copy.copy(comment_list)
            review_obj.save()

def add_user_review(movie_name, rate, comment):
    """
    This will add review
    """
    try:
        rate = int(rate)
    except BaseException as err:
        LOGGER.error("Rating should be integer value")
        LOGGER.error(str(err))
        return 400, {"error":"Rating should be integer value"}
    try:
        if rate not in range(1, 6):
            LOGGER.error("Rating should be integer value")
            return 400, {"error":"Rating should be in range 1 to 5"}
        review_obj = Usereview.objects.get(name=movie_name.lower())
        add_review(movie_name, rate, comment, found=True)
        return 201, {"sucess":"Movie review added"}
    except BaseException as err:
        LOGGER.error("Movie Review not added for "+movie_name.lower()+" adding new entry")
        LOGGER.error(str(err))
        add_review(movie_name, rate, comment)
        return 201, {"success": "Movie review added"}

def movie_info(movie_name):
    """
    This method will return movie dict
    """
    try:
        movie_dict = dict()
        review_obj = Usereview.objects.get(name=movie_name.lower())
        total_rate = review_obj.rating
        total_comments = review_obj.comments
        average_rating = sum(total_rate)//len(total_rate)
        movie_dict["name"] = movie_name
        movie_dict["total_review"] = len(total_rate)
        movie_dict["total_comments"] = len(total_comments)
        movie_dict["average_rating"] = average_rating
        movie_dict["list_of_comments"] = total_comments
        return 200, movie_dict
    except BaseException as err:
        LOGGER.error("Erro while fetching movie info "+movie_name.lower())
        LOGGER.error(str(err))
        return 400, {"error":"Erro while fetching movie info"}
