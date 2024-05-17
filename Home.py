import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention
from pathlib import Path
from PIL import Image
from utils import social_icons
import sqlite3

st.set_page_config(page_title="Aman Singh", 
                   page_icon="📚",
                   layout = "wide", 
                   initial_sidebar_state = "auto")

# -- Path Setings --
curent_dir = Path(__file__).parent if  "__file__" in locals() else Path.cwd()
css_file = curent_dir/"style"/"main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 Aman Singh';
    position:relative;
    color:black;
}
"""

img = "assets/prof_img1.jpg"
img_horus  = "assets/horus.png"
img_clg = "assets/clg.jpg"
img_dip = "assets/crrit.jpeg"
img_plant_pro = "assets/img_plant.jpeg"
img_waste_pro = "assets/img_waste.png"
img_eda = "assets/img_EDA.jpg"
img_deep = "assets/deepracer.jpeg"
img_sand = "assets/sandrover.jpeg"
img_sand1 = "assets/sand.jpg"
img_airflicks = "assets/airflicks.jpg"
img_gdsc = "assets/gdsc.png"


st.markdown("""
  <style>

    /*the main div*/
    .css-1v0mbdj {
        width: 200px; /*max value according to image width, can be smaller but not larger*/
        height: 200px;
        position: relative;
        overflow: hidden;
        border-radius: 50%;
    }
    
    /*the img elements in the main div class*/
    .css-1v0mbdj > img{
        display: inline;
        margin: 0 auto;
        margin-top: -35%; /*Tweak this one according to your need*/
    }
  
  </style>
""", unsafe_allow_html=True)

def text1(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Aman Singh", 
                        ["About Me", "Technical Skills", "Education", "Projects", "Experience","Competitions", "Extra Curricular", "Contact"],
                         icons=['person fill', 'tools', 'book half', 'clipboard', 'clock history', 'trophy fill', 'heart', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         
    )
    linkedin_url = "https://www.linkedin.com/in/amansingh977/"
    github_url = "https://github.com/aman977381"
    email_url = "mailto:asingh97781@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30,LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()



st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Aman Singh")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Passionate Data Science/ML Engineer")
            st.write("👋🏻 Hi, I am Aman!, I'm a passionate ML engineer currently contributing to open source projects to gain more knowledge and engage within the community. 🚀, I am constantly seeking unique working experience to broaden my horizons in the realm of Ai")
            st.write("💼 I thrive on problem-solving and innovative thinking, driven by purpose and the challenge of finding solutions. With expertise in Python, Pandas, Numpy, Sklearn, Tensorflow, OpenCV, and more. Passionate about building scalable products from scratch to make a positive impact through technology. I am thus aiming to enter this industry for my first full-time job.")
            st.write("🏋🏻 In addition, I like to go for Cycling 🚴, Walk, play video games and... enjoy eating good food in my free time!")
            st.write("👨🏼‍💻 Academic interests: Data Visualization, Computer Vision, Recommendation Systems, Natural Language Processing")
            st.write("💭 Ideal Career Prospects: Data Scientist, ML Engineer, Computer Vision, Generative Ai")
            #st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/164EEVH6BmvC89q2M4WsBNF1JyddDAbNY/view?usp=sharing)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img)

elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_horus)
        with text_column:
            st.subheader("UAV System Engineer, [Horus Innovations](https://www.linkedin.com/in/horus-innovations-708262246/?originalSubdomain=in)")
            st.write("*August to November 2023*")
            st.markdown("""
            - Successfull integretion and tuning of new electronics, sensors, payloads and new software into UAV systems, ensuring compatibility, reliability and optimal performance
            - Plaining and excuting the flight test plans for new software features
            - Perfoms functional testing and troubleshoting of equipment and systems in assigned area
            - Obtain the flight data and analyze it closely for optimal performance
            - Collaborated with Project design and development teams to define and design UAV that align the project objective and client requirements 
            """)

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)


elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    text1("Programming Languages","`Python`, `MySQL`")
    text1("Academic Interests","`Data Visualization`, `Computer Vision`, `Recommendation Systems`, `Natural Language Processing`")
    text1("Data Visualization", "`matplotlib`, `seaborn`, `Plotly`")
    text1("Database Systems", "`MySQL`")
    text1("Cloud Platforms", "`Amazon Web Services`, `Streamlit Cloud`, `Hugging Face`")
    text1("Natural Language Processing", "`NLTK`, `Word2Vec`, `TF-IDF`, `TextStat`")
    text1("Computer Vision Processing", "`OpenCV`, `YOLOv9`, `YOLOv8`, `R-CNN`")
    text1("Version Control", "`Git`, `Docker`, `MLFlow`, `Weight&Biases`")
    text1("Design and Front-end Development", "`CSS`, `Streamlit`,")
    text1("Data Science Techniques", "`Regression`, `Clustering`, `Association Rules Mining`, `Random Forest`, `Decison Trees`, `Principal Components Analysis`, `Text Classification`, `Sentiment Analysis`")
    text1("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`")
    #text1("Miscellaneous", "`Google Firebase`, `Microsoft Office`, `Retool`, `Google Ads`")

elif choose == "Education":
    st.header("Education")

    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_clg)
        with text_column:
            st.subheader("Bachelor of Technology - [EEE](https://eee.mait.ac.in/), [Maharaja Agrasen Institute of Technology](https://mait.ac.in/) (2019-2023)")
            st.write("Relevant Coursework: Fundamental principles and applications in electrical and electronics engineering, including circuit analysis, Data Structures and Algorithms,digital systems, electromagnetics, power systems, control systems, communication technologies and Electrical Machine Design")
            st.markdown("""
            - [Airflick MAIT](https://www.instagram.com/airflicks.mait?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==) - Co-founder & President (2022-2023)
                """)
            
    
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_dip)
        with text_column:
            st.subheader("Diploma - Electrical Engineering, [Chhotu Ram Rural Institute of Technology](http://www.crritonline.com/ShowPage.aspx?ConTabID=40) (2017-2020)")
            st.write("Relevant Coursework: Fundamental principles and applications in electrical and electronics engineering, including circuit analysis,digital systems, power systems, and control systems")

elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Plant Disease Recoginition 🌱")
            st.write("*self initiated project*")
            st.markdown("""
            - Used dataset of +17000 images belonging to 38 classes
            - Used state of the art ResNet CNN model to train and achieved accuracy of more than 65%
            - For the model version control used Weight&Biases
            - Built webapp based on Streamlit and deployed on Streamlit cloud
            """)
            mention(label="Streamlit App", icon="streamlit", url="https://plant-disease-recoginition.streamlit.app/",)
            mention(label="Github Repo", icon="github", url="https://github.com/aman977381/Plant-Disease-Detection.git",)
        with image_column:
            st.image(img_plant_pro)

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Waste Detection WebApp 🗑️")
            st.write("*Self-initiated project*")
            st.markdown("""
            - Trained model on anoted dataset more than 10000 images belongs to 6 different classes
            - Traied YOLOv8 model for waste ditection and achieved acccuracy of about 58% and model performance tracked using Weight&Biases
            - Build a webapp based on Streamlit for waste detection in Image and Live video and deployed on Streamlit Cloud
            """)
            mention(label="Streamlit App", icon="streamlit", url="https://waste-detector.streamlit.app/",)
            mention(label="Github Repo", icon="github", url="https://github.com/aman977381/Waste-Detection-using-YOLO.git",)
        with image_column:
            st.image(img_waste_pro)

    
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Student Performance Prediction 👨‍🎓")
            st.write("*Self-initiated project*")
            st.markdown("""
            - Achieved a 96% accuracy rate in forcasting student academic performance by developing and deploing a machine learning model
            - Managed data integrity by handling missing value and encding categorical variables, enhancing quality by 33%
            - Identified and comprehended key factor influencing academic performance through thorough analysis
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/aman977381/ML_Project.git",)

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Exploritry Data Analysis of Obesity data from kaggle 📊")
            st.write("*Self-initiated project for participating in a compitition from Kaggle*")
            st.markdown("""
            - Conducted Exploratory Data Analysis (EDA) on obesity data to glean insights into patterns and trends related to obesity prevalence
            - Utilized statistical techniques and data visualization tools to explore the distribution, correlations, and outliers within the dataset
            - Ran regression models and performed hyperparameter tuning to predict Obesity level (linear regression, random forest, XGBoost, CATBoost)
            - Implemented under-sampling and ensemble techniques to adress class imbalance, leading to 10% improvement in performance
            """)
            mention(label="Kaggle Notebook", icon="kaggle", url="https://www.kaggle.com/code/amansingh2130/obesity-catboost",)
            mention(label="Github Repo", icon="github", url="https://github.com/aman977381/EDA.git",)
        
        with image_column:
            st.image(img_eda,width=300)

elif choose == "Competitions":
    # Create section for Competitions
    #st.write("---")
    st.header("Competitions")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_deep,width = 250)
            #st.empty()
        with text_column:
            st.subheader("AWS Deepracer Student League 2022 - Hosted by [AWS-Deepracer](https://aws.amazon.com/deepracer/)")
            st.write("*Placed in top 3 globaly out of 2000 competitors in September leaderboard*")
            st.write("Trained a Reinforcement Learning based agent to follow a track in Simulation wold on different tracks each month and submited to Global leaderboard")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_deep,width = 250)
            #st.empty()
        with text_column:
            st.subheader("AWS Deepracer Student League India 2022 - Hosted by [AWS-Deepracer](https://aws.amazon.com/deepracer/) and [AICTE](https://www.aicte-india.org/)")
            st.write("*Placed in top 10 finalist in Indian league*")
            st.write("Trained a Reinforcement Learning based agent to follow a track in Simulation wold on different tracks each month and submited to Indian leaderboard")
    
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_sand1)
            #st.empty()
        with text_column:
            st.subheader("Sandover-KSHITIJ 2022 - Hosted by [KSHITIJ IITK](https://www.instagram.com/ktj.iitkgp?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==)")
            st.write("Build a robot that can run across the arena of uneven topography in minimum time")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_deep,width = 250)
            #st.empty()
        with text_column:
            st.subheader("AWS Deepracer Student League 2023 - Hosted by [AWS-Deepracer](https://aws.amazon.com/deepracer/)")
            st.write("*Placed in top 6 globaly out of 3000 competitors in August leaderboard*")
            st.write("*Placed in top 8 in India by the end of the league*")
            st.write("Trained a Reinforcement Learning based agent to follow a track in Simulation wold on different tracks each month and submited to Global leaderboard")

elif choose =='Extra Curricular':
    st.header("Societies")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_airflicks)
        with text_column:
            st.subheader("Airflicks MAIT")
            st.write("*March 2022 to April 2023*")
            st.write("*Co-founder & President*")
            st.markdown("""
            - Designed recruitment poster using and club logo using Canva for brand awarness of new club, recruit more than 50 students in first session Jul 2022 to April 2023
            - Organised varius club events and workshops to aware student about UAVs and Drone technologies
            - Volunteered in many college level events and provided full Ariel Coverege to event
            - Trained students to fly drone and make them familier of differnet types of drone, hardwared and softwares
            """)
    
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_gdsc)
        with text_column:
            st.subheader("Google Developer Student Club MAIT")
            st.write("*March 2021 to April 2023*")
            st.markdown("""
            - Designed posters and brochures for various events
            - Participated in team events and workshops and gained experience in Ai and Goole Cloud
            """)

elif choose == "Contact":
# Create section for Contact
    #st.write("---")
    st.header("Contact")
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid = st.columns((1,0.5))
        with text_column:
            st.write("Let's connect! You may either reach out to me at asingh97781@gmail.com or use the form below!")
            def create_database_and_table():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS contacts
                            (name TEXT, email TEXT, message TEXT)''')
                conn.commit()
                conn.close()
            create_database_and_table()

            st.subheader("Contact Form")
            if "name" not in st.session_state:
                st.session_state["name"] = ""
            if "email" not in st.session_state:
                st.session_state["email"] = ""
            if "message" not in st.session_state:
                st.session_state["message"] = ""
            st.session_state["name"] = st.text_input("Name", st.session_state["name"])
            st.session_state["email"] = st.text_input("Email", st.session_state["email"])
            st.session_state["message"] = st.text_area("Message", st.session_state["message"])


            column1, column2= st.columns([1,5])
            if column1.button("Submit"):
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                        (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
                conn.commit()
                conn.close()
                st.success("Your message has been sent!")
                # Clear the input fields
                st.session_state["name"] = ""
                st.session_state["email"] = ""
                st.session_state["message"] = ""
            def fetch_all_contacts():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("SELECT * FROM contacts")
                rows = c.fetchall()
                conn.close()
                return rows
            
            if "show_contacts" not in st.session_state:
                st.session_state["show_contacts"] = False
            if column2.button("View Submitted Forms"):
                st.session_state["show_contacts"] = not st.session_state["show_contacts"]
            
            if st.session_state["show_contacts"]:
                all_contacts = fetch_all_contacts()
                if len(all_contacts) > 0:
                    table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
                    table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
                    markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
                    st.markdown(markdown_table)
                else:
                    st.write("No contacts found.")


            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/amansingh977/"
            github_url = "https://github.com/aman977381"
            email_url = "mailto:asingh97781@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
        with mid:
            st.empty()