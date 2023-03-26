# Get the csv in df
import pandas as pd

df = pd.read_csv('flavor.csv')

flavor_list = df['flavor'].tolist()
# print(type(flavor_list), type(df['flavor'][0]))

print('***********************')
# print('flavor: ' + df.iloc[0,1])
# print(f'index: {df.iloc[3,0]}, flavor: {df.iloc[3,1]}')

# Empty list to append
user_input_list = []

print(df['flavor'])
print('***********************')

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

# Move it into the directory / create directory w/ same name if doesn't already exist
