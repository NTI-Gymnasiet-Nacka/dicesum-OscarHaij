
def main():
    user_input = input().split(" ")
    user_input = user_input
    if int(user_input[0]) == int(user_input[1]):
        print(int(user_input[0])+1)
    else:
        if int(user_input[0]) >= int(user_input[1]):
            for i in range(int(user_input[0]) - int(user_input[1])+1):
                print(i + int(user_input[1])+1)
        else:
            for i in range(int(user_input[1]) - int(user_input[0])+1):
             print(i + int(user_input[0])+1)



if __name__ == "__main__":
    main()