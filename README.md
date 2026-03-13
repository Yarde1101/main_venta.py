# Simulation Work-of script_venta
In this proyect, a simulation of a sales register program for a store was created
## Description oh the Proyect 
This proyect automates the recording of a store's daily sales. A script allows the administrator to record the day's sales 
and genrate a summary showing the products sold, quantities, and total revenue.

The The script prompts the user to enter:
- Product name
- Quantity
- Price

The program then calculates the total price of the sale.
All sales are stored in a list, and at the end, the program displays a summary of the sales and the total amount for the day.
The program runs in the console and interacts with the user through input prompts

# How the Program Works
1. Welcome Message

The program prints a welcome message.

Example: welcome to the Store 

## 2. Creating a List

The program creates an empty list to store the sales.

## 3. Registering a Sale

The function register() asks the user for information.

- The user enters:

- Product name

- Quantity

- Price

The program is reading the information.

## 4. Calculating the Total

The program calculates the total price.

## 5. Saving the Sale

The program creates a dictionary with the sale information.

## 6. Asking for Another Sale

The program is asking the user:

- If the answer is "y", the program continues, return to the point 3 again add to new sale 

- If the answer is "n", the program stops.
