import requests
import json

#add your keys/tokens below
apikey = ""
secretkey = ""
bearertoken = ""

headers = {
    'Authorization': f"Bearer {bearertoken}",
}
params = (
    ('max_results', '15'),
    ('user.fields', 'description')
)

ids = [
    #format for adding new accounts:
    #['TWITTER_HANDLE', 'TWITTER_ID']
    #first parentheses is twitter handle (must be correct), next is twitter ID (must be correct)
    #get twitter ID here https://tweeterid.com/

    #private accounts will break the script
    
    
    ['@ceazor7', '1290239278413262848'],
    ['@larry0x', '1134151355776585729'],
    # ['@Cryptoyieldinfo', '1241561583450390528'], //not working? because his account is locked?
    ['@noahseidman', '38810696'],
    ["@billybogbaghold", "971741153530757120"],
    ["@korpi87", "2375428142"],
    ['@sourcex', '1365181321073451009'],
    # ['@cryptoexpert101', '951353538851950594'],
    # ['@degencryptoinfo', '1313895595292139523'],
    # ['@TheShual', '1334586569076903937'],
    # ['@DCF GOD', '1350996311777161219'],
    # ['@rektdiomedes', '1470955425084235780'], 
    # ['@305_capital', '1451221504973316107'],
    # ['@daman_n_diu', '3581663354'], 
    # ['@18decimals', '947156434340298752']
    ]



for i in ids:
    emptyDict = {}
    response = requests.get(
        f"https://api.twitter.com/2/users/{i[1]}/following", headers=headers, params=params)
    
    print(response)
    getUserName = requests.get(
        f"https://api.twitter.com/2/users/{i[1]}", headers=headers)

    response = response.json()['data']

    for account in response:
        account['url'] = f"twitter.com/{account['username']}"

    dump = json.dumps(response, indent=2)

    print('Twitter Account: ' + i[0])
    print(dump)
    print("********************")
    print("NEXT ACCOUNT......")
    print("********************")



