import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from visualization import *
from AnalyseData import Analyse

engine = create_engine('sqlite:///db.sqlite3') 
Session = sessionmaker(bind=engine)
sess = Session()

analysis = Analyse("datasets/vgsales.csv")


st.title('Video Games Sales Analysis')
st.image("https://blog.vinfotech.com/sites/default/files/styles/blog-list-img-new/public/how-to-build-a-successful-real-money-gaming-website-banner.png?itok=MJI4LKyG")

st.markdown("""
##### Made By - Rohan Kr Ojha
""")

st.markdown("----")

sidebar = st.sidebar


def viewDataset():
    st.markdown("""
    ### In this project, I have analyzed the most sold games in the global perspective, then analyze the games in terms of genre and platform, the game genres according to the region with game names and finally the year the most sold games are released and their publishers. Also some information are given about games, publishers and platforms.
    """)

    st.text(" ")
    st.text(" ")
    st.markdown("---")
    st.header("Dataset Used for Video Game Sales Analysis")
    dataframe = analysis.getDataframe()

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")


def analysePlatform():
    data = analysis.getPlatform()
    st.plotly_chart(plotBar(analysis.getPlatform(
    ), 'Video Games Sales Platform Data', 'Name of Platform', 'Global sales in millions'))
    st.markdown("""
    ### In this graph, it shows that the global sales in million dollars platform wise which the top platform is PS2 and revenue is about 1200 millions dollars and after that X360 and this platform revenue is about 980 million dollars , the PS2 platform is highly demanded which gamers like to play most game and this platform PCFX is not popular and revenue is about 0.03 million dollars """)


def analysePublisher():

    

    num = st.select_slider(
        options=[5, 10, 15, 20, 25, 30], label="Select the number of Publishers to show")
    st.header('Top Publishers By Release Count')
    st.plotly_chart(plotBar(analysis.getTopPublishersByCount(
        num), 'Video Games Sales Publisher Data', 'Name Of Publisher', 'Total sales in millions'))
    st.markdown("""
    ### In this graph, it shows the top publishers which are the highest in global sales and the top publisher is electronics arts which total sales is about 1350 million dollars and Electronic Arts is a leading publisher of games on Console, PC and Mobile. We exist to inspire the world through Play. Electronic Arts is a leading publisher of games on Console, PC and Mobile. EA Play FIFA 21 Madden NFL 21 Apex Legends Star Wars.
    # """)

    st.markdown("""
    ### The second top publishers is activision which global sales is about 950 million dollars and Activision Publishing, Inc. is an American video game publisher based in Santa Monica, California. It currently serves as the publishing business for its parent company, Activision Blizzard, and consists of several subsidiary studios. Activision is one of the largest third-party video game publishers in the world and was the top United States publisher in 2016.
     """)

    st.markdown("""
    """)
    st.markdown("""
    """)
    st.markdown("""
    """)
    st.markdown("""
    """)
    st.markdown("""
    """)
    st.markdown("""
    ---------
    """)
    st.header('Top Publishers By Total Sales')
    st.plotly_chart(plotBar(analysis.getTopPublishersBySum(
        num), 'Total Sales of Publisher Data', 'Name Of Publisher', 'Global sales in millions'))

    st.markdown(""" In this graph, it shows the top publishers which are the highest in total sales and the top publisher is Nintendo which total sales is about 1700 million dollars and 
Nintendo Co., Ltd. is a Japanese multinational consumer electronics and video game company headquartered in Kyoto. The company was founded in 1889 as Nintendo Karuta by craftsman Fusajiro Yamauchi and originally produced handmade hanafuda playing cards. After venturing into various lines of business during the 1960s and acquiring a legal status as a public company under the current company name, Nintendo distributed its first video game console, the Color TV-Game, in 1977. It gained international recognition with the release of the Nintendo Entertainment System in 1985.

The second top publishers is Electronics Arts and total sales is about 1100 million dollars and Electronic Arts is a leading publisher of games on Console, PC and Mobile.

    """)

    st.header('Top Publishers By Total Sales in Region')
    for region, name in analysis.getRegion():
        st.plotly_chart(plotBar(analysis.getTopPublishersBySumInRegion(
            num, region), 'Total Sales in '+name, 'Top Publisher', 'Global sales in millions'))
            


def analyseGenre():

    st.header('Top Genres By Release Count')
    st.plotly_chart(plotBar(analysis.getTopGenresByCount(),
                            'Top Genre', 'Name Of Genre', 'Global sales in millions'))
    st.markdown(""" In this graph we can see that the top genres and its release count and the top genre is Action and its release count is about 3100 million dollars and the next top genre is sports and its release count is about 2300 million dollars and after Misc is about 1700 million dollars release count.
    """)

    st.header('Top Genres By Total Sales')
    st.plotly_chart(plotBar(analysis.getTopGenresBySum(
    ), ' Total Sales of Top Genre', 'Name Of Genre', 'Global sales in millions'))
    st.markdown(""" In this graph we can see that the top genres and its total sales and the top genre is Action and its total sales is about 1700 million dollars and the next top genre is sports and its total sales is about 1300 million dollars and after shooter is about 1000 million dollars total sales.
    """)
    
    st.header('Top Genres By Total Sales in Region')
    for region, name in analysis.getRegion():
        st.plotly_chart(plotBar(analysis.getTopGenresBySumInRegion(
            region), 'Total Sales By Region of Top Genre '+name, 'Name Of Genre', 'Global sales in millions'))
       
      
        

def analyseGameRelease():
    st.header("Year wise release")
    st.plotly_chart(plotLine(analysis.getYearWiseRelease(),
                             'Exponential Growth in Video Games sales can be seen after 2000 as many new Gaming Plaforms such as Playstation, Xbox etc. were released', 'Year', 'Global releases'))
    st.markdown("""
    ###  In this graph , here the growth of video game year wise from 1980 up to 2016 and we see that in 2008 - 2009 the highest growth of game during this year because PC games are highly demanded after 2001and also gamers like to play but after 2009 we also see that, the graph goes deep because of the publisher not releases that type of game which gamers like it and also in 2015, the publisher releases good game and also by time gamers switches from PC to mobile.
    # """)


sidebar.title('Video Games Sales Analysis')
sidebar.header('Choose Your Option')
options = ['View Database', 'Timeline Analysis',
           'Analyse Platform', 'Analyse Publisher', 'Analyse Genre']
choice = sidebar.selectbox(options=options, label="Choose Action")
with st.spinner("please wait.."):
    if choice == options[0]:
        viewDataset()
    elif choice == options[1]:
        analyseGameRelease()
    elif choice == options[2]:
        analysePlatform()
    elif choice == options[3]:
        analysePublisher()
    elif choice == options[4]:
        analyseGenre()
