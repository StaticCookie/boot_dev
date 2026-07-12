## function sorts dates and calls format date
def sort_dates(dates: list[str]) -> list[str]:
    u_date = sorted(dates, key=format_date)
    return u_date


## Function sorts date from mm-dd-yyyy -> yyyy-mm-dd
def format_date(date: str) -> str:
    month, day, year = date.split("-")
    return year + month + day

