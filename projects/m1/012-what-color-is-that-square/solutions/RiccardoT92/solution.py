'''Positions on a chess board are identified by a letter and a number. 
The letter identifies the column, while the number identifies the row, as shown below:

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5b/Chess-board-with-letters_nevit_111.svg" />

Write a program that reads a position from the user. 
Use an if statement to determine if the column begins with a black square or a white square. 
Then use modular arithmetic to report the color of the square in that row. 
For example, if the user enters a1 then your program should report that the square is black. 
If the user enters d5 then your program should report that the square is white. 
Your program may assume that a valid position will always be entered. 
It does not need to perform any error checking.'''

#inizializzo il tipo di coordinata e la trasformo in stringa per poterla indicizzare
coordinate=str(input("quale coordinata scrivere: "))
#attraverso if ed elif controllo se la colonna è pari o dispari e in base a quello scelgo il colore
if coordinate[0]=="a" and int(coordinate[1]) % 2 == 0:
    print("la casella è bianca")
elif coordinate[0]=="a" and int(coordinate[1]) % 2 == 1:
    print("la casella è nera")    
if coordinate[0]=="b" and int(coordinate[1]) % 2 == 0:
    print("la casella è nera")
elif coordinate[0]=="b" and int(coordinate[1]) % 2 == 1:
    print("la casella è bianca")     
if coordinate[0]=="c" and int(coordinate[1]) % 2 == 0:
    print("la casella è bianca")
elif coordinate[0]=="c" and int(coordinate[1]) % 2 == 1:
    print("la casella è nera")
if coordinate[0]=="d" and int(coordinate[1]) % 2 == 0:
    print("la casella è nera")
elif coordinate[0]=="d" and int(coordinate[1]) % 2 == 1:
    print("la casella è bianca") 
if coordinate[0]=="e" and int(coordinate[1]) % 2 == 0:
    print("la casella è bianca")
elif coordinate[0]=="e" and int(coordinate[1]) % 2 == 1:
    print("la casella è nera")
if coordinate[0]=="f" and int(coordinate[1]) % 2 == 0:
    print("la casella è nera")
elif coordinate[0]=="f" and int(coordinate[1]) % 2 == 1:
    print("la casella è bianca")
if coordinate[0]=="g" and int(coordinate[1]) % 2 == 0:
    print("la casella è bianca")
elif coordinate[0]=="g" and int(coordinate[1]) % 2 == 1:
    print("la casella è nera")
if coordinate[0]=="h" and int(coordinate[1]) % 2 == 0:
    print("la casella è nera")
elif coordinate[0]=="h" and int(coordinate[1]) % 2 == 1:
    print("la casella è bianca") 
else:
    print("errore coordinata")
