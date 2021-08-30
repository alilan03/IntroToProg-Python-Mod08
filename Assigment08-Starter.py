# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# ALanger,8.19.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALanger,8.19.2021,Modified code to complete assignment 8
    """
    product_name = ""
    product_price = 0.0

    def __init__(self, name, price):
        """ initializes a new product object

                :param self: the object being created
                :param name: (string) of the product's name
                :param price (float) of the product's price
                """
        self.product_name = name
        self.product_price = price


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ALanger,8.19.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves all data currently in the list to the specified file

                :param file_name: (string) of the specified file to write to
                :param list_of_product_objects: (list) of all objects in the list
                """
        file = open(file_name, "w")
        for item in list_of_product_objects:
            file.write(item.product_name + ":" + item.product_price)
        file.close()

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads all data stored in the file and adds it to the list

                :param file_name: (string) of the specified file to read from
                """
        file = open(file_name, "r")
        for item in file:
            name, price = item.split(":")
            product = Product(name, price)
            lstOfProductObjects.append(product)
        file.close()


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes data to and from the user:

        methods:
            show_menu(): Displays the menu of options to the user

            get_choice(): Gets the user's choice from the menu

            show_current_data(): Displays the current information in the list

            new_product(): Gets information from the user for a new product and adds it to the list

        changelog: (When,Who,What)
            ALanger,8.19.2021,Created Class
        """

    @staticmethod
    def show_menu():
        """ Prints out the menu of options for the user """
        print("\nMenu of Options:")
        print("\t1) Display Current Data")
        print("\t2) Add a Product")
        print("\t3) Save and Exit")

    @staticmethod
    def get_choice():
        """ Asks the user to choose an option from the menu """
        choice = input("Please Choose a Menu Option [1-3]: ")
        return choice

    @staticmethod
    def show_current_data():
        """ Prints out all products currently in the list """
        counter = 1
        for item in lstOfProductObjects:
            print(counter.__str__() + ") " + item.product_name + " is $" + item.product_price)
            counter += 1

    @staticmethod
    def new_product():
        """ Asks the user for information and creates a new product object """
        name = input("Please enter the name of your new product: ")
        price = input("Please enter a price for your new product: $")
        new_product = Product(name, price)
        lstOfProductObjects.append(new_product)
        print(new_product.product_name + " for $" + new_product.product_price + " has been added to the list.")


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
FileProcessor.read_data_from_file(strFileName)
while True:
    IO.show_menu()
    option = IO.get_choice()
    if option == "1":
        if len(lstOfProductObjects) != 0:
            print("Here is the current list of products: ")
            IO.show_current_data()
        else:
            print("*There is currently nothing in the list*")
    elif option == "2":
        print("Creating new product...")
        IO.new_product()
    elif option == "3":
        print("Do you want to save the current data to the file? ")
        save = input("Please enter 'y' or 'n': ")
        if save == 'y':
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print("Save Successful!")
        else:
            print("Save Canceled!")
        input("Press enter to exit the program...")
        break
    else:
        print("Sorry that's not a menu option! Please try again...")
# Main Body of Script  ---------------------------------------------------- #
