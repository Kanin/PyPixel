import pypixel, json

# More documentation on auctions at https://github.com/HypixelDev/PublicAPI/blob/61520d7ff71d6c102bb6b526695c8fffdfd70ee1/Documentation/methods/skyblock/auctions.md
api = pypixel.HypixelAPI('KEY_HERE')

player = pypixel.Player('PROFILE_NAME', api)

# player.setMainSkyblockProfile(2) # Optional

auctions = player.getSkyblockAuctions()

option = input("Print, Save, or Exit (p/s/e)? ")
while not option in ['p', 's', 'e']:
    if option == 'p': 
        print(auctions)
    elif option == 's': 
        f = open('auctions.json', 'w+')
        f.write(json.dumps(auctions, indent=2))
        f.close
    elif option == 'e':
        break
    else:
        option = input("Print or Save (p/s)? ")