#Keith-Chimuzinga
#R249079H
#Assignment-3


# Question 1
def classify_number():
    while True:
        user_input = input("Please enter an integer: ")
        try:
            number = int(user_input)
            break  # Exit the loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# --- Demonstration ---
if __name__ == "__main__":
    result1 = classify_number()
    print(f"The number is: {result1}\n")

    result2 = classify_number()
    print(f"The number is: {result2}\n")

    result3 = classify_number()
    print(f"The number is: {result3}\n")






#Question 2
def calculate_average(*args):
    if not args:
        print("Warning: No numbers provided to calculate_average. Returning 0.0.")
        return 0.0

    total = sum(args)
    count = len(args)
    return total / count

# --- Demonstration ---
if __name__ == "__main__":
    # Example usage with different numbers of arguments
    print(f"Average of (1, 2, 3, 4, 5): {calculate_average(1, 2, 3, 4, 5)}")
    print(f"Average of (10, 20): {calculate_average(10, 20)}")
    print(f"Average of (7,): {calculate_average(7)}")
    print(f"Average of (1.5, 2.5, 3.0): {calculate_average(1.5, 2.5, 3.0)}")

    # Example with no arguments
    print(f"Average of (): {calculate_average()}")

    # Example with a list unpacked
    numbers_list = [100, 200, 300]
    print(f"Average of {numbers_list}: {calculate_average(*numbers_list)}")







#Question 3
def get_valid_number():
    while True:
        user_input = input("Please enter a number: ")
        try:
            # Attempt to convert the input to a float
            number = float(user_input)
            # If successful, break the loop and return the number
            return number
        except ValueError:
            # If a ValueError occurs, print an error message and the loop continues
            print("Invalid input. Please enter a valid numerical value (e.g., 10, 3.14, -5).")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}. Please try again.")

# --- Demonstration of the function ---
if __name__ == "__main__":
    print("Welcome to the number validation program!")

    first_number = get_valid_number()
    print(f"You entered a valid number: {first_number}")

    print("\nLet's try again with another number.")
    second_number = get_valid_number()
    print(f"You entered another valid number: {second_number}")







#Question 4
def write_names_to_file(filename, names_list):
    try:
        # Use 'with' statement for writing to ensure the file is properly closed
        with open(filename, 'w') as file:
            for name in names_list:
                file.write(name + '\n')
        print(f"Successfully wrote names to '{filename}'.")
    except IOError as e:
        print(f"Error writing to file '{filename}': {e}")

def read_names_from_file(filename):
    read_names = []
    try:
        # Use 'with' statement for reading to ensure the file is properly closed
        with open(filename, 'r') as file:
            for line in file:
                name = line.strip()  # Remove leading/trailing whitespace, including newline characters
                if name:  # Only add non-empty lines
                    read_names.append(name)
                    print(f"Read name: {name}")
        print(f"Successfully read names from '{filename}'.")
        return read_names
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except IOError as e:
        print(f"Error reading from file '{filename}': {e}")
        return []

# --- Main part of the program ---
if __name__ == "__main__":
    file_name = "names.txt"
    my_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    # 1. Write the names to the file
    print("--- Writing names to file ---")
    write_names_to_file(file_name, my_names)
    print("-" * 30) # Separator

    # 2. Read the names from the file and print them
    print("--- Reading names from file ---")
    names_from_file = read_names_from_file(file_name)
    print("-" * 30) # Separator

    # Optional: Verify the list of names read
    if names_from_file:
        print("\nAll names read from file:")
        print(names_from_file)
    else:
        print("\nNo names were read from the file.")







#Question 5
def convert_celsius_to_fahrenheit(celsius_temps):
    # Define the lambda function for Celsius to Fahrenheit conversion
    # Formula: F = C * 9/5 + 32
    c_to_f_converter = lambda c: (c * 9/5) + 32

    # Use map to apply the lambda function to each temperature in the list
    fahrenheit_temps = list(map(c_to_f_converter, celsius_temps))

    return fahrenheit_temps

# Sample list of Celsius temperatures
celsius_temperatures = [0, 10, 20, 30, -5, 25.5]

print("--- Celsius to Fahrenheit Converter ---")
print(f"Original Celsius temperatures: {celsius_temperatures}")

# Convert the temperatures
converted_fahrenheit_temperatures = convert_celsius_to_fahrenheit(celsius_temperatures)

print(f"Converted Fahrenheit temperatures: {converted_fahrenheit_temperatures}")

# Another example
another_celsius_list = [37.7, 100, -17.8]
print(f"\nOriginal Celsius temperatures: {another_celsius_list}")
converted_another_fahrenheit_list = convert_celsius_to_fahrenheit(another_celsius_list)
print(f"Converted Fahrenheit temperatures: {converted_another_fahrenheit_list}")




#Question 6
def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please provide a non-zero denominator.")
        return None
    except TypeError:
        print("Error: Invalid input types. Both numerator and denominator must be numbers.")
        return None
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Demonstrating divide_numbers function ---")

    # Valid division
    print(f"10 / 2 = {divide_numbers(10, 2)}")

    # Division by zero
    print(f"5 / 0 = {divide_numbers(5, 0)}")

    # Invalid input types (string as denominator)
    print(f"10 / 'a' = {divide_numbers(10, 'a')}")

    # Invalid input types (list as numerator)
    print(f"[1, 2] / 2 = {divide_numbers([1, 2], 2)}")

    # Valid division with floats
    print(f"7.5 / 2.5 = {divide_numbers(7.5, 2.5)}")

    # Valid division resulting in float
    print(f"9 / 2 = {divide_numbers(9, 2)}")




#Question 7
class NegativeNumberError(Exception):
    def __init__(self, message="Number cannot be negative"):
        self.message = message
        super().__init__(self.message)

def check_positive(number):
    if number < 0:
        raise NegativeNumberError(f"Received a negative number: {number}. Only positive numbers are allowed.")
    return f"Number {number} is positive."

# --- Demonstration of custom exception handling ---
if __name__ == "__main__":
    print("--- Demonstrating Custom Exception: NegativeNumberError ---")

    # Test: Positive number
    try:
        print(check_positive(10))
    except NegativeNumberError as e:
        print(f"Caught an error: {e}")
    except Exception as e:
        print(f"Caught an unexpected error: {e}")

    print("\n")





    # Question 8
import random

def generate_random_numbers(count, min_val, max_val):
    if count <= 0:
        return []
    return [random.randint(min_val, max_val) for _ in range(count)]

def calculate_average(numbers_list):
    if not numbers_list:
        print("Warning: The list is empty, returning average as 0.0.")
        return 0.0
    return sum(numbers_list) / len(numbers_list)

if __name__ == "__main__":
    # Define parameters for random number generation
    num_count = 10
    min_value = 1
    max_value = 100

    print(f"--- Generating {num_count} Random Numbers and Calculating Average ---")

    # Generate the list of random numbers
    random_numbers = generate_random_numbers(num_count, min_value, max_value)
    print(f"Generated numbers: {random_numbers}")

    # Calculate the average of the generated numbers
    average_value = calculate_average(random_numbers)
    print(f"Average of the numbers: {average_value:.2f}") # Format to 2 decimal places





#Question 9
import re

# Part I: Extract all email addresses from a given text
def extract_emails(text):
    # Regex pattern for a common email format
    # It covers alphanumeric characters, dots, underscores, percents, pluses, hyphens
    # before the @, followed by a domain name (alphanumeric, dots, hyphens)
    # and a top-level domain (2-4 letters/digits)
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

# Part II: Validate a date in the format "YYYY-MM-DD"
def validate_date(date_string):
    # Regex pattern for YYYY-MM-DD format
    # YYYY: 4 digits
    # MM: 01-12
    # DD: 01-31 (simplified, not checking for month-specific days like Feb 30)
    date_pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    return re.match(date_pattern, date_string) is not None

# Part III: Replace all occurrences of a word with another word in a string
def replace_word(text, old_word, new_word):
    # Use re.sub for replacement, re.IGNORECASE makes the search case-insensitive
    # \b ensures whole word matching
    return re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, text, flags=re.IGNORECASE)

# Part IV: Split a string by all non-alphanumeric characters
def split_non_alphanumeric(text):
    # \W matches any non-alphanumeric character (equivalent to [^a-zA-Z0-9_])
    # + means one or more occurrences
    return re.split(r'\W+', text)





#Question 10
import socket
import sys

# Server configuration
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def run_server():
    print("--- Server Program Started ---")
    print(f"Server listening on {HOST}:{PORT}")

    # Create a socket object
    # AF_INET for IPv4, SOCK_STREAM for TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Bind the socket to the address and port
            s.bind((HOST, PORT))
            # Enable the server to accept connections
            # 1 specifies that it should queue up to 1 incoming connection request
            s.listen(1)

            # Accept an incoming connection
            # conn is a new socket object representing the connection
            # addr is the address of the client
            print("Waiting for a client connection...")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                message_to_send = "Hello from server!"
                # Encode the message to bytes before sending
                conn.sendall(message_to_send.encode('utf-8'))
                print(f"Sent message: '{message_to_send}' to {addr}")

        except socket.error as e:
            print(f"Socket error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in the server: {e}")
        finally:
            print("Server program finished.")

if __name__ == '__main__':
    run_server()






    #Question 11
    # --- What is an API? ---
# An API (Application Programming Interface) is a set of rules and protocols
# that allows different software applications to communicate with each other.
# It defines the methods and data formats that applications can use to request
# and exchange information. Think of it as a menu in a restaurant: it lists
# what you can order, and the kitchen (server) knows how to fulfill that order.
# You don't need to know the internal workings, just how to interact with the interface.

# --- How to make a GET request to an API using the requests library in Python ---
# The 'requests' library is a popular and easy-to-use HTTP library in Python.
# A GET request is used to retrieve data from a specified resource (e.g., a website or a service).

import requests# First, you need to install it: pip install requests
import json     # Used to pretty-print JSON responses

def make_get_request_example():
    """
    Demonstrates how to make a GET request to a public API and handle the response.
    """
    print("\n# --- Making a GET Request Example ---")

    # The API endpoint (URL) you want to retrieve data from.
    # This is a public test API that provides placeholder data.
    api_url = "https://jsonplaceholder.typicode.com/posts/1"

    print(f"# Attempting to make a GET request to: {api_url}")

    try:
        # Make the GET request
        response = requests.get(api_url)

        # Check the status code to see if the request was successful (200 OK)
        if response.status_code == 200:
            print(f"# Request successful! Status Code: {response.status_code}")
            # Parse the JSON response body into a Python dictionary
            data = response.json()
            print("# Data received (JSON format):")
            print(json.dumps(data, indent=2)) # Use json.dumps for pretty printing
        else:
            print(f"# Error: Received status code {response.status_code}")
            print(f"# Response text: {response.text}")
    except requests.exceptions.ConnectionError as e:
        print(f"# Connection Error: Could not connect to the API. Check your internet or URL: {e}")
    except requests.exceptions.Timeout as e:
        print(f"# Timeout Error: The request took too long to respond: {e}")
    except requests.exceptions.RequestException as e:
        print(f"# An unexpected requests error occurred: {e}")
    except Exception as e:
        print(f"# An general error occurred: {e}")

# --- How to connect to a SQLite database using Python ---
# SQLite is a lightweight, file-based SQL database. Python has a built-in
# module 'sqlite3' for interacting with SQLite databases.

import sqlite3 # Built-in Python module

def connect_to_sqlite_example():
    """
    Demonstrates how to connect to a SQLite database, create a table,
    insert data, query data, and close the connection.
    """
    print("\n# --- SQLite Database Connection Example ---")

    conn = None # Initialize connection to None
    try:
        # Step 1: Connect to the database
        # sqlite3.connect('my_database.db') will connect to the specified file.
        # If the file does not exist, it will be created automatically.
        # The 'conn' object represents the connection to the database.
        print("# Step 1: Connecting to 'example.db' database...")
        conn = sqlite3.connect('example.db')
        print("# Connection established.")

        # Step 2: Create a Cursor object
        # A cursor is an object that allows you to execute SQL commands.
        # It acts like a pointer or control structure for traversing and processing database records.
        print("# Step 2: Creating a cursor object...")
        cursor = conn.cursor()
        print("# Cursor created.")

        # Step 3: Execute SQL queries
        # Use cursor.execute() to run SQL statements.
        # Here, we create a table named 'users' if it doesn't already exist.
        print("# Step 3: Executing SQL queries (creating table, inserting data)...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE
            )
        ''')
        print("# Table 'users' created or already exists.")

        # Insert some data. The '?' are placeholders for safe parameter substitution.
        # This helps prevent SQL injection attacks.
        try:
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
            print("# Inserted Alice.")
        except sqlite3.IntegrityError:
            print("# Alice already exists (email must be unique).")

        try:
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))
            print("# Inserted Bob.")
        except sqlite3.IntegrityError:
            print("# Bob already exists (email must be unique).")


        # Step 4: Commit changes (for write operations)
        # For any changes that modify the database (INSERT, UPDATE, DELETE, CREATE),
        # you need to call conn.commit() to save them permanently to the database file.
        # Without committing, changes would only exist in memory and be lost.
        print("# Step 4: Committing changes...")
        conn.commit()
        print("# Changes committed.")

        # Query data
        print("# Querying all users from the database:")
        cursor.execute("SELECT id, name, email FROM users")
        # cursor.fetchall() retrieves all rows of a query result.
        # Other methods include cursor.fetchone() for one row, or iterating over the cursor.
        rows = cursor.fetchall()
        for row in rows:
            print(f"  ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    except sqlite3.Error as e:
        print(f"# SQLite Error occurred: {e}")
    except Exception as e:
        print(f"# An unexpected error occurred: {e}")
    finally:
        # Step 5: Close the connection
        # It's important to close the connection when you're done with the database
        # to release resources and ensure the database file is not locked.
        if conn:
            print("# Step 5: Closing database connection...")
            conn.close()
            print("# Connection closed.")

# --- Main execution block to demonstrate both examples ---
if __name__ == "__main__":
    make_get_request_example()
    connect_to_sqlite_example()
