import streamlit as st
import base64
from PIL import Image

st.set_page_config(page_title = "Cristian Rivas - Data Analyst", layout = "wide")

#tabs
tab1, tab2 = st.tabs(["Portfolio", "CV"])

with tab1:
    
    col1, col2, col3, col4 = st.columns([1, 4, 0.4, 1])
    
    with col1:
        profile_pic = Image.open("profile_pic.jpg")
        st.image(profile_pic, width = 180)

    with col2:
        st.title("Cristian Rivas")
        st.subheader("Data Analyst")
        st.write("email: crisalexis3008@gmail.com")
        
    with col3:   
        st.image(Image.open("icons/Linkedin.png"), width = 50)#linkedin
        st.image(Image.open("icons/upwork.png"), width = 100)#upwork
        st.image(Image.open("icons/githubcat.png"), width = 50) #github
        
    with col4:
        st.button("LinkedIn", "https://www.linkedin.com/in/cristian-rivas-0b4a0212b/")#linkedin
        st.button("Hire me on UpWork", "https://www.upwork.com/freelancers/cristianr16")#upwork
        st.button("GitHub", "https://github.com/potatocris/DA")#github

    st.divider()
    colp1, colp2, colp3 = st.columns(3)
    
    #Maritime Dashbaord
    with colp1:
        with st.container():
            st.markdown("#### Tableau Revenue Dashbaord")
            st.image(Image.open("portfolio_examples/maritime_revenue.png"))
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
    
    