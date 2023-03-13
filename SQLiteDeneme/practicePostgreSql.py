import requests

def havaDurumu():
    url_link = "http://api.weatherapi.com/v1/current.json"
    access_key = "fe661b56017447dab3d24625220704"

    iller = [
        "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"
    ]

    veriler = []

    for i in iller:
        response = requests.get(url=url_link, params={
            "key": access_key, "q": i}).json()

        try:
            if response["current"]["temp_c"] > 13:

                deger = {
                    "il": response["location"]["name"],
                    "sicaklik": response["current"]["temp_c"],
                    "tarih": response["location"]["localtime"][:-6]
                }
                veriler.append(deger)

            else:
                continue

        except:
            continue

    # print("0 :: ",veriler[0])
    # values=veriler[0].values()
    # values=list(values)
    # for i in values:
    #     print(i)
    
    # print("burada:", values[0])

    vaalues = veriler.values()
    print(vaalues)
    



havaDurumu()
