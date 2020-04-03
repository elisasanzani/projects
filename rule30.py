# Rule 30
"""

stato_iniziale = '0000000000000000000001000000000000000000000'
darwin = {"111": '0', "110": '0', "101": '0', "000": '0',
        "100": '1', "011": '1', "010": '1', "001": '1'}

#This function separates my state in triplets that have 2 elements in common
def slot(statoa): 
   for indice in range(len(statoa) - 2):
        yield statoa[indice:indice + 3]        

#rule è una dict
#terzetti è una list
        
def evolvi(stato):
    for linee in range(25):
        print(stato)
        terzetti = slot(stato)
        stato = ''.join(darwin[terzetto] for terzetto in terzetti)
        stato = '0{}0'.format(stato)
    print(stato)
    
evolvi(stato_iniziale)

"""  
    
 

stato_iniziale = '...............................0...............................'
darwin = {"000": '.', "00.": '.', "0.0": '.', "...": '.',
        "0..": '0', ".00": '0', ".0.": '0', "..0": '0'}

#This function separates my state in triplets that have 2 elements in common
def slot(statoa): 
   for indice in range(len(statoa) - 2):
        yield statoa[indice:indice + 3]        

#rule è una dict
#terzetti è una list
        
def evolvi(stato):
    for linee in range(30):
        print(stato)
        terzetti = slot(stato)
        stato = ''.join(darwin[terzetto] for terzetto in terzetti)
        stato = '.{}.'.format(stato)
    print(stato)
    
evolvi(stato_iniziale)

        


