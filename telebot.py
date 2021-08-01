import requests
from datetime import date, datetime
import time 
import schedule 


url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?"
tele_api="https://api.telegram.org/bot1905181947:AAHY68M-BrAyoRn7b3jJLz_ssxcGIQ2Bm8I/sendMessage?chat_id=@mygroup78&text="
now = datetime.now()
today=now.strftime("%d-%m-%Y")
# print(today)
grp_id="t.me/mygroup78"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


states=[{"state_id":1,"state_name":"Andaman and Nicobar Islands"},{"state_id":2,"state_name":"Andhra Pradesh"},{"state_id":3,"state_name":"Arunachal Pradesh"},{"state_id":4,"state_name":"Assam"},{"state_id":5,"state_name":"Bihar"},{"state_id":6,"state_name":"Chandigarh"},{"state_id":7,"state_name":"Chhattisgarh"},{"state_id":8,"state_name":"Dadra and Nagar Haveli"},{"state_id":37,"state_name":"Daman and Diu"},{"state_id":9,"state_name":"Delhi"},{"state_id":10,"state_name":"Goa"},{"state_id":11,"state_name":"Gujarat"},{"state_id":12,"state_name":"Haryana"},{"state_id":13,"state_name":"Himachal Pradesh"},{"state_id":14,"state_name":"Jammu and Kashmir"},{"state_id":15,"state_name":"Jharkhand"},{"state_id":16,"state_name":"Karnataka"},{"state_id":17,"state_name":"Kerala"},{"state_id":18,"state_name":"Ladakh"},{"state_id":19,"state_name":"Lakshadweep"},{"state_id":20,"state_name":"Madhya Pradesh"},{"state_id":21,"state_name":"Maharashtra"},{"state_id":22,"state_name":"Manipur"},{"state_id":23,"state_name":"Meghalaya"},{"state_id":24,"state_name":"Mizoram"},{"state_id":25,"state_name":"Nagaland"},{"state_id":26,"state_name":"Odisha"},{"state_id":27,"state_name":"Puducherry"},{"state_id":28,"state_name":"Punjab"},{"state_id":29,"state_name":"Rajasthan"},{"state_id":30,"state_name":"Sikkim"},{"state_id":31,"state_name":"Tamil Nadu"},{"state_id":32,"state_name":"Telangana"},{"state_id":33,"state_name":"Tripura"},{"state_id":34,"state_name":"Uttar Pradesh"},{"state_id":35,"state_name":"Uttarakhand"},{"state_id":36,"state_name":"West Bengal"}]
state ={}
# for i in range(len(states)):
#     # print(states[i])
#     for state_id in states[i].items():
#         # print(state_id)
#         state[state_id[0]]=state_id
#     # print(states[i])
# print(state)


# print(districts)
    
def get_data(district_id):
    # print(today)
    query_params="district_id={}&date={}".format(district_id,today)

    final_url=url+query_params
    # print(final_url)
    
    res=requests.get(final_url,headers=headers)
    time.sleep(1)
    extract_data(res)
    # print(res.json())

def extract_data(res):
    c=0
    message=""
    data_json=res.json()
    for center in data_json["centers"]:
    
        for session in center["sessions"]:
            if(session["available_capacity_dose1"]>0 and session["min_age_limit"]>=18):
                c+=1
                message +="Pincode:{}\nName:{}\nAvailable Slots:{}\nMinimum age:{}\n------------------------\n".format(center["pincode"],center["name"],session["available_capacity_dose1"],session["min_age_limit"])
                # print(center["pincode"],center["name"],session["available_capacity_dose1"],session["min_age_limit"])
                # print(message)
    
    send_message(message)
def send_message(message):
    # print(message)
    # chat_id="t.me/mygroup78"
    # tele_api.replace("__grpid__","mygroup78")
    final_telegram_call=tele_api+str(message)
    # time.sleep(1)
    print(final_telegram_call)
    res=requests.get(final_telegram_call)
    print(res)
    # print("total centers= ",c)

def get_all():
    districts=[]
    for i in range(312,320,1):
        districts.append(i)
    for i in districts:
        get_data(i)
if __name__ == "__main__":
    # schedule.every(10).hours.at(':45').do(get_all(districts))
    
    # schedule.every(10).seconds.do(get_all)
    schedule.every().day.at("10:30").do(get_all)

    while True:
        schedule.run_pending()
        time.sleep(1)
    # get_states()
    
    # get_data(314)
    

    