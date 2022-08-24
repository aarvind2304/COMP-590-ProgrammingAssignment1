import requests, json
myheader = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRUTkiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNjYxMzUwODMzLCJpYXQiOjE2NjA3NDYwMzN9.-6KKpR38nXavOTwsBrJBKuMQD3thwGeFDguLTMiOPM0"}
myurl = "https://api.fitbit.com/1/user/-/br/date/2022-08-17.json"
resp = requests.get(myurl, headers=myheader).json()
print(resp)
