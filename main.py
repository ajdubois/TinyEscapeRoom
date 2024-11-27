# Code by DUBCODdien

import time

start_time = time.time()

desk_opened = False
desk_lighter_obtained = False
carpet_key_obtained = False
candle_lit_time = 9999999999
door_checked = False
candle_key_obtained = False
candle_lit = False

def candle_burn_duration():
  return time.time() - candle_lit_time

# Clears text from the console (recovered from v0.1)
def _clear_console():
  cursorToStart = "\033[1;1H"
  returnCursor = "\033[2E"
  clearConsole = "\033[0J\033[1J" + cursorToStart
  print(clearConsole)


print("You are trapped in an escape room! It's dark but you can make out a few things...")
print("Type the number next to the item you want to check out!")
while True:
  print("1 - There is a door.")
  if not candle_lit:
    print("2 - There is an unlit candle.")
  elif not candle_key_obtained:
    print("2 - The candle is lit.")
  if not carpet_key_obtained:
    print("3 - There is a carpet on the floor.")
  if not desk_opened:
    print("4 - There is a desk.")
  elif not desk_lighter_obtained:
    print("4 - Grab the lighter.")
  users_choice = input()

  if users_choice == "cls":
    _clear_console()

  elif users_choice == "4":
    if not desk_opened:
      print("You open the desk and look inside and see a lighter.")
      desk_opened = True
    elif not desk_lighter_obtained:
      print("You grab the lighter.")
      desk_lighter_obtained = True
    print("")

  elif users_choice == "1":
    if not door_checked:
      print("There is a door here, with two keyholes.")
      door_checked = True
    elif not (carpet_key_obtained or candle_key_obtained):
      print("The door has two key holes, but you haven't got any keys...")
    elif carpet_key_obtained ^ candle_key_obtained:
      print("You put one of your keys in the door, and it fit. Just one key left.")
    elif carpet_key_obtained and candle_key_obtained:
      print("The door has been unlocked and you have escaped!\n")
      break

    print("")

  elif users_choice == "2":
    if not desk_lighter_obtained:
      print("It's a nice looking candle :D")
    elif not candle_lit:
      print("You light the candle.")
      candle_lit = True
      candle_lit_time = time.time()
    elif not candle_key_obtained and (candle_burn_duration() > 7):
      candle_key_obtained = True
      print("The candle melted and a key was in the wax. You took the key.")
    elif not candle_key_obtained and candle_lit:
      print("The candle is burning, and melting pretty quickly.")

    print("")

  elif users_choice == "3":
    if not carpet_key_obtained:
      print("You look under the carpet and find a key!")
      carpet_key_obtained = True

    print("")



# End of program
print("It took you", int(time.time() - start_time), "seconds to escape!")