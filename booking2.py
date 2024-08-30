import requests

url = "http://51.21.17.206:8081/booking/create"

bid = 1
uid = 200
mid = 110
booking_date = "2024-08-28"
booking_time = "10:00 AM"
visit_date = "2024-09-01"
visit_time = "12:00 PM"
payment_status = "Pending"
payment_amount = "100.00"
total_people = "4"
booking_status = "Confirmed"

# Convert to f-string JSON payload
payload = f"""{{"bid":{bid},"user":{{"uid":{uid}}},"mu":{{"mid":{mid}}},"booking_date":"{booking_date}","booking_time":"{booking_time}","visit_date":"{visit_date}","visit_time":"{visit_time}","payment_status":"{payment_status}","payment_amount":"{payment_amount}","total_people":"{total_people}","booking_status":"{booking_status}"
}}"""
response = requests.request("POST", url, json=payload)

print(response.text)