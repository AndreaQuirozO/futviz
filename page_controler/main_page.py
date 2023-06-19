import pandas as pd
from data.global_stats import get_global_stats


def page(page_controller, team=None):
    if page_controller == "output":
        team_df = get_global_stats(team)
        # Display input
        with open("templates/selected_team.html", "r") as f:
            html = f.read()
            html = html.replace("{{name}}", team_df.get_name())
        with open("design/style.css", "r") as f:
            css = f.read()
            css = css.replace("--color", team_df.get_color())
        return html, css
    elif page_controller == "input":
        with open("templates/team_select.html", "r") as f:
            html = f.read()
        with open("design/style.css", "r") as f:
            css = f.read()
            css = css.replace("--color", "red")
        return html, css

