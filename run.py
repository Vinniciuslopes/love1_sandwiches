data1 = [[280, 300, 320, 320],[270, 280, 260, 270],[320, 310,300, 290]]


def get_data():

    while True:
        print("Please enter the number of items picked.")
        print('Please provide 4 numnber, separate by comma.')
        print('Example: 290,300,280,300\n')

        data_str = input('Enter your data: ')

        picked_items = data_str.split(',')
        
        if validate_data(picked_items):
            print('Data is valid!')
            break
    return picked_items    

def validate_data(values):
    
   
    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f'You have provided {len(values)} numbers, insted of 4 numbers!!'
        )
    except ValueError as e:
        print(f"invalid data: {e}, please try again.")
        return False
    return True


data = get_data()

