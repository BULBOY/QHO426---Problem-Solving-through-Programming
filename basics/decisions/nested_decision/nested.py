book_type = str(input("What type of cover does the book have?\n"))
if (book_type == "soft"):
    bound = str(input("\nIs the book perfect-bound?\n"))
    if (bound == "yes"):
        print("\nSoft cover, perfect bound books are very popular!")
    else:
        print("\nSoft covers with coils or stitches are great for short books")
else:
   print("\nBooks with hard covers can be more expensive!")        