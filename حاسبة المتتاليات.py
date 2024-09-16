while True:
    print("this is the Sequences calculator, choose which sequence is the one you want...\n")
    print("1.  an=a_1+(n-1)*d")
    print("2.\na1=\n an=an-1+d,  n>= ")
    choice = int(input("Pls choose a formula 1 or 2 or other modes 'type in any other number':\n"))
    if choice == 1:
        print("1.  an=a_1+(n-1)*d\n")
        a_1 = float(input("The first number in the sequence"))
        n = float(input("the number u want"))
        d = float(input("The differance rate"))
        an = a_1 + (n - 1) * d
        value_1 = an = a_1 + (n - 1) * d
        print("The answer is : " + str(value_1))
    elif choice == 2:
        print("2.\na1=\n an=an-1+d,  n>= ")
        an_1 = float(input("what is the an?"))
        d = float(input("The differance rate"))
        a_1 = float(input("The first number in the sequence"))
        n = float(input("the 'n' value 'n>= '"))
        an = (a_1) + ((an_1 - 1) * d)
        value_2 = (a_1) + ((an_1 - 1) * d)
        print("a1=" + str(a_1), "\n", "this is the number " + str(value_2), ", n>=" + str(n))
    else:
        print("Pls choose other options")
        print("Do you want to know what is the value of your number as a (n)? \n")
        answer = input("yes or no")
        if answer == "yes":
            print("1.  an=a_1+(n-1)*d")
            print("2. a1=\n an=an-1+d,  n>= ")
            choice = int(input("Pls choose a formula 1 or 2:\n"))
            if choice == 1:
                an = int(input("what is the number u want to know it's value as a (n)? \n"))
                d = float(input("The differance rate"))
                a_1 = float(input("The first number in the sequence"))
                n = (an - a_1 + d) / d
                value_3 = n = (an - a_1 + d) / d
                print("the number is " + str(value_3))
            elif choice == 2:
                an = int(input("what is the number u want to know it's value as a (n)? \n"))
                d = float(input("The differance rate"))
                a_1 = float(input("The first number in the sequence"))
                n_1 = float(input("the 'n' value 'n>= '"))
                n = (an - a_1 + d) / d
                value_4 = n = (an - a_1 + d) / d
                print("a1=" + str(a_1), "\n", "this is the number " + str(value_4), ", n>=" + str(n_1))
        else:
            print("bye")
    x = input("do u want to exit? y or n")
    if x == "y":
        break
    else:
        continue
