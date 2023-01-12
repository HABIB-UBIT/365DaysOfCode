#####      MORE CHANGES AND OPTIMIZATION IS REQUIRED
menu_options = {"burger" : 300 , "juices" : 40 , "roll" : 180}
menu_options_list = list(menu_options)
print(menu_options_list)
menu_options_key = int(input("Enter value:"))
d = []
if menu_options_key == 0:
    print("you selected burger")
    d.append(menu_options.get("burger"))
elif menu_options_key == 1:
    print("you selected juices")
    d.append(menu_options.get("juices"))
elif menu_options_key == 2:
    print("you selected roll")
    d.append(menu_options.get("roll"))
else:
    print("thanks for shopping")
    print("your total bill is:" , sum(d))
ans = str(input("Do you want to select more :"))
if ans == "yes":
    print(menu_options_list)
    menu_options_key = int(input("Enter value:"))
    if menu_options_key == 0:
        print("you selected burger")
        d.append(menu_options.get("burger"))
        print("your total bill is:" , sum(d))
    elif menu_options_key == 1:
        print("you selected juices")
        d.append(menu_options.get("juices"))
        print("your total bill is:" , sum(d))
    elif menu_options_key == 2:
        print("you selected roll")
        d.append(menu_options.get("roll"))
        print("your total bill is:" , sum(d))
elif ans == "no":
        print("thanks for shopping")
        print("your total bill is:" , sum(d))






