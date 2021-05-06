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
st.header("In my project, analysis the sales of games according to ranking wise, revenue wise, growth wise and my project also analyze the pupolarity of games according to genre, platform, publisher")

st.markdown("    ")
st.markdown("    ")
st.markdown("    ")
st.markdown("----")


sidebar = st.sidebar

def viewForm():

    st.plotly_chart(plot())

    title = st.text_input("Report Title")
    desc = st.text_area('Report Description')
    btn = st.button("Submit")

    if btn:
        report1 = Report(title = title, desc = desc, data = "")
        sess.add(report1)
        sess.commit()
        st.success('Report Saved')

def viewDataset():
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

        types = {'object' : 'Categorical', 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")

  


def analyse():
    data = analysis.getpublisher()
    st.plotly_chart(plotBar(data.index, data.values))

def analysePlatform():
    data = analysis.getPlatform()
    st.plotly_chart(plotBar(analysis.getPlatform(), 'VG Sales Platform Data', 'Name of Platform', 'Number Of Sales'))

def analysePublisher():

    num = st.select_slider(options=[5, 10, 15, 20, 25, 30], label="Select the number of Publishers to show")
    st.header('Top Publishers By Release Count')
    st.plotly_chart(plotBar(analysis.getTopPublishersByCount(num), 'VG Sales Publisher Data', 'Name Of Publisher', 'Number Of Sales'))

    st.header('Top Publishers By Total Sales')
    st.plotly_chart(plotBar(analysis.getTopPublishersBySum(num), 'Total Sales of Pubisher Data', 'Name Of Publisher', 'Number Of Sales'))

    st.header('Top Publishers By Total Sales in Region')
    for region, name in analysis.getRegion():
        st.plotly_chart(plotBar(analysis.getTopPublishersBySumInRegion(num, region), 'Total Sales in '+name, 'Top Publisher', 'Number Of Sales'))

def analyseGenre():

    st.header('Top Genres By Release Count')
    st.plotly_chart(plotBar(analysis.getTopGenresByCount(), 'Top Genre', 'Name Of Genre', 'Number Of Sales'))

    st.header('Top Genres By Total Sales')
    st.plotly_chart(plotBar(analysis.getTopGenresBySum(), ' Total Sales of Top Genre', 'Name Of Genre', 'Number Of Sales'))

    st.header('Top Genres By Total Sales in Region')
    for region, name in analysis.getRegion():
        st.plotly_chart(plotBar(analysis.getTopGenresBySumInRegion(region), 'Total Sales By Region of Top Genre '+name, 'Name Of Genre', 'Number Of Sales'))

    st.header('Top Genres By Total Sales in Region')
    for region, name in analysis.getRegion():
        st.plotly_chart(plotBar(analysis.getTopGenresByCountInRegion(region), 'Total Release Count in '+name, 'Name Of Genre', 'Number Of Sales'))
   

def analyseGameRelease():
    st.header("Year wise release")
    st.plotly_chart(plotLine(analysis.getYearWiseRelease(), 'Game Growth By Year', 'Year', 'Number Of Sales'))

# def 

def viewReport():
    reports = sess.query(Report).all()
    titlesList = [ report.title for report in reports ]
    selReport = st.selectbox(options = titlesList, label="Select Report")
    
    reportToView = sess.query(Report).filter_by(title = selReport).first()

    markdown = f"""
        ## {reportToView.title}
        ### {reportToView.desc}
        
    """

    st.markdown(markdown)

sidebar.header('Choose Your Option')
options = [ 'View Database', 'Timeline Analysis', 'Analyse Platform', 'Analyse Publisher', 'Analyse Genre' ]
choice = sidebar.selectbox( options = options, label="Choose Action" )

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