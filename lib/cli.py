#!/usr/bin/env python
# lib/cli.py

from helpers import (
    exit_program,
    create_restaurant,
    update_restaurant,
    delete_restaurant,
    list_restaurants,
    find_restaurant_by_id,
    create_shift,
    update_shift,
    delete_shift,
    list_shifts,
    find_shift_by_id,
    create_worker,
    update_worker,
    delete_worker,
    list_workers,
    find_worker_by_id,
    shifts_for_restaurant,
    workers_for_restaurant,
    workers_for_shift,
    shifts_for_worker
)


def main():
    while True:
        menu()
        choice = input("\n> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            while True:
                restaurant_manager()
                restaurant_choice = input("\n> ")
                if restaurant_choice == "0":
                    break
                if restaurant_choice == "1":
                    create_restaurant()
                    break
                elif restaurant_choice == "2":
                    print("\nPlease select a way to update ")
                    print("1. Update by name")
                    print("2. Update by Id")
                    restaurant_update_choice = input("\n> ")
                    if restaurant_update_choice == "1":
                        update_restaurant(restaurant_update_choice)
                        break
                    elif restaurant_update_choice == "2":
                        update_restaurant(restaurant_update_choice)
                        break
                    else:
                        print("\nInvalid choice")
                elif restaurant_choice == "3":
                    print("\nPlease select a way to delete ")
                    print("1. Delete by name")
                    print("2. Delete by Id")
                    restaurant_delete_choice = input("\n> ")
                    if restaurant_delete_choice == "1":
                        delete_restaurant(restaurant_delete_choice)
                        break
                    elif restaurant_delete_choice == "2":
                        delete_restaurant(restaurant_delete_choice)
                        break
                    else:
                        print("\nInvalid choice")
                    break
                else:
                    print("Invalid choice")   
        elif choice == "2":
            while True:
                shift_manager()
                shift_choice = input("\n> ")
                if shift_choice == "0":
                    break
                if shift_choice == "1":
                    create_shift()
                    break
                elif shift_choice == "2":
                    update_shift()
                    break
                elif shift_choice == "3":
                    delete_shift()
                    break
                else:
                    print("Invalid choice")
        elif choice == "3":
            while True:
                worker_manager()
                worker_choice = input("\n> ")
                if worker_choice == "0":
                    break
                if worker_choice == "1":
                    create_worker()
                    break
                elif worker_choice == "2":
                    print("\nPlease select a way to update ")
                    print("1. Update by name")
                    print("2. Update by Id")
                    worker_update_choice = input("\n> ")
                    if worker_update_choice == "1":
                        update_worker(worker_update_choice)
                        break
                    elif worker_update_choice == "2":
                        update_worker(worker_update_choice)
                        break
                    else:
                        print("\nInvalid choice")
                    break
                elif worker_choice == "3":
                    delete_worker()
                    break
                else:
                    print("Invalid choice")
        elif choice == "4":
            list_restaurants()
        elif choice == "5":
            find_restaurant_by_id()
        elif choice == "6":
            list_shifts()
        elif choice == "7":
            find_shift_by_id()
        elif choice == "8":
            list_workers()
        elif choice == "9":
            find_worker_by_id()
        elif choice == "*":
            while True:
                more()
                more_choices = input("\n> ")
                if more_choices == "0":
                    break
                elif more_choices == "1":
                    shifts_for_restaurant()
                    break
                elif more_choices == "2":
                    workers_for_restaurant()
                    break
                elif more_choices == "3":
                    workers_for_shift()
                    break
                elif more_choices == "4":
                    shifts_for_worker()
                    break
                else:
                    print("Invalid choice")
        else:
            print("Invalid choice")


def menu():
    print("\nWELCOME TO RESTAURANT CLI")
    print("========================================================")
    print("Please select an option:\n")
    print("0. Exit the program")
    print("1. Go to Restaurant Manager")
    print("2. Go to Shift Manager")
    print("3. Go to Worker Manager")
    print("4. List all restaurants")
    print("5. Find restaurant by Id")
    print("6. List all shifts")
    print("7. Find shift by Id")
    print("8. List all workers")
    print("9. Find workers by Id")
    print("*. More")

def restaurant_manager():
    print("\n Restaurant Manager\n____________________\n")
    print("0: Exit Restaurant Manager")
    print("1. Add a restaurant")
    print("2. Update a restaurant")
    print("3. Delete a restaurant")

def shift_manager():
    print("\n Shift Manager\n____________________\n")
    print("0: Exit Shift Manager")
    print("1. Add a shift")
    print("2. Update a shift")
    print("3. Delete a shift")

def worker_manager():
    print("\n Worker Manager\n____________________\n")
    print("0: Exit Worker Manager")
    print("1. Add a worker")
    print("2. Update a worker")
    print("3. Delete a worker")

def more():
    print("\n More\n____________________\n")
    print("0. Back")
    print("1. Get shifts for restaurant")
    print("2. Get workers for restaurant")
    print("3. Get workers for shift")
    print("4. Get shifts for worker")

if __name__ == "__main__":
    main()
