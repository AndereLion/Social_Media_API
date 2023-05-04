# Social Media API

This project aims to build a REST API for a social 
media platform using Django and Django REST framework. 
The API should allow users to create profiles, 
follow other users, create and retrieve posts, 
manage likes and comments, 
and perform basic social media actions.

## Features

### User Registration and Authentication:

Users can register with their email and password to create an account.
Users can log in with their credentials and receive a token for authentication.
Users can log out and invalidate their token.
### User Profile:
Users can create and update their profile, including profile picture, bio, and other details.
Users can retrieve their own profile and view profiles of other users.
Users can search for users by username or other criteria.
### Follow/Unfollow:
Users can follow and unfollow other users.
Users can view the list of users they are following and the list of users following them.
### Post Creation and Retrieval:
Users can create new posts with text content and optional media attachments (e.g., images).
Users can retrieve their own posts and posts of users they are following.
Users can retrieve posts by hashtags or other criteria.

## Installation
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver