from sql_interaction import make_table, get_genres, get_auth
import pandas as pd


def render_table():
    table = make_table()
    data = {"Title": table[0],
            "Author": table[1],
            "Genre": table[2]}

    data_frame = pd.DataFrame(data, columns=["Title", "Author", "Genre"])

    return data_frame


def render_research(keyword, optkey=""):
    genr_results = get_genres(keyword)
    auth_results = get_auth(keyword, optkey)

    if genr_results != []:

        data = {"Book Matches": genr_results}

        data_frame = pd.DataFrame(data, columns=["Book Matches"])

        return data_frame

    elif auth_results != []:

        data = {"Book Matches": auth_results}

        data_frame = pd.DataFrame(data, columns=["Book Matches"])

        return data_frame

    else:
        return f" > No match found for keyword '{keyword}'"
