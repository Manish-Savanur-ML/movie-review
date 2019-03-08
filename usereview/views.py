"""
This module return response for movie review
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from movie_inventory import add_movie, add_user_review, movie_info
class AddMovie(APIView):
    """
    This class will add new movie
    """
    def post(self, request):
        """
        This class will add movie
        """
        movie_data = request.data
        name = movie_data["name"]
        code, msg = add_movie(name)
        if code == 403:
            return Response(msg, status=403)
        return Response(msg, status=201)

class AddReview(APIView):
    """
    This class will add movie review
    """
    def post(self, request):
        """
        This method will add movie review
        """
        review_data = request.data
        name = review_data["name"]
        rate = review_data["rate"]
        comment = review_data["comment"]
        code, msg = add_user_review(name, rate, comment)
        if code == 400:
            return Response(msg, status=400)
        return Response(msg, status=201)

class MovieInfo(APIView):
    """
    This class will get movie info
    """
    def get(self, request):
        """
        This mehtod will get movie info
        """
        movie_name = request.GET.get("movie_name")
        code, info_dict = movie_info(movie_name)
        if code == 400:
            return Response(info_dict, status=400)
        return Response(info_dict)
