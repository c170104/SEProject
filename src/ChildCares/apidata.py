import urllib
import json

urlwCost = "https://data.gov.sg/api/action/datastore_search?resource_id=0c14ceec-da1b-43c6-92fc-e82d7219840b"
urlwInfo = "https://data.gov.sg/api/action/datastore_search?resource_id=4fc3fd79-64f2-4027-8d5b-ce0d7c279646"

def main(query):
    dataWithCost = apiQuery(urlwCost + "&q=" + query)
    dataWithInfo = apiQuery(urlwInfo + "&q=" + query)

    newList = combineList(dataWithCost, dataWithInfo)
    return newList


def apiQuery(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
        response.close()
    return data['result']['records']

def combineList(list1, list2):
    for c in list1:
        for i in list2:
            if(c['\ufeffcentre_code'] == i['\ufeffcentre_code']):
                c['citizenship'] = c['remarks']
                c.update(i)
                c['centre_code'] = c['\ufeffcentre_code']
    return list1
