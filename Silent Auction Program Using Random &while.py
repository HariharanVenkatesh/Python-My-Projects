#Project no 5 - Silent Auction Program

import os
print(">>>>>Welcome to the Silent Auction Program<<<<<")  
def Find_Winner(Bidders_Details):
    Highest_Bid = 0
    Winner = ""
    for Bidder in Bidders_Details:
        Bidding_Price = Bidders_Details[Bidder]
        if Bidding_Price > Highest_Bid:
            Highest_Bid = Bidding_Price
            Winner = Bidder
    print(f"Here is the list of all the bidders : {Bidders_Details}")        
    print(f"The Winner is {Winner} with Bid Price of {Highest_Bid} ")

Bidders_Data = {}
End_of_Bidding = False
while not End_of_Bidding:
    Name = input("What is your Name?: ")
    Bid_Price = int(input("What is your Bid Price?: "))
    Bidders_Data[Name] = Bid_Price
    More_Bidders = input("Are There more Bidders? Type 'yes' or 'no' : ").lower()
    if More_Bidders == 'no':
        End_of_Bidding = True
        Find_Winner(Bidders_Data)
    elif More_Bidders == 'yes':
        os.system('cls')
