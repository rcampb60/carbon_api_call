import requests

headers = {
  'Accept': 'application/json'
}

postcode = input("Please enter your postcode area (for example EH2): ")
postcode_upper = postcode.upper()
 
#If the response from the API isn't correct this section will run, print an error message and then close the script down 
try:
    r = requests.get('https://api.carbonintensity.org.uk/regional/postcode/'+ postcode, params={}, headers = headers)
    response_data = r.json()
except requests.exceptions.RequestException as e:  
    print("Invalid input, please run again")
    raise SystemExit(e)

#If the input isn't in the correct format this section will run, print an error message and then close the script down
try:
  region_name = response_data['data'][0]['shortname']
except:  
  print("Invalid input, please run again. Input should be a postcode area which is the first half of your postcode.")
  raise SystemExit()

#This section locates the 'generation mix' section of the JSON data we are interested in
generation_mix = response_data['data'][0]['data'][0]['generationmix']

#this section presents the information requested above and pretties it up for display using f strings
data_output = f"""In the {postcode_upper} postcode area, in {region_name}, the usage of fuels in the last half hour was:"""
print(data_output)

#this section uses a loop to iterate through the API response. It finds the fuel key, capatilises it and then returns the percentage value and appends it with a percentage sign
for i in generation_mix:
    print(f"{i['fuel'].capitalize()}: {i['perc']}%")