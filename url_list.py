#Aisha Siddiq lab 12:00 - 1:50 pm (project 3)

import json
import urllib.parse
import urllib.request



def return_url(location_list)->str:
    '''Returns the url of map quest
    '''
    MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?key=Fmjtd%7Cluu82q0yl1%2C20%3Do5-94y0dw'
    location_from_to = []
    location_from_to.append(('from', location_list[0]))
    for items in range(len(location_list) -1):
        query = ('to', location_list[items + 1]) 
        location_from_to.append(query)
    return MAPQUEST_URL + '&' + urllib.parse.urlencode(location_from_to) 


    
def get_result(url:str)->'json':
    '''This function takes the URL and returns a Python object representing the
    parsed JSON response (professors code example) 
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    
    except:
        return None 
    
     
    finally:
        if response != None:
            response.close()


                
def lat_long(json_result: 'json')->list:
    '''Returns a list of longitude and latitude (used to get the elevation) 
    '''    
    lat_long_list = []
     
    for items in json_result['route']['locations']:
        lat_long = items['latLng']
        lat_long_list.append([str(lat_long['lat']), str(lat_long['lng'])])
    return lat_long_list



def elevation(lat_long_list:list)->list:
    '''Returns the decoded elevation by taking in a list of longitude and latitude as
    its parameter
    '''
    ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?key=Fmjtd%7Cluu82q0yl1%2C20%3Do5-94y0dw'
    url_list = []
    for my_list in lat_long_list:
        join_lat_long = ','.join(my_list)
        url_list.append(ELEVATION_URL + '&' + urllib.parse.urlencode([('latLngCollection', join_lat_long)]))
            
    return url_list
            

def json_dictionary(location_list:list)->'json_data':
    '''Returns the json dictionary response (function created already but it
    ties the two functions together to make the importation simpler)
    '''
        
    location_url = return_url(location_list)
    json_data = get_result(location_url)
    return json_data


def elevation_dictionary_list(json_data)->list:
    '''Returns a list of elevation (json dictionary) 
    '''
    
    elevation_list = []
    latlong_list = lat_long(json_data)
    elevation_url_list = elevation(latlong_list)
    for elevation_urls in elevation_url_list:
        elevation_list.append(get_result(elevation_urls))
    return elevation_list
    






