x = int(input("Podaj punkt x: "))
y = int(input("Podaj punkt y: "))

if ( x > 0 and y > 0 ):
    print("Punkt P({},{}) znajduje się w pierwszej ćwiartce układu współrzędnych".format(x,y))
    
if ( x < 0 and y > 0 ):
    print("Punkt P({},{}) znajduje się w drugiej ćwiartce układu współrzędnych".format(x,y))
    
if ( x > 0 and y < 0 ):
    print("Punkt P({},{}) znajduje się w czwartej ćwiartce układu współrzędnych".format(x,y))
    
if ( x < 0 and y < 0 ):
    print("Punkt P({},{}) znajduje się w trzeciej ćwiartce układu współrzędnych".format(x,y))
    
if ( (x > 0 or x < 0) and y == 0 ):
    print("Punkt P({},{}) znajduje się na osi OX".format(x,y))
    
if ( x == 0 and ( y > 0 or y < 0 ) ):
    print("Punkt P({},{}) znajduje się na osi OY".format(x,y))
    
if ( x == 0 and y == 0 ):
    print("Punkt P({},{}) znajduje się w początku układu współrzędnych".format(x,y))