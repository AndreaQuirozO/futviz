import streamlit as st


def main():
    st.title(st.experimental_get_query_params()["team"][0])


if __name__ == "__main__":
    main()