# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# my_str = 'автомобиль, компьютерабв, самокат, ручкаабв'
# my_str = my_str.split(' ')

# res = ''
# for word in my_str:
#     if word.find('абв') == -1:
#         res += word + ''

# print(res)



# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# count_of_candys = int(input('введите количество конфет: '))
# gamer_1, gamer_2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
# current_gamer = gamer_1
# while count_of_candys > 0:
#     print('количество оставшихся конфет: {}'.format(count_of_candys))
#     while True:
#         number_to_delete = int(input('ход игрока {} (1 - 3): '.format(current_gamer)))
#         if number_to_delete >= 1 and number_to_delete <= 3:
#             break
#     count_of_candys -= number_to_delete
#     current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

# print('Победил {}'.format(current_gamer))




# Создайте программу для игры в "Крестики-нолики".

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def encode(s):
 
#     encoding = ""
 
#     i = 0
#     while i < len(s):
#         count = 1
 
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
 
#         encoding += str(count) + s[i]
#         i = i + 1
 
#     return encoding
 
# if __name__ == '__main__':
 
#     s = open('enter.txt', 'r+')
#     s.write(encode(s.readline())) 
#     print(encode(s.readline()))






