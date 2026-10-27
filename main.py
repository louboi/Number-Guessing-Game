def get_input():
    '''Gets the users guess and validates it is an integer. Returns the input when valid'''
    
    # Initialise a temporary variable as a string type
    temp = str 

    # Continue looping until it is an integer
    while type(temp) != int: # Check if it's an integer
        try:
            temp = int(input("What is your guess? ")) # Get the input and try and try to make it an integer
        except:
            print("Number must be an integer, try again!") # If not an integer, tell the user...
            continue # ...And continue doing the loop

    # Return the value
    return temp

def validate_range():
    '''Check the input is in the valid range of  0 to 100 inclusive. Takes no variables, calls get_input itself'''
    
    # Initialise a temporary variable with the valid integer input
    temp = get_input() 
    
    # Keep looping until it is in the correct range
    while temp < 0 or temp > 100: # Check if it's NOT in the range
        print("Number not in valid range, try again!") # Tell the user ...
        temp = get_input() # ... Get the input again

    # Return the Value
    return temp

def main():
    validate_range()

if __name__ == "__main__":
    main()
