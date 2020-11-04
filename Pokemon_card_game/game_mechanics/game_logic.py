import random

class Cards:

    player_1_score = 0
    player_2_score = 0
    battle = 1
    god_spell_count_1 = 0
    god_spell_count_2 = 0
    resurrect_spell_count_1 = 0
    resurrect_spell_count_2 = 0
    outdated_deck = []

    def __init__(self):
        self.build_deck()

    def build_deck(self):
        c1 = {'Name':'Pikachu','Attributes':{'attack':8,'defense':5,'speed':9}}
        c2 = {'Name':'Squirtle','Attributes':{'attack':7,'defense':9,'speed':6}}
        c3 = {'Name':'Charmander','Attributes':{'attack':9,'defense':7,'speed':8}}
        c4 = {'Name':'Ditto','Attributes':{'attack':2,'defense':1,'speed':1}}
        c5 = {'Name':'Magikarp','Attributes':{'attack':3,'defense':0,'speed':0}}
        c6 = {'Name':'Rhydon','Attributes':{'attack':6,'defense':8,'speed':5}}
        c7 = {'Name':'Eevee','Attributes':{'attack':5,'defense':6,'speed':7}}
        c8 = {'Name':'Butterfee','Attributes':{'attack':1,'defense':2,'speed':3}}
        c9 = {'Name':'Pidgey','Attributes':{'attack':4,'defense':4,'speed':2}}
        c10 = {'Name':'Rattata','Attributes':{'attack':0,'defense':3,'speed':4}}
        self.deck = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
        return self.deck

    def assign_cards(self):
        self.player_1 = random.sample(self.deck,5)
        self.player_2 = []
        for item in self.deck:
            if item not in self.player_1:
                self.player_2.append(item)
        print(f'No. of Player_1 cards: {len(self.player_1)}')
        print(f'No. of Player_2 cards: {len(self.player_2)}')
        print('\n')
        return self.player_1, self.player_2

    def dice_roll(self):
        self.player_1_dice = random.randint(1,6)
        self.player_2_dice = random.randint(1,6)
        if self.player_1_dice == self.player_2_dice:
            print(f'Player 1 dice value: {self.player_1_dice}')
            print(f'Player 2 dice value: {self.player_2_dice}')
            print('Same value! Rolling dice again!')
            print('\n')
            self.dice_roll()

    def assign_rounds(self):
        if self.player_1_dice > self.player_2_dice:
            print(f'dice of player 1: {self.player_1_dice}')
            print(f'dice of player 2: {self.player_2_dice}')
            print('\n')
            self.play_round_1()
        else:
            print(f'dice of player 1: {self.player_1_dice}')
            print(f'dice of player 2: {self.player_2_dice}')
            print('\n')
            self.play_round_2()
            print('\n')       

    def play_round_1(self):
        while len(self.player_1) or len(self.player_2) != 0:
            print(f'Battle: {self.battle}')
            self.round_start = self.player_1
            print(f'Player 1 starts the battle!')
            print(f'Resurrect Spell selection')
            print(f'1. Yes')
            print(f'2. No')
            selection = int(input('Enter number of your selection: '))
            if selection == 1:
                self.resurrect_spell_1()
                if self.value_1 > self.value_2:
                    self.play_round_1()
                else:
                    self.play_round_2()
            elif selection == 2:
                print(f'Player 1 card: {self.player_1[0]}')
                print(list(self.player_1[0]['Attributes'].keys()))
                self.name = input('Enter an Attribute: ').lower()
                print(f'Use God spell')
                print(f'1. Yes')
                print(f'2. No')
                selection = int(input('Enter number of your selection: '))
                if selection == 1:
                    self.god_spell_1()
                    if self.value_1 > self.value_2:
                        self.play_round_1()
                    else:
                        self.play_round_2()
                elif selection == 2:
                    self.value_1 = self.player_1[0]['Attributes'][self.name]
                    self.value_2 = self.player_2[0]['Attributes'][self.name]
                    if self.value_1 > self.value_2:
                        print(f'Player 1 won the battle')
                        self.player_1_score += 1
                        self.battle += 1
                        print(f'Player 1 card: {self.player_1[0]}')
                        print(f'Player 2 card: {self.player_2[0]}')
                        print('\n')
                        print(f'Player 1 score: {self.player_1_score}')
                        print(f'Player 2 score: {self.player_2_score}')
                        print('\n')
                        self.outdated_deck.append(self.player_1.pop(0))
                        self.outdated_deck.append(self.player_2.pop(0))
                    else:
                        print(f'Player 2 won the battle')
                        self.player_2_score += 1
                        self.battle += 1
                        print(f'Player 2 card: {self.player_2[0]}')
                        print(f'Player 1 card: {self.player_1[0]}')
                        print('\n')
                        print(f'player 2 score: {self.player_2_score}')
                        print(f'player 1 score: {self.player_1_score}')
                        print('\n')
                        self.outdated_deck.append(self.player_1.pop(0))
                        self.outdated_deck.append(self.player_2.pop(0))
                        self.play_round_2()
                else:
                    print(f'Spell is already used!')
                    self.play_round_1()
        else:
            if self.player_1_score > self.player_2_score:
                print("Player 1 has won the match")
            elif self.player_1_score == self.player_2_score:
                print("Match draw")
            else:
                print("Player 2 has won the match")
            exit()

    def play_round_2(self):
        while len(self.player_1) or len(self.player_2) != 0:
            print(f'Battle: {self.battle}')
            self.round_start = self.player_2
            print(f'Player 2 starts the battle!')
            print(f'Resurrect spell selection')
            print(f'1. Yes')
            print(f'2. No')
            selection = int(input('Enter number of your selection: '))
            if selection == 1:
                self.resurrect_spell_2()
                if self.value_1 > self.value_2:
                    self.play_round_2()
                else:
                    self.play_round_1()
            elif selection == 2:
                print(f'Player 2 card: {self.player_2[0]}')
                print(list(self.player_2[0]['Attributes'].keys()))
                self.name = input('Enter an Attribute: ').lower()
                print(f'Use God Spell')
                print(f'1. Yes')
                print(f'2. No')
                selection = int(input('Enter number of your selection: '))
                if selection == 1:
                    self.god_spell_2()
                    if self.value_1 > self.value_2:
                        self.play_round_2()
                    else:
                        self.play_round_1()
                elif selection == 2:
                    self.value_1 = self.player_2[0]['Attributes'][self.name]
                    self.value_2 = self.player_1[0]['Attributes'][self.name]
                    if self.value_1 > self.value_2:
                        print(f'Player 2 won the battle')
                        self.player_2_score += 1
                        self.battle += 1
                        print(f'Player 2 card: {self.player_2[0]}')
                        print(f'Player 1 card: {self.player_1[0]}')
                        print('\n')
                        print(f'Player 2 score: {self.player_2_score}')
                        print(f'Player 1 score: {self.player_1_score}')
                        print('\n')
                        self.outdated_deck.append(self.player_1.pop(0))
                        self.outdated_deck.append(self.player_2.pop(0))
                    else:
                        print(f'Player 1 won the battle')
                        self.player_1_score += 1
                        self.battle += 1
                        print(f'Player 1 card: {self.player_1[0]}')
                        print(f'Player 2 card: {self.player_2[0]}')
                        print('\n')
                        print(f'player 1 score: {self.player_1_score}')
                        print(f'player 2 score: {self.player_2_score}')
                        print('\n')
                        self.outdated_deck.append(self.player_1.pop(0))
                        self.outdated_deck.append(self.player_2.pop(0))
                        self.play_round_1()
                else:
                    print(f'Spell is already used!')
                    self.play_round_2()
        else:
            if self.player_1_score > self.player_2_score:
                print("Player 1 has won the match")
            elif self.player_1_score == self.player_2_score:
                print("Match draw")
            else:
                print("Player 2 has won the match")
            exit()

    def god_spell_1(self):
        if self.round_start == self.player_1 and self.god_spell_count_1 == 0:
            print(f'No. of player 2 cards: {len(self.player_2)}')
            self.index = int(input(f'Enter index of player 2 card: '))
            self.value_1 = self.player_1[0]['Attributes'][self.name]
            self.value_2 = self.player_2[self.index]['Attributes'][self.name]
            print(f'Player 2 spell available')
            print(f'1. Use resurrect spell')
            print(f'2. No')
            decision = int(input(f'Enter your selection: '))
            if decision == 1 and len(self.outdated_deck) == 0:
                print(f'Cannot use resurrect now!')
                self.god_spell_1()
            elif decision == 1 and len(self.outdated_deck) != 0:
                self.god_resurrect_1()
                if self.value_1 > self.value_2:
                    self.play_round_1()
                else:
                    self.play_round_2()
            elif decision == 2:
                if self.value_1 > self.value_2:
                    print(f'Player 1 won the battle')
                    self.player_1_score += 1
                    self.battle += 1
                    self.god_spell_count_1 += 1
                    print(f'Player 1 card: {self.player_1[0]}')
                    print(f'Player 2 card: {self.player_2[self.index]}')
                    print('\n')
                    print(f'Player 1 score: {self.player_1_score}')
                    print(f'Player 2 score: {self.player_2_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(self.index))
                else:
                    print(f'Player 2 won the battle')
                    self.player_2_score += 1
                    self.battle += 1
                    self.god_spell_count_1 += 1
                    print(f'Player 2 card: {self.player_2[self.index]}')
                    print(f'Player 1 card: {self.player_1[0]}')
                    print('\n')
                    print(f'Player 2 score: {self.player_2_score}')
                    print(f'Player 1 score: {self.player_1_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(self.index))
            else:
                print(f'Resurrect spell has been used already!')
                self.god_spell_1()            
        else:
            print(f'God spell has been used already')
            self.play_round_1()
        

    def god_spell_2(self):
        if self.round_start == self.player_2 and self.god_spell_count_2 == 0:
            print(f'No. of player 1 cards: {len(self.player_1)}')
            self.index = int(input(f'Enter index of player 1 card: '))
            self.value_1 = self.player_2[0]['Attributes'][self.name]
            self.value_2 = self.player_1[self.index]['Attributes'][self.name]
            print(f'Player 1 spell available')
            print(f'1. Use resurrect spell')
            print(f'2. No')
            decision = int(input(f'Enter your selection: '))
            if decision == 1 and len(self.outdated_deck) == 0:
                print(f'Cannot use resurrect spell now!')
                self.god_spell_2()
            elif decision == 1 and len(self.outdated_deck) != 0:
                self.god_resurrect_2()
                if self.value_1 > self.value_2:
                    self.play_round_2()
                else:
                    self.play_round_1()
            elif decision == 2:
                if self.value_1 > self.value_2:
                    print(f'Player 2 won the battle')
                    self.player_2_score += 1
                    self.battle += 1
                    self.god_spell_count_2 += 1
                    print(f'Player 2 card: {self.player_2[0]}')
                    print(f'Player 1 card: {self.player_1[self.index]}')
                    print('\n')
                    print(f'Player 2 score: {self.player_2_score}')
                    print(f'Player 1 score: {self.player_1_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(self.index))
                    self.outdated_deck.append(self.player_2.pop(0))
                else:
                    print(f'Player 1 won the battle')
                    self.player_1_score += 1
                    self.battle += 1
                    self.god_spell_count_2 += 1
                    print(f'Player 1 card: {self.player_1[self.index]}')
                    print(f'Player 2 card: {self.player_2[0]}')
                    print('\n')
                    print(f'Player 1 score: {self.player_1_score}')
                    print(f'Player 2 score: {self.player_2_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(self.index))
                    self.outdated_deck.append(self.player_2.pop(0))
            else:
                print(f'Resurrect spell has been used already!')
                self.god_spell_2()
        else:
            print(f'God spell has been used already')
            self.play_round_2()

        #print(f'Outdated deck: {self.outdated_deck}')
    
    def resurrect_spell_1(self):
        if self.round_start == self.player_1 and self.resurrect_spell_count_1 == 0 and len(self.outdated_deck) != 0:
            print(f'No. of cards in outdated deck: {len(self.outdated_deck)}')
            self.player_1.insert(0,random.choice(self.outdated_deck))
            print(list(self.player_1[0]['Attributes'].keys()))
            self.name = input('Enter an Attribute: ').lower()
            self.value_1 = self.player_1[0]['Attributes'][self.name]
            self.value_2 = self.player_2[0]['Attributes'][self.name]
            if self.value_1 > self.value_2:
                print(f'Player 1 won the battle')
                self.player_1_score += 1
                self.battle += 1
                self.resurrect_spell_count_1 += 1
                print(f'Player 1 card: {self.player_1[0]}')
                print(f'Player 2 card: {self.player_2[0]}')
                print('\n')
                print(f'Player 1 score: {self.player_1_score}')
                print(f'Player 2 score: {self.player_2_score}')
                print('\n')
                self.outdated_deck.append(self.player_1.pop(0))
                self.outdated_deck.append(self.player_2.pop(0))
            else:
                print(f'Player 2 won the battle')
                self.player_2_score += 1
                self.battle += 1
                self.resurrect_spell_count_1 += 1
                print(f'Player 2 card: {self.player_2[0]}')
                print(f'Player 1 card: {self.player_1[0]}')
                print('\n')
                print(f'Player 2 score: {self.player_2_score}')
                print(f'Player 1 score: {self.player_1_score}')
                print('\n')
                self.outdated_deck.append(self.player_1.pop(0))
                self.outdated_deck.append(self.player_2.pop(0))
        
        elif len(self.outdated_deck) == 0:
            print("Cannot use resurrect spell now!")
            self.play_round_1()
        else:
            print(f'Resurrect spell has been used already')
            self.play_round_1()

    def resurrect_spell_2(self):
        if self.round_start == self.player_2 and self.resurrect_spell_count_2 == 0 and len(self.outdated_deck) != 0:
            print(f'No. of cards in outdated deck: {len(self.outdated_deck)}')
            self.player_2.insert(0,random.choice(self.outdated_deck))
            print(list(self.player_2[0]['Attributes'].keys()))
            self.name = input('Enter an Attribute: ').lower()
            self.value_1 = self.player_2[0]['Attributes'][self.name]
            self.value_2 = self.player_1[0]['Attributes'][self.name]
            if self.value_1 > self.value_2:
                print(f'Player 2 won the battle')
                self.player_2_score += 1
                self.battle += 1
                self.resurrect_spell_count_2 += 1
                print(f'Player 2 card: {self.player_2[0]}')
                print(f'Player 1 card: {self.player_1[0]}')
                print('\n')
                print(f'Player 2 score: {self.player_2_score}')
                print(f'Player 1 score: {self.player_1_score}')
                print('\n')
                self.outdated_deck.append(self.player_1.pop(0))
                self.outdated_deck.append(self.player_2.pop(0))
            else:
                print(f'Player 1 won the battle')
                self.player_1_score += 1
                self.battle += 1
                self.resurrect_spell_count_2 += 1
                print(f'Player 1 card: {self.player_1[0]}')
                print(f'Player 2 card: {self.player_2[0]}')
                print('\n')
                print(f'Player 1 score: {self.player_1_score}')
                print(f'Player 2 score: {self.player_2_score}')
                print('\n')
                self.outdated_deck.append(self.player_1.pop(0))
                self.outdated_deck.append(self.player_2.pop(0))
        
        elif len(self.outdated_deck) == 0:
            print("Cannot use resurrect spell now!")
            self.play_round_2()
        else:
            print(f'Resurrect spell has been used already')
            self.play_round_2()


    def god_resurrect_1(self):
        if self.round_start == self.player_1 and self.resurrect_spell_count_2 == 0 and len(self.outdated_deck) != 0:
            print(f'No. of cards in outdated deck: {len(self.outdated_deck)}')
            self.value_1 = self.player_1[0]['Attributes'][self.name]
            print(f'Player 2 has played resurrect spell')
            print(f'Player 1 Choice of index for Player 2')
            print(f'1. Index chosen in god spell')
            print(f'2. Resurrected card of player 2')
            select = int(input('Enter the number of choice: '))
            if select == 1:
                self.value_2 = self.player_2[self.index]['Attributes'][self.name]
                if self.value_1 > self.value_2:
                    print(f'Player 1 won the battle')
                    self.player_1_score += 1
                    self.battle += 1
                    self.god_spell_count_1 += 1
                    self.resurrect_spell_count_2 += 1
                    print(f'Player 1 card: {self.player_1[0]}')
                    print(f'Player 2 card: {self.player_2[self.index]}')
                    print('\n')
                    print(f'Player 1 score: {self.player_1_score}')
                    print(f'Player 2 score: {self.player_2_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(self.index))
                else:
                    print(f'Player 2 won the battle')
                    self.player_2_score += 1
                    self.battle += 1
                    self.god_spell_count_1 += 1
                    self.resurrect_spell_count_2 += 1
                    print(f'Player 2 card: {self.player_2[self.index]}')
                    print(f'Player 1 card: {self.player_1[0]}')
                    print('\n')
                    print(f'player 2 score: {self.player_2_score}')
                    print(f'player 1 score: {self.player_1_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(self.index))

            elif select == 2:
                self.player_2.insert(0,random.choice(self.outdated_deck))
                self.value_2 = self.player_2[0]['Attributes'][self.name]
                if self.value_1 > self.value_2:
                    print(f'Player 1 won the battle')
                    self.player_1_score += 1
                    self.battle += 1
                    self.god_spell_count_1 += 1
                    self.resurrect_spell_count_2 += 1
                    print(f'Player 1 card: {self.player_1[0]}')
                    print(f'Player 2 card: {self.player_2[0]}')
                    print('\n')
                    print(f'Player 1 score: {self.player_1_score}')
                    print(f'Player 2 score: {self.player_2_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(0))
                else:
                    print(f'Player 2 won the battle')
                    self.player_2_score += 1
                    self.battle += 1
                    self.god_spell_count_1 += 1
                    self.resurrect_spell_count_2 += 1
                    print(f'Player 2 card: {self.player_2[0]}')
                    print(f'Player 1 card: {self.player_1[0]}')
                    print('\n')
                    print(f'player 2 score: {self.player_2_score}')
                    print(f'player 1 score: {self.player_1_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(0))
        else:
            print(f'Cannot use resurrect spell now!')
            self.god_spell_1()
    
    def god_resurrect_2(self):
        if self.round_start == self.player_2 and self.resurrect_spell_count_1 == 0 and len(self.outdated_deck) != 0:
            print(f'No. of cards in outdated deck: {len(self.outdated_deck)}')
            self.value_1 = self.player_2[0]['Attributes'][self.name]
            print(f'Player 1 has played resurrect spell')
            print(f'Player 2 Choice of index for Player 1')
            print(f'1. Index chosen in god spell')
            print(f'2. Resurrected card of player 1')
            select = int(input('Enter the number of choice: '))
            if select == 1:
                self.value_2 = self.player_1[self.index]['Attributes'][self.name]
                if self.value_1 > self.value_2:
                    print(f'Player 2 won the battle')
                    self.player_2_score += 1
                    self.battle += 1
                    self.god_spell_count_2 += 1
                    self.resurrect_spell_count_1 += 1
                    print(f'Player 2 card: {self.player_2[0]}')
                    print(f'Player 1 card: {self.player_1[self.index]}')
                    print('\n')
                    print(f'Player 1 score: {self.player_1_score}')
                    print(f'Player 2 score: {self.player_2_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(self.index))
                else:
                    print(f'Player 1 won the battle')
                    self.player_2_score += 1
                    self.battle += 1
                    self.god_spell_count_2 += 1
                    self.resurrect_spell_count_1 += 1
                    print(f'Player 1 card: {self.player_1[self.index]}')
                    print(f'Player 2 card: {self.player_2[0]}')
                    print('\n')
                    print(f'player 1 score: {self.player_1_score}')
                    print(f'player 2 score: {self.player_2_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(self.index))

            elif select == 2:
                self.player_1.insert(0,random.choice(self.outdated_deck))
                self.value_2 = self.player_1[0]['Attributes'][self.name]
                if self.value_1 > self.value_2:
                    print(f'Player 2 won the battle')
                    self.player_2_score += 1
                    self.battle += 1
                    self.god_spell_count_2 += 1
                    self.resurrect_spell_count_1 += 1
                    print(f'Player 2 card: {self.player_2[0]}')
                    print(f'Player 1 card: {self.player_1[0]}')
                    print('\n')
                    print(f'Player 2 score: {self.player_2_score}')
                    print(f'Player 1 score: {self.player_1_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(0))
                else:
                    print(f'Player 1 won the battle')
                    self.player_1_score += 1
                    self.battle += 1
                    self.god_spell_count_2 += 1
                    self.resurrect_spell_count_1 += 1
                    print(f'Player 1 card: {self.player_1[0]}')
                    print(f'Player 2 card: {self.player_2[0]}')
                    print('\n')
                    print(f'player 1 score: {self.player_1_score}')
                    print(f'player 2 score: {self.player_2_score}')
                    print('\n')
                    self.outdated_deck.append(self.player_1.pop(0))
                    self.outdated_deck.append(self.player_2.pop(0))
        else:
            print(f'Cannot use resurrect spell now!')
            self.god_spell_2()

