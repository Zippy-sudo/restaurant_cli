# RESTAURANT CLI

A simple CLI that allows the user to access and manipulate table data in a database. It is built using python and sqlite3.

By Nehemiah Madahana.

## Description

This simple Restaurant CLI app built using python enables users to access and modify data in a table. It also allows them to sort through the tables and data in order to present a clearer picture of the data.

## Features

- A CLI menu to enable users to access the data and modify it.

- Persistence of data through a database.

## How to Use

### Requirements

- A computer.
- [Python](https://wiki.python.org/moin/BeginnersGuide/Download) version 3.18.3 or higher.
- The [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#linuxunix) package manager

#### Check if You Have Python

Run:

```bash
python --version
```

You should see this if python is installed:

![python_installed](/assets/python_installed.png)

If not consult [this page](https://wiki.python.org/moin/BeginnersGuide/Download) on how to install python.

#### Check if You Have Pyenv

Run

```bash
pyenv versions
```

You should see this if pyenv is installed:

![pyenv_installed](/assets/pyenv_installed.png)

If not follow the instructions [this page](https://github.com/pyenv/pyenv?tab=readme-ov-file#linuxunix) to download pyenv.

### Installation Process

1. Clone this repository by typing the following command into your terminal:

```bash
git clone git@github.com:Zippy-sudo/restaurant_cli.git
```

or by downloading a ZIP file of the code.

2. Navigate to the project directory:

```bash
cd /path-to/dir/restaurant-cli
```

Be sure to replace */path-to/dir* with the path to the directory into which you downloaded this repository.

3. Install the required dependencies

```bash
pipenv Install
```

4. Enter the virtual environment

```bash
pipenv shell
```

5. Run the cli.py file by typing the following command into your terminal:

```bash
./lib/cli.py
```

## Usage

The terminal should display a menu:

![menu](/assets/menu.png)

### Options

#### Table Managers

The methods in this section are also applicable to Shift Manager (Option 2 on the main menu) and Worker Manager (Option 3 on the main menu).

1. To exit type "0" and press Enter:

![exit](/assets/exit.png)

This will exit the CLI and you'll have to re-do step 5 of the installation Process.

2. To add a new row to Restaurant:

- First type "1" into the terminal. This takes you to the Restaurant Manager.Each model has its own manager and the menu is similar to this one:

![restaurant_manager](/assets/restaurant_manager.png)

- From here you can add, update or delete a row from the database table associated with the manager, in this case the table is restaurants. You can also return to the main menu from this point by typing "0", but we are currently interested in adding a new Restaurant to the table, therefore we type "1":

![add_restaurant_1](/assets/add_restaurant_1.png)

- This causes the program to prompt us for more information about the Restaurant we are trying to add:

![add_restaurant_1](/assets/add_restaurant_1.png)

- Fill in the information  required  and you will get a success message:

![add_restaurant_2](/assets/add_restaurant_2.png)

- To check if the data has been persisted. Type "4" into the terminal:

![success_restaurant](/assets/success_restaurant.png)

3. Now let's update this restaurant.

- Enter the Restaurant Manager by typing "1", then type "2" to enter the update menu:

![update_menu](/assets/update_menu.png)

- There are two ways to update a database entry for every Manager: by name and by id. Since we can easily remember a name as opposed to remembering an id, let's use the restaurant's name:

![update_restaurant_1](/assets/update_restaurant_1.png)

- Fill in the required details then press Enter:

![update_restaurant_2](/assets/update_restaurant_2.png)

- To confirm the data has been persisted we again type "4" then hit Enter.

![update_restaurant_3](/assets/update_restaurant_3.png)

4. Let's delete the restaurant.

- Enter the restaurant manager by first typing "1", then enter the delete menu by typing "2" and hitting Enter.

![delete_restaurant_1](/assets/delete_restaurant_1.png)

- Here we again have an option to delete either by name or id. Now that we know the restaurant's id, let's try that path. Choose the second option by typing "2" and hitting enter, then input the restaurant's id which is "1".

![delete_restaurant_2](/assets/delete_restaurant_2.png)

- We get a confirmation message, but just to be sure, let's list all restaurants (Option 4 on the main menu)

![delete_restaurant_3](/assets/delete_restaurant_3.png)

- Woohoo! There are no restaurants in the table. It worked!

#### Find by Id

What if you knew a restaurant's Id and wanted to find more about it? Look no further than the Find by Id option.

- Find restaurant by Id (Option 5 on the main menu) lets you find  a restaurant by its Id.

- Find shift by Id (Option 7 on the main menu) lets you find a shift by its Id.

- Find worker by Id (Option 9 on the main menu) lets you find a worker by their Id.

Create a restaurant using the instructions from the segment on Table Managers above, then from the main menu:

1. Enter "5" into the input field.

![find_res_by_id_1](/assets/find_res_by_id_1.png)

2. Input the id of the restaurant in this case "1":

![find_res_by_id_2](/assets/find_res_by_id_2.png)

and Voilà!

#### More

You're probaly wondering about the More option(*). Well, let's find out what it does.

![more_1](/assets/more_1.png)

The More option enables us to extract relationship data from the tables

The queries are generally structured in this way: Get *many* for *one*.

- Get shifts for restaurant (Option 1), can be said as "Get *all* the shifts associated with the **restaurant Id** that I pass in.

- Get workers for restaurant (Option 2), can be said as "Get *all* the workers associated with the **restaurant Id** that I pass in.

- Get workers for shift (Option 3), can be said as "Get *all* the workers associated with the **shift Id** that I pass in.

- Get shifts for worker (Option 4), can be said as "Get *all* the shifts associated with the **worker Id** that I pass in.

Lets see it in action, We'll use Option 1 (Get shifts for restaurant).

1. We navigate to the More Menu by typing "*" into the terminal.

![more_1](/assets/more_1.png)

2. We select the First Option (Get shifts for restaurant) by typing in "1" then hitting Enter.

![more_2](/assets/more_2.png)

3. We enter the restaurant Id, in this case "1" and get the result. (I'd added a new restaurant and some shifts to help demonstarate the query behaviour more clearly)

![more_3](/assets/more_3.png)

The list of all shifts by comparison:

![more_4](/assets/more_4.png)

## Technologies Used

- python3
- pyenv
- sqlite3

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

- Email: <nehemiah.madahana@student.moringaschool.com>

## License

MIT License

Copyright &copy; 2024 Nehemiah Madahana

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
