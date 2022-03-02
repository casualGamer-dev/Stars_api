



import csv

rows = []

with open("test2.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]
print(headers)
print(planet_data_rows[0])

"""Here, we can see that there is an extra field added into the CSV, denoting the row count but the first header is an empty string. Let's fix that and then proceed with finding the number of planets in each of the solar system!"""

headers[0] = "id"


temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  planet_mass = planet_data[4]
  if planet_mass.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue

  planet_radius = planet_data[3]
  if planet_radius.lower() == "unknown":
    planet_data_rows.remove(planet_data)
    continue




temp_planet_data_rows = list(planet_data_rows)

planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[5])
  planet_names.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index].replace(',', ''))*5.972e+24) / (float(planet_radiuses[index].replace(',', ''))*float(planet_radiuses[index].replace(',', '') )*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

print(headers)


planet_masses=[]
planet_radii=[]






planet_masses=[]
planet_radii=[]


final_dict={}
for index,planet_data in enumerate(planet_data_rows):
  features_list=[]
  gravity = (float(planet_data[3].replace(',', ''))*5.972e+24) / (float(planet_data[5].replace(',', ''))*float(planet_data[5].replace(',', ''))*6371000*6371000) * 6.674e-11
  try:
    if gravity < 100:
      features_list.append("gravity")
  except:
    pass 
  final_dict[index]=features_list             
print(final_dict)

final_dict = {}

headers.append("gravity")

for index, planet_data in enumerate(planet_data_rows):
  features_list = []
  gravity = (float(planet_data[3].replace(',', ''))*5.972e+24) / (float(planet_data[5].replace(',', ''))*float(planet_data[5].replace(',', ''))*6371000*6371000) * 6.674e-11
  try:
    if gravity < 100:
      features_list.append("gravity")
    planet_data.append(gravity)
  except: planet_data.append("Unknown")
  
  final_dict[planet_data[1]] = features_list

print(final_dict)




gravity_planet_count=0
for key,value in final_dict.items():
  if "gravity" in value:
    gravity_planet_count+=1
print(gravity_planet_count)  
planet_type_count=0



final_dict = {}

for index, planet_data in enumerate(planet_data_rows):
  features_list = []
  gravity = (float(planet_data[3].replace(',', ''))*5.972e+24) / (float(planet_data[5].replace(',', ''))*float(planet_data[5].replace(',', ''))*6371000*6371000) * 6.674e-11
  try:
    if gravity < 100:
      features_list.append("gravity")
  except: pass
  final_dict[planet_data[1]] = features_list

print(final_dict)



final_planet_list=[]
for planet_data in planet_data_rows:
  temp_dict={
      "name":planet_data[1],
      "planet_mass":planet_data[4],
      "planet_radius":planet_data[3],
      "gravity":(float(planet_data[3].replace(',', ''))*5.972e+24) / (float(planet_data[5].replace(',', ''))*float(planet_data[5].replace(',', ''))*6371000*6371000) * 6.674e-11,
  }
  temp_dict["specifications"]=final_dict[planet_data[1]]
  final_planet_list.append(temp_dict)
print(final_planet_list)
