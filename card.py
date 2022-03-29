import pygame
import pygwidgets


class Card:
    BACK_IMAGE = pygame.image.load('images/BackOfCard.png')

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.card_name = f'{rank} of {suit}'
        self.value = value
        front_image_path = f'images/{self.card_name}.png'
        self.images = pygwidgets.ImageCollection(window, (0, 0),
                                                 {'front': front_image_path, 'back': self.BACK_IMAGE}, 'back')

    def conceal(self):
        self.images.replace('back')

    def reveal(self):
        self.images.replace('front')

    def get_name(self):
        return self.card_name

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def set_loc(self, loc):
        self.images.setLoc(loc)

    def get_loc(self):
        return self.images.getLoc()

    def draw(self):
        self.images.draw()
