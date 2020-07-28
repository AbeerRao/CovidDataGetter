from covid import Covid
from matplotlib import pyplot as plt
import pandas as pd

#* The COVID obj
covid = Covid()

#* Asking the user which country they want no.1
def getCountry1():
    countryWants = input("What is the name of the country? ").title()
    print()

    if countryWants == "Uk":
        countryWants = "United Kingdom"
    elif countryWants == "Usa" or countryWants == "Us" or countryWants == "America":
        countryWants = "US"

    countryGot = covid.get_status_by_country_name(countryWants)
    print()

    baseToDisplay = "{name}:\nTotal Confirmed Cases: {cases}\nTotal Deaths: {deaths}\nTotal Recovered: {reco}\nCurrent Active Cases: {active}"
    print(baseToDisplay.format(
        name = countryGot["country"],
        cases = countryGot["confirmed"],
        deaths = countryGot["deaths"],
        reco = countryGot["recovered"],
        active = countryGot["active"]
    ))
    print()

    if countryGot == None:
        tryAgain = input("Country not found! Wanna try again? (y/n): ")
        print()
        if tryAgain == "y":
            getCountry1()
        elif tryAgain == "n":
            pass
    
    wantAnother = input("Would you like to get the data of another country? (y/n): ")
    print()
    if wantAnother == "y":
        getCountry2(countryWants)
    elif wantAnother == "n":
        pass
    
    return countryWants

#* Asking the user which country they want no.2
def getCountry2(c1):
    countryWants = input("What is the name of the country? ").title()
    print()

    if countryWants == "Uk":
        countryWants = "United Kingdom"
    elif countryWants == "Usa" or countryWants == "Us" or countryWants == "America":
        countryWants = "US"

    countryGot = covid.get_status_by_country_name(countryWants)
    print()

    baseToDisplay = "{name}:\nTotal Confirmed Cases: {cases}\nTotal Deaths: {deaths}\nTotal Recovered: {reco}\nCurrent Active Cases: {active}"
    print(baseToDisplay.format(
        name = countryGot["country"],
        cases = countryGot["confirmed"],
        deaths = countryGot["deaths"],
        reco = countryGot["recovered"],
        active = countryGot["active"]
    ))
    print()

    if countryGot == None:
        tryAgain = input("Country not found! Wanna try again? (y/n): ")
        print()
        if tryAgain == "y":
            getCountry2()
        elif tryAgain == "n":
            pass
    
    wantCompare = input("Would you like to compare the two countries? (y/n): ")
    if wantCompare == "y":
        compareCountries(c1, countryWants)
    elif wantCompare == "n":
        wantAnother = input("Would you like to get the data of another country? (y/n): ")
        print()
        if wantAnother == "y":
            getCountry1()
        elif wantAnother == "n":
            pass
    
    return countryWants

#* Comparing the countries
def compareCountries(C1, C2):
    country1Stats = covid.get_status_by_country_name(C1)
    country2Stats = covid.get_status_by_country_name(C2)

    if country1Stats["confirmed"] > country2Stats["confirmed"]:
        increase = country1Stats["confirmed"] - country2Stats["confirmed"]
        ans = str(round(((increase / country2Stats["confirmed"]) * 100 ), 2))
        print()
        print(f"{country1Stats['country']} has {ans}% more confirmed cases than {country2Stats['country']}")
    elif country2Stats["confirmed"] > country1Stats["confirmed"]:
        increase = country2Stats["confirmed"] - country1Stats["confirmed"]
        ans = str(round(((increase / country1Stats["confirmed"]) * 100 ), 2))
        print()
        print(f"{country2Stats['country']} has {ans}% more confirmed cases than {country1Stats['country']}")
    
    if country1Stats["deaths"] > country2Stats["deaths"]:
        increase = country1Stats["deaths"] - country2Stats["deaths"]
        ans = str(round(((increase / country2Stats["deaths"]) * 100 ), 2))
        print(f"{country1Stats['country']} has {ans}% more deaths than {country2Stats['country']}")
    elif country2Stats["deaths"] > country1Stats["deaths"]:
        increase = country2Stats["deaths"] - country1Stats["deaths"]
        ans = str(round(((increase / country1Stats["deaths"]) * 100 ), 2))
        print(f"{country2Stats['country']} has {ans}% more deaths than {country1Stats['country']}")
    
    if country1Stats["recovered"] > country2Stats["recovered"]:
        increase = country1Stats["recovered"] - country2Stats["recovered"]
        ans = str(round(((increase / country2Stats["recovered"]) * 100 ), 2))
        print(f"{country1Stats['country']} has {ans}% more recovered cases than {country2Stats['country']}")
    elif country2Stats["recovered"] > country1Stats["recovered"]:
        increase = country2Stats["recovered"] - country1Stats["recovered"]
        ans = str(round(((increase / country1Stats["recovered"]) * 100 ), 2))
        print(f"{country2Stats['country']} has {ans}% more recovered cases than {country1Stats['country']}")

    if country1Stats["active"] > country2Stats["active"]:
        increase = country1Stats["active"] - country2Stats["active"]
        ans = str(round(((increase / country2Stats["active"]) * 100 ), 2))
        print(f"{country1Stats['country']} has {ans}% more active cases than {country2Stats['country']}")
        print()
    elif country2Stats["active"] > country1Stats["active"]:
        increase = country2Stats["active"] - country1Stats["active"]
        ans = str(round(((increase / country1Stats["active"]) * 100 ), 2))
        print(f"{country2Stats['country']} has {ans}% more active cases than {country1Stats['country']}")
        print()

    params = ["Confirmed", "Active", "Deaths", "Recovered"]
    country1StatsInList = []
    country2StatsInList = []

    for x, y in country1Stats.items():
        if x != 'id' and x != 'country' and x != 'latitude' and x != 'longitude' and x != 'last_update':
            country1StatsInList.append(y)
    for x, y in country2Stats.items():
        if x != 'id' and x != 'country' and x != 'latitude' and x != 'longitude' and x != 'last_update':
            country2StatsInList.append(y)

    plt.bar(params,
            country1StatsInList,
            label = country1Stats["country"])
    plt.bar(params,
            country2StatsInList,
            bottom = country1StatsInList,
            label = country2Stats["country"])
    plt.legend()
    plt.show()

#* Calling the function
getCountry1()