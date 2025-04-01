# Total_amt=50000
# while True:
#     print("Menu:\n1.Cheack Balance \n2.Deposite Balance \n3.Withdrae Balance \n4.Exit")
#     option= int(input("Enetr Your Choice :-"))
#     if option ==1:
#         print(f"Total Balace in your account {Total_amt}")
#     elif option == 2:
#         anmt=int(input("Enter the amount :-"))
#         Total_amt=Total_amt+  anmt  
#     elif option == 3  :
#         with1=int(input("Enter the amount :-"))
#         Total_amt=Total_amt-with1
#     elif option == 4:
#         print("You choose exist..")
#         break
#     else:
#         print("Enetr Valid option")
        
task=[]
while True:
    print("Menu:\n1.Add task \n2.View task \n3.Remove task \n4.Exit")   
    choice=int(input("Enetr the number for perform operetion :-"))
    if choice==1:
        Add_task=input("Enetr the task in list :-")
        task.append(Add_task)
    elif choice == 2:
        print("Task are as follow :")
        for i,task in enumerate(task,start=1):   
            print(f"{i}.{task}")
 
    elif choice == 3:
        Rm_task = int(input("Enter task number to remove: "))  
        if 1 <= Rm_task <= len(task):  # Check if index is valid
            task.pop(Rm_task - 1)  # Remove task based on its number
        else:
            print("Invalid task number.")
    elif choice == 4:
        print("Your choice exit...")
        break
    else:
        print("Please enter valid choice...")      

# import random
# num=random.randint(0,100)
# while True:
#     n=int(input("Guess the number :"))
#     if n>num:
#         print("your number is grater..") 
#     elif n<num:
#         print("your number is smaller..")
#     else:
#         print("Correct")         
             

                 
              
    
    