import streamlit as st
import base64
from PIL import Image
import plotly.express as px
import pandas as pd
import plotly
import seaborn as sns
import matplotlib.pyplot as plt
import base64

st.set_page_config(page_title = "Cristian Rivas - Data Analyst", layout = "wide")

# import streamlit_analytics

# with streamlit_analytics.track():

# st.session_state

def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

#tabs
tab1, tab2 = st.tabs(["Portfolio","CV"])

with tab1:
    width = 10
    col1, col2, col3 = st.columns([3, 5, 1])
    
    with col1:
        profile_pic = Image.open("profile_pic.jpg")
        st.image(profile_pic, width = 150)

    with col2:
        st.title("Cristian Rivas")
        st.subheader("Data Analyst")
        
    with col3:   
        linkedin_url = "https://www.linkedin.com/in/cristian-rivas-0b4a0212b/"
        upwork_url = "https://www.upwork.com/freelancers/cristianr16"
        github_url = "https://github.com/potatocris/DA"
        
        linkedin_icon_base64 = img_to_base64("icons/Linkedin.png")
        upwork_icon_base64 = img_to_base64("icons/upwork.png")
        github_icon_base64 = img_to_base64("icons/githubcat.png")
        
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <img src="data:image/png;base64,{linkedin_icon_base64}" width="30" style="margin-right: 10px;"/>
                <a href="{linkedin_url}" target="_blank">LinkedIn</a>
            </div>
            
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <img src="data:image/png;base64,{upwork_icon_base64}" width="40" style="margin-right: 10px;"/>
                <a href="{upwork_url}" target="_blank">UpWork</a>
            </div>
            
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <img src="data:image/png;base64,{github_icon_base64}" width="30" style="margin-right: 10px;"/>
                <a href="{github_url}" target="_blank">GitHub</a>
             </div>
            
            """,
            unsafe_allow_html=True,)
    st.divider() 
    #-------------------------------------------------------------------------------------------------------------

    st.subheader(":red[Freelance Jobs]", divider = "red")

    projects = [
    
    {"title": "  Power Bi Sales Dashbaord", 
     "description":
         """Set up an efficient invoice database system with Excel
            ETL pipeline with Power Query 
            Power Bi dashboard informing the client of monthly revenue""", 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/jfab_sales.png')}", 
     "stars": 5, 
     "review":"""This is my second time hiring Cristian and I am happier with the 
                results. He's an exceptional freelancer! Created an impressive 
                interactive salesdashboard, capturing overall and per-item sales 
                data. Attentive to every detail, incorporated perfect branding 
                colors, and maintained clear and professional communication 
                throughout. Highly recommended!"""},
    
    {"title": "  Tableau Revenue Dashboard", 
    "description": 
        """ ETL pipeline with Python,
            Parsing of text to extract mentions of marketing with FuzzyWuzzy,
            Monthly reports with Tableau""", 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/maritime_marketing.png')}", 
    "stars": 5, 
    "review":"""It was amazing to work with Cris! The guy is exceptional at what 
                he does, and he is he is friendly, communicates well, and created 
                a beautiful dashboard for this project. He provided more value and 
                data insights than I had originally expected. He is extremely 
                talented in Excel, Tableau, and is a true expert in his field, and 
                this shows in the outcomes and high-quality delivery; highly 
                recommended for efficient execution and outcomes!"""},
    
    {"title": "Streamlit Performance Web App", 
    "description":
        """Data cleaning with Python, 
           Rating methodology to rank student's performance, 
           Visualizations of progress and comparison with Plotly""", 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/sports_app.png')}", 
    "stars": 5, 
    "review":"""Cris is amazing! Once again over delivered on this project and we 
                were able to get a little more creative on our dashboard. He took 
                the time to troubleshoot and fix any minor bugs we ran into."""},
    
    {"title": "Gantt Chart Planner", 
    "description":
        """Custom Gantt Chart in Excel, 
           Conditional formatting for tracking progress, 
           User friendly""", 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/gantt_chart.png')}", 
    "stars": 0, 
    "review": "No feedback"},
    
    {"title": "Product Comparison", 
     "description":
         """Extracted data from research papers
            Carried an exploratory analysis to compare products 
            Created a custom visualization using Seaborn""", 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/product_marketing.png')}", 
     "stars": 0, 
     "review": "No feedback "},
    
    ]

    # Start building HTML for the gallery
    gallery_html = """<div style='white-space: nowrap; overflow-x: auto;'>"""

    for project in projects:
        bullet_points = project["description"].split("\n")
        list_items = "".join([f"<li>{item}</li>" for item in bullet_points])
        stars = "&#9733;" * project["stars"] + "&#9734;" * (5 - project["stars"])
        
        review_with_breaks = project["review"].replace('\n', '<br>')
        
        project_html = f"""
        <div style='display: inline-block; text-align: left; vertical-align: top;'>
            <p style='font-size: 22px; font-weight: bold;'>{project["title"]}</p>
            <img src='{project["image"]}' style='width:450px; height: 350px; margin: 5px;'/>
            <h5 style='margin-bottom: 0;'>Description</h5> <!-- Reduced margin-bottom -->
            <ul>{list_items}</ul>
            <h5>Client Feedback</h5>
            <div style='font-size: 24px;'>{stars}</div>
            <div word-wrap: break-word;'>
                <p style='font-style: italic; color:grey;'>{review_with_breaks}</p>
        </div>
        </div>"""

        gallery_html += project_html

    gallery_html += "</div>"

    
    # Display the gallery in Streamlit
    st.markdown(gallery_html, unsafe_allow_html=True)
    
    st.divider()
    #st.header("Personal Projects")
    #-------------------------------------------------------------------------------------------------------------

    st.subheader(":red[Personal Projects]", divider = "red")
    colp1, colp2, colp3 = st.columns(3)
    personal_projects = [
    
    {"title": "Zillow Api", 
     "description":
         """Aiming to find good rental prices
            Setting up an API connection to Zillow data
            Cleaning the data with Pandas""", 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/zillow_api.png')}"},
    
    {"title": "Power Bi Earnings Dashboard", 
    "description": 
        """Using Power Query to combine monthly statements
            Creating a dashboard to track personal freelance earnings""", 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/earnings_dash.png')}"},
    
    {"title": "Bitcoin Cycles", 
    "description":
        """Visualizing Bitcoin cycle patterns
            Using Pandas to organize and query data
            Employing Seaborn to plot and annotate""", 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/bitcoin_cycles.png')}"},
    
    {"title": "Inflation", 
     "description":
         """Plotting inflation in the US and the UK with Plotly
            Organising data in Excel
            """, 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/inflation.png')}"}, 
    
    {"title": "Logistic Regression", 
     "description":
         """Plotting inflation in the US and the UK using Plotly
            Organizing data in Excel""", 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/logisitc_regression.png')}", }
    ]

    # Start building HTML for the gallery
    gallery_html = """<div style='white-space: nowrap; overflow-x: auto;'>"""

    for project in personal_projects:
        bullet_points = project["description"].split("\n")
        list_items = "".join([f"<li>{item}</li>" for item in bullet_points])
        
        project_html = f"""
        <div style='display: inline-block; text-align: left; vertical-align: top;'>
            <p style='font-size: 22px; font-weight: bold;'>{project["title"]}</p>
            <img src='{project["image"]}' style='width:450px; height: 350px; margin: 5px;'/>
            <h5 style='margin-bottom: 0;'>Description</h5> <!-- Reduced margin-bottom -->
            <ul>{list_items}</ul>
        </div>"""

        gallery_html += project_html

    gallery_html += "</div>"

    # Display the gallery in Streamlit
    st.markdown(gallery_html, unsafe_allow_html=True)
    st.divider()
    #-------------------------------------------------------------------------------------------------------------

    
    st.subheader(":red[Technical Skills & Strengths]", divider = "red")
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
        plt.figure(figsize=(5, 5))
        ax = sns.barplot(x="Competency", y="Tools", data=dg, palette="viridis")

        # Add labels and title
        ax.set_xlabel("Years of Experience", color="white")
        ax.set_ylabel("Tools", color="white")
        
        
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white', labelsize=14) 
        
        sns.despine(left = True)

        # Show the plot
        st.pyplot(plt, transparent=True)
    
    with col2:
        with st.container():
        
            stack = {
            "Understanding Stakeholder Needs" : 8,
            "Problem Solving" : 9, 
            "Processing Data" : 9, 
            "Analyzing Data" : 8, 
            "Visualize & Story Telling" : 8, 
            "Communication " : 8, 
                }
            
            data = list(stack.items())
            df = pd.DataFrame(data, columns=["Skill", "Competency"])
            fig = px.line_polar(df, r="Competency", theta="Skill", line_close=True)
            
            fig.update_traces(fill='toself', line_color = 'green')
            fig.update_layout(title="Skills")
            
            fig.update_layout(
                height=700,  # Set the height of the plot
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
                    tickfont=dict(size=20, family="Arial", color="white")  # Customize font properties
                )
                ))

            # Show the plot
            st.plotly_chart(fig, use_container_width=True)


with tab2:
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
    
    


