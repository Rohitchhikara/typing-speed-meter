import time

main_line = ["the quick brown fox jumped over the lazy dog"]
def heading():
    print("\n---------typeing test -------- \n ", main_line)
    print("you have to type this line above ^ and press enter")
    heaing_input = input("`y` to start , `q` to quit , 'e' to change line : ")
    if heaing_input == "y":
        print("start in 3 sec")
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        metying()  # corrected function name
    if heaing_input == "q":
        exit()

    if heaing_input == 'e':
        line = input("enter the line you want to set: ")
        if line != "":
            main_line[0] = line
        heading()
    else:
        print("no option found")
        heading()


def metying():
    start_time = time.time()  # save the current time
    print(main_line)
    type = input(": ")
    end_time = time.time()  # save the current time again after the code has run
    elapsed_time = end_time - start_time  # calculate the elapsed time
    if type == main_line[0]:  # corrected indexing
        print("you type correct")
        print("Elapsed time: ", elapsed_time, "seconds")
        heading()
    else:
        print("you type wrong word")
        heading()

heading()
def exit():
    pass
