import requests

headers = {
  'Accept': 'application/json'
}

postcode = input("Please enter your postcode area (for example EH2): ")
postcode_upper = postcode.upper()
 
try:
    r = requests.get('https://api.carbonintensity.org.uk/regional/postcode/'+ postcode, params={}, headers = headers)
    response_data = r.json()
except requests.exceptions.RequestException as e:  #If the response from the API isn't correct this section will run, print an error message and then close the script down
    print("Invalid input, please run again")
    raise SystemExit(e)

try:
  region_name = response_data['data'][0]['shortname']
except:  #If the input isn't in the correct format this section will run, print an error message and then close the script down
  print("Invalid input, please run again. Input should be a postcode area which is the first half of your postcode.")
  raise SystemExit()


#this section picks out each fuel type percentage
biomass = response_data['data'][0]['data'][0]['generationmix'][0]['perc']
coal = response_data['data'][0]['data'][0]['generationmix'][1]['perc']
imports = response_data['data'][0]['data'][0]['generationmix'][2]['perc']
gas = response_data['data'][0]['data'][0]['generationmix'][3]['perc']
nuclear = response_data['data'][0]['data'][0]['generationmix'][4]['perc']
other = response_data['data'][0]['data'][0]['generationmix'][5]['perc']
hydro = response_data['data'][0]['data'][0]['generationmix'][6]['perc']
solar = response_data['data'][0]['data'][0]['generationmix'][7]['perc']
wind = response_data['data'][0]['data'][0]['generationmix'][8]['perc']

#this section presents the information requested above and pretties it up for display using f strings
data_output = f"""
In the {postcode_upper} postcode area, in {region_name}, the usage of fuels in the last half hour was:

Biomass: {biomass}%
Coal: {coal}%
Imports: {imports}%
Gas: {gas}%
Nuclear: {nuclear}%
Other: {other}%
Hydro: {hydro}%
Solar: {solar}%
Wind: {wind}%
"""

print(data_output)