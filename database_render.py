from sql_interaction import make_table


def render_table():
    table = make_table()
    data = {"Title": table[0],
            "Author": table[1],
            "Genre": table[2]}

    data_frame = pd.DataFrame(data, columns=["Title", "Author", "Genre"])

    return data_frame
