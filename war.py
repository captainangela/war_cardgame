#make cards
#deal cards
#play

#!/usr/bin/python
# -*- coding: ascii -*-
import os, sys
import random

playing_cards = []
players_hand = []
suits = ['heart', 'diamond', 'club', 'spade']
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits_symbols = [('heart', u'\u2665'), ('diamond', u'\u2666'), ('club', u'\u2663'), ('spade', u'\u2660')]



def make_cards():
    """creates the deck of cards"""

    playing_cards = [(s, v) for s in suits for v in card_values] 
        
    return playing_cards
    
    
def deal_cards():
    """gives each player 26 cards"""
    
    players_hand = []
    
    while len(players_hand) < 26:
        card = random.choice(playing_cards)
        players_hand.append(card)
        playing_cards.remove(card)
    
    return players_hand

def play_war():
    """compares cards"""
    play = raw_input("Do you want to play? Y or N > ").title()
    if play == "Y":
        print "Type P to draw or E to exit at any time"
        while players_hand > 0 or playing_cards > 0:
            draw = raw_input("> ").title()
            if draw == "P":
                player_card = random.choice(players_hand)
                #print player_card
                players_hand.remove(player_card)
                comp_card = random.choice(playing_cards)
                #print comp_card
                playing_cards.remove(comp_card)
                suit_word = player_card[0]
                ind = suits.index(suit_word)
                symbol = suits_symbols[ind][1]
                print "Player 1:              Computer:"
                print "-----------", "           ", "-----------"
                print "|{}       |".format(player_card[1]), "           ", "|{}       |".format(comp_card[1]) 
                print "|         |", "           ", "|         |"
                print "|         |", "           ", "|         |" 
                print "|   ", u"{0}".format(symbol), "   |", "    vs     ", "|   ", u"{0}".format(symbol), "   |"
                print "|         |", "           ", "|         |"
                print "|         |", "           ", "|         |"
                print "|        {}|".format(player_card[1]), "           ", "|{}       |".format(comp_card[1]) 
                print "-----------", "           ", "-----------"

                if player_card[1] > comp_card[1]:
                    print "Player 1 wins this round!"
                    players_hand.extend((player_card, comp_card))
                    print len(players_hand)
                elif player_card[1] == comp_card[1]:
                    print "They're tied - drawing again"
                    player_card2 = random.choice(players_hand)
                    players_hand.remove(player_card2)
                    comp_card2 = random.choice(playing_cards)
                    print comp_card2
                    playing_cards.remove(comp_card2)
                    if player_card2[1] > comp_card2[1]:
                        print "Player 1 wins this round!"
                        players_hand.extend((player_card, comp_card, player_card2, comp_card2))
                        print len(players_hand)
                    else:
                        print "Computer wins this round!"
                        playing_cards.extend((player_card, comp_card,player_card2, comp_card2))
                        print len(players_hand)
                else:
                    print "Computer wins this round!"
                    playing_cards.extend((player_card, comp_card))
                    print len(players_hand)
            else:
                print "K, bye!"
                exit()
    else: 
        print "K, bye!"
        exit()

def war():
    """plays game"""
playing_cards = make_cards()
players_hand = deal_cards()
play_war()
