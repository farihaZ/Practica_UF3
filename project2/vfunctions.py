import lit as l
def validate_id():
    id = int(input(l.TEXT07))
    while id <= 0 :
        id = int(input(l.TEXT09))

    return id

def validate_time():
    hour = int(input(l.TEXT10))
    while hour < 10 or hour >20:
        hour = int(input(l.TEXT11))

    min = int(input(l.TEXT12))
    while min < 0 or min >59 :
        min = int(input(l.TEXT13))

    hora = str(hour )+":"+str(min)+":"+ "00"
    return hora
def validate_date():
    day = int(input(l.TEXT14))
    while day < 1 or day > 31 :
        day = int(input(l.TEXT15))
    month= int(input(l.TEXT16))
    while month < 1 or month > 31:
        month = int(input(l.TEXT17))
    year = int(input(l.TEXT18))
    while year < 2000 or year > 2023:
        year = int(input(l.TEXT19))

    date = str(year)+"-"+str(month)+"-"+str(day)
    return date