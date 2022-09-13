def ask_for_int():
    while True:
        try:
            result = int(input("enter a number："))
        except ValueError as ve:
            print(ve)
            print("enter again!")
        except:
            print("enter again!")
        else:
            print("no error detected")
            return result
        finally:
            print("finally will alwasy run!!")


ask_for_int()

# result = int(input("enter a number"))
