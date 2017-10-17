#Aisha Siddiq lab 12:00 - 1:50 pm (project 3)

class STEPS:

    def __init__(self, jsondata):
        
        self.jsonD = jsondata

    
    def return_data(self)->list:
        '''Returns the json steps in a list
        '''
        
        directions = ["DIRECTIONS"]
        for items in self.jsonD['route']['legs']:
            for maneuvers in items['maneuvers']:
                directions.append(maneuvers['narrative'])
        return directions


class TOTALDISTANCE:

    def __init__(self, jsondata):
        
        self.jsonD = jsondata

    def return_data(self)->list:
        '''Returns the total distance in a list
        '''
        distance = []
        distance.append('TOTAL DISTANCE: ' + str(round(self.jsonD['route']['distance'])) + ' '+ "miles")
        return distance         
        


class TOTALTIME:

    def __init__(self, jsondata):
        
        self.jsonD = jsondata

    def return_data(self)->list:
        '''Returns the total time in a list
        '''
        time = []
        time_mins = round(self.jsonD['route']['time']/60)
        time.append('TOTAL TIME: ' + str(time_mins) + ' ' + 'minutes')
        return time


class LATLONG:

    def __init__(self, jsondata):
        
        self.jsonD = jsondata

        
    def return_data(self)->list:
        '''Returns the formatted longitude and latitude in a list
        '''
        
        latlonglist = ['LATLONGS']
        
        for items in self.jsonD['route']['locations']:
            latlong = items['latLng']
            if latlong['lat'] <  0:
                latitude = '{:.2f}S'.format(latlong['lat'] * -1)
            elif latlong['lat'] > 0: 
                latitude = '{:.2f}N'.format(latlong['lat'])
            else:
                latitude = '{}'.format(latlong['lat']) 
        
            if latlong['lng'] < 0:
                longitude = '{:.2f}W'.format(latlong['lng'] * -1)
            elif latlong['lng'] > 0: 
                longitude = '{:.2f}E'.format(latlong['lng'])
            else:
                longitude = '{}'.format(latlong['lng'])
                
            latlonglist.append(latitude + ' ' + longitude)
            
        return latlonglist

    


class ELEVATION:

    def __init__(self, jsonlist):
        
        self.jsonDlist = jsonlist

    def return_data(self)->list:
        '''Returns the elevation in a list
        '''
        
        elevation_list = ['ELEVATIONS']
        for jsondatalist in self.jsonDlist: 
            for distance in jsondatalist['elevationProfile']:
                elevation_list.append(round(distance['height'] * 3.2808))
        return elevation_list
