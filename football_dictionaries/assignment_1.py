def players_as_dictionaries(squads_list):
    myli = []
    for players in squads_list:
        mydict = {
            'caps': players[4],
            'club': players[5],
            'club_country': players[7],
            'country': players[6],
            'date_of_birth': players[3],
            'name': players[2],
            'number': players[0],
            'position': players[1],
            'year': players[8]
        }
        myli.append(mydict)
        
    print(myli)
    return myli
