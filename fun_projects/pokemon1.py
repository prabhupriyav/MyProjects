

class pokemon():

    def __init__(self):
        self.identifier = 0
        self.end_point_pkm = []
        self.abl_end_point = []
        self.end_point_mv = []
        self.end_point_clr = []
        self.pkmn_url = []
        self.pkmn_dict = []
        self.abl_dict = []
        self.mv_dict = []
        self.clr_dict = []

    def retrv_pokemon_name(self):
        url = "https://pokeapi.co/api/v2/pokemon/"
        r = requests.get(url )
        pkmn_list = dict(r.json())
        values = pkmn_list.get('results')
        for each_pkm in values:
            self.pkmn_dict.append(each_pkm['name'])
            self.end_point_pkm.append(each_pkm['url'].split('/')[-2])
            self.pkmn_url.append(each_pkm['url'])

    def ability_pokmn(self):
        url = "https://pokeapi.co/api/v2/ability/"
        l = requests.get(url)

        abl_pkmn_list = dict(l.json())
        abl_values = abl_pkmn_list.get('results')
        for each_abl in abl_values:
            self.abl_dict.append(each_abl['name'])
            self.abl_end_point.append(each_abl['url'].split('/')[-2])

    def move_pokmn(self):
        url = "https://pokeapi.co/api/v2/move/"
        mv = requests.get(url)
        pkmn_mv = dict(mv.json())
        mv_values = pkmn_mv.get('results')
        for each_mv in mv_values:
               self.mv_dict.append(each_mv['name'])
               self.end_point_mv.append(each_mv['url'].split('/')[-2])

    def color_pokmn(self):
        url = "https://pokeapi.co/api/v2/pokemon-color/"
        clr = requests.get(url)
        pkmn_clr = dict(clr.json())
        clr_values = pkmn_clr.get('results')
        for each_clr in clr_values:
                self.clr_dict.append(each_clr['name'])
                self.end_point_clr.append(each_clr['url'].split('/')[-2])
                #print(each_clr.values())

    def process(self):
        final_list = []
        print(f'Name \t\t Ability \t\t Movement \t color of Pokemon \n' )
        for i in range(0,10):
            if (self.end_point_pkm[i] == self.abl_end_point[i]) and (self.end_point_mv[i] == self.end_point_pkm[i]) \
                and (self.end_point_mv[i] == self.end_point_clr[i]):
                print(f'{self.pkmn_dict[i]} \t {self.abl_dict[i]}  \t\t {self.mv_dict[i]} \t {self.clr_dict[i]}\n')
            else:
                print('fail')

    def pok_comp(self):
        from tabulate import tabulate
        comp_list = []
        for poke in self.pkmn_url:
            cp = requests.get(poke)
            pkmn_list1 = dict(cp.json())
            r = requests.get(pkmn_list1['species']['url'])
            species_list = dict(r.json())
            egg_list = []
            for i in species_list['egg_groups']:
                egg_list.append(i['name'])

            comp_list.append([pkmn_list1['name'], pkmn_list1['weight'], pkmn_list1['height'],\
                 pkmn_list1['base_experience'],species_list['habitat']['name'],\
                species_list['color']['name'],egg_list])
        print(tabulate(comp_list,headers = ["Name","Weight","Height","Base Experience",'Habitat','color','Egg Group']))

import requests
my_pokemon = pokemon()
my_pokemon.ability_pokmn()
my_pokemon.retrv_pokemon_name()
my_pokemon.move_pokmn()
my_pokemon.color_pokmn()
#my_pokemon.process()
my_pokemon.pok_comp()
