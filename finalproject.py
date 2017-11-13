from flask import Flask, render_template, url_for, request
from flask import redirect, flash, jsonify
app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    # return "this page will show all the restaurants"
    return render_template('restaurants.html', app_restaurants=restaurants)


@app.route('/restaurant/new/')
def newRestaurant():
    print("this is the GET response from def newRestaurant():")
    return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    print("this is the GET method def editRestaurant(restaurant_id):")
    app_rest_menu = restaurants[restaurant_id-1]['name']
    print(app_rest_name)
    return render_template('editRestaurant.html', app_restaurant_id=restaurant_id, rest_menu=app_rest_menu)


@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    print("this is the GET Method of def deleteRestaurant(restaurant_id):")
    app_rest_name = restaurants[restaurant_id-1]['name']
    return render_template('deleteRestaurant.html', app_restaurant_id=restaurant_id, rest_name=app_rest_name)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    app_rest_name = restaurants[restaurant_id-1]['name']
    app_items = items
    return render_template('menu.html', app_restaurant_id=restaurant_id, rest_name=app_rest_name, rest_menu=app_items)


@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    print("this is the GET Method of def newMenuItem(restaurant_id):")
    return render_template('newMenuItem.html', app_restaurant_id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    print("this is the GET Method of def editMenuItem(restaurant_id, menu_id):")
    return render_template('editMenuItem.html', app_restaurant_id=restaurant_id, app_menu_id=menu_id, app_items=items)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    print("this is the GET Method of def deleteMenuItem(restaurant_id, menu_id):")
    return render_template('deleteMenuItem.html', app_restaurant_id=restaurant_id, app_menu_id=menu_id, app_items=items)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
