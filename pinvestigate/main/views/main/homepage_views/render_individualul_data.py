import json
from django.shortcuts import render

class RenderIndividualJSONData:
    def __init__(self):
        pass
    #fyi: This method takes the object data from the json files and renders it onto the html page(homepage.html) 
    #fyi: and renders the data onto the template.
    # Gets the JSON file and stores it in json_dir, 
    # then uses json.loads() from json module to convert data into a python object,
    # then returns the data object to the webpage 
    def render_json_data(request):
        json_dir = {"case":"theft","name": "John Wilks", "desc":"This guy stole me money, and me wallets >:(", }
        individual_object = json.loads(json_dir)
        return render(request, 'main/homepage_html/homepage.html', {'individual_object': individual_object})

    def check_topic_page(url_name):
        #This is to check which page the user is viewing
        return print("it works")