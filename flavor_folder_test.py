# Get the csv in df
import pandas as pd

df = pd.read_csv('flavor.csv')

flavor_list = df['flavor'].tolist()
# print(type(flavor_list), type(df['flavor'][0]))

print('***********************')
# print('flavor: ' + df.iloc[0,1])
# print(f'index: {df.iloc[3,0]}, flavor: {df.iloc[3,1]}')


print(df['flavor'])
print('***********************')

# Empty list to append
user_input_list = []

# User make selection
while True:
    
    try:
        # Prompt for user: 
        # Select number for the flavor user want
        user_input = int(input(f'Select the # of the flavor:'))
        selected_index = df['flavor'][user_input]

        # Add item in the list if it exists
        if selected_index in flavor_list:
            # Don't add the same iteam in the list
            if  selected_index in user_input_list:
                continue
            else:
                print(f'"{selected_index}" entered')
                # Append list with flavor
                user_input_list.append(selected_index)
                print('>>>>>Input string or press enter to move on<<<<<<<')
        else:
            break

    except KeyError:
        print('---------Selection does not exist. Try again.---------')
    
    except:
        print('I guess you are done!')
        break

# What do we have at the end?
print('*****************************')
print(f'Here is your selection: {user_input_list}')
print('*****************************')


# Write a file with the same file name as the flavor selected
import os

for l in user_input_list:
    # path_name = l

    # Check to see if path exist
    is_exist = os.path.exists(l)

    if not is_exist:
        
        # create a new directory
        os.makedirs(l)
        print(f'{l} directory created')

    else:
        print(f'{l} directory exists.')

    # Create a file
    # Move it into the directory 