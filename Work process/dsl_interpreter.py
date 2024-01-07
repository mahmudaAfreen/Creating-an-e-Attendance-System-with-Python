# Import the sys module
import sys

# Define a dictionary of functions to perform calculation based on time unit
functions = {'minutes': lambda x, y: x + round(y/60, 2),
             'hours': lambda x, y: x + y}

# Check if exactly two arguments are given
if len(sys.argv) != 2:
    # Exit the program with error code 1 if not
    sys.exit(1)

# Open the file specified as the second argument
with open(sys.argv[1]) as file:
    # Initialize a dictionary to keep track of total time spent on each activity
    routine = {"Exercise": 0,
               "Prayer": 0,
               "Reading": 0,
               "Walk": 0,
               "Study": 0,
               "Work": 0,
               "Entertainment": 0,
               "Social Media": 0,
               "Cooking": 0,
               "Laundry": 0,
               "Groceries": 0              
               }

    # Loop through each line in the file
    for line in file:
        # Strip the line of any leading/trailing whitespaces
        line = line.strip()
        # Skip empty lines or comments (lines starting with '~')
        if not line or line[0] == '~':
            continue
        # Split the line into separate parts, using spaces as the separator
        single_parts = line.split()
        # Check if the first part of the line is 'Time'
        if single_parts[0] == 'Time':
            # Print the total time spent on the activity specified in the line
            print(f"You spent: {routine[single_parts[3]]} hours {single_parts[3]} this week.")
        else:
            # Retrieve the current time spent on the activity
            x = routine[single_parts[2]]
            # Convert the first part (time value) to integer
            y = int(single_parts[0])
            # Update the time spent on the activity by calling the appropriate function
            routine[single_parts[2]] = functions[single_parts[1]](x, y)
