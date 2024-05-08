import os

load_dotenv()

api_route_get_file_route = os.getenv("API_ROUTE_GET_FILE")
api_route_set_file_route = os.getenv("API_ROUTE_SET_FILE")

# Line Proccess Function
def lineProcess(line: list, apiRoute: list):
    for line in lines:
        if "@app." in line:
            start_index = line.find('"') + 1
            end_index = line.find('"', start_index)
            route = line[start_index:end_index]

            # Eğer "{" parantezi varsa, onu ve sonrasındaki kısmı sil
            if '{' in route:
                route = route.split('{')[0]
            api_routes.append(route.strip())
    return apiRoute

# Get data from txt file unrequest file route
def getDataFromTxtFile(getDataFileRoute: str= None):
    apiRoutes = []
    # Get data from txt file
    if getDataFileRoute is None:
        fileRoute = api_route_get_file_route
    else:
        fileRoute = getDataFileRoute
    with open(fileRoute, "r") as file:
        data = file.read()
    file.close()

    lines = data.split("\n")
    # Line process
    response= lineProcess(lines, apiRoutes)
    if response is not None:
        return {'Success': True, 'Data': response}
    else:
        return {'Success': False}

def getSelectedTerminalData():
    apiRoutes = []
    # Get data from terminal
    while True:
        print("Enter the API routes one by one. If you want to finish, enter 'exit'.")
        route = input("Enter the API route: ")
        if route == "exit":
            break
        apiRoutes.append(route)
    setDatatoTxtFile(apiRoutes)
    return apiRoutes

# Set data to txt file
def writeDatatoTxtFile(setDataFileRoute: str= None, apiRoutes: list):
    # Get data from txt file
    if fileRoute is None:
        fileRoute = api_route_set_file_route
    else:
        fileRoute = setDataFileRoute

    # Write data to txt file
    with open(fileRoute, "w") as file:
        for route_url in apiRoutes:
            if '/' in route_url:
                route_name = route_url.split('/')[1]
            else:
                route_name = route_url
            if api_tag != "":
                if api_tag.upper() == "E":
                    route_url = f"{base_url}/{api_tag}/{route_url}"
                else:
                    route_url = f"{base_url}{api_tag}{route_url}"
            else:
                if api_tag.upper() == "E":
                    route_url = f"{base_url}/{route_url}"
                else:
                    route_url = f"{base_url}{route_url}"
            file.write(f'static const String {route_name} = "{route_url}";\n')
    file.close()
    if language == 1:
        print("The routes have been created successfully.")
    else:
        print("Rotalar başarıyla oluşturuldu.")

def setDatatoTxtFile(apiRoute: list):
    # Write data to txt file
    with open(api_route_set_file_route, "w") as file:
        for route_url in api_routes:
            file.write(route_url+"\n")
    file.close()
    if language == 1:
        print("The entered routes were written to txt file.")
    else:
        print("Girilen rotalar txt dosyasına yazıldı.")
