import pygame.mixer
import pygwidgets
from deck import *
from card import *


class Game:
    CARD_OFFSET = 110
    CARDS_TOP = 300
    CARDS_LEFT = 75
    N_CARDS = 8
    POINTS_CORRECT = 15
    POINTS_INCORRECT = 10
    WHITE = (255, 255, 255)

    def __init__(self, window):
        self.deck = Deck(window)
        self.score = 100
        self.score_text = pygwidgets.DisplayText(window, (450, 164), f'Score: {self.score}',
                                                 fontSize=36, textColor=self.WHITE, justified='right')
        self.message_text = pygwidgets.DisplayText(window, (50, 460), '', width=900, justified='center',
                                                   fontSize=36, textColor=self.WHITE)
        self.lose_sound = pygame.mixer.Sound('assets/sounds/loser.wav')
        self.win_sound = pygame.mixer.Sound('assets/sounds/ding.wav')
        self.card_shuffle_sound = pygame.mixer.Sound('assets/sounds/cardShuffle.wav')
        self.card_x_position_list = []
        this_left = self.CARDS_LEFT
        for _ in range(self.N_CARDS):
            self.card_x_position_list.append(this_left)
            this_left += self.CARD_OFFSET
        self.reset()

    def reset(self):
        self.card_shuffle_sound.play()
        self.deck.shuffle()
        self.card_list = []
        for this_card in range(self.N_CARDS):
            card = self.deck.get_card()
            self.card_list.append(card)
            this_x_position = self.card_x_position_list[this_card]
            card.set_loc((this_x_position, self.CARDS_TOP))
        self.show_card(0)
        self.current_card_index = 0
        self.current_card_name, self.current_card_value = self.get_card_name_and_value(self.current_card_index)
        self.message_text.setValue(f'Starting card is {self.current_card_name}. '
                                   'Will the next card be higher or lower?')

    def show_card(self, index):
        card = self.card_list[index]
        card.reveal()

    def get_card_name_and_value(self, index):
        card = self.card_list[index]
        return card.get_name(), card.get_value()

    def evaluate_guess(self, user_guess):
        next_card_index = self.current_card_index + 1
        self.show_card(next_card_index)
        next_card_name, next_card_value = self.get_card_name_and_value(next_card_index)

        correct_guess = 'higher' if next_card_value > self.current_card_value else 'lower'
        if user_guess == correct_guess:
            self.win_sound.play()
            self.score += self.POINTS_CORRECT
            self.message_text.setValue(f'Correct, {next_card_name} was {user_guess}')
        else:
            self.lose_sound.play()
            self.score -= self.POINTS_INCORRECT
            self.message_text.setValue(f'Incorrect, {next_card_name} was not {user_guess}')
        self.score_text.setValue(f'Score: {self.score}')

        self.current_card_index = next_card_index
        self.current_card_value = next_card_value

        finish = self.current_card_index == self.N_CARDS - 1
        return finish

    def draw(self):
        for card in self.card_list:
            card.draw()
        self.score_text.draw()
        self.message_text.draw()
