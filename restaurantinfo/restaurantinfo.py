from random import choice
from flask import Flask, request, redirect, url_for, abort, \
    render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key'
))
app.config.from_envvar('RESTAURANTINFO_SETTINGS', silent=True)

from restaurantinfo import restaurantdata


@app.route('/')
def welcome():
    if len(restaurantdata.restaurants) == 0:
        return "Hello! There are no restaurants configured for this network. Please check back later."
    else:
        restaurants = []
        for restaurant in restaurantdata.restaurants:
            restaurants.append(restaurant)
        return render_template('list.html', restaurants=restaurants)
 

@app.route('/<restaurant_name>')
def view_restaurant_info(restaurant_name):
    if restaurant_name in restaurantdata.restaurants:
        return render_template('info.html',
                                restaurant_name=restaurant_name,
                                restaurant_info=restaurantdata.restaurants[restaurant_name]
        )
    else:
        return "That restaurant was not found in our network. Please try again."
