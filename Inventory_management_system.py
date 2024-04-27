stock = {'mazza':30,'burger':40,'vegetable':35,'icecream':30,'cake':25}
print('')
print('PRODUCT        PRICE ')
print('-------------------')
print('mazza       -  30rs ')
print('burger      -  40rs ')
print('vegetable   -  35rs ')
print('icecream    -  30rs ')
print('cake        -  25rs ')
print('-------------------')
basket = {}
while True:
      item=input("Enter The Product Name : ")
      if item in stock:
            while True:
                  try:
                        qty=int(input("Enter The Quantity : "))
                        break
                  except ValueError:
                        print("Please enter a valid quantity ")
            while qty<1:
                  print("PLEASE ENTER VALID QUANTITY : ")
                  while True:
                        try:
                              qty=int(input("Enter The Quantity : "))
                              break
                        except ValueError:
                              print("Please enter a valid quantity ")
            if item in basket:
                  basket[item]+=qty
            else:
                  basket[item]=qty
            more=(input("For adding more items press 1 \nFor exit press 2 \n: "))
            if more=='1':
                  continue
            elif more=='2':
                  break
            elif more!='1' or more!= '2' :
                  print("Press Valid Button to continue or exit (3 attempts left )")
                  more=(input("For adding more items press 1 \nFor exit press 2 \n: "))
                  if more=='1':
                        continue
                  elif more=='2':
                        break
                  elif more!='1' or more!='2':
                        print("Press Valid Button to continue or exit (2 attempts left )")
                        more=(input("For adding more items press 1 \nFor exit press 2 \n: "))

                        if more=='1':
                              continue
                        elif more=='2':
                              break
                        elif more!='1' or more!='2':
                              print("Press Valid Button to continue or exit (1 attempt left )")
                              more=(input("For adding more items press 1 \nFor exit press 2 \n: "))
      elif item not in stock:
            print("")
            print("Item not available :( \nEnter valid item name : ")
print("")
print('Items In Your Basket')
print('-------------------------------------------------------')
print('')
print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
sub_total=0
for item,qty in basket.items():
      price_per_unit=stock[item]
      total_price=qty*price_per_unit
      sub_total=sub_total+total_price
      print("",item[0:5], "      ",qty,'    ',price_per_unit,'                  ',qty*price_per_unit)
print('')
print('-------------------------------------------------------') 
print('')
print("TOTAL BASKET AMOUNT IS RS. ",sub_total)
while True:
      try:
            print("")
            print("SELECT YOUR PREFERRED PAYMENT MODE")
            payment=int(input("For cash press 1 \nFor card press 2  \nIf you want to exit PRESS any other key : "))
            break
      except ValueError:
            print("")
            print('Please enter valid payment mode')
cash=0
while payment==1:
      while True:
            try:
                  cash=int(input("Enter Amount You Have : "))
                  break
            except ValueError:
                  print("Please Enter Only Numeric Value")
      while cash<sub_total:
            print('')
            print("YOU DON'T HAVE SUFFICIENT BALANCE")
            while True:
                  try:
                        print("")
                        print("SELECT YOUR PREFERRED PAYMENT MODE")
                        payment=int(input("For re-entering cash PRESS 1 : \nFor changing mode of payment PRESS 2 : \nTo discard basket PRESS 3 : "))
                        break
                  except ValueError:
                        print("")
                        print('Please enter valid payment mode')
            if payment==1:
                  while True:
                        try:
                              cash=int(input("Enter Amount You Have : "))
                              break
                        except ValueError:
                              print("Please Enter Only Numeric Value")
            else:
                  break
      else:
            print('')
            print("")
            print('Items In Your Basket')
            print('-------------------------------------------------------')
            print('')
            print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
            print('')
            for item,qty in basket.items():
                  price_per_unit=stock[item]
                  print("",item[0:5:1], "      ",qty,'    ',price_per_unit,'                  ',qty*price_per_unit)
            print('-------------------------------------------------------')
            print("")
            print("BILL")
            print('----------------------------------------')
            print("AMOUNT PAID - ",sub_total)
            print("AMOUNT LEFT WITH YOU - ",cash-sub_total)
            print('----------------------------------------')
            print("THANKS FOR SHOPPING. HAVE A NICE DAY :) ")
            print("")
            break
while payment==3:
      print("")
      print("YOUR BASKET IS DISCARDED SUCCESSFULLY")
      break
while payment==2:
      while True:
            try:
                  card=int(input("Please Input Your 16 Digit Card No. (for ex- 1234123412341234) :: "))
                  break
            except ValueError:
                  print("Please enter only numeric values")
      while card<1000000000000000 or card>9999999999999999:
            print("PLEASE ENTER VALID CARD NO.")
            while True:
                  try:
                        card=int(input("Please Input Your 16 Digit Card No. (for ex- 1234123412341234) :: "))
                        break
                  except ValueError:
                        print("Please enter only numeric values")
      else:
            while True:
                  try:
                        exp_mon,exp_year=map(int,input("ENTER EXPIRY MONTH / ENTER EXPIRY YEAR ex-(MM/YY) : ").split('/'))
                        break
                  except ValueError:
                        print("Please enter valid details")
            while True :
                  if exp_mon<1 or exp_mon>12:
                        print("PLEASE ENTER VALID YEAR AND MONTH")
                        while True:
                              try:
                                    exp_mon,exp_year=map(int,input("ENTER EXPIRY MONTH / ENTER EXPIRY YEAR ex-(MM/YY) : ").split('/'))
                                    break
                              except ValueError:
                                    print("Please enter valid details")
                  elif exp_year<24 or exp_year>99:
                        print("PLEASE ENTER VALID YEAR AND MONTH")
                        while True:
                              try:
                                    exp_mon,exp_year=map(int,input("ENTER EXPIRY MONTH / ENTER EXPIRY YEAR ex-(MM/YY) : ").split('/'))
                                    break
                              except ValueError:
                                    print("Please enter valid details")
                  elif exp_year==24 and exp_mon<3:
                        print("PLEASE ENTER VALID YEAR AND MONTH")
                        while True:
                              try:
                                    exp_mon,exp_year=map(int,input("ENTER EXPIRY MONTH / ENTER EXPIRY YEAR ex-(MM/YY) : ").split('/'))
                                    break
                              except ValueError:
                                    print("Please enter valid details")
                  else:
                        break
      while True:
            try:
                  cvv=int(input("ENTER YOUR 3 DIGIT CVV : "))
                  break
            except ValueError:
                  print("PLEASE ENTER VALID CVV")
      while cvv<100 or cvv>999:
            print("PLEASE ENTER VALID CVV")
            while True:
                  try:
                        cvv=int(input("ENTER YOUR 3 DIGIT CVV : "))
                        break
                  except ValueError:
                        print("PLEASE ENTER VALID CVV")
      while True:
            try:
                  print("")
                  card_amt=int(input("PLEASE ENTER TOTAL AVAILABLE BALANCE IN YOUR CARD : "))
                  break
            except ValueError:
                  print("PLEASE ENTER ONLY NUMERIC VALUE")
      while card_amt<sub_total:
            print("YOU DON'T HAVE SUFFICIENT BALANCE")
            while True:
                  try:
                        print("")
                        print("SELECT YOUR PREFERRED PAYMENT MODE")
                        payment=int(input("For changing mode of payment to cash PRESS 1 : \nFor re-entering amount PRESS 2 : \nTo discard basket PRESS any other key : "))
                        break
                  except ValueError:
                        print("")
                        print('Please enter valid payment mode')

            if payment==2:
                  while True:
                        try:
                              card_amt=int(input("Enter Amount You Have : "))
                              break
                        except ValueError:
                              print("Please Enter Only Numeric Value")
                  
                  while card_amt<sub_total:
                        print("YOU DON'T HAVE SUFFICIENT BALANCE")
                        while True:
                              try:
                                    print("")
                                    print("SELECT YOUR PREFERRED PAYMENT MODE")
                                    payment=int(input("For re-entering card amount PRESS 1 : \nTo discard basket PRESS any other key : "))
                                    break
                              except ValueError:
                                    print("")
                                    print('Please enter valid payment mode')
                        if payment==1:
                              while True:
                                    try:
                                          card_amt=int(input("Enter Amount You Have : "))
                                          break
                                    except ValueError:
                                          print("Please Enter Only Numeric Value")
                        else:
                              print("")
                              print("YOUR BASKET IS DISCARDED SUCCESSFULLY")
                              break
                        break
                  else:
                        print('')
                        print("")
                        print('Items In Your Basket')
                        print('-------------------------------------------------------')
                        print('')
                        print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
                        print('')
                        for item,qty in basket.items():
                              price_per_unit=stock[item]
                              print("",item[0:5:1], "      ",qty,'    ',price_per_unit,'                  ',qty*price_per_unit)
                        print('-------------------------------------------------------')
                        print("")
                        print("BILL")
                        print('----------------------------------------')
                        print("AMOUNT PAID - ",sub_total)
                        print("AMOUNT LEFT WITH YOU - ",card_amt-sub_total)
                        print('----------------------------------------')
                        print("THANKS FOR SHOPPING. HAVE A NICE DAY :) ")
                        print("")
                        break
                  break
            elif payment==1:
                  while True:
                        try:
                              cash=int(input("Enter Amount You Have : "))
                              break
                        except ValueError:
                              print("Please Enter Only Numeric Value")
                  while cash<sub_total:
                        print("YOU DON'T HAVE SUFFICIENT BALANCE")
                        while True:
                              try:
                                    print("")
                                    print("SELECT YOUR PREFERRED PAYMENT MODE")
                                    payment=int(input("For re-entering cash PRESS 1 : \nTo discard basket PRESS any other key : "))
                                    break
                              except ValueError:
                                    print("")
                                    print('Please enter valid payment mode')
                        if payment==1:
                              while True:
                                    try:
                                          cash=int(input("Enter Amount You Have : "))
                                          break
                                    except ValueError:
                                          print("Please Enter Only Numeric Value")
                        else:
                              print("")
                              print("YOUR BASKET IS DISCARDED SUCCESSFULLY")
                              break
                        break
                  else:
                        print('')
                        print("")
                        print('Items In Your Basket')
                        print('-------------------------------------------------------')
                        print('')
                        print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
                        print('')
                        for item,qty in basket.items():
                              price_per_unit=stock[item]
                              print("",item[0:5:1], "      ",qty,'    ',price_per_unit,'                  ',qty*price_per_unit)
                        print('-------------------------------------------------------')
                        print("")
                        print("BILL")
                        print('----------------------------------------')
                        print("AMOUNT PAID - ",sub_total)
                        print("AMOUNT LEFT WITH YOU - ",cash-sub_total)
                        print('----------------------------------------')
                        print("THANKS FOR SHOPPING. HAVE A NICE DAY :) ")
                        print("")
                        payment=0
                        break
                  break
            elif payment==3:
                  print("")
                  print("YOUR BASKET IS DISCARDED SUCCESSFULLY")
                  break
            break
      else:
            print('')
            print("")
            print('Items In Your Basket')
            print('-------------------------------------------------------')
            print('')
            print(" ITEMS       QTY     PRICE(per piece)      TOTAL PRICE")
            print('')
            for item,qty in basket.items():
                  price_per_unit=stock[item]
                  print("",item[0:5:1], "      ",qty,'    ',price_per_unit,'                  ',qty*price_per_unit)
            print('-------------------------------------------------------')
            print("")
            print("BILL")
            print('----------------------------------------')
            print("AMOUNT PAID - ",sub_total)
            print("AMOUNT LEFT WITH YOU - ",card_amt-sub_total)
            print('----------------------------------------')
            print("THANKS FOR SHOPPING. HAVE A NICE DAY :) ")
            print("")
            break
else:
      print("YOUR BASKET IS DISCARDED SUCCESSFULLY")
