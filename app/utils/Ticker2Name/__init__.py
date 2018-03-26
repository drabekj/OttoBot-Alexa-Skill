from bs4 import BeautifulSoup as bs
from urllib.request import urlopen


# TODO cite https://stackoverflow.com/questions/43907977/finding-company-name-from-a-ticker-in-bloomberg

def ticker_to_name(ticker, corp_suffix=False):
    url = "https://www.bloomberg.com/markets/symbolsearch?query=" + ticker
    soup = bs(urlopen(url), "html.parser")

    tables = soup.findAll("table", {"class": "dual_border_data_table"})
    if len(tables) > 0:
        # parse first row in table
        bm_table = tables[0]
        rows = bm_table.findAll("tr")
        row = rows[1]

        # check if the ticker matches
        cells = row.findAll("td")
        if cells[0].get_text().split(':')[0] == ticker:
            company_name = cells[1].get_text()
            if corp_suffix:
                return company_name
            else:
                return _remove_corp_suffix(company_name)
    return ""


def _remove_corp_suffix(company_name):
    suffix_list = ['inc', 'Inc', 'Corp', 'corp']

    split_words = company_name.split()
    if split_words[-1] in suffix_list:
        company_name = " ".join(split_words[:-1])

    return company_name
