import random;
hotel_sachin=True;
while hotel_sachin:   
   print("Welcome to **$achin's hotel**.\nI am your hotel guide.Use me for your quries.\nplease select an option to proceed.");
   print("1) Query for hotel rooms\t2) Want some food orders\n3) Any Thing Else!!");
   print("4) Exit!!")
   print("select your option using number keyboard",end=':')
   n=int(input());
   hotel_no=random.randint(100,500);

   if n==1:
      print("Thanks for choosing this.Please provide your details");
      name=input("Enter your full name:");
      phone_no=int(input("Please enter your phone number:"));
      print("Thanku so much.\nWhich type of room you want?");
      print("1) luxery\t2) Normal");
      n1=int(input("Please select your option:"));
      if n1==1:
          print("Prize for luxery room is 5000 rupees with all fetures and prize for normal room is 3000 rupees with some features.Do you want to continue");
          print("1) Yes\tOR 2) NO");
          n2=int(input('Please select your option:'));
          if n2==1:
             print(f"Thank you {name}.Have a nice day.");
             print(f"Your room prize is 5000 rupees and your room number is {hotel_no}");
          elif n2==2:
             print("1) luxery\t2) Normal");
             n3=int(input("Please select your option again:"));
             if n3==1:
                print(f"Thank you {name}.Have a nice day.");
                print(f"Your room prize is 5000 rupees and your room number is {hotel_no}");
             elif n3==2:
                print(f"Thank you {name}.Have a nice day.");
                print(f"Your room prize is 3000 rupees and your room number is {hotel_no}\n");
      elif n1==2:
          print("Prize for Normal room is 3000 rupees with some fetures and prize for luxery room is 5000 with all fetures.Do you want to continue");
          print("1) Yes\tOR 2) No");
          n4=int(input('Please select your option:'));
          if n4==1:
              print(f"Thank you {name}.Have a nice day.");
              print(f"Your room prize is 3000 rupees and your room number is {hotel_no}\n");
          elif n4==2:
              print("1) luxery\t2) Normal");
              n5=int(input("Please select your option again:"));
              if n5==1:
                  print(f"Thank you {name}.Have a nice day.");
                  print(f"Your room prize is 5000 rupees and your room number is {hotel_no}\n");
              elif n5==2:
                  print(f"Thank you {name}.Have a nice day.");
                  print(f"Your room prize is 3000 rupees and your room number is {hotel_no}\n"); 
   elif n==2:
       print("Thanks for choosing this.You can check our menu.");
       print("\t\ta.***Sandwich varieties***");
       print("1) Sada Sandwhich-40rs/-\t2) Toast Sandwhich-50rs/-\n3) Grilled Sandwhich-60rs/-\t4) Chiken Sandwhich-80rs/-");
       print("\t\tb.***Thali varieties***");
       print("1) Sada Thali-150rs/-\t2) Jain Thali-250rs/-\n3) Punjabi roti and bhaji with extra cheese-360rs/-\n4) Chiken tandoori roti with gravy chicken-580rs/-");
       print("\t\tc.***soup varieties***");
       print("1) Veg Manchow Soup-70rs/-\t2)Palak Soup-60rs/-\n3)Mushroom Cream Soup-70rs/-\tNoodle Soup-60rs/-");
       print("\t\td.***Tnadoori Starter varieties***");
       print("1) Aloo Tikka-70rs/-\t2) Gobhi Tikka-80rs/-\t3) Mushroom Tikka-90rs/-\n4) Paneer Tikka-120rs/-\t5) Paneer Kalamiri Kebab-130rs/-\n6) Veg Seekh Kebab-100rs/-\t7) Veg Tandoori Lollypop-100rs/-");

       a1=input("Please first select your variety as a or b or c or d using word keyboard:");
       if a1=='a':
           a2=int(input("Now select your sandwhich options using number keyboard:"));
       elif a1=='b':
           a2=int(input("Now select your Thali options using number keyboard:"));
       elif a1=='c':
           a2=int(input("Now select your Soup options using number keyboard:"));
       elif a1=='d':
           a2=int(input("Now select your Tandoori Starter options using number keyboard:"));
       print("Thanku for your order.\nYou will receive your order soon.You can sit and wait.");    

   elif n==3:
       print("you can ask at analog counter which is front of this cabin.\n");
   elif n==4:
       hotel_sachin=False;
   else:
       print("Something went wrong.Pleae choose valid option.") 
        
    
          
    
        
        
    

