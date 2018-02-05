import random

capitals = {'Islandia': 'REJKIAWIK', 'Norwegia': 'OSLO', 'Szwecja': 'SZTOKHOLM', 'Finlandia':'HELSINKI',
'Dania': 'KOPENHAGA', 'Holandia': 'AMSTERDAM', 'Belgia':'BRUKSELA', 'Niemcy': 'BERLIN', 'Luksemburg': 'LUKSEMBURG',
'Francja': 'PARYŻ', 'Wielka Brytania': 'LONDYN', 'Irlandia': 'DUBLIN', 'Portugalia': 'LIZBONA', 'Hiszpania': 'MADRYT',
'Monako': 'MONAKO', 'Włochy': 'RZYM', 'San Marino': 'SAN MARINO', 'Watykan': 'Watykan', 'Malta': 'VALLETTA',
'Słowenia': 'LUBLANA', 'Chorwacja': 'ZAGRZEB', 'Bośnia i Hercegowina': 'SARAJEWO', 'Andora': 'ANDORA',
'Serbia': 'BELGRAD', 'Czarnogóra': 'PODGORICA', 'Albania': 'TIRANA', 'Macedonia': 'SKOPIE', 'Grecja': 'ATENY',
'Polska': 'WARSZAWA', 'Czechy': 'PRAGA', 'Słowacja': 'BRATYSŁAWA', 'Węgry': 'BUDAPESZT', 'Rumunia': 'BUKARESZT',
'Bułgaria': 'SOFIA', 'Rosja': 'MOSKWA', 'Litwa': 'WILNO', 'Łotwa': 'RYGA', 'Estonia': 'TALLIN', 'Białoruś': 'MIŃSK',
'Ukraina': 'KIJÓW', 'Mołdawia': 'KISZYNIÓW', 'Szwajcaria': 'BERNO', 'Austria': 'WIEDEŃ', 'Lichtenstein': 'VEDUZ'}

for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answer%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Imię i nazwisko: \n\nData:\n\nKlasa:\n\n')
    quizFile.write((' ' *20) + 'Quiz stolic europy (Quiz %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    counrty = list(capitals.keys())
    random.shuffle(counrty)
    for questionNum in range(44):
        correctAnswer = capitals[counrty[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write('%s. Co jest stolicą kraju %s?\n' % (questionNum + 1,
                        counrty[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' %('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n'  % (questionNum + 1, 'ABCD'[
                    answerOptions.index(correctAnswer)]))
     quizFile.close()
     answerKeyFile.close()
