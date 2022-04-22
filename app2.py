import json

import requests

#Translation function, what word needs to translate
def translate(word):
    #Youdao dictionary api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    #Parameters of the transmission, where i is the content to be translated
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    #key this dictionary is the content sent to the Youdao dictionary server
    response = requests.post(url, data=key)
    #Judge whether the server is successful
    if response.status_code == 200:
        #And then the corresponding results
        return response.text
    else:
        print("Failed to call dictionary")
        #Corresponding failure returns null
        return None

def get_result(repsonse):
    #Load the returned result into JSON format through json.loads
    result = json.loads(repsonse)

    print ("results:%s" % result['translateResult'][0][0]['tgt'])

def main():
    word = input('Input:')
    list_trans = translate(word)
    get_result(list_trans)

if __name__ == '__main__':
    main()