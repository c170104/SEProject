import urllib
import json

urlwCost = "https://data.gov.sg/api/action/datastore_search?resource_id=0c14ceec-da1b-43c6-92fc-e82d7219840b&limit=3000"
urlwInfo = "https://data.gov.sg/api/action/datastore_search?resource_id=4fc3fd79-64f2-4027-8d5b-ce0d7c279646&limit=1433"

def main(query, sort):
    dataWithCost = apiQuery(urlwCost + "&q=" + query)
    dataWithInfo = apiQuery(urlwInfo + "&q=" + query)

    newList = combineList(dataWithCost, dataWithInfo)
    newList = removeEmptyData(newList)

    if sort != '':
        newList = sortData(newList, sort)

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

def removeEmptyData(list1):
    for c in list1[:]:
        if not 'centre_code' in c:
            list1.remove(c)
    return list1

def sortData(list1, preference):
    if preference == 'cc':
        preference = 'centre_code'
    elif preference == 'name':
        preference = 'centre_name'
    elif preference == 'fee':
        preference = 'fees'
    elif preference == 'programme':
        preference = 'programmes_offered'
    elif preference == 'time':
        preference = 'weekday_full_day'
    else:
        preference = ''

    if preference == 'fees':
        newList = sorted(list1, key=lambda x: float(x[preference]))
    else:
        newList = sorted(list1, key=lambda x: x[preference])
    
    return newList
