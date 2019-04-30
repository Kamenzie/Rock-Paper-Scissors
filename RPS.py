#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock', 'paper', 'scissors']


class Player:
    my_move = 'None'
    their_move = 'None'

    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return(random.choice(moves))


'''class OtherPlayer(Player):
    def move(self):
        return(random.choice(moves))'''


class HumanPlayer(Player):
    def move(self):
        while True:
            my_move = input(f"rock, paper or scissors?")
            if my_move.lower() not in moves:
                print("Please choose a move from the list, and try again.")
            else:
                break
        return my_move.lower()


class ReflectPlayer(Player):
    def __init__(self):
        self.move_temp = 'rock'

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        self.move_temp = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is 'None':
            return random.choice(moves)
        index = moves.index(self.my_move) + 1
        if index == len(moves):
            index = 0
        return moves[index]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            self.p1_score += 1
            print("You Win!")
        elif beats(move2, move1) is True:
            self.p2_score += 1
            print("Computer wins!")
        elif move1 == move2:
            self.p1_score += 0
            self.p2_score += 0
            print("It's a Draw!")

    def play_game(self):
        print("Game start!")
        num = int(input(f"How many rounds would you like to play?"))
        for round in range(num):
            print(f"Round {round}:")
            self.play_round()
            print(f"Current Score: {self.p1_score} to {self.p2_score}")
        if self.p1_score > self.p2_score:
            winner = 'You'
        elif self.p2_score > self.p1_score:
            winner = 'Computer'
        elif self.p1_score == self.p2_score:
            winner = 'No one has'
        print(f"Game over! {winner} won!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()
