

def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    i = game.index('Paper')
    print(i)
    print('Length of game:', len(game))
    print(game[i])
    game.append('Computer')
    game.insert(0, 'Ramen')
    game.insert(1, 'Noodles')
    print(game)
    print(' / '.join(game))
    # Ramen / Noodles / Rock / Paper / Scissors / Lizard / Spock / Computer
    print(len(game))


if __name__ == '__main__':
    main()
