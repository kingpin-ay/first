secret_number = 18
total_play_no = 2 # how many attempts you want to give user writer down the number -1
attempt = 0
user_inp = int(input('please enter your no : '))
while attempt < total_play_no :
    attempt += 1
    if user_inp == secret_number :
        print(f"you won ...! by  {(total_play_no+1)-attempt} attempts")

        break
    elif user_inp < secret_number :
        print('please chose some thing bigger than this ')

        print(f"you have only {(total_play_no+1)-attempt} attempt left....")
        user_inp = int(input('please enter your no : '))
    else :
        print('chose something smaller ')

        print(f"you have only {(total_play_no+1) -attempt} attempt  left....")
        user_inp = int(input('please enter your no : '))

if user_inp != secret_number :
    print("game over try again")