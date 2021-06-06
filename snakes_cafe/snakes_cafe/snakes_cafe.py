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

snake_menu=('Wings','Cookies','Spring Rolls','Salmon' ,'Steak','Meat Tornado'
'A Literal Garden','Ice Cream' ,'Cake','Pie','Coffee','Tea','Unicorn Tears')
order=[]
user=input().lower().capitalize()
count=1
while user :
  if user in snake_menu:
     print(f'\n** {count} order of {user} have been added to your meal **')
     count+=1
     order.append(user)
  elif user.lower()=='> quit':
        if len(order)>0:
          string_order=', '.join(order)
          print(f'\n your complete order are " {string_order} "')
        break
  else:
    print(f'\nSORRY,your order not on the menu. please reOrder depend on what exist.\n i suggest on you "{random.choice(snake_menu)}" ;it\'s so Delicious') 

  print('\n***********************************')

  user=input().lower().capitalize()
 
