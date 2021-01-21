AllVar = ['Intro','NameOfMyFavoriteSong','PublishedYear','Artist','DurationInSec','Genre','Desciption','WhereYouCanEnjoy']
EachVarValue = ['My song of choice is : ','Beautiful Sunday', 1972 , 'Daniel Boone',188,'Rock','Although this song is quite old for now, listening to this song is quite recommended.','You can find this song in YouTube, Spotify, Joox and any other applications that fuctions to play music.']
songdictionary = {} #Normally the dictionary will not keep the key in the same order, but adding things into the dictionary wil keep the key in ascending value
counterforlist2 = 0

for a in AllVar:
    songdictionary[a] = EachVarValue[counterforlist2]
    counterforlist2 += 1

print('Hello, welcome!')
userinput = str(input('Do you want to guess my favorite song? Y/N\n'))
if userinput == 'Y':
    for loop in range(10):
        answer, chance = str(input('Your answer: ')), print('Chances left:',9-loop)
        if answer == EachVarValue[1]:
            print('Absolutely correct!')
        elif answer != EachVarValue[1] and loop < 9:
            print('Uh oh, it is a wrong guess.')
        elif answer != EachVarValue[1] and loop == 9:
            print('Your chances ran out. The answer is:', EachVarValue[1]+'!')
elif userinput == 'N':
    for loop2 in songdictionary:
        print(loop2,songdictionary[loop2])
        exit
else:
    exit
userinput2 = str(input('\nDo you want to guess the characteristics of my favorite song? (There are 4 of them) Y/N\n')) #Here is the error
if userinput2 == 'Y':
    for loop3 in range(2,6):
        for loop4 in range(10):
            answer2 = str(input('What is the',EachVarValue[loop3],'of Beautiful Sunday?'))
            if answer2 == EachVarValue[loop3]:
                print('Absolutely correct!')
            elif answer2 != EachVarValue[loop3] and loop4 <= 9:
                print('Uh oh, it is a wrong guess.')
            else:
                print('Your chances ran out. The answer is:', EachVarValue[1]+'!')
elif userinput2 == 'N':
    print(songdictionary)
else:
    print('Bye')
print('\nThank you for participating!')
