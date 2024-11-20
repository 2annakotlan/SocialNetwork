import requests

web_app_url = "https://script.google.com/macros/s/YOUR_DEPLOYMENT_ID/exec"

try:
    response = requests.post(web_app_url)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)
