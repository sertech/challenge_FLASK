from flask import Flask, render_template, url_for, request
from flask import redirect, flash, jsonify, flash
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

'''Bind the engine to the metadata of the Base class so that the declaratives can be accessed through a DBSession instance'''

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
''' A DBSession() instance establishes all conversations with the database and represents a "staging zone" for all the objects loaded into the database session object. Any change made against the objects in the session won't be persisted into the database until you call session.commit(). If you're not happy about the changes, you can revert all of them back to the last commit by calling session.rollback()'''
session = DBSession()


@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    print("this is the GET response from def showRestaurants():")
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', app_restaurants=restaurants)


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        print("This is using a POST message from def newRestaurant():")
        newRestaurant = Restaurant(name=request.form['r_name'])
        session.add(newRestaurant)
        session.commit()
        flash("new restaurant created")
        return redirect(url_for('showRestaurants'))
    else:
        print("this is the GET message from def newRestaurant():")
        return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    edit_rest = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        print("This is using a POST message from def editRestaurant(restaurant_id):")
        if request.form['r_name'] != '':
            edit_rest.name = request.form['r_name']
            session.add(edit_rest)
            session.commit()
            flash("Restaurant edited")
            return redirect(url_for('showRestaurants'))
    else:
        print("This is using a GET message from def editRestaurant(restaurant_id):")
        return render_template('editRestaurant.html', app_restaurant_id=restaurant_id, app_edit_rest=edit_rest)


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    delete_rest = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        print("this is POST message from def deleteRestaurant(restaurant_id):")
        print("the following record will be deleted")
        print(delete_rest.id)
        print(delete_rest.name)
        session.delete(delete_rest)
        session.commit()
        flash("Restaurant Deleted")
        return redirect(url_for('showRestaurants'))
    else:
        print("this is the GET Method of def deleteRestaurant(restaurant_id):")
        return render_template('deleteRestaurant.html', app_restaurant_id=restaurant_id, app_del_rest=delete_rest)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    print("this have only a get message does not process anything")
    selected_rest = session.query(Restaurant).filter_by(id=restaurant_id).one()
    # the first restaurant_id is from the table and the file database_setup.py
    rest_menu = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', app_selected_rest=selected_rest, app_rest_menu=rest_menu)


@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        print("this is the POST message from def newMenuItem(restaurant_id):")
        app_new_menuItem = MenuItem(name=request.form['menu_item_name'], description=request.form['menu_item_description'], price=request.form['menu_item_price'], course=request.form['course'], restaurant_id=restaurant_id)
        session.add(app_new_menuItem)
        session.commit()
        flash("New menu item created")
        return redirect(url_for('showMenu',restaurant_id=restaurant_id))
    else:
        print("this is the GET Method of def newMenuItem(restaurant_id):")
        return render_template('newMenuItem.html', app_restaurant_id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    edit_menu_item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        print("this is the post call of def editMenuItem(restaurant_id, menu_id):")
        edited_menu_item = MenuItem(name=request.form['new_item_name'], description=request.form['new_item_description'], price=request.form['new_item_price'], course=request.form['new_course'], restaurant_id=restaurant_id)
        session.add(edited_menu_item)
        session.commit()
        flash("menu item edited")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        print("this is the GET Method of def editMenuItem(restaurant_id, menu_id):")
        return render_template('editMenuItem.html', app_restaurant_id=restaurant_id, app_selected_menu=edit_menu_item)



@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    selected_rest = session.query(Restaurant).filter_by(id=restaurant_id).one()
    delete_menu_item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        print("this is the POST response from def deleteMenuItem(restaurant_id, menu_id):")
        print("the following menu item record will be deleted")
        print(delete_menu_item.id)
        print(delete_menu_item.name)
        print(delete_menu_item.description)
        print(delete_menu_item.price)
        print(delete_menu_item.course)
        print(delete_menu_item.restaurant_id)
        session.delete(delete_menu_item)
        session.commit()
        flash("menu item deleted")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        print("this is the GET Method of def deleteMenuItem(restaurant_id, menu_id):")
        return render_template('deleteMenuItem.html', app_del_menu_item=delete_menu_item, app_selected_rest=selected_rest)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
