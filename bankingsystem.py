print("*"*20)

personNames=['Ramu','kiran','sagar','sachin','sreekanth','jaga']
personPins=['0123','4569','7894','4561','2589','3698']
personBalance=[15000,20000,30000,40000,50000,60000]
deposition=0
withdrawel=0
balance=0
counter_1=1
counter_2=6
i=0

# this statement below helps the programe to run continusly.
while True:
    # os.system("cls")

 print("==========================================")
 print("******WELCOME TO KIRAN BANK===============")
 print("******************************************")
 print("=<< 1. Open a new account              >>=")   
 print("=<< 2. Withdrawel money                >>=")
 print("=<< 3. Deposite money                  >>=")
 print("=<< 4.  Exit/Quit                      >>=")
 print("******************************************")
 # the below statement takes the choice number from the user.
 choiseNumber=input("select your choice number from the above menu: ")
 if choiseNumber== "1":
     print("choice number 1 is selected by the customer")
     # the line below will take the no:of customers from the users
     Noc=eval(input("Number of customers:"))

     i=i +Noc
     # the if condition will restrict the number of new account 
     if i> 5:
        print("\n")
        print("customers registrataion exceed reached or customer registration too low")
        i=i-Noc
     else:
          # the while loop will run according to the no:of customer
          while counter_1 <=i:
             # these few lines will take information from customer
             name=input("Input Fullname:")
             personNames.append(name)
             pin=str(input("please input a pin of your choice: "))
             personPins.append(pin)
             balance=0
             deposition=eval(input("please input a value deposite to start an account:"))
             balance=balance+deposition
             personBalance.append(balance)
             print("\nname=",end="")
             print(personNames[counter_2])
             print("pin=",end="")
             print(personPins[counter_2])
             print(personBalance[counter_2],end="")
             print("-/Rs")
             counter_1=counter_1+1
             counter_2=counter_2+1
             print("\n yours name is added to customers system")
             print(" your pin is added to customer system")
             print("your balance is added to customers system")
             print("-----New account created successfully !-------")
             print("\n")
             print("your name is available on the customers list now :")
             print(personNames)
             print("\n")
             print("Note! please remember the name and pin")
             print("=========================================")
           # this statement  below helps the user to go back to the start 
     mainmenu=input(" choice number 2 is selected by the customer:")
 elif choiseNumber=="2":
    j=0
    print("choice number 2 is selected by the customer")
    # this while loop will prevent the user using the account
    while j<1:
       k=-1
       name=input("please input name:")
       pin=input("please input pin:")
       # this while loop will keep the function running running when variable k is smaller than length
       # personNames list.
       while k<len(personNames)-1:
          k=k+1
          # these two if condition find where both the 
          if name== personNames[k]:
             if pin== personPins[k]:
                j=j+1
                # these few statements would show the balance
                print("your current balance:",end="")
                print(personBalance[k],end="")
                print("-/Rs\n")
                balance=(personBalance[k])
                # statement below would take the amount withdraw from user.
                withdrawel=eval(input(" Input value to withdraw:"))
                   # the if condition below would look whether  is gre
                if withdrawel> balance:
                    deposition=eval(input("please deposite a higher value because your balance mentioned above is not enough: "))
                    balance=balance+deposition
                    print("your current balnce:",end="")
                    print(balance,end="")
                    print("-/Rs\n")
                    balance=balance-withdrawel
                    print("-\n")
                    print("-------withdrwel successfully------") 
                    personBalance[k]=balance
                    print("your new balance:",balance,end="")
                    print("-/Rs\n\n")
                else:

                   balance=balance-withdrawel
                   print("\n")
                   print("-------withdrawel successfull!-----")
                   personBalance[k]=balance
                   print("your new balance:",balance,end="")
                   print("/Rs\n\n")

    if j<1:
       
       print("your na,e and pin does not match!\n")
       break
    mainmenu=input("please press enter key to go back to main menu:")
 elif choiseNumber=="3":
      print(" choice number 3 is selected by the customer")
      n=0

      while n<1:
         k=-1
         name=input("please input name:")
         pin=input("please input pin:")

         while k< len(personNames)-1:
            k=k+1

            if name==personNames[k]:
               if pin==personPins[k]:
                  n=n+1

                  print("your current balnace:",end="")
                  print(personBalance[k],end="")
                  print("-/Rs")
                  balance=(personBalance[k])

                  deposition=eval(input("enter the value you want to deposition: "))
                  balance=balance+deposition
                  personBalance[k]=balance
                  print("\n")
                  print("-----Deposition successfull!----")
                  print("your new balance:",balance,end="")
                  print("-Rs\n\n")
         if n<1:
            print("your name and pin does not match!\n")
            break
      mainmenu=input("please press enter key to go back to main menu:")
 elif choiseNumber=="4":
    print("choice number 4 is selected by customer")
    k=0
    print("customer name list and balnce mentioned below:")
    print("\n")

    while k<=len(personNames)-1:
       print("->.person=",personNames[k])
       print("->.balance=",personBalance[k],end="")
       print("-/Rs")
       print("\n")
       k=k+1

       mainmenu=input("please press enter key to go back main menu:")
 elif choiseNumber=="5":

    print("choice number 5 is selected by the customer")
    print("Thank you for using our banking system!")
    print("\n")
    print("come again")
    print("bye bye")
    break
 else:

    print("Invalid option selected by the customer")
    print("please Try again")
    mainmenu=input("please press enter key to go back to main menu:")
        


               

         
   



                        
            
