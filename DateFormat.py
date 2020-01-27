def format_date(date):
    myDateList = date.split("/")
    newFormat = myDateList[2]+myDateList[1]+myDateList[0]
    return newFormat

    

def main():
    oldDate = "11/12/2019"
    format_date(oldDate)


if __name__ == "__main__":
    main()