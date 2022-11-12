def directions():
    dierection  = ["Move Forward", "Move Backward", "Turn Left","Turn Right"]
    return dierection

def menu():
    print("Please select a direction:")
    a = directions()
    for i in range(len(a)):
        print(f"{i}: {a[i]}")
        
def run():
    menu()
    
run()    