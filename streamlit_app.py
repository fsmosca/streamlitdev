import streamlit as st


st.set_page_config(layout='wide')


def Home():
    st.header('Streamlit Navigator')

    st.markdown('A new page navigation system is introduced by the latest streamlit version.')


def main():
    pg = st.navigation({
        "Overview": [
            st.Page(Home, title="Home", default=True, icon=":material/home:")
        ],
        "Sports": [
            st.Page('sports/basketball.py', title="Basketball", icon=":material/sports_basketball:"),
            st.Page('sports/cricket.py', title="Cricket", icon=":material/sports_cricket:"),
            st.Page('sports/soccer.py', title="Soccer", icon=":material/sports_soccer:")
        ]
    })

    try:
        pg.run()
    except Exception as e:
        st.error(f"Something went wrong: {str(e)}", icon=":material/error:")


if __name__ == '__main__':
    main()
