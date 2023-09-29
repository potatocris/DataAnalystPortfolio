import streamlit as st
import base64
from PIL import Image
import plotly.express as px
import pandas as pd
import plotly
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser

st.set_page_config(page_title = "Cristian Rivas - Data Analyst", layout = "wide")

#tabs
tab1, tab2, tab3 = st.tabs(["Portfolio", "Tech Stack", "CV"])

with tab1:
    
    col1, col2, col3, col4 = st.columns([2, 4, 0.3, 1])
    
    with col1:
        profile_pic = Image.open("profile_pic.jpg")
        st.image(profile_pic, width = 180)

    with col2:
        st.title("Cristian Rivas")
        st.subheader("Data Analyst")
        st.write("email: crisalexis3008@gmail.com")
        
    with col3:   
        st.image(Image.open("icons/Linkedin.png"), width = 30)#linkedin
        st.write("")
        st.image(Image.open("icons/upwork.png"), width = 70)#upwork
        st.write(" ")
        st.image(Image.open("icons/githubcat.png"), width = 30) #github
        
    with col4:
        if st.button("LinkedIn"):
            webbrowser.open_new_tab("https://www.linkedin.com/in/cristian-rivas-0b4a0212b/")
        if st.button("Hire me on UpWork"):
            webbrowser.open_new_tab("https://www.upwork.com/freelancers/cristianr16")
        if st.button("GitHub"):
            webbrowser.open_new_tab("https://github.com/potatocris/DA")#github

    st.divider()
    colp1, colp2, colp3 = st.columns(3)
    
    #Maritime Dashbaord
    with colp1:
        with st.container():
            
            st.markdown("#### Tableau Revenue Dashbaord")
            st.image(Image.open("portfolio_examples/Maritime_revenue.png"))
            #st.image(Image.open("portfolio_examples/maritime_revenue_feedback.png"))
            
            col1, col2, col3 = st.columns([1, 1, 8])
            with col1:
                st.image(Image.open("icons/python.png"), width = 30)
            with col2: 
                st.image(Image.open("icons/tableau.png"), width = 160)
            with st.expander("Project Summary"):
                st.write("""
                         Objective: Link revenue to marketing strategies. 
                         Actions:
                         - Data processing with Python
                         - Parsing of text to extract mentions of marketing with FuzzyWuzzy
                         - Monthly reports with Tableau
                         """)
    
    #Streamlit dashbaord
    with colp2:
        with st.container():
            st.markdown("#### Streamlit Performance Web App")
            st.image(Image.open("portfolio_examples/streamlit_sports.png"))
            
            col1, col2, col3 = st.columns([1, 1, 8])
            with col1:
                    st.image(Image.open("icons/python.png"), width = 30)
            with col2: 
                st.image(Image.open("icons/streamlit.png"), width = 60)
                
            with st.expander("Project Summary"):
                st.write("""
                         Objective: Interactive Web App for student athelets to track their progress in physical tests. 
                         Actions:
                         - Data cleaning with Python
                         - Scoring methodology to rate stuents
                         - Visualizations of progress and compariso with Plotly
                         """)
     #Jfab dashbaord   
    with colp3:
        with st.container():
            st.markdown("#### Power Bi Sales Dashbaord")
            st.image(Image.open("portfolio_examples/jfab_sales.png"))
            
            col1, col2, col3 = st.columns([1, 1, 8])
            with col1:
                    st.image(Image.open("icons/power bi.png"), width = 65)
            with col2: 
                st.image(Image.open("icons/Excel logo.png"), width = 50)
                
                
            with st.expander("Project Summary"):
                st.write("""
                         Objective: Keep track of sales and product inventory. 
                         Actions:
                         - Set up an invoice system with Excel
                         - Leveraged Power Query to clean sales and aggregate all sales invoices
                         - Developed a Power Bi dashboard for client to keep track on monthly sales and other KPIs
                         """) 
with tab2:
    col1, col2 = st.columns([4, 6])
    
    with col1:
        st.markdown("Tech Stack")
        tools = {"Excel" : 6, 
         "Python" : 2.5,
         "Power Bi" : 1.5, 
         "SQL" : 1,
         "PySpark" : 1,
         "Streamlit" : 1,
         "GitHub" : 1, 
         "Tableau" : 0.6,
        }
        tools_data = list(tools.items())
        dg = pd.DataFrame(tools_data, columns=["Tools", "Competency"])
        
        #sns.set_style("darkgrid", {"axes.edgecolor": (0, 0, 0, 0)})
        # Create the bar plot
        plt.figure(figsize=(6, 8))
        ax = sns.barplot(x="Competency", y="Tools", data=dg, palette="viridis")

        # Add labels and title
        ax.set_xlabel("Years of Experience", color="white")
        ax.set_ylabel("Tools", color="white")
        
        
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white', labelsize=16) 
        
        sns.despine(left = True)

        # Show the plot
        st.pyplot(plt, transparent=True)
    
    with col2:
        with st.container():
        
            stack = {
            "Understanding Stakeholder Needs" : 7,
            "Problem Solving" : 7, 
            "Processing Data" : 9, 
            "Analyzing Data" : 7, 
            "Visualize & Story Telling" : 8, 
            "Communication " : 7, 
                }
            
            data = list(stack.items())
            df = pd.DataFrame(data, columns=["Skill", "Competency"])
            fig = px.line_polar(df, r="Competency", theta="Skill", line_close=True)
            
            fig.update_traces(fill='toself', line_color = 'green')
            fig.update_layout(title="Skills")
            
            fig.update_layout(
                height=800,  # Set the height of the plot
                width=700
            )
            fig.update_layout(
            polar=dict(
                bgcolor='#15161A'  # Set the background color to dark grey
            ))
            
            fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    range=[0, 10]  # Set the range from 0 to 10
                )
            ))
            
            fig.update_layout(
            polar=dict(
                angularaxis=dict(
                    tickfont=dict(size=22, family="Arial", color="white")  # Customize font properties
                )
                ))

            # Show the plot
            st.plotly_chart(fig, use_container_width=True)
    

with tab3:
    st.title("CV")
    
    #enable cv download
    with open('Cristian_Rivas_Data_Analyst_CV.pdf', 'rb') as file:
        PDFbyte = file.read()        
    
    st.download_button(
            label = "Download PDF", 
            data = PDFbyte,
            file_name="CV.pdf",
            mime='application/octet-stream') 
    
    st.image(Image.open("cv.jpg"))
    
    


    