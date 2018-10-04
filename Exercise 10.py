import requests
import time
import os

def menu():
    """This function is used as the main menu to navigate through the options"""

    wipe_screen()
    print "+--------------------------------------------------------------------+"
    print "|Introduction to Computer Science - Exercise 10  (ten)               |"
    print "+--------------------------------------------------------------------+"
    print "|To exit, Type: 1                                                    |"
    print "|For the supported crypto-currencies, Type: 2                        |"
    print "|For the prices at a given time stamp, Type: 3                       |"
    print "+--------------------------------------------------------------------+"
    while True:
        selectedOption = raw_input(">> ")
        if (selectedOption == "1"):
            raise SystemExit
        elif (selectedOption == "2"):
            option2()
        elif (selectedOption == "3"):
            option3()
        else:
            print "Your input doesn't match the available options. Please try again!"

def go_back():
    """This function is used to go back to the main menu"""

    selectedOption = raw_input("Press ENTER to go back >> ")
    menu()

def wipe_screen():
    """This function is used to clear the console for better readability. Mainly used for creating the UI tables"""

    os.system('cls' if os.name=='nt' else 'clear')

def fetch_results(cryptocoin, date, equalityCoin="EUR"):
    """This function is used to connect with the API and return the results for the given cryptocoin"""

    apiURL = "https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}".format(cryptocoin, "EUR", date)
    print "URL Used: {}".format(apiURL)
    r = requests.get(apiURL)
    if (r.status_code == 200):
        r = r.json()
        return (cryptocoin, r[cryptocoin][equalityCoin])
    else:
        print "Failed to connect with the server. Please try again later."


def option2():
    """This function wraps the whole logic behind the option 2"""

    wipe_screen()

    # A not so clever way to create the UI tables
    def maxLen(keyword, columnName, flag):
        maxLen = len(columnName)
        for i in r["Data"]:
            if (len(r["Data"][i][keyword]) > maxLen):
                maxLen = len(r["Data"][i][keyword])
        if (flag == 0):
            return maxLen
        else:
            return (maxLen - len(columnName))

    apiURL = "https://www.cryptocompare.com/api/data/coinlist/"
    r = requests.get(apiURL)
    if (r.status_code == 200):
        r = r.json()
        lenOfName = len("Name")
        lenOfFullName = len("Full Name")
        lenOfTotalCoinSupply = len("Total Coin Supply")
        print "+{}+{}+{}+".format("-" * maxLen("Name", "Name", 0), "-" * maxLen("CoinName", "Coin Name", 0), "-" * maxLen("TotalCoinSupply", "Total Coin Supply", 0))
        print "|Name{}|Full Name{}|Total Coin Supply{}|".format(" " * maxLen("Name", "Name", 1), " " * maxLen("CoinName", "Coin Name", 1), " " * maxLen("TotalCoinSupply", "Total Coin Supply", 1))
        print "+{}+{}+{}+".format("-" * maxLen("Name", "Name", 0), "-" * maxLen("CoinName", "Coin Name", 0), "-" * maxLen("TotalCoinSupply", "Total Coin Supply", 0))
        for i in r["Data"]:
            if not(i == "XPOKE"):
                print "|{}{}|{}{}|{}{}|".format(r["Data"][i]["Name"],  " " * (maxLen("Name", "Name", 0) - len(r["Data"][i]["Name"])),
                r["Data"][i]["CoinName"], " " * (maxLen("CoinName", "Coin Name", 0) - len(r["Data"][i]["CoinName"])),
                r["Data"][i]["TotalCoinSupply"], " " * (maxLen("TotalCoinSupply", "Total Coin Supply", 0) - len(r["Data"][i]["TotalCoinSupply"])))
        print "+{}+{}+{}+".format("-" * maxLen("Name", "Name", 0), "-" * maxLen("CoinName", "Coin Name", 0), "-" * maxLen("TotalCoinSupply", "Total Coin Supply", 0))
    else:
        print "Failed to connect with the server. Please try again later."
    go_back()

def option3():
    """This function wraps the whole logic behind the option 3"""

    try:
        # Receives the name of the deseirable Cryptocurrencies
        wipe_screen()
        print "Use Option 2 to check the available cryptocurrencies."
        currencyList = raw_input("Type the names of the Cryptocurrencies(seperated by commas) >> ").replace(" ", "").upper()
        currencyList = currencyList.split(",")
        wipe_screen()

        # Receives and converts the desirable date from human to epoch/unix form
        date = raw_input("Type the date you want to get results (Valid Format: DD.MM.YYYY HH:MM:SS)>> ")
        date = int(time.mktime(time.strptime(date, "%d.%m.%Y %H:%M:%S")))

        wipe_screen()

        # Output is a list of tuples i.e [("CoinName","Value in Euros"), ..., ()]
        output = [fetch_results(i,date) for i in currencyList]

        # Sorting the output
        for i in range(0, len(output)):
            for j in range(i,len(output)):
                if (output[i][1] > output[j][1]):
                    temp = output[i]
                    output[i] = output[j]
                    output[j] = temp
        for i in output:
            print "1 {} is {} EUR(s)".format(i[0], i[1])
    except:
        wipe_screen()
        print  "Something went wrong! Please check your inputs again."

    go_back()

menu()
