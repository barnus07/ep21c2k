with open("valaszok.txt", "rt", encoding="UTF-8") as fajl:
    print("1.Feladat: Az adatok beolvasása")
    sor = [sor.strip() for sor in fajl]
    print(f'2.Feladat: A versenyen {len(sor)-1} versenyző indult.')
    i = 1
    Id = []
    answers = []
    while i < len(sor):
        Id.append(sor[i].split(" ")[0])
        answers.append(sor[i].split(" ")[1])
        i+=1
        if i == len(sor):
            break
    try:
        Id_be = str(input("3.Feladat: Adja me a versenyző azonosítóját: "))
        if Id_be not in Id:
            print("Ilyen kóddal nem indult versenyző.")
        else:
            index = Id.index(Id_be)
            print(answers[index])
        print("4.Feladat: A helyes megoldás:")
        print(sor[0])
        eredmeny = ""
        index = Id.index(Id_be)
        i = 0
        while i< len(sor[0]):
            if answers[index][i] == sor[0][i]:
                eredmeny += "+"
            else:
                eredmeny += " "
            i += 1
            if i == len(sor[0]):
                break
        print(eredmeny)
        Task = int(input("5.Feladat: Kérem adja meg a feladat sorszámát: "))
        b = 0
        Task_id = Task-1
        Correct_answers = 0
        while (b+1)<len(sor):
            if sor[0][Task_id] == answers[b][Task_id]:
                Correct_answers += 1
            b +=1
            if b == len(sor):
                break
        percent = round((Correct_answers / (len(sor)-1))*100,2)
        print(f'A feladatra {Correct_answers} fő, a versenyzők {percent}%-a adott helyes választ.')
    except ValueError:
        print("nem megfelelő az érték")
with open("pontok.txt", "wt", encoding="UTF-8") as fajl:
    print("6.Feladat: A versenyzők pontszámának meghatározása.")
    i=0
    b=0
    eredmeny = []
    eredmenyek = 0
    while i < (len(sor)-1):
        while b<len(answers):
            if sor[0][b] == answers[i][b] and b<=4:
                eredmenyek +=3
            if sor[0][b] == answers[i][b] and b<=9 and b >=5:
                eredmenyek +=4
            if sor[0][b] == answers[i][b] and b>=10:
                eredmenyek +=5
            b += 1
            if b == (len(sor[0])):
                b = 0
                break
        eredmenyek += 1
        eredmeny.append(eredmenyek)
        eredmenyek = 0
        i +=1
        if i == len(sor):
            break
    i=0
    b=0
    while i < len(Id):
        fajl.write(Id[b]+" "+str(eredmeny[i])+"\n")
        b += 1
        i += 1
        if i == len(eredmeny):
            break
    i=1
    elso = eredmeny.index(max(eredmeny))
    print("7.Feladat: A verseny legjobbjai:")
    print(f'{i}.díj: ({eredmeny[elso]}. pont): {Id[elso]}')
    print(f'{i+1}.díj: ({eredmeny[0]}. pont): {Id[0]}')
    print(f'{i+2}.díj: ({eredmeny[0]}. pont): {Id[0]}')
