import random

print(
  """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
**What would you like to order?**
***********************************
  """
)
snake_menu ={'Wings':0,'Cookies':0,'Spring Rolls':0,'Salmon':0
 ,'Steak':0,'Meat Tornado':0 ,'A Literal Garden':0,'Ice Cream':0 ,'Cake':0,'Pie':0,'Coffee':0,'Tea':0,'Unicorn Tears':0}

order=set([])
user=input('> ').title()
while user :
  if user in snake_menu:
     snake_menu[user]+=1
     print(f'\n** {snake_menu[user]} order of {user} have been added to your meal **')
     order.add(user)
     
  elif user.lower()=='quit':
        if len(order)>0:
          print(f'\nyour complete order are : ')
          totally=0
          for item in order:
            print(f'{snake_menu[item]} of {item}')
            totally+=snake_menu[item]
        print(f'Totally order\'s are {totally}')    
        break
  else:
    print(f'\nSORRY,your order {user} not on the menu. please reOrder depend on what exist.\n i suggest on you "{random.choice(list(snake_menu.keys()))}" ;it\'s so Delicious') 

  print('\n***********************************')

  user=input('> ').title()
 
