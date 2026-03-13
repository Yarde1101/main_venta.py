# definition of variable of the Store 
print("\n---------- Welcome to the Store-----------")

sales_list = []

def register():
    
    Product = input("Enter product name: ") 
    quantity = int(input ("Enter product quantity:"))
    price= int(input(" Enter price: ")) 
    total = price * quantity
    
    
    N = {
        
        "Product": Product,
        "quantity": quantity,
        "price": price,
        "total": total
        
    }
    
    sales_list.append(N)
    
    # in this part, we define the sales record and peroform the sales calculation
continuar = "y"
while continuar == "y":
    register()
    continuar = input(" Do you  want to add another sale (y/n):").lower()
    
    if continuar == "n":
        print("Thank you for you purshase, see you later  ")
    elif continuar != "y":
        print("please, Respond with 'y' o 'n'. ")    

print("\n------ Resume of sale------")

total_dia = 0

for N in sales_list:
    print(f"Product: {N['Product']}")
    print(f"quantity: {N['quantity']}")
    print(f"price: {N['price']}")
    print(f"total: {N['total']}")
    
    total_dia += N["total"]
    print(f"Total recount of the day: {total_dia}")
    print("\n------------------------------------------")