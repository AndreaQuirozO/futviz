import streamlit as st
from data.global_stats import global_data
import page_controler.main_page


def columns():
    df = global_data()
    txt = ""
    for i in df.columns:
        txt += f"""<th>
            {i}
        </th>"""
    return txt


def get_rows():
    df = global_data()
    txt = ""
    for i in range(len(df)):
        txt += "<tr>"
        for j in df.columns:
            if j == "Team":
                txt += f"""<td>
                <a href="/table?team={df[j].iloc[i]}" target="_self" class="equipo_row">
                    {df[j].iloc[i]}
                </a>"""
            else:
                txt += f"""<td>
                    {df[j].iloc[i]}
                </td>"""
        txt += "</tr>"
    return txt


def main():
    st.set_page_config(layout="wide", page_title="FUTVIZ")
    html, css = page_controler.main_page.page("input")
    cols = columns()
    rows = get_rows()
    html = html.replace("{{variable}}", "Premier League")
    html = html.replace("{{ info_columns }}", cols)
    html = html.replace("{{ info_rows }}", rows)
    st.markdown(html, unsafe_allow_html=True)
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
