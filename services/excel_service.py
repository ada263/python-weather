from pandas import DataFrame





def save_to_excel(data):
    try:
        df = DataFrame(data, index=[0])
        df.to_excel("weather.xlsx")
    except Exception as error:
        print(error)




