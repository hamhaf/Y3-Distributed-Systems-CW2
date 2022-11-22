
import time, numpy as np
import http.client, json

def externalAPI():
    try:
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "7070e4c98d8ff888e50ff23ce14d6c4c"
            }
        conn.request("GET", f"/teams?name=Chelsea", headers=headers)

        res = conn.getresponse()
        data = res.read()
        #print(data.decode("utf-8"))
        #data = json.loads(res.read().decode("utf-8"))
        
        #print(data)
    except:
        data = {'response':[{'team':"no response"}]}
        print("error in teamInfo")



n=1000
results = []
for x in range(1,n+1):
    start = time.time()
    externalAPI()
    end = time.time()
    elapsed = end -start
    print(x)
    results.append(elapsed)


print(f"avg = {np.mean(results)}")
print(f"std = {np.std(results)}")

