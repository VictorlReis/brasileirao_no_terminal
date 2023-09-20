from bs4 import BeautifulSoup
import requests


def obter_tabela_campeonato():
    url = "https://gauchazh.clicrbs.com.br/esportes/tabelas/brasileirao"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        team_table = soup.find('div', class_='team-table')

        stats_table = soup.find('div', class_='stats-table')

        team_names = [team.text.strip()
                      for team in team_table.find_all('span', class_='team_name')]

        status_rows = stats_table.find_all('tr')[1:]

        team_status = []
        for row in status_rows:
            cols = row.find_all('td')
            status = [col.text.strip() for col in cols]
            team_status.append(status)

        combined_data = []
        for i in range(len(team_names)):
            team_info = {
                'Posição': str(i+1).ljust(8),
                'Time': team_names[i].ljust(20),
                'P': team_status[i][0].ljust(5),
                'J': team_status[i][1].ljust(5),
                'V': team_status[i][2].ljust(5),
                'E': team_status[i][3].ljust(5),
                'D': team_status[i][4].ljust(5),
                'GP': team_status[i][5].ljust(5),
                'GC': team_status[i][6].ljust(5),
                'SG': team_status[i][7].ljust(5),
                '%': team_status[i][8].ljust(5)
            }
            combined_data.append(team_info)

        table_header = {
            'Posição': 'Posição'.ljust(8),
            'Time': 'Time'.ljust(20), 'P': 'P'.ljust(5), 'J': 'J'.ljust(5), 'V': 'V'.ljust(5),
            'E': 'E'.ljust(5), 'D': 'D'.ljust(5), 'GP': 'GP'.ljust(5), 'GC': 'GC'.ljust(5),
            'SG': 'SG'.ljust(5), '%': '%'.ljust(5)
        }

        header_row = [table_header[column] for column in table_header]
        header_row_str = ' | '.join(header_row)
        print(header_row_str)

        for row in combined_data:
            row_str = [row[column] for column in table_header]
            row_str = ' | '.join(row_str)
            print(row_str)


if __name__ == "__main__":
    obter_tabela_campeonato()
