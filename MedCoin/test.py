import requests
r = requests.post('http://127.0.0.1:5000/new?first_name=Yo&last_name=You&blood_type=A-&allergies=nuts/milk')
print r.text
