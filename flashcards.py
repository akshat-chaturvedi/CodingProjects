keyWords = {
    "Short Serve": "ball bounces in front of or on second solid line of the service area",
    "Long Serve": "ball carries to back wall before bouncing.",
    "Three Wall Serve": "any served ball that first hits the front wall and on the rebound, strikes both side walls before bouncing",
    "Foot Fault": "player steps over the service lines during service",
    "Out of Court Serve": "any served ball that first hits the front wall and before striking the floor, goes out of the court",
    "Screen Serve": "a served ball that first hits the front wall and on the rebound passes so closely to the server that it prevents the receiver from having a clear view of the ball",
    "Ace Serve": "Serve of any type that goes untouched by the receiver",
    "Drive Serve": "Low, fast, powerful serve into either rear corner",
    "Lob Serve": "High, slow, wall-hugging serve into rear corners. Often used as second serve",
    "High Lob Z": "High, slow front wall to side wall combination that makes a 'Z' pattern as it approaches the receiver.",
    "Z-Serve": "Front wall to side wall combination that makes a 'Z' pattern as it approaches the receiver. May be hit with power or softly, depending on the desired effect.",
    "Rally": "Each legal return after the serve.",
    "Skip Shot": "Ball hits the floor before reaching the front wall.",
    "Kill Shot": "Ball hits the front wall 3 inches or lower and is unreturnable by opponent.",
    "Pinch Shot": "Side wall to front wall combination shot into either front corner 6 inches or lower.",
    "Rollout Shot": "An irretrievable shot, when the ball strikes so low on the front wall that it rolls rather than bounces back.",
    "Court hinder": "play stops when a ball strikes any part of the court that was designated as a court hinder or when the ball takes an abnormal bounce off a rough or irregular surface.",
    "What are the 6 kinds of faults": "short, long, 3 wall, foot, out of court, screen"}

for item in keyWords:
    print(item)
    moveForward = input("Press enter to reveal answer")
    if moveForward == '':
        print(keyWords[item] + "\n")
    else:
        break

