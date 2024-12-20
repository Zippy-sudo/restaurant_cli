# lib/helpers.py
from models.restaurant import Restaurant
from models.shift import Shift
from models.worker import Worker

def exit_program():
    print("\nGoodbye!")
    exit()


#RESTAURANTS
def create_restaurant():
    name = input("\nEnter the restaurant name: ")
    location = input("Enter the restaurant location: ")
    try:
        new_restaurant = Restaurant.create(name, location)
        print(f"\nSuccess: {new_restaurant.name} added")
    except Exception as exc:
        print("\nError adding restaurant : ", exc)

def update_restaurant(choice):
    if choice == "1":
        name = input("\nEnter the restaurant's name: ")
        if Restaurant.find_by_name(name):
            try:
                restaurants = Restaurant.find_by_name(name)
                if len(restaurants) > 1:
                    counter = 1
                    modded_restaurants = {}
                    for restaurant in restaurants:
                        modded_restaurants.update({str(counter) : restaurant})
                        print(f"{counter}: {restaurant}")
                        counter += 1
                    print("Please choose a restaurant: ")
                    restaurant_to_update = input("\n> ")
                    if len(restaurants) < int(restaurant_to_update) <= 0:
                        print("Invalid Choice")
                    else:
                        restaurant = modded_restaurants.get(restaurant_to_update)
                        name = input("Enter the restaurant's new name: ")
                        restaurant.name = name
                        location = input("Enter the restaurant's new location: ")
                        restaurant.location = location

                        restaurant.update()
                        print(f'\nSuccess: {restaurant.name} updated')
                else:
                    restaurant = restaurants[0]
                    name = input("Enter the restaurant's new name: ")
                    restaurant.name = name
                    location = input("Enter the restaurant's new location: ")
                    restaurant.location = location

                    restaurant.update()
                    print(f'\nSuccess: {restaurant.name} updated')
            except Exception as exc:
                print("Error updating restaurant: ", exc)
        else:
                   print(f'\nRestaurant {name} not found')
    else:
        id_ = input("\nEnter the restaurant's id: ")
        if Restaurant.find_by_id(id_):
            try:
                restaurant = Restaurant.find_by_id(id_)
                name = input("Enter the restaurant's new name: ")
                restaurant.name = name
                location = input("Enter the restaurant's new location: ")
                restaurant.location = location

                restaurant.update()
                print(f'\n{restaurant.name} updated')
            except Exception as exc:
                print("Error updating restaurant: ", exc)
        else:
            print(f'\nRestaurant {id_} not found')

def delete_restaurant(choice):
    if choice == "1":
        name = input("\nEnter the restaurant's name ")
        if Restaurant.find_by_name(name):
            try:
                restaurants = Restaurant.find_by_name(name)
                if len(restaurants) > 1:
                    counter = 1
                    modded_restaurants = {}
                    for restaurant in restaurants:
                        modded_restaurants.update({str(counter) : restaurant})
                        print(f"{counter}: {restaurant}")
                        counter += 1
                    print("\nPlease choose a restaurant: ")
                    restaurant_to_delete = input("\n> ")
                    if str(len(restaurants)) < restaurant_to_delete <= str(0):
                        print("Invalid Choice")
                    else:
                        restaurant = modded_restaurants.get(restaurant_to_delete)
                        restaurant.delete()
                        print(f'\nSuccess: {restaurant.name} deleted')
                else:
                    restaurant = restaurants[0]
                    restaurant.delete()
                    print(f'\nSuccess: {restaurant.name} deleted')
            except Exception as exc:
                print("Error deleting restaurant: ", exc)
        else:
                   print(f'\nRestaurant {name} not found')
    else:
        id_ = input("\nEnter the restaurant's id: ")
        if Restaurant.find_by_id(id_):
            try:
                restaurant = Restaurant.find_by_id(id_)
                restaurant.delete()
                print(f'\n{restaurant.name} deleted')
            except Exception as exc:
                print("Error deleting restaurant: ", exc)
        else:
            print(f'\nRestaurant {id_} not found')

def find_restaurant_by_id():
    id_ = input("Enter the restaurant's Id: ")
    restaurant = Restaurant.find_by_id(id_)
    return print(f"Restaurant : {restaurant}") if restaurant else print(f"Restaurant {id_} not found")

def list_restaurants():
    print("\n")
    restaurants = Restaurant.get_all()
    if restaurants:
        for restaurant in restaurants:
            print(f"{restaurant}\n")
    else:
        print("\nNo restaurants found")


#SHIFTS
def create_shift():
    time_in = input("Enter the shift's starting time (e.g 900): ")
    time_out = input("Enter the shift's closing time (e.g 1700): ")
    restaurant_id = input("Enter the shifts restaurant's id: ")
    if 1 <= len(time_in) <= 4 and 1 <= len(time_out) <= 4:
        if Restaurant.find_by_id(restaurant_id):
            try:
                new_shift = Shift.create(time_in, time_out, restaurant_id)
                print(f"\nSuccess: Shift {new_shift.id_} added")
            except Exception as exc:
                print("\nError adding shift : ", exc) 
        else:
            print("\nCreation failed. Please enter valid restaurant Id")
    else:
        print("\nCreation failed. Please enter valid 24HR time.")

def update_shift():
    id_ = input("Enter the Shift's id: ")
    if Shift.find_by_id(id_):
        try:
            shift = Shift.find_by_id(id_)
            time_in = input("Enter shift's new time in: ")
            shift.time_in = time_in
            time_out = input("Enter shift's new time out: ")
            shift.time_out = time_out
            restaurant_id = input("Enter the shift's new restaurant id: ")
            if Restaurant.find_by_id(int(restaurant_id)):
                shift.restaurant_id = int(restaurant_id)
                shift.update()
                print (f'\nSuccess: Shift {shift.id_} updated')
            else:
                print("\nUpdate failed. Please enter valid restaurant Id")
        except Exception as exc:
            print("Error updating shift: ", exc)
    else:
        print(f'\nShift {id_} not found')

def delete_shift():
    id_ = input("Enter the shift Id: ")
    shift = Shift.find_by_id(int(id_))
    if shift:
        shift.delete()
        print(f"\nShift {id_} deleted")
    else:
        print(f"\nShift {id_} not found")

def find_shift_by_id():
    id_ = input("Enter the shift's id: ")
    shift = Shift.find_by_id(id_)
    return print(f"Shift {shift.id_} : {shift}") if shift else print(f"Shift {id_} not found")

def list_shifts():
    print("\n")
    shifts = Shift.get_all()
    if shifts:
        for shift in shifts:
            print(f"Shift {shift.id_} : {shift}\n")
    else:
        print("\nNo shifts found")


#WORKERS
def create_worker():
    name = input("Enter worker's name: ")
    role = input("Enter the worker's role: ")
    shift_id = input("Enter the worker's shift id: ")
    restaurant_id = input("Enter the worker's restaurant id: ")
    try:
        if Shift.find_by_id(shift_id):
            if Restaurant.find_by_id(restaurant_id):
                new_worker = Worker.create(name, role, shift_id, restaurant_id)
                print(f"\nSuccess: Worker {new_worker.name} added")
            else:
                print("\nPlease enter a valid restaurant Id")
        else:
            print("\nPlease enter a valid shift id")
    except Exception as exc:
        print("\nError adding worker : ", exc)

def update_worker(choice):
    if choice == "1":
        name = input("\nEnter the worker's name: ")
        if Worker.find_by_name(name):
            try:
                workers = Worker.find_by_name(name)
                if len(workers) > 1:
                    counter = 1
                    modded_workers = {}
                    for worker in workers:
                        modded_workers.update({str(counter) : worker})
                        print(f"{counter}: {worker}")
                        counter += 1
                        print("Please choose a worker: ")
                        worker_to_update = input("\n> ")
                    if len(workers) < int(worker_to_update) <= 0:
                        print("Invalid Choice")
                    else:
                        worker = modded_workers.get(worker_to_update)
                        name = input("Enter the worker's new name: ")
                        worker.name = name
                        role = input("Enter the worker's new role: ")
                        worker.role = role
                        shift_id = input("Enter worker's new shift id: ")
                        worker.shift_id = shift_id
                        restaurant_id = input("Enter worker's new restaurant id: ")
                        worker.restaurant_id = restaurant_id

                        worker.update()
                        print(f'\nSuccess: {worker.name} updated')
                else:
                    worker = workers[0]
                    name = input("Enter the worker's new name: ")
                    worker.name = name
                    role = input("Enter the worker's new role: ")
                    worker.role = role
                    shift_id = input("Enter worker's new shift id: ")
                    worker.shift_id = shift_id
                    restaurant_id = input("Enter worker's new restaurant id: ")
                    worker.restaurant_id = restaurant_id

                    restaurant.update()
                    print(f'\nSuccess: {worker.name} updated')
            except Exception as exc:
                print("Error updating worker: ", exc)
        else:
                   print(f'\nWorker {name} not found')
    else:
        id_ = input("\nEnter worker's id: ")
        if Worker.find_by_id(id_):
            try:
                worker = Worker.find_by_id(id_)
                name = input("Enter the worker's new name: ")
                worker.name = name
                role = input("Enter the worker's new role: ")
                worker.role = role
                shift_id = input("Enter worker's new shift id: ")
                worker.shift_id = shift_id
                restaurant_id = input("Enter worker's new restaurant id: ")
                worker.restaurant_id = restaurant_id

                worker.update()
                print(f'\n{worker.name} updated')
            except Exception as exc:
                print("Error updating worker: ", exc)
        else:
            print(f'\nWorker {id_} not found')

def delete_worker():
    id_ = input("Enter the worker's Id: ")
    worker = Worker.find_by_id(int(id_))
    if worker:
        worker.delete()
        print(f"\nWorker {worker.id_} deleted")
    else:
        print(f"\nWorker {id_} not found")

def find_worker_by_id():
    id_ = input("Enter the worker's id: ")
    worker = Worker.find_by_id(id_)
    return print(f"{worker.name} : {worker}") if worker else print(f"Worker {id_} not found")

def list_workers():
    print("\n")
    workers = Worker.get_all()
    if workers:
        for worker in workers:
            print(f"{worker}\n")
    else:
        print("\nNo workers found")

#MORE
def shifts_for_restaurant():
    restaurant_id = input("Enter restaurant id: ")
    restaurant = Restaurant.find_by_id(restaurant_id)
    shifts = restaurant.shifts()
    for shift in shifts:
        print(f"\n{shift}")
    return shifts

def workers_for_restaurant():
    restaurant_id = input("Enter restaurant id: ")
    restaurant = Restaurant.find_by_id(restaurant_id)
    workers = restaurant.workers()
    for worker in workers:
        print(f"\n{worker}")
    return workers

def workers_for_shift():
    shift_id = input("Enter shift id: ")
    shift = Shift.find_by_id(shift_id)
    workers = shift.workers()
    for worker in workers:
        print(f"\n{worker}")
    return workers

def shifts_for_worker():
    worker_id = input("Enter worker id: ")
    worker = Worker.find_by_id(worker_id)
    shifts = worker.shifts()
    for shift in shifts:
        print(f"\n{shift}")
    return shifts
