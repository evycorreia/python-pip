import random
round=1
com_wins=0
user_wins=0

while True:
  print('*'*10)
  print(' ROUND ',round)
  print('*'*10)
  options= ('piedra','papel','tijera')
  print('')
  user_option = input ('piedra, papel, o tijera: ')
  user_option= user_option.lower()
  computer_option = random.choice(options)
    
  if not user_option in options:
    print('opcion no valida')
  else:
    print('user option: ',user_option)
    print('computer option: ', computer_option)
    round+=1
  
  if user_option == computer_option: 
    print('empate')
    print('')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera, user gana')
      print('')
      user_wins+=1
    else:
      print ('papel gana a piedra, computer gano')
      print('')
      com_wins+=1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print ('papel gana a piedra, user gana')
      print('')
      user_wins+=1
    else:
      print('tijera gana a papel, computer gana')
      print('')
      com_wins+=1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel, user gana')
      print('')
      user_wins+=1
    else:
      print('piedra gana a tijera, computer gana')
      print('')
      com_wins+=1

  print('puntos del user: ', user_wins)
  print('puntos de la computadora: ',com_wins)
  print('')
  if user_wins==3:
    print('User gana el juego')
    break
  elif com_wins==3:
    print('Computer gana el juego')
    break

  
