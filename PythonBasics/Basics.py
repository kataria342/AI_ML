# pizzaList = ["PizzaA", "PizzaB", "PizzaC"]
#
# for i in pizzaList:
#     print(i, " on offer")
#
# print("I like pizza")
#
# animalList = ["Cat", "Tiger", "Leopard"]
#
# for i in animalList:
#     print(i, " is a great animal")
#
# print("I love to pet animals")
#
# for i in range(1, 21):
#     print(i)
oneMillionList = []
for i in range(1000001):
    oneMillionList.append(i);
for i in oneMillionList:
    print(i)

print("Min number is : ", min(oneMillionList))
print("Max number is : ", max(oneMillionList))
print("Sum is : ", sum(oneMillionList))

oddNumbersList = []
for i in range(1, 21, 2):
    oddNumbersList.append(i)

for i in oddNumbersList:
    print(i)

buffetList = ("Food1", "Food2", "Food3", "Food4", "Food5")

for i in buffetList:
    print(i)

# buffetList[1] = "NewValue"
ls = list(buffetList)
ls[0] = "NewFood1"
ls[1] = "NewFood2"
buffetList = tuple(ls)
print(buffetList)


def make_shirt(shirtSize='Large', shirtText='I love Python'):
    print("Size -", shirtSize, " : Text - ", shirtText)


make_shirt('Medium', 'Prabhjeet')

size = input("Enter your size")
text = input("Enter your text")
make_shirt(size, text)
make_shirt()
make_shirt("Medium")
make_shirt("Very Large", "USA")


def describe_city(city, country="USA"):
    print(city, "is in ", country)


describe_city('Toronto', 'Canada')
describe_city('New York')
describe_city('New York')


def city_country(cityName, country):
    str = cityName+" , "+country
    return str


print(city_country("Brampton", "Canada"))
print(city_country("Mississauga", "Canada"))
print(city_country("Etobicoke", "Canada"))

def make_album(artistname, albumtitle, none=0):
    if(none > 0):
        dict = {
            "Artist Name" : artistname,
            "Album Name" : albumtitle,
            "Number of Songs" : none
             }
    else:
        dict = {
            "Artist Name" : artistname,
            "Album Name" : albumtitle
             }
    return dict


print(make_album("SingerA", "AlbumA"))
print(make_album("SingerB", "AlbumB"))
print(make_album("SingerB", "AlbumB", 10))

while True:
    singerName = input("Enter Singer Name: \n")
    albumName = input("Enter Album name: \n")
    print(make_album(singerName, albumName))
    quit()
