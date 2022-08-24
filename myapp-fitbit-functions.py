import re
import requests, json
myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSNkIiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMjk1NDQ0LCJpYXQiOjE2NjA3NTk0NDR9.bILcGIrPRXPWRrWBZDKRLsZdtTKKqPUpZ4NZZ-U3k5g"}
def get_name():
    myurl = "https://api.fitbit.com/1/user/-/profile.json"
    resp = requests.get(myurl, headers=myheader).json()
    print(resp['user']['fullName'])
get_name()

def get_steps():
    myurl2 = "https://api.fitbit.com/1/user/-/activities/steps/date/today/1d.json"
    resp2 = requests.get(myurl2, headers=myheader).json()
    print("Your total step count today is " + resp2['activities-steps'][0]['value'])
get_steps()

def get_sleep():
    myurl3 = "https://api.fitbit.com/1.2/user/-/sleep/date/today.json"
    resp3 = requests.get(myurl3, headers=myheader).json()
    print("Total time slept is "+ str(resp3['summary']['totalMinutesAsleep'] // 60) + " hours and " +str(resp3['summary']['totalMinutesAsleep']%60) + " minutes.")
get_sleep()

def get_activeness():
    myurl4 = "https://api.fitbit.com/1/user/-/activities/list.json?afterDate=2022-08-07&sort=asc&offset=0&limit=2"
    resp4 = requests.get(myurl4, headers=myheader).json()
    respString = ""
    for x in range(4):
        if resp4['activities'][0]['activityLevel'][x]['minutes'] > 0:
            if resp4['activities'][0]['activityLevel'][x]['name']=="sedentary":
                respString += "You were sedentary for " + str(resp4['activities'][0]['activityLevel'][x]['minutes']//60) + " hours and " + str(resp4['activities'][0]['activityLevel'][x]['minutes']% 60) + " miuntes. " 
            else:
                respString += "You were " + resp4['activities'][0]['activityLevel'][x]['name'] + " active for " + str(resp4['activities'][0]['activityLevel'][x]['minutes']//60) + " hours and " + str(resp4['activities'][0]['activityLevel'][x]['minutes']% 60) + " miuntes. " 

    print(respString)
get_activeness()

def get_heartrate():
    myurl5 = "https://api.fitbit.com/1/user/-/activities/heart/date/2022-08-24/1d/15min.json"
    resp5 = requests.get(myurl5, headers=myheader).json()
    lastHR = resp5['activities-heart-intraday']['dataset'][len(resp5['activities-heart-intraday']['dataset'])-1];
    print("Your most recent heart rate recorded at " + str(lastHR['time']) + " was " + str(lastHR['value']) + "BPM.")
get_heartrate()

