import requests
import pandas as pd


uri = "https://api.spotify.com/v1/"

testTrack = "1yjY7rpaAQvKwpdUliHx0d?si=d9efa56e28844bb6"

headers = {
    "access_token": "BQAQS4dDCsMrsa7fEy61L-AXOSuNkvCE8rOZoADz77bebRSF5rN1w4iBuGFRJq629dId7Fi9laHkdaet3PUzMVCPZ1mGNqI5Ybmv3RbKWbq49N3voEE",
	"token_type": "Bearer",
}

def getTrack(track):
    response = requests.get(uri + "tracks/" + track, headers)
    return response

# def flattenjson(b, delim):
#     val = {}
#     for i in b.keys():
#         if isinstance(b[i], dict):
#             get = flattenjson(b[i], delim)
#             for j in get.keys():
#                 val[i + delim + j] = get[j]
#         else:
#             val[i] = b[i]
            
#     return val


# data = flattenjson(getTrack(testTrack).json(), '_')

# input = map(lambda x: flattenjson( x, "_" ), data)

# columns = [x for row in input for x in row.keys()]
# columns = list(set(columns))

# with open(fname, 'wb') as out_file:
#     csv_w = csv.writer(out_file)
#     csv_w.writerow(columns)

#     for i_r in input:
#         csv_w.writerow(map(lambda x: i_r.get(x, ""), columns))

data = getTrack(testTrack).json()

df = pd.json_normalize(data)

df.to_csv('output.csv', index=False, encoding='utf-8')