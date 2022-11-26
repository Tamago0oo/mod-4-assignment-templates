'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #check if to_member is followed by from_member
    if to_member in social_graph[from_member]["following"]:
        #if follower, check if followed back
        if from_member in social_graph[to_member]["following"]:
            return "friends"
        else:
            return "follower"
    else:
        #check if from_member is followed by to_member
        if from_member in social_graph[to_member]["following"]:
            return "followed by"
        else:
            return "no relationship"

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    xWins = []
    oWins = []

    #Horizontal Clear
    for i in board:
        if "X" in i and "O" not in i and "" not in i:
            xWins.append("X Horizontal")
        if "O" in i and "X" not in i and "" not in i:
            oWins.append("O Horizontal")

    if len(xWins) == 1:
        return "X"
    if len(oWins) == 1:
        return "O"

    #Reset data
    xWins =[]
    oWins =[]

    #Vertical Clear
    currentCol = 0
    for c in board:
        #Clear currentCol
        for w in board:
            if "X" in w[currentCol]:
                xWins.append("X")
            if "O" in w[currentCol]:
                oWins.append("O")
            if len(xWins) == len(board):
                return "X"
            if len(oWins) == len(board):
                return "O"
        #Move col number up by 1
        currentCol += 1
        #Clear Data set
        xWins =[]
        oWins =[]

    xWins =[]
    oWins =[]


    currentCol = 0

    #Diagonal Win TL-BR
    for s in board:
        if "X" in s[currentCol]:
            xWins.append("X")
        if "O" in s[currentCol]: 
            oWins.append("O")
        currentCol += 1

    if len(xWins) == len(board):
        return "X"
    if len(oWins) == len(board):
        return "O"

    xWins =[]
    oWins =[]

    #Diagonal Win TR-BL
    currentCol = len(board)-1
    for s in board:
        if "X" in s[currentCol]:
            xWins.append("X")
        if "O" in s[currentCol]: 
            oWins.append("O")
        currentCol -= 1

    if len(xWins) == len(board):
        return "X"
    if len(oWins) == len(board):
        return "O"
    if len(xWins) != len(board) and len(oWins) != len(board):
        return "NO WINNER"

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    currentStop = ""
    key = 0
    timeTotal = 0
    temp = ["Filller text here","Also filler text"]
    
    if (first_stop,second_stop) in route_map:
        return route_map[(first_stop, second_stop)]["travel_time_mins"]
    else:
        while temp[1] != second_stop:
            #save current stop into a temp variable
            temp = list(legs.keys())[key]
            #if starting position is first stop
            if temp[0] == first_stop and currentStop == "":
                timeTotal += route_map[temp]["travel_time_mins"]
            #if position has passed first stop but is not at second stop
            if temp[1] != second_stop and currentStop != "":
                timeTotal += route_map[temp]["travel_time_mins"]
            if temp[1] == second_stop:
                timeTotal += route_map[temp]["travel_time_mins"]
            currentStop = temp[1]
            key += 1
        return timeTotal

