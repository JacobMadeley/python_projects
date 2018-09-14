import csv
from operator import itemgetter

FILE_NAME = "songs.csv"
REQUIRED = 'y'
LEARNED = 'n'


def main():
    print('Songs To Learn 1.0 - by Jacob Madeley')
    list_of_songs = load_songs()
    menu_choices(list_of_songs)


def load_songs():
    open_csv = open(FILE_NAME, 'r')
    read_csv = csv.reader(open_csv, delimiter=',')
    list_of_songs = list(read_csv)
    print('{} songs loaded'.format(str(len(list_of_songs))))
    open_csv.close()
    return list_of_songs


def menu_choices(list_of_songs):
    print('Menu: \nL - List Songs \nA - Add a new song \nC - Complete a song \nQ - Quit')
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == "L":
            display_list_of_songs(list_of_songs)
        elif choice == "A":
            add_to_songs(list_of_songs)
        elif choice == "C":
            complete_a_song(list_of_songs)
        else:
            print('Please enter a valid choice \n'
                  'Menu: \nL - List Songs \nA - Add a new song \nC - Complete a song \nQ - Quit')
        choice = input('>>> ').upper()
    end_program(list_of_songs())


def display_list_of_songs(list_of_songs):
    songs_known = 0
    list_of_songs.sort(key=itemgetter(1))
    for x, learnings in enumerate(list_of_songs):
        learnings = [y for y in learnings]
        if learnings[3] == LEARNED:
            if_known = ''
        else:
            if_known = '*'
        print('{:2}. {:>1} {:<30} - {:<25} ({})'.format(x, if_known, learnings[0], learnings[1], learnings[2]))
        if LEARNED in learnings[3]:
            songs_known += 1
    print('{} song/s learnt, {} songs/s still to learn'.format(songs_known, len(list_of_songs) - songs_known))
    menu_choices(list_of_songs)


def add_to_songs(list_of_songs):
    song_name = str(input('Enter songs name: '))
    while song_name == '':
        print('The songs name cannot me blank')
        song_name = str(input('Enter songs name: '))
    artist = str(input('Enter artists name: '))
    while artist == '':
        print('The artists name cannot me blank')
        artist = str(input('Enter songs name: '))
    year_released = input('Enter year the song was released: ')
    while year_released == '':
        if year_released == '':
            print('year cannot be blank')
            year_released = int(input('Enter year the song was released'))
        else:
            print('letters and/or symbols are not allowed')
            year_released = int(input('Enter year the song was released'))
    list_of_songs.append([song_name, artist, year_released, REQUIRED])
    print('{} by {} ({}) added to songs list'.format(song_name, artist, year_released))
    menu_choices(list_of_songs)


def complete_a_song(list_of_songs):
    songs_completed = [z[3] for z in list_of_songs]
    if REQUIRED not in songs_completed:
        print('No more songs to be learnt.')
        return
    print('What song do you want to learn, enter the songs number.')
    choice = False
    while not choice:
        try:
            songs_completed = int(input('>>> '))
            if songs_completed >= len(list_of_songs):
                print('Input number cannot exceed number of songs.')
            elif songs_completed < 0:
                print('Invalid song number.')
            elif songs_completed >= 0 <= len(list_of_songs):
                song_to_change = songs_completed
                change_list = list_of_songs[song_to_change]
                if LEARNED not in change_list[3]:
                    change_list[3] = LEARNED
                    list_of_songs[song_to_change] = change_list
                    print('{} by {} learnt'.format(change_list, change_list[songs_completed]))
                    menu_choices(list_of_songs)
                else:
                    print('Invalid input.')
        except ValueError:
            print('Invalid input.')
            menu_choices(list_of_songs)


def end_program(list_of_songs):
    with open(FILE_NAME, "w", newline="") as add_songs_into_csv:
        adding_in_csv = csv.writer(add_songs_into_csv, delimitor=',')
        adding_in_csv.writerows(list_of_songs)
    print("{} songs saved to {}".format(len(list_of_songs), adding_in_csv))


main()
