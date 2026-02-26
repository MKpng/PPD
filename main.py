import csv

with open('steam_games.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    my_dict = {}
    # count = -1 #starting from -1 so we dont count the headers
    # free_games = 0
    # paid_games = -1
    more_realeses = 0
    year_games = []
    for i in reader:
        print(i)
        break
    for i in reader:
        try:
            my_dict[i[2][-4:]] += 1
        except KeyError:
            my_dict[i[2][-4:]] = 1
    for k, v in my_dict.items():
        if v >= more_realeses:
            year_games = []
            more_realeses = v
            year_games.append((k, v))
    print(more_realeses)
    print(year_games)

    # for i in reader:
    # count += 1
    ##if i[6] == "0.0":
    #  free_games += 1
    # else:
    #   paid_games += 1

    # print(f"Total games = {count}\nFree games = {free_games}\nPercentage of Free games = {free_games * 100 / count:.2f}%")
# print(f"\nTotal games = {count}\nPaid games = {paid_games}\nPercentage of Paid games = {paid_games * 100 / count:.2f}%")
