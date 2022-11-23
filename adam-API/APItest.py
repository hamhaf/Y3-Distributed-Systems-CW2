


import http.client
import time, numpy as np


n=5
results = []
for x in range(1,n+1):
    start = time.time()
    conn = http.client.HTTPConnection("127.0.0.1:8002")
    conn.request("GET",f"/team/Bundesliga")
    res = conn.getresponse()
    conn.request("POST",f"/team/add/Adamfc/Bundesliga")
    res = conn.getresponse()
    conn.request("PUT",f"/team/update/Adamfc/Adamfc/Premier%20League")
    res = conn.getresponse()
    conn.request("DELETE",f"/team/delete/Adamfc")
    res = conn.getresponse()
    end = time.time()
    elapsed = end -start
    print(x)
    results.append(elapsed)


print(f"avg = {np.mean(results)}")
print(f"std = {np.std(results)}")