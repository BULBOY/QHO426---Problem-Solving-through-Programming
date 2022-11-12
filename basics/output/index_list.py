def movements():
    
    path = ["Move Forward",10, "Move Backward",5, "Move Left",3,"Move Right",1]
    
    for i in range(0,len(path),2):
       print(f"Move {path[i]} for {path[i+1]} steps")    


def run():
    print("Moving...")
    movements()

run()   