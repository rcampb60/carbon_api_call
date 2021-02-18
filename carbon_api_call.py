import requests

headers = {
  'Accept': 'application/json'
}

postcode = input("Please enter your postcode area (for example EH2): ")
 
r = requests.get('https://api.carbonintensity.org.uk/regional/postcode/'+ postcode, params={}, headers = headers)
response_data = r.json()

region_name = response_data['data'][0]['shortname']

biomass = response_data['data'][0]['data'][0]['generationmix'][0]['perc']
coal = response_data['data'][0]['data'][0]['generationmix'][1]['perc']
imports = response_data['data'][0]['data'][0]['generationmix'][2]['perc']
gas = response_data['data'][0]['data'][0]['generationmix'][3]['perc']
nuclear = response_data['data'][0]['data'][0]['generationmix'][4]['perc']
other = response_data['data'][0]['data'][0]['generationmix'][5]['perc']
hydro = response_data['data'][0]['data'][0]['generationmix'][6]['perc']
solar = response_data['data'][0]['data'][0]['generationmix'][7]['perc']
wind = response_data['data'][0]['data'][0]['generationmix'][8]['perc']

print(f"In the {postcode} postcode area, in {region_name}, the usage of fuels in the last half hour was:")
print(f"Biomass: {biomass}%") 
print(f"Coal: {coal}%") 
print(f"Imports: {imports}%") 
print(f"Gas: {gas}%")
print(f"Nuclear: {nuclear}%")
print(f"Other: {other}%")
print(f"Hydro: {hydro}%")
print(f"Solar: {solar}%")
print(f"Wind: {wind}%")