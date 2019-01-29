from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    mydict = players_as_dictionaries(squads_list)
    newdict = {}
    
    for players in mydict:
        group_by_position = players['position']
        newdict.setdefault(group_by_position,[])
        newdict[group_by_position].append(players)
        
    return newdict
    
