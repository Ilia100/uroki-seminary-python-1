# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

n = int(input("Введите общее количество журавликов: "))


petyaSeroja=n//4
katya=n-petyaSeroja*2


print(f"Петя сделал {petyaSeroja} журавлей, Катя сделала {katya} журавлей, Сережа сделал {petyaSeroja} журавлей")