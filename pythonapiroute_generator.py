# !-----------------------------------------------------------------------------------------------------------------------------------
# ! Fast Api Route Generator
# !-----------------------------------------------------------------------------------------------------------------------------------
#! Bu program fast api için api yollarını istediğiniz dilde değişken olarak vermektedir.
#! This program provides API routes for fast api as variables in the language you want.
#! Dieses Programm bietet API-Routen für Fast API als Variablen in der von Ihnen gewünschten Sprache.
#!
#! Programın çalışması için .env dosyasına BASE_URL ve API_TAG anahtarlarını eklemeniz gerekmektedir.
#! To run the program, you need to add BASE_URL and API_TAG keys to the .env file.
#! Um das Programm auszuführen, müssen Sie die Schlüssel BASE_URL und API_TAG in die .env-Datei aufnehmen.
#!
#! Copyright
#! © 2021, Fast Api Route Generator by Ali Birkan BAYRAM
#!

#! Github -> https://github.com/alibirkanbayram
# !-----------------------------------------------------------------------------------------------------------------------------------

# !-----------------------------------------------------------------------------------------------------------------------------------
# ! Menu
# !-----------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from dotenv import set_key

flagFileRoute = {
    "TR": "assets/flag_tr.png",
    "EN": "assets/flag_en.png",
    "DE": "assets/flag_de.png"
}
helpMenuItems=[
    "Bu program fast api için api yollarını istediğiniz dilde değişken olarak vermektedir.",
    "This program provides API routes for fast api as variables in the language you want.",
    "Dieses Programm bietet API-Routen für Fast API als Variablen in der von Ihnen gewünschten Sprache."
]




class APIRouteGenerator(tk.Tk):

    # Base URL to .env docs save
    def saveBaseUrltoEnvFile(self, window, base_url):
        set_key('.env', 'BASE_URL', base_url)
        language = self.language_var.get()
        if language == "TR":
            message = "Ana URL kaydedildi:"
        elif language == "EN":
            message = "Base URL saved:"
        elif language == "DE":
            message = "Haupt-URL gespeichert:"
        print(message, base_url)
        window.destroy()

    # Set Api Tag
    def setApiTag(self, window, api_tag):
        set_key('.env', 'API_TAG', api_tag)
        language = self.language_var.get()
        if language == "TR":
            message = "API Etiketi kaydedildi:"
        elif language == "EN":
            message = "API Tag saved:"
        elif language == "DE":
            message = "API-Tag gespeichert:"

# !-----------------------------------------------------------------------------------------------------------------------------------
# ! Menu
# !-----------------------------------------------------------------------------------------------------------------------------------
def helpMenu(self):
    # Get language
    language = self.language_var.get()
    window = tk.Toplevel(self)
    window.title("Help")
    
    if language == "TR":
        label_text = helpMenuItems[0]
    elif language == "EN":
        label_text = helpMenuItems[1]
    elif language == "DE":
        label_text = helpMenuItems[2]
    else:
        label_text = helpMenuItems[1]
    
    label = ttk.Label(window, text=label_text)
    label.pack(padx=20, pady=10)
    
    # GitHub button
    github_button = ttk.Button(window, text="GitHub", command=lambda: self.open_url("https://github.com/username"))
    github_button.pack(pady=5)

    # Twitter button
    twitter_button = ttk.Button(window, text="Twitter", command=lambda: self.open_url("https://twitter.com/username"))
    twitter_button.pack(pady=5)

    # Instagram button
    instagram_button = ttk.Button(window, text="Instagram", command=lambda: self.open_url("https://instagram.com/username"))
    instagram_button.pack(pady=5)

def open_url(self, url):
    import webbrowser
    webbrowser.open_new(url)

    # Get API Tag
    def get_api_tag(self):
        api_tag = self.text1_entry.get()
        print("API Etiketi:", api_tag)

    # Get Data Source
    def get_data_source(self):
        data_source = self.text1_entry.get()
        print("Veri Kaynağı:", data_source)

    def __init__(self):
        super().__init__()

        self.title("API Route Generator")
        self.geometry("600x350")

        # Dil seçimi dropdown menüsü
        self.language_var = tk.StringVar()
        self.language_var.set("TR")  # Başlangıçta Türkçe seçili olsun

        self.language_dropdown = ttk.Combobox(self, textvariable=self.language_var, values=["TR", "EN", "DE"], state="readonly", width=5)
        self.language_dropdown.place(x=500, y=10)  # Sağ üst köşe için koordinatlar
        self.language_dropdown.bind("<<ComboboxSelected>>", self.refresh_menu)

        # Bayraklar
        self.flag_icons = {}
        for lang, fileRoute in flagFileRoute.items():
            flag = ImageTk.PhotoImage(Image.open(fileRoute).resize((20, 20)))
            self.flag_icons[lang] = flag

        self.flag_label = ttk.Label(self, image=self.flag_icons["TR"])
        self.flag_label.place(x=540, y=10)

        # Menü
        self.menu_frame = ttk.LabelFrame(self, text="Menu")
        self.menu_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.menu_options_tr = ["Ana URL", "API Etiketi", "Veri Kaynağı", "Çıkış"]
        self.menu_options_en = ["Base URL", "API Tag", "Data Source", "Exit"]
        self.menu_options_de = ["Haupt-URL", "API-Tag", "Datenquelle", "Beenden"]
        self.menu_buttons = []

        for i, option in enumerate(self.menu_options_tr, start=1):
            button = ttk.Button(self.menu_frame, text=option, command=lambda o=option: self.menu_selection(o))
            button.grid(row=i, column=0, pady=5)
            self.menu_buttons.append(button)

        # Logo
        logo_img = Image.open("assets/logo.png").resize((150, 150))
        logo_with_transparency = self.add_transparency(logo_img, 0.4)  # %40 transparanlık
        self.logo = ImageTk.PhotoImage(logo_with_transparency)
        self.logo_label = ttk.Label(self, image=self.logo)
        self.logo_label.place(relx=0.5, rely=0.05, anchor="n")

        # Soru işareti butonu
        self.question_button = ttk.Button(self, text="?", command=self.helpMenu)
        self.question_button.place(relx=1.0, rely=1.0, anchor="se")

    def refresh_menu(self, event=None):
        # Dil değiştiğinde menüyü yenile
        language = self.language_var.get()

        if language == "TR":
            options = self.menu_options_tr
        elif language == "EN":
            options = self.menu_options_en
        elif language == "DE":
            options = self.menu_options_de

        for button, option in zip(self.menu_buttons, options):
            button.config(text=option)

        self.flag_label.config(image=self.flag_icons[language])

    def menu_selection(self, option):
        if option == "Ana URL":
            self.get_base_url_window()
        elif option == "API Etiketi":
            self.get_api_tag()
        elif option == "Veri Kaynağı":
            self.get_data_source()
        elif option == "Çıkış":
            self.destroy()

    def get_base_url_window(self):
        language = self.language_var.get()
        window = tk.Toplevel(self)
        if language == "TR":
            window.title("Ana URL Girisi")
            label = ttk.Label(window, text="Ana URL Giriniz:")
        elif language == "EN":
            window.title("Enter Base URL")
            label = ttk.Label(window, text="Enter Base URL:")
        elif language == "DE":
            window.title("Haupt-URL eingeben")
            label = ttk.Label(window, text="Geben Sie die Haupt-URL ein:")
        else:
            window.title("Enter Base URL")
            label = ttk.Label(window, text="Enter Base URL:")

        label.pack(pady=10)

        entry = ttk.Entry(window)
        entry.pack(pady=5)
        if language == "TR":
            button = ttk.Button(window, text="Kaydet", command=lambda: self.saveBaseUrltoEnvFile(window, entry.get()))
        elif language == "EN":
            button = ttk.Button(window, text="Save", command=lambda: self.saveBaseUrltoEnvFile(window, entry.get()))
        elif language == "DE":
            button = ttk.Button(window, text="Speichern", command=lambda: self.saveBaseUrltoEnvFile(window, entry.get()))
        else:
            button = ttk.Button(window, text="Save", command=lambda: self.saveBaseUrltoEnvFile(window, entry.get()))
        button.pack(pady=5)


    def add_transparency(self, img, factor):
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[3] == 255:
                newData.append(item[:3] + (int(255 * factor),))
            else:
                newData.append(item)

        img.putdata(newData)
        return img


if __name__ == "__main__":
    app = APIRouteGenerator()
    app.mainloop()










# global language

# # Set the language
# def setLanguage():
#     global language
#     print ("TR | Hangi dilde API rotaları oluşturmak istersiniz?\n")
#     print ("EN | Which language do you want to create API routes in?\n")
#     print("English Lanuge : 1\n")
#     print("Türkçe Dil : 2\n")
#     language = int(input("TR | Dil Seçimi için giriş yapınız.\n EN | Enter for Language Selection.\n(1/2):"))

# # Menu Selection
# def menuSelection(selection:int =0):
#     if(selection =1):
#         setLanguage()
#     elif(selection =2):
#         baseURL = getBaseURL(language)
#     elif(selection =3):
#         apiTag = getApiTag(language)
#     elif(selection =4):
#         isAddBracket = getisAddBracket(language)
#         dataFormat = getDataFormat(language)
#         data = getData(language, dataFormat["source"])
#         if data["Success"]:
#             for route in data["Data"]:
#                 if isAddBracket:
#                     route = f"{baseURL}/{apiTag}/{route}"
#                 else:
#                     route = f"{baseURL}{apiTag}{route}"
#                 setTextFile(route)
#         else:
#             print("Data could not be retrieved.")
#     else:
#         if language == 1:
#             print("Invalid Selection. Please try again.")
#         else:
#             prin("Geçersiz seçim. Lütfen tekrar deneyin.")

# def setTextFile(api_routes):
#     with open(api_route_get_file, "a") as file:
#         file.write(api_routes+"\n")
#     file.close()

# def getBaseURL(language: int):
#     if language == 1:
#         return input("Enter the Main URL for the API: ")
#     else:
#         return input("API için ana URL (base URL) girin: ")

# def getApiTag(language: int):
#     if language == 1:
#         return input("Enter the URL Prefix for the API: ")
#     else:
#         return input("API için URL ön etiketi girin: ")

# def getisAddBracket(language: int):
#     if language == 1:
#         response= input("Do you want to put a \"/\" sign between the Main URL and the API? (Y/N): ")
#         if response.upper() == "Y":
#             return True
#         else:
#             return False
#     else:
#         response= input("API için Ana Url ile api arasına \"/\" işareti koyulmasını ister misiniz? (E/H): ")
#         if response.upper() == "E":
#             return True
#         else:
#             return False

# def getDataFormat(language: int):
#     if language == 1:
#         response= input("Determine the Source of the Data (Txt/Console) (T/C): ")
#         if response.upper() == "T":
#             return {"source": "T",}
#         else:
#             return {"source": "C",}
#     else:
#         response= input("Verilerin kaynağını belirleme (Txt/Konsol) (T/K): ")
#         if response.upper() == "T":
#             return {"source": "T",}
#         else:
#             return {"source": "C",}

# def getData(language: int, source: str):
#     if source.upper() == "T":
#         return data_function.getDataFromTxtFile()
#     else:
#         return data_function.getSelectedTerminalData()

# def main():
#     setLanguage()
#     while True:
#         if language == 1:
#             print("English API Route Generator Menu:\n")
#             print("Language Selection: 1\n")
#             print("Enter the Main URL for the API: 2\n")
#             print("Enter the URL Prefix for the API: 3\n")
#             print("Determine the Source of the Data: 4\n")
#         else:
#             print("Türkçe API Route Generator Menüsü:\n")
#             print("Dil Seçimi: 1\n")
#             print("Api İçin Ana Url Girişi için: 2\n")
#             print("Api İçin Url Ön Etiketi Girişi için: 3\n")
#             print("Verilerin Kaynağını Belirleme için: 4\n")
#             print("Çıkış: 0\n")
#         selection = int(input("TR| Seçim yapınız.\nEN| Make a selection.\n(Language:1,Base Url:2,Api Tag:3, Data Source: 4, Exit:0): "))
#         if selection == 0:
#             break
#         else:
#             menuSelection(selection)

# if __name__ == "__main__":
#     main()
