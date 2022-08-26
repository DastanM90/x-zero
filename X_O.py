print("*" * 5, " Игра Крестики-нолики ", "*" * 5)

pole = list(range(1,10))


def draw_pole(pole):
   print("-" * 13)
   for i in range(3):
      print("|", pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3], "|")
      print("-" * 13)


def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(pole[player_answer-1]) not in "XO"):
            pole[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(pole):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if pole[each[0]] == pole[each[1]] == pole[each[2]]:
          return pole[each[0]]
   return False


def main(pole):
    counter = 0
    win = False
    while not win:
        draw_pole(pole)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(pole)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_pole(pole)


main(pole)

input("Нажмите Enter для выхода!")