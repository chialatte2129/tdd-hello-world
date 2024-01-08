def run(year):
    if ( year % 400 ) == 0:
        return "is"
    if ( year % 100 ) == 0:
        return "is not"
    if ( year % 4 ) == 0:
        return "is"
    return "is not"