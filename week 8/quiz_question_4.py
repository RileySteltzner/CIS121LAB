def find_winner(p1 = "rock", p2 = "rock"):
    if (p1 == p2):
        return "tie"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return "p1 wins"
    else:
        return "p2 wins"
print(find_winner("scissors"))
    