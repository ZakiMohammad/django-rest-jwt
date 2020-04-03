import requests

headers = {}
headers[
    "Authorization"
]: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1OTI4ODE5LCJqdGkiOiI5ZDNkYjBmNTY1YTA0ZTBkOTVmZTAxODM2ODRhZWY1ZSIsInVzZXJfaWQiOjF9.OnOaunJT-oegP7o0WTd1TicUFNtbIwD87CJtitWY5E4"

r = requests.get("http://127.0.0.1:8000/paradigm/", headers=headers)

print(r.text)
