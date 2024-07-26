import time

start_time = time.time() # save the current time
title = "the quick brown fox jumped over the lazy dog"
type = input("type \"the quick brown fox jumped over the lazy dog\" : ")

end_time = time.time() # save the current time again after the code has run

elapsed_time = end_time - start_time # calculate the elapsed time

if title == ("the quick brown fox jumped over the lazy dog"):
    print("you type correct")
    print("Elapsed time: ", elapsed_time, "seconds")
else:
    print("you type wrong word")


