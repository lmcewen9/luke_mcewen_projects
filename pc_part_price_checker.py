from bs4 import BeautifulSoup
import requests


def add_to_dic(page):
    dic = {}

    for i in range(len(page)):
        try:
            name = page[i].find(class_="item-title").text
            tmp = page[i].find(class_="price-current")
            price = tmp.find("strong")
            dic[name] = price.string
        except:
            pass
    return dic

def search_dictionary(dic, component, high_price, low_price=0):
    flag = 0
    for i in dic:
        if int(dic[i].replace(",", "")) >= low_price and int(dic[i].replace(",", "")) <= high_price:
            flag += 1
            print(i + " is $" + dic[i] + "\n")
    if flag == 0:
        print(f"There are no {component} which match your price point.")


def main():
    print("\n\tWelcome to computer system price checker\n")
    d = False
    while not d:
        _input = input("Which part would you like to look for today (Enter help for list of parts): ")
        if _input.lower() == "help":
            print("Parts you can search for are Graphics Card, Processor-Intel, Processor-AMD, RAM, Motherboard-Intel, Motherboard-AMD.")
        elif _input.lower() == "graphics card":
            source = requests.get("https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96&Order=4").text
            d = True
            component = "graphics cards"
        elif _input.lower() == "processor-intel":
            source = requests.get("https://www.newegg.com/p/pl?N=100007671%20601306860&PageSize=96&Order=4").text
            d = True
            component = "intel processors"
        elif _input.lower() == "processor-amd":
            source = requests.get("https://www.newegg.com/p/pl?N=100007671%20601306869&PageSize=96&Order=4").text
            d = True
            component = "AMD processors"
        elif _input.lower() == "ram": 
            source = requests.get("https://www.newegg.com/Desktop-Memory/SubCategory/ID-147?Tid=7611&PageSize=96&Order=4").text  
            d = True
            component = "RAM's"
        elif _input.lower() == "motherboard-intel":
            source = requests.get("https://www.newegg.com/Intel-Motherboards/SubCategory/ID-280?Tid=7627&PageSize=96&Order=4").text
            d = True
            component = "intel motherboards"
        elif _input.lower() == "motherboard-amd":
            source = requests.get("https://www.newegg.com/AMD-Motherboards/SubCategory/ID-22?PageSize=96&Order=4").text
            d = True
            component = "AMD motherboards"
        else:
            print("Please enter a valid part name.")
    soup = BeautifulSoup(source, "html.parser")
    page_content = soup.find_all(class_="item-container")
    dic = add_to_dic(page_content)
    done = False
    while not done:
        high = input("Please enter the maximum price (Please exlcude '$'): ")
        low = input("Please enter the minimum price (For 0 hit enter): ")
        print()
        if low == "":
            low = 0
        
        try:
            high = int(high)
            low = int(low)
            done = True
        except:
                print("Please enter number values, dont't forget to exclude '$'")
    search_dictionary(dic, component, high, low)

if __name__ == "__main__":
    main()