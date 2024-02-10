import time  # Import the time module

nca_variable = []  # List to store non-current assets
ca_variable = []   # List to store current assets
cl_variable = []   # List to store current liabilities

nca_count = 0
ca_count = 0
cl_count = 0

print("This is a balance sheet maker")
time.sleep(2)
print("You are welcome to use other useful programs in my GitHub")
time.sleep(2)

company = input("What is the name of your company? ")

print(f"What are non-current assets of your {company}")
time.sleep(2)

def non_current_assets():
    global nca_count
    while True:
        user_input = input("Type the name of non-current asset you want to use, once you are done with it, type 'done': ")
        if user_input.lower() == "done":
            print("Next step!")
            break
        
        elif nca_count >= 5:
            print("Too many non-current assets!")
            continue
    
        else:
            value = float(input(f"Enter value for {user_input}: "))
            nca_variable.append((user_input, value))
            nca_count += 1
            print(f"You have {nca_count} non-current assets")
            time.sleep(1)

non_current_assets()

def current_assets():
    print(f"What are current assets of your {company}")
    time.sleep(2)
    while True:
        user_input = input("Type the name of current asset you want to use, once you are done with it, type 'done': ")
        if user_input.lower() == "done":
            print("Next step!")
            break
        else:
            value = float(input(f"Enter value for {user_input}: "))
            ca_variable.append((user_input, value))

current_assets()

def current_liabilities(): 
    global cl_count
    while True:
        user_input = input("Type the name of current liabilities you want to use, once you are done with it, type 'done': ")
        if user_input.lower() == "done":
            print("Next step!")
            break
        
        elif cl_count >= 7:
            print("Too many current liabilities!")
            continue
    
        else:
            value = float(input(f"Enter value for {user_input}: "))
            cl_variable.append((user_input, value))
            cl_count += 1
            print(f"You have {cl_count} current liabilities")
            time.sleep(1)

current_liabilities()

print(f"{company} balance sheet is as follows:")
time.sleep(1)

# Print Non-Current Assets
print("Non-Current Assets:")
for asset, value in nca_variable:
    print(f"{asset}:  {value}")

# Calculate and Print Total Non-Current Assets Value
total_nca_value = sum(value for _, value in nca_variable)
print("Total Non-Current Assets Value:", total_nca_value) 

# Print Current Assets
print("Current Assets:")
for asset, value in ca_variable:
    print(f"{asset}:  {value}")

# Calculate and Print Total Current Assets Value
total_ca_value = sum(value for _, value in ca_variable)
print("Total Current Assets Value:", total_ca_value) 

# Print Current Liabilities
print("Current Liabilities:")
for liability, value in cl_variable:
    print(f"{liability}:  {value}")

# Calculate and Print Total Current Liabilities Value
total_cl_value = sum(value for _, value in cl_variable)
print("Total Current Liabilities Value:", total_cl_value) 

exit()
