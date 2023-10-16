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

def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

#tabs
tab1, tab2 = st.tabs(["Portfolio","CV"])

with tab1:
    
    col1, col2, col3, col4 = st.columns([1, 6, 1, 1])
    
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
    # Start building HTML for the gallery
    st.markdown('<p style="color:#FF4B4B; font-size: 26px;">Delivered Projects</p>', unsafe_allow_html=True)
    
    
    projects = [
    
    {"title": "Power Bi Sales Dashbaord", 
     "description":
         """Set up an efficient invoice database system with Excel
            ETL pipeline with Power Query 
            Power Bi dashboard informing the client of monthly revenue""", 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/jfab_sales.png')}", 
     "stars": 5},
    
    {"title": "Tableau Revenue Dashboard", 
    "description": 
        """ ETL pipeline with Python,
            Parsing of text to extract mentions of marketing with FuzzyWuzzy,
            Monthly reports with Tableau""", 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/maritime_marketing.png')}", 
    "stars": 5},
    
    {"title": "Streamlit Performance Web App", 
    "description":
        """Data cleaning with Python, 
           Rating methodology to rank student's performance, 
           Visualizations of progress and comparison with Plotly""", 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/sports_app.png')}", 
    "stars": 5},
    
    {"title": "Gantt Chart Planner", 
    "description":
        """Custom Gantt Chart in Excel, 
           Conditional formatting for tracking progress, 
           User friendly
           """, 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/gantt_chart.png')}", 
    "stars": 5},
    
    {"title": "Product Comparison", 
     "description":
         """Extracted data from research papers
            Carried an exploratory analysis to compare products 
            Created a custom visualization using Seaborn""", 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/product_marketing.png')}", 
     "stars": 5},
    
    ]

    # Start building HTML for the gallery
    gallery_html = """<div style='white-space: nowrap; overflow-x: auto;'>"""

    for project in projects:
        bullet_points = project["description"].split("\n")
        list_items = "".join([f"<li>{item}</li>" for item in bullet_points])
        stars = "&#9733;" * project["stars"] + "&#9734;" * (5 - project["stars"])
        
        project_html = f"""
        <div style='display: inline-block;'>
            <p style='font-size: 22px; font-weight: bold;'>{project["title"]}</p>
            <img src='{project["image"]}' style='width:500px; height: 400px; margin: 10px;'/>
            <ul>{list_items}</ul>
            <div style='font-size: 24px;'>{stars}</div>
        </div>"""

        
        gallery_html += project_html

    gallery_html += "</div>"

    # Display the gallery in Streamlit
    st.markdown(gallery_html, unsafe_allow_html=True)
    
    
    st.divider()
    #st.header("Personal Projects")
    st.markdown('<p style="color:#FF4B4B; font-size: 26px;">Personal Projects</p>', unsafe_allow_html=True)
    colp1, colp2, colp3 = st.columns(3)
    
    personal_projects = [
    
    {"title": "Zillow Api", 
     "description":
         """Set an API connection to Zillow""", 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/zillow_api.png')}"},
    
    {"title": "Power Bi Earnings Dashboard", 
    "description": 
        """Dashboard to track personal Freelance earnings""", 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/earnings_dash.png')}"},
    
    {"title": "Bitcoin Cycles", 
    "description":
        """Visualizing Bitcoin cycle patterns""", 
    "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/bitcoin_cycles.png')}"},
    
    {"title": "Inflation", 
     "description":
         """Plotting inflation in the US and the UK""", 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/inflation.png')}"}, 
    
    {"title": "Logistic Regression", 
     "description":
         """Biggest factors in a logistic regression model""", 
     "image": f"data:image/png;base64,{img_to_base64('portfolio_examples/personal/logisitc_regression.png')}", }
    ]

    # Start building HTML for the gallery
    gallery_html = """<div style='white-space: nowrap; overflow-x: auto;'>"""

    for project in personal_projects:
        bullet_points = project["description"].split("\n")
        list_items = "".join([f"<li>{item}</li>" for item in bullet_points])
        
        project_html = f"""
        <div style='display: inline-block;'>
            <p style='font-size: 22px; font-weight: bold;'>{project["title"]}</p>
            <img src='{project["image"]}' style='width:500px; height: 400px; margin: 10px;'/>
            <ul>{list_items}</ul>
        </div>"""

        
        gallery_html += project_html

    gallery_html += "</div>"

    # Display the gallery in Streamlit
    st.markdown(gallery_html, unsafe_allow_html=True)
    

#with tab2:
    st.divider()
    st.markdown('<p style="color:#FF4B4B; font-size: 26px;">Technical Skills & Strengths</p>', unsafe_allow_html=True)
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
    
    


    