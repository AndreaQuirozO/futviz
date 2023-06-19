import pandas as pd


df = pd.DataFrame(
    {
        "name": ["Chelsea", "Arsenal", "Manchester Utd"],
        "color": ["Blue", "#00FF00", "#0000FF"],
        "logo_url": ["https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Chelsea_FC.svg/1200px-Chelsea_FC.svg.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png"],
        "shirt_url": ["https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Chelsea_FC.svg/1200px-Chelsea_FC.svg.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png"],
        "goalkeeper_url": ["https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Chelsea_FC.svg/1200px-Chelsea_FC.svg.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png"]

    })


class Team:
    def __init__(self, team_df):
        self.name = team_df["name"].iloc[0]
        self.logo_url = team_df["logo_url"].iloc[0]
        self.color = team_df["color"].iloc[0]
        self.shirt_url = team_df["shirt_url"].iloc[0]
        self.goalkeeper_url = team_df["goalkeeper_url"].iloc[0]

    def get_name(self):
        return self.name

    def get_logo_url(self):
        return self.logo_url

    def get_color(self):
        return self.color

    def get_shirt_url(self):
        return self.shirt_url

    def get_goalkeeper_url(self):
        return self.goalkeeper_url


def global_data():
    prem = pd.read_csv("data/export.csv")
    return prem


def get_global_stats(team):
    team_df = df[df["name"] == team]
    team = Team(team_df)
    return team
