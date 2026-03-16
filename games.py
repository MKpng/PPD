import csv
import random

'''def _get_sample(size=20):
    """cria um sample .csv file do valor default = 20
        através do file steam_games.csv"""
        
    my_dict = []
    with open('steam_games.csv', newline='', encoding='utf-8') as f:
        r = csv.reader(f)
        header = next(r)
        for i in r:
            my_dict.append(i)

    rand_pos = [random.randint(0, len(my_dict) - 1) for _ in range(size)]

    with open('sample_games.csv', 'w', newline='', encoding='utf-8') as w:
        writer = csv.writer(w)
        writer.writerow(header)
        for i in rand_pos:
            writer.writerow(my_dict[i])'''

def _get_dict(arq):
    """arq is expected to be a .csv file"""

    with open(arq, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        # Criando dicionário com as colunas a serem usadas por otimização.
        my_dict = {'years': {}}

        for i in reader:
            # adiciona mais 1 à key years[ano] sempre que o ano aparece no dataset.
            try:
                my_dict['years'][i[2][-4:]] += 1
            except KeyError:
                my_dict['years'][i[2][-4:]] = 1

            # jogos gratis/pagos, free_players/paid_player
            try:
                if i[6] == "0.0":
                    my_dict['free'] += 1
                    my_dict['free_players'] += int(i[4])
                else:
                    my_dict['paid'] += 1
                    my_dict['paid_players'] += int(i[4])

            except KeyError:
                if i[6] == "0.0":
                    my_dict['free'] = 1
                    my_dict['free_players'] = int(i[4])
                else:
                    my_dict['paid'] = 1
                    my_dict['paid_players'] = int(i[4])

        #total_num_players, total_jogos
        my_dict['player_count'] = my_dict['paid_players'] + my_dict['free_players']
        my_dict['game_count'] = my_dict['paid'] + my_dict['free']

    return my_dict

class Game:
    """Game class accepts only one required parameter (file).
        This parameter is expected to be a .csv file,
        Instancing this class (e.g: my_game = Game())
        will give you all questions within this class,
        there is no point on calling any method or variable."""

    def __init__(self, file):
        self._my_dict = _get_dict(file)
        self._years = self._get_year_games()
        self._question_one()
        self._question_two()
        self._question_three()

    def _get_year_games(self):
        more_games = 0  # more_games checa qual key em years tem o valor mais alto
        year_games = []  # salva um set com o a key years (ano(s)) e seu valor (more_games)

        for k, v in self._my_dict['years'].items():
            if v >= more_games:
                if v == more_games:
                    more_games = v
                    year_games.append(k)
                else:
                    year_games = []
                    more_games = v
                    year_games.append(k)
        year_games.append(more_games)

        return year_games

    def _question_one(self):
        one = '\n[1] Qual o percentual de jogos gratuitos e pagos na plataforma?\n\n'
        a = f"Total de jogos = {self._my_dict["game_count"]} [100%]\n"
        b = f"Total de jogos pagos = {self._my_dict['paid']} [{self._my_dict['paid'] * 100 / self._my_dict['game_count']:.2f}%]\n"
        c = f"Total de jogos grátis = {self._my_dict['free']} [{self._my_dict['free'] * 100 / self._my_dict['game_count']:.2f}%]"
        return print(f"{one}{a}{b}{c}")

    def _question_two(self):
        two = '[2] Qual o ano com o maior número de novos jogos?\n\n'
        return print(f"\n{two}{', '.join(i for i in self._years[:-1])} foi(foram) o(s) ano(s) com mais lançamentos com {self._years[-1]} jogos!")

    def _question_three(self):
        three = '\n[3] Qual o total de jogadores em jogos grátis e pagos?\n\n'
        a = f"Dentro deste dataset o número máximo de usuários simultâneos entre todos os jogos é {self._my_dict["player_count"]} jogadores.\n"
        b = f"De todos esses jogadores:\n\n"
        c = f"  {self._my_dict["paid_players"]} [{self._my_dict['paid_players'] * 100 / self._my_dict['player_count']:.2f}%] jogam em jogos pagos\n"
        d = f"  {self._my_dict["free_players"]} [{self._my_dict['free_players'] * 100 / self._my_dict['player_count']:.2f}%] jogam em jogos grátis"
        return print(f"{three}{a}{b}{c}{d}")

#_get_sample()