#Aisha Siddiq lab 12:00 - 1:50 pm (project 3)

import projurl
import classoutput


def number_location()->list:
    '''Prompts the user to input a valid location and returns a list of
    all the locations
    '''

    
    while True:
        
        location_list = []
        
        try:
            number_of_locations = int(input())
            if number_of_locations >= 2:
                for x in range(number_of_locations):
                    enter_input = input() 
                    location_list.append(enter_input) 
                return location_list
                
            else:
                print('Integer must be at least 2 or greater')
                
        except ValueError:
            print('Please enter an integer')



def enter_output()->list:
    '''Prompts the user to input the data recieved from the location
    '''
    
    while True:
        
        command_list = [] 
        
        try: 
            location_output = int(input())
            if location_output >= 1:
                for x in range(location_output):
                    enter_output = input()
                    command_list.append(enter_output)
                return command_list
            
            else:
                print('Integer must be at least 1 or greater')

        except ValueError:
            print('Please print an integer')
            

    

def enter_command()->list:
    '''Returns a list of classes for each output specified if the list is empty
    then either a Mapquest error was found or no route was found. 
    '''
    location_list = number_location()
    json_data = projurl.json_dictionary(location_list)

    if json_data == None:
        print('\nMAPQUEST ERROR')
        return []
        
    for items in json_data['route']:
        if items == 'routeError':
            print('\nNO ROUTE FOUND')
            return []
        
        else:
            
            elevation_list = projurl.elevation_dictionary_list(json_data)
    

            while True:
            
                commands = enter_output() 
                classes = []
                for response in commands:
                    if response.upper().strip() == 'LATLONG':
                        classes.append(classoutput.LATLONG(json_data))

                    elif response.upper().strip() == 'STEPS':
                        classes.append(classoutput.STEPS(json_data))

                    elif response.upper().strip() == 'TOTALTIME':
                        classes.append(classoutput.TOTALTIME(json_data))

                    elif response.upper().strip() == 'TOTALDISTANCE':
                        classes.append(classoutput.TOTALDISTANCE(json_data))

                    elif response.upper().strip()  == 'ELEVATION':
                        classes.append(classoutput.ELEVATION(elevation_list))

                    else:
                        print('Invalid input')                      
                               
                return classes



def print_output(commands:list):
    '''Prints all the data within the list of classes
    '''

    if commands == []:
        pass
    
    else:
        
        for commandclass in commands:
            print() 
            for all_data in commandclass.return_data():
                print(all_data)
                
        print() 
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')



def user_interface():
    '''Executes everything in a single function
    '''
    commandlist = enter_command()
    print_output(commandlist) 
    

                    
if __name__ == '__main__':
    user_interface() 
   
         
    





