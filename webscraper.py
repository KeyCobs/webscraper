import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {"Accept-Language" : "en-US, en;q=0.5"}
url = "https://www.procyclingstats.com/rider/"


nameList = [
'Tadej-Pogacar',
'Remco-Evenepoel',
'Wout-van-Aert',
'Jonas-Vingegaard',
'Jasper-Philipsen',
'Primoz-Roglic',
'Mads-Pedersen',
'Mattias-Skjelmose',
'Adam-Yates',
'Christophe-Laporte',
'Enric-Mas',
'Joao-Almeida',
'Mathieu-van-der-Poel',
'Neilson-Powless',
'Thomas-Pidcock',
'Thibaut-Pinot',
'David-Gaudu',
'Olav-Kooij',
'Geraint-Thomas',
'Mikel-Landa',
'Romain-Bardet',
'Michael-Matthews',
'Dylan-Groenewegen',
'Arnaud-Demare',
'Stefan-Kung',
'Pello-Bilbao',
'Filippo-Ganna',
'Valentin-Madouas',
'Matteo-Jorgenson',
'Axel-Zingle',
'Juan-Ayuso',
'Lorenzo-Rota',
'Tao-Geoghegan-Hart',
'Simon-Yates',
'Guillaume-Martin',
'Thymen-Arensman',
'Marc-Hirschi',
'Ben-Healy',
'Giulio-Ciccone',
'Louis-Meintjes',
'Sergio-Higuita',
'Tim-Merlier',
'Carlos-Rodriguez',
'Diego-Ulissi',
'Jai-Hindley',
'Jordi-Meeus',
'Fabio-Jakobsen',
'Einer-Augusto-Rubio',
'Rigoberto-Uran',
'Matteo-Trentin',
'Mauro-Schmid',
'Kevin-Vauquelin',
'Matej-Mohoric',
'Ben-OConnor',
'Ethan-Hayter',
'Gerben-Thijssen',
'Aleksandr-Vlasov',
'Pavel-Sivakov',
'Magnus-Sheffield',
'Santiago-Buitrago',
'Magnus-Cort',
'Patrick-Konrad',
'Alexey-Lutsenko',
'Brandon-McNulty',
'Damiano-Caruso',
'Bryan-Coquard',
'Benoit-Cosnefroy',
'Richard-Carapaz',
'Jesus-Herrada',
'Jonathan-Milan',
'Tiesj-Benoot',
'Andreas-Leknessund',
'Jay-Vine',
'Yves-Lampaert',
'Biniam-Girmay',
'Sam-Welsford',
'Pascal-Ackermann',
'Alberto-Bettiol',
'Toms-Skujins',
'Kaden-Groves',
'Ilan-Van-Wilder',
'Ben-Tulett',
'Ivan-Garcia-Cortina',
'Felix-Gall',
'Fred-Wright',
'Sepp-Kuss',
'Lennard-Kamna',
'Filippo-Zana',
'Danny-van-Poppel',
'Ion-Izagirre',
'Alex-Aranburu',
'Bauke-Mollema',
'Ruben-Guerreiro',
'Luca-Mozzato',
'Daniel-Felipe-Martinez',
'Sam-Bennett',
'Soren-Kragh-Andersen',
'Romain-Gregoire',
'Marc-Soler'
]




#Data 
names = []
dob = []
nats =[]
odr = []
gc = []
timeTrials = []
sprints = []
climbers = []
allTimes = []
uciWorlds = []
pcsRankings = []
dates = []
resultStages = [],[]
results = []
races = []
distances = []
pointsPCS = []
pointsUCI = []



for elem in nameList:
    print("Player detail")
    url = "https://www.procyclingstats.com/rider/" + elem 
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    runner_div = soup.find('div', class_ = 'rdr-info-cont')

    #DO: GET NAME
    name = elem.replace('-', ' ')
    names.append(name)

    #DO: GET DATE OF BIRTH
    info_div = soup.find('div', class_='rdr-info-cont')
    birthText = info_div.get_text()
    birth = birthText.split(':')[1].strip().split('(')[0].strip()
    dob.append(birth)

    #DO: GET NATIONALITY
    nationality = info_div.find('a')
    nat = nationality.text
    nats.append(nat)

    #DO: GET YEAR ACHIEVMENTS
    OneDayRace  = info_div.find_all('div', class_ = "pnt")[0].text
    odr.append(OneDayRace)
    gcSingle    = info_div.find_all('div', class_ = "pnt")[1].text
    gc.append(gcSingle)
    timeTrial   = info_div.find_all('div', class_ = "pnt")[2].text
    timeTrials.append(timeTrial)
    sprint      = info_div.find_all('div', class_ = "pnt")[3].text
    sprints.append(sprint)
    climber     = info_div.find_all('div', class_ = "pnt")[4].text
    climbers.append(climber)

    #DO: GET RANKING
    alltime     = info_div.find_all('div', class_ = "rnk")[0].text
    allTimes.append(alltime)
    ucWorld     = info_div.find_all('div', class_ = "rnk")[1].text
    uciWorlds.append(ucWorld)
    pcsRanking  = info_div.find_all('div', class_ = "rnk")[2].text
    pcsRankings.append(pcsRanking)

    #print some stuff in terminal
    #print("CYCLIST-DATA")
    #print("visiting: " + elem + " URL: " + url)
    #print("Name: " + name)
    #print("Date of Birth: " + birth)
    #rint("Nationality: " + nat)
    #rint("Place one day race: " + OneDayRace)
    #rint("Place GCSingle: " + gcSingle)
    #rint("Place Time trial: " + timeTrial)
    #rint("Place climbing: " + climber)
    #rint("Place Sprinting: " + sprint)
    #rint("Place All time: " + alltime)
    #print("Place UCWorld: " + ucWorld)
    #rint("Place pcsRank: " + pcsRanking)     

    #DO: GATHER RACE DETAILS
    year = soup.find_all('a', class_ = 'seasonResults')
    j = 0
    checkYear = "0"
    for e in year:
        print("Race year")
        #DO: GET ALL YEAR RACE DETAILS
        y = e.text
        urlYears = "https://www.procyclingstats.com/rider/" + elem+ "/" + y
        result = requests.get(urlYears, headers=headers)
        soup = BeautifulSoup(result.text, "html.parser")
        race_info = soup.find('tbody')
        race_details = race_info.find_all('tr')

        #It continues after the last year
        if checkYear == y:
            break
        else:
            checkYear = "2023"
        
        i = 0
        #print("Year races: "+ urlYears)

        for element in race_details:
            #print("Race detail")
            data_td = element.find_all('td')
            date = data_td[0].text
            if date == "":
                date = temp + '(' + str(i) + ')'
                i += 1
            else:
                i = 0
                temp = date
            #print("Date: " + date)
            dates.append(date)
            

            result = data_td[1].text
            if result == "":
                resultStage = data_td[0].next
                results.append(resultStage)
                #print("Results stage: " + resultStage)
            else:
                results.append(result)
            
            #DO: GATHER POINTS
            race = element.find('a').text
            races.append(race)
            distance = data_td[5].text
            distances.append(distance)
            pointspc = data_td[6].text
            pointsPCS.append(pointspc)
            pointuci = data_td[7].text
            pointsUCI.append(pointuci)

            #PRINT STUFF
            #print("Race: " + race)
            #print("Results Race: " + result)
            #print("Distance: " + distance)
            #rint("Points PC: " + pointspc)
            #rint("Points UCI: " + pointuci)

        
    break




cyclist = pd.unique({
    'name' : names,
    'Date of birth' : dob,
    'Nation' : nats,
    'One day race' : odr,
    'GC' : gc,
    'time trials' : timeTrials,
    'sprint' : sprints,
    'climber' : climbers,
    'all time rank' : allTimes,
    'UCI World rank' : uciWorlds,
    'PC Ranking' : pcsRankings,
    'Date race' : dates,
    'Result Stage Race' : resultStages,
    'Result Race' : results,
    'Distance' : distances,
    'Points PC' : pointsPCS,
    'Points UCI' : pointsUCI
})



