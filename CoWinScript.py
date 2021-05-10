import requests
import smtplib
import ssl
import json
import time

alwaysTrue = True

print("Script started")

while alwaysTrue:
    print("\n START :: hitting the URL and script started \n")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    ploads1 = {'district_id': '392', 'date': '10-05-2021'}
    ##ploads1 = {'district_id': '512', 'date': '10-05-2021'}
    try:
        r = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict', params=ploads1,
                     headers=headers)
        data = json.loads(r.text)
    except:
        print("Exception occurred while sending and API")
        time.sleep(15)
        continue
    try:
        if "centers" in data.keys():
            centresData = data["centers"]
            for singleCentreDetails in centresData:
                centerId = singleCentreDetails["center_id"]
                name = singleCentreDetails["name"]
                address = singleCentreDetails["address"]
                stateName = singleCentreDetails["state_name"]
                districtName = singleCentreDetails["district_name"]
                block_name = singleCentreDetails["block_name"]
                pincode = singleCentreDetails["pincode"]
                lat = singleCentreDetails["lat"]
                long = singleCentreDetails["long"]
                fromDate = singleCentreDetails["from"]
                toDate = singleCentreDetails["to"]
                fee_type = singleCentreDetails["fee_type"]
                sessions = singleCentreDetails["sessions"]

                for session in sessions:
                    sessionId = session["session_id"]
                    date = session["date"]
                    vaccine = session["vaccine"]
                    available_capacity = session["available_capacity"]
                    min_age_limit = session["min_age_limit"]

                    """""    
                    if ((isinstance(min_age_limit, int) and min_age_limit == 45) or (
                            isinstance(min_age_limit, str) and min_age_limit == "45")):
                        continue
                    """""

                    slots = session["slots"]
                    date = session["date"]

                    if(available_capacity > 0):
                        print("seats available for 18 years slot, book instantly")
                        port = 465  # For SSL
                        smtp_server = "smtp.gmail.com"
                        sender_email = "testingkushal@gmail.com"  # Enter your address
                        receiver_email = ["skushal746@gmail.com", "sharmaritu1506@gmail.com",
                                          "akashkhurangale@gmail.com",
                                          "jyotivarma06@gmail.com", "ruchirmeena@gmail.com",
                                          "ishitaraj1811@gmail.com", "kushal.sharma2208@gmail.com",
                                          "kush.sharma.2208@gmail.com"]  # Enter receiver address
                        password = "#CoWinRegister"
                        message = """Subject: CoWIn Email

                        The slots are available in thane, kindly register ASAP!!!!!
                        """

                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                            server.login(sender_email, password)
                            server.sendmail(sender_email, receiver_email, message)
                    print("currently seats are not available")        
    except:
        print("Exception while parsing the JSON and getting data or while sending the mail")
        time.sleep(15)
        continue

    print("\n END   :: hitting the URL and script ended \n")
    time.sleep(15)
