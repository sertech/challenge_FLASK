from flask import Flask, render_template, url_for, request
from flask import redirect, flash, jsonify
app = Flask(__name__)


@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return "this page will show all the restaurants"


@app.route('/restaurant/new/')
def newRestaurant():
    return "this page will be for making a new restaurant"


@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return "this page will be for editing restaurant %s" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return "this page will be for deleting restaurant %s" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    return "this page is for the menu of restaurant %s" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    return "this page is for making a new menu item for restaurant %s" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "this page is for editing menu item %s for restaurant %s" % (restaurant_id, menu_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "this page is for deleting meni item %s from restaurant %s" % (restaurant_id, menu_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
