import streamlit as st
from streamlit import components
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
from streamlit_elements import elements, mui, html, sync
import json
#from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander

#test

# Set page title
st.set_page_config(page_title="Prekshi Vyas", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 Harry Chang';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_utown = Image.open("images/frenz3.jpeg")
img_utown_2 = Image.open("images/intro.jpeg")
img_pv = Image.open("images/grad.jpeg")
img_drdo = Image.open("images/drdo.png")
#Assets for competitions
img_lit = Image.open("images/legalease.jpg")
img_lifehack2 = Image.open("images/lifehack2.jpg")
img_lifehack = Image.open("images/lifehack.jpg")
img_he4d = Image.open("images/he4d.jpg")
img_ecc = Image.open("images/ecc.jpg")
img_shopee = Image.open("images/shopee.png")
img_sbcc = Image.open("images/sbcc.png")
img_runes = Image.open("images/runes.png")
# Assets for education
img_sji = Image.open("images/sji.jpg")
img_tpjc = Image.open("images/tpjc.jpg")
img_vit = Image.open("images/frenz7.jpeg")
img_frenx = Image.open("images/frenz2.jpeg")
img_gmss = Image.open("images/gmss.jpg")
img_sjij = Image.open("images/sjij.jpg")
img_dsa = Image.open("images/dsa.jpg")
# Assets for experiences
img_quest = Image.open("images/questlogo.jpg")
img_penn = Image.open("images/penn.png")
img_cisco = Image.open("images/cisco.jpg")
img_sg = Image.open("images/sg.png")
img_smartek = Image.open("images/smartek.png")
# Assets for projects
image_names_projects = ["ds", "sentiment", "imagecls"] # , "sentiment", "imageclassify", "blockchain", "recsystem"
images_projects = [Image.open(f"images/{name}.{'png' if name in ('ds') else 'jpg'}") for name in image_names_projects]
# Assets for volunteering
image_names_vol = ["sdslogo", "sportslogo", "gdsclogo", "csclogo", 
                         "nussulogo", "sklogo", "simlogo", "tpjclogo", 
                         "sjilogo", "nuspc", "hcs", "fintech"]
images_vol = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_vol]
# Assets for blog
img_qb = Image.open("images/qb.jpg")
img_mayans = Image.open("images/mayans.jpg")
img_outlier = Image.open("images/outlier.png")
img_dac = Image.open("images/dac.png")
img_raffles = Image.open("images/raffles.jpg")
img_covid = Image.open("images/covid.jpg")
img_gender = Image.open("images/gender.jpg")
img_hci = Image.open("images/hci.jpg")
img_wordcloud = Image.open("images/wordcloud.jpg")
img_taste = Image.open("images/taste.jpg")
img_measles = Image.open("images/measles.jpeg")
img_bmsaew = Image.open("images/bmsaew.png")
img_dac1 = Image.open("images/dac1.png")
img_dac2 = Image.open("images/dac2.png")


# Assets for tech talks
img_techtalk = Image.open("images/airflowsummit.jpg")
#img_lottie_animation = Image.open("images/lottie_animation.gif")
# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_linkedin = Image.open("images/linkedin.png")
img_github = Image.open("images/github.png")
img_email = Image.open("images/email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "youtube": "https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png",
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "wordpress": "https://img.icons8.com/ios-filled/100/ff8c00/wordpress--v1.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

#def txt3(a, b):
  #col1, col2 = st.columns([1,2])
  #with col1:
    #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  #with col2:
    # Split the text at the comma and wrap each part in backticks separately
    #b_parts = b.split(',')
    #b_formatted = '`' + ''.join(b_parts) + '`'
    #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')   


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_pv, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Prekshi Vyas", 
                        ["About Me", "Experience & Research", "Technical Skills", "Education", "Talks", "Projects", "Certifications", "Leadership and Volunteering"],
                         icons=['person-fill', 'clock-fill', 'tools', 'book-half', 'star-half', 'pencil-fill', 'award-fill', 'heart-half'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    youtube_url = "https://www.youtube.com/@prekshivyas"
    linkedin_url = "https://www.linkedin.com/in/prekshi-vyas/"
    github_url = "https://github.com/prekshivyas"
    email_url = "mailto:prvyas@seas.upenn.edu"
    resume = "https://drive.google.com/file/d/1CPW5glbrIDu7CwS1kx-CH7EmBzy7vqE8/view"
    
    def get_icons(url):
        icons = ""
        icons+=social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url)
        icons += f'<a href="{url}" target="_blank" style="color: orange; font-weight: bold;"><span style="font-size: 24px;">📋</span>CV</a>'
        icons+=social_icons(30, 30, Youtube=youtube_url)
        return icons

    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                get_icons(resume),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Prekshi Vyas")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            # st.subheader("All things Cloud and ML!")
            # st.markdown("<h4 style='font-size: 20px;'>Currently looking for Summer 2025 Internships</h4>", unsafe_allow_html=True)

            st.write("👋🏻 Hello, I'm Prekshi, currently pursuing a Master's in Computer Science at the University of Pennsylvania. I have 3 years of professional experience as a Software Engineer specializing in Cloud and DevOps, and have made significant contributions to Open Source projects and Machine Learning benchmarks. ")
                     
            st.write("My journey so far also includes speaking at global summits, leading academic projects, and conducting research in Natural Language Processing. I excel in automating and optimizing processes to ensure reliability and scalability. I am actively seeking opportunities for Summer 2025 internships.")

            st.write("💃 Beyond coding, I am a professional street style dancer, pianist and love reading non-fiction!")

            st.write("👨🏼‍💻 Interests: Microservices, Distributed Systems, Cloud, DevOps, MultiModal Large Models, Machine Learning, Natural Language Processing, Computer Vision, Data Orchestration")
            # st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/164EEVH6BmvC89q2M4WsBNF1JyddDAbNY/view?usp=sharing)")
        with middle_column:
            st.empty()
        
        def slideshow_swipeable(images):
            # Create a unique key for this instance of the slideshow
            key = f"slideshow_{str(images).encode().hex()}"

            # Initialize the index in session state if it doesn't exist
            if key not in st.session_state:
                st.session_state[key] = 0

            # Get the current index from session state
            index = st.session_state[key]

            # Display the current image
            st.image(images[index], use_column_width=True)

            # Create two columns for previous and next buttons
            col1, col2 = st.columns(2)

            # Previous button
            with col1:
                if st.button("Previous", key=f"{key}_prev"):
                    st.session_state[key] = (index - 1) % len(images)
                    st.experimental_rerun()

            # Next button
            with col2:
                if st.button("Next", key=f"{key}_next"):
                    st.session_state[key] = (index + 1) % len(images)
                    st.experimental_rerun()
            
        images = ["images/frenz3.jpeg", "images/intro.jpeg", "images/frenz4.jpeg"]
        with right_column:
            slideshow_swipeable(images)
        
        st.markdown(
        """
    <div style="position: fixed; bottom: 10px; right: 10px; text-align: right;">
        <p style="font-size: 12px; color: grey;">Portfolio design inspired by <a href="https://github.com/harrychangjr/portfolio" target="_blank">Harry Chang</a></p>
    </div>
    """,
        unsafe_allow_html=True
    )
                

elif choose == "Experience & Research":

    # Assuming 'experiences' is a list of dictionaries containing experience details
    experiences = [
        {
            'image_url': img_penn,
            'position': "NLP Research Assistant - Cognitive Computation Group",
            'duration': "*May 2024 to Present*",
            'company_name': "University of Pennsylvania",
            'company_url': "https://nlp.cis.upenn.edu/",
            'description': "- Created a novel benchmark to evaluate cognitive capabilities of large multimodal models, utilizing complex charts as visual contexts.\n"
                           "- Designed and created end-to-end pipeline for dataset generation integrating APIs of Gen-AI models viz. GPT-4o, Gemini 1.5 Pro and Selenium for Web Automation.\n"
                           "- Implemented statistical analysis and clustering algorithms to process, group 6532 charts and CSVs into structurally relevant, insightful data.\n"
                           "- Engineered custom web application using Streamlit and Firebase in 3 days, streamlining collection of human generated QA pairs across distinct categories.",
            'skills': "`VLMs` `Web Automation` `Roboflow` `GenerativeAI` `Data Analytics` `Streamlit` `Firebase`"
        },
        {
            'image_url': img_cisco,
            'position': "Cloud Engineer",
            'duration': "*June 2022 to July 2023*",
            'company_name': "Cisco",
            'company_url': "https://www.cisco.com/site/in/en/index.html",
            'description': "- Configured alerts and metrics for storage and service availability.\n"
                           "- Created visually intuitive dashboards for real-time insights.\n"
                           "- Automated the EKS upgrade process and fixed security vulnerabilities.",
            'skills': "`Python` `AWS` `Prometheus` `Grafana` `Terraform` `Docker` `Git` `Jira` `Confluence`"
        },
        {
            'image_url': img_sg,
            'position': "Software Engineer",
            'duration': "*June 2020 to June 2022*",
            'company_name': "Société Générale",
            'company_url': "https://www.societegenerale.com/en",
            'description': "- Led the full software development life cycle for crucial features.\n"
                           "- Automated and scaled instance patching process to 1500+ instances, eliminating manual efforts and support assistance using Airflow.\n"
                           "- Boosted service availability by delivering capacity planning feature and configuring rolling updates cutting down deployment time by 50%.\n"
                           "- Designed and developed a micro-service based, workflow logging, and monitoring system which catalyzed 20% surge in service adoption.",
            'skills': "`Airflow` `API Development` `Kubernetes` `Jenkins` `Terraform` `Docker`"
        },
        {
            'image_url': img_sg,
            'position': "Software Engineer Intern",
            'duration': "*May to August 2020*",
            'company_name': "Société Générale",
            'company_url': "https://www.societegenerale.com/en",
            'description': "- Spearheaded front line tasks and production support.\n"
                           "- Researched architecture designs and service migration plans.",
            'skills': "`Airflow` `API Development` `Docker` `System Architecture` `Devops`"
        },
        {
            'image_url': img_smartek,
            'position': "NLP Intern",
            'duration': "*February to May 2022*",
            'company_name': "SmarTek21",
            'company_url': "https://smartek21.com/",
            'description': "- Created a Python app for text-to-speech synthesis.\n"
                           "- Implemented Tkinter, PyPDF2, and Pyttsx3 for graphical interface, PDF handling, and speech functionality.\n"
                           "- Incorporated Google Speech Recognition API for speech-to-text capabilities.",
            'skills': "`Python` `GUI Programming` `NLP`"
        },
        {
            'image_url': img_drdo,
            'position': "Software Intern",
            'duration': "*January to May 2021*",
            'company_name': "DRDO",
            'company_url': "https://drdo.gov.in/drdo/",
            'description': "- Developed a Human Machine Interface module for the Operator Control Unit of an Unmanned Ground Vehicle.",
            'skills': "`Java` `Networking/Socket Programming` `LabView`"
        }
    ]

    # Create rows with 2 experiences side by side
    for i in range(0, len(experiences), 2):
        with st.container():
            cols = st.columns(2)
            for idx, col in enumerate(cols):
                if i + idx < len(experiences):
                    exp = experiences[i + idx]
                    with col:
                        st.image(exp['image_url'], width=200)
                        st.subheader(exp['position'])
                        st.write(exp['duration'])
                        st.markdown(f"**[{exp['company_name']}]({exp['company_url']})**")
                        st.markdown(f"- {exp['description']}")
                        st.markdown(f"`{exp['skills']}`")

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)

elif choose == "Technical Skills":
    # Define skills categories with images and text
    software_engineering_skills = [
        {"name": "Python", "image_url": "images/skills/python.svg"},
        {"name": "Java", "image_url": "images/skills/java.svg"},
        {"name": "Flask-Restful APIs", "image_url": "images/skills/Flask.svg"},
        {"name": "Firebase", "image_url": "images/skills/firebase.svg"},
        {"name": "Jenkins CI/CD", "image_url": "images/skills/Jenkins.svg"},
        {"name": "JIRA", "image_url": "images/skills/Jira.svg"},
        {"name": "Confluence", "image_url": "images/skills/Confluence.svg"},
        {"name": "SQL", "image_url": "images/skills/sql.svg"},
        {"name": "Hugging Face", "image_url": "images/skills/huggface.png"},
        {"name": "RoboFlow", "image_url": "images/skills/roboflow.jpg"},
        {"name": "Numpy", "image_url": "images/skills/NumPy.svg"},
        {"name": "Pandas", "image_url": "images/skills/Pandas.png"},
        {"name": "PyTorch", "image_url": "images/skills/PyTorch.svg"},
        {"name": "Scikit-learn", "image_url": "images/skills/scikit-learn.svg"},
        {"name": "PostgresDB", "image_url": "images/skills/PostgresSQL.svg"},
        {"name": "Apache Spark", "image_url": "images/skills/spark.svg"},
        {"name": "Apache Kafka", "image_url": "images/skills/kafka.svg"},
        {"name": "Apache Airflow", "image_url": "images/skills/airflow.svg"},
        {"name": "AWS", "image_url": "images/skills/icons8-amazon-web-services.svg"},
        {"name": "Linux", "image_url": "images/skills/linux.svg"},
        {"name": "Docker", "image_url": "images/skills/icons8-docker.svg"},
        {"name": "Kubernetes", "image_url": "images/skills/kubernetes.svg"},
        {"name": "Helm", "image_url": "images/skills/helm.svg"},
        {"name": "Terraform", "image_url": "images/skills/terraform.svg"},
        {"name": "Grafana", "image_url": "images/skills/grafana.svg"},
        {"name": "Prometheus", "image_url": "images/skills/prometheus.svg"},
        {"name": "Bash/Shell Scripting", "image_url": "images/skills/bash.svg"},
        {"name": "Microservices", "image_url": "images/skills/microservices.svg"}
    ]

    # Function to display skills with images
    def display_skills_in_rows(skills):
        num_skills = len(skills)
        rows = (num_skills // 5) + (1 if num_skills % 5 > 0 else 0)  # Calculate number of rows needed
        
        for i in range(rows):
            cols = st.columns(5)  # Create 5 columns for each row
            for j in range(5):
                idx = i * 5 + j
                if idx < num_skills:
                    with cols[j]:
                        try:
                            st.image(skills[idx]['image_url'], width=40)
                            st.write(skills[idx]['name'])
                        except:
                            continue

    # Display skills categories
    display_skills_in_rows(software_engineering_skills)

    # st.write("**DevOps-Cloud:**")
    # display_skills(devops_cloud_skills)

# For Certifications
elif choose == "Certifications":
    # Data for certifications
    certifications = [
        {
            'name': 'Machine Learning in Production',
            'issuer': 'DeepLearning.AI',
            'date_issued': 'Jul 2024',
            'skills': 'Machine Learning, MLOps',
            'credential_url': 'https://www.coursera.org/account/accomplishments/verify/UK7CZEHMANGK',
            'image_url': 'images/deeplai.png'
        },
        {
            'name': 'Oracle Cloud Generative AI Certified Professional',
            'issuer': 'Oracle',
            'date_issued': 'Jun 2024',
            'expiry_date': 'Jun 2026',
            'skills': 'Oracle Cloud, Generative AI',
            'credential_url': 'https://brm-certview.oracle.com/ords/certview/ecertificate?ssn=OC5078969&trackId=OCI2024GAIOCP&key=abc99789ba478af4aff1515997c13536da339489',
            'image_url': 'images/oci.png'
        },
        {
            'name': 'AWS Certified Solutions Architect',
            'issuer': 'Udemy',
            'date_issued': 'May 2024',
            'credential_url': 'https://www.udemy.com/certificate/UC-3bdd35e3-a356-41eb-b0f4-e94e86d05bd2/',
            'image_url': 'images/aws.png'
        },
        {
            'name': 'Microsoft Technology Associate: Software Development Fundamentals (MTA)',
            'issuer': 'Microsoft 365',
            'date_issued': 'Jun 2019',
            'credential_id': 'wLkHa-FaXo',
            'credential_url': 'http://verify.certiport.com',
            'image_url': 'images/ms.png'
        },
        {
            'name': 'Introduction to Big Data',
            'issuer': 'Coursera',
            'date_issued': 'Nov 2018',
            'credential_url': 'https://www.coursera.org/account/accomplishments/certificate/Q8WQYX4VJTCG',
            'image_url': 'images/coursera.png'
        },
        {
            'name': 'Fundamentals of Network Communication',
            'issuer': 'Coursera',
            'date_issued': 'Apr 2018',
            'credential_url': 'https://www.coursera.org/account/accomplishments/certificate/CW6JXKZ7XZ2U',
            'image_url': 'images/coursera.png'
        },
    ]

    # Create rows with 3 certifications each
    for i in range(0, len(certifications), 3):
        cols = st.columns(3)
        for idx, col in enumerate(cols):
            if i + idx < len(certifications):
                cert = certifications[i + idx]
                with col:
                    st.image(cert['image_url'], width=200)
                    st.markdown(f"**[{cert['name']}]({cert['credential_url']})**")
                    st.markdown(f"Issued by {cert['issuer']} in {cert['date_issued']}")
                    if 'expiry_date' in cert:
                        st.markdown(f"Expires {cert['expiry_date']}")
                    if 'skills' in cert:
                        st.markdown(f"Skills: {cert['skills']}")
                    if 'credential_id' in cert:
                        st.markdown(f"Credential ID: {cert['credential_id']}")
# Create section for Education
#st.write("---")
elif choose == "Education":
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_frenx)
        with text_column:
            st.subheader("Master of Science and Engineering - Computer and Information Science, [University of Pennsylvania](https://www.upenn.edu/) (2023-2025)")
            st.write("GPA: 4.0/4.0")
            st.write("Coursework: Natural Lanaguage Processing, Computer Vision, Analysis of Algorithms, Big Data and Cloud, Artificial Intelligence, Applied Machine Learning")

    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_vit)
        with text_column:
            st.subheader("Bachelor of Technology - Information Technology, [VIT Vellore](https://vit.ac.in/) (2016-2020)")
            st.write("GPA: 9.01/10")
            st.write("Relevant Coursework: Applied Linear Algebra, Machine Learning, Big Data, Human Computer Interaction, Data Structures and Algorithms, Database Managment Systems, Networking, Operating Systems, Advanced Java Programming, Mobile Application Development, Web Programming")


elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Recent Projects")

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data Driven Real Estate Forecasting")
            st.markdown("""
            - Led a comprehensive real estate price prediction project, integrating socioeconomic indicators and property features. 
            - Conducted data wrangling, cleaning, aggregation, exploratory data analysis, and PCA to prepare and optimize a dataset of over 200,000 data points.
            - Fine-tuned diverse models, including RandomForest, XGBoost, and FeedForward Neural Network, achieving 80% accuracy by navigating challenges in data preprocessing, hyperparameter tuning, and model training
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/biopics) | [RPubs](https://rpubs.com/harrychangjr/biopics)")
            mention(label="Github Repo", icon="github", url="https://github.com/prekshivyas/CIS-595-Big-Data-Analytics",)
        with image_column:
            st.image(images_projects[0])

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Sentiment Analysis - Traditional Machine Learning vs Deep Learning")
            st.markdown("""
            - Pre-processed Movie Reviews and ran several traditional classfication ML Models performing extensive hyperparameter turning and dataset shifts.
            - Developed a custom deep learning architecture for Sentiment Analysis on movie reviews using Bi-LSTM layers and GloVe embeddings.
            - Executed rigorous hyperparameter tuning, exploring 3 different epoch counts, learning rates, batch sizes, and optimizers across long and short sentences, achieving an F1 score of 0.86.
            """)
            mention(label="Github Repo", icon="github", url="https://github.com/prekshivyas/CIS-5190-Applied-ML",)
        with image_column:
            st.image(images_projects[1])


    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Image Classification - Traditional Machine Learning vs Deep Learning")
            st.markdown("""
            - Pre-processed ImageNet Dataset and ran traditional classfication ML Models performing extensive hyperparameter turning and dataset shifts.
            - Improved Image Classification using a custom CNN architecture with advanced pre-processing techniques, including normalization, Gaussian blur, and augmentation via data-set shifts.
            - Conducted a comprehensive grid search, resulting in 288 different model configurations achieving best accuracy of 86%.
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/dsa4212) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%202%20Group%2039%20Report.pdf)")
            mention(label="Github Repo", icon="github", url="https://github.com/prekshivyas/CIS-5190-Applied-ML",)
        with image_column:
            st.image(images_projects[2])
    
elif choose == "Competitions":
    # Create section for Competitions
    #st.write("---")
    st.header("Competitions")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lit)
            #st.empty()
        with text_column:
            st.subheader("[SMU-LIT Hackathon 2023](https://www.smulit.org/hackathon-2023/) - Hosted by [SMU Legal-in-Tech Club](https://smulit.org)")
            st.write("Built LegalEase with OpenAI - a Streamlit-based web application empowering lawyers in hybrid working environments with optimal task scheduling.")
            #st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/legalease",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lifehack2)
            #st.empty()
        with text_column:
            st.subheader("[NUS LifeHack 2023](https://lifehack-website.web.app//) - Hosted by [NUS Students' Computing Club](https://nuscomputing.com/)")
            st.write("Awarded Top 15 Finalist out of 141 team submissions")
            st.write("Built and integrated PassionPassport with ChatGPT - a Streamlit-based web application that recommends travel locations based on one’s hobbies.")
            #st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
            mention(label="Github Repo", icon="github", url="https://github.com/BrendanCheong/lifehack-2023",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lifehack)
        with text_column:
            st.subheader("[NUS LifeHack 2022](https://lifehack-2022.vercel.app/) - Hosted by [NUS Students' Computing Club](https://nuscomputing.com/)")
            st.write("Awarded Theme Best - Safety and Overall 2nd Place out of 117 team submissions")
            st.write("Ideated and developed Drive Woke! - a Flutter-based mobile application that aims to keep drivers awake by simulating conversations")
            #st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
            mention(label="Github Repo", icon="github", url="https://github.com/yuechen2001/LifeHack2022",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_he4d)
        with text_column:
            st.subheader("NUS Fintech Month Hackathon 2021 - Hosted by [NUS Fintech Society](https://fintechsociety.comp.nus.edu.sg/)")
            st.write("Awarded Overall 2nd Place")
            st.write("Ideated a multi-pronged approach using blockchain and machine learning methods to improve fraud detection amongst complex entities in a digital or hybrid (digital and manual) operating environment")
            #st.write("[Pitch Deck](https://www.linkedin.com/feed/update/urn:li:ugcPost:6761489595420037120/)")
            mention(label="Pitch Deck", icon="🪧", url="https://www.linkedin.com/feed/update/urn:li:ugcPost:6761489595420037120/)",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_ecc)
        with text_column:
            st.subheader("NUS Economics Case Competition - Hosted by [NUS Economics Society](https://www.nuseconsoc.com/)")
            st.write("Performed financial modelling and market research to suggest methods for brick-and-mortar retailers to compete against e-commerce stores")
            #st.write("[Report](https://drive.google.com/drive/u/4/folders/1NfsRr1P3xAkuJq3HEJ9LQU1uCo6TZIFK)")
            mention(label="Report", icon="📄", url="https://drive.google.com/drive/u/4/folders/1NfsRr1P3xAkuJq3HEJ9LQU1uCo6TZIFK",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_shopee)
        with text_column:
            st.subheader("[Shopee Product and Design Challenge 2021](https://careers.shopee.sg/event-detail/396)")
            st.write("Redesigned user interface of Shopee mobile app using Figma to reduce clutter and increase user utilization of in-app rewards")
            #st.write("[Figma Prototype](https://www.figma.com/proto/3UXT29N1RgVGDUlSBeWcPN/UI-Prototype-1?node-id=18-3&viewport=-675%2C231%2C0.32458001375198364&scaling=scale-down) | [Pitch Deck](https://drive.google.com/file/d/12qnveB-SMjG_gF_gwNj3Nr-JsKeyKd6g/view)")
            mention(label="Figma", icon="📱", url="https://www.figma.com/proto/3UXT29N1RgVGDUlSBeWcPN/UI-Prototype-1?node-id=18-3&viewport=-675%2C231%2C0.32458001375198364&scaling=scale-down",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_sbcc)
        with text_column:
            st.subheader("Singapore Business Case Competition 2020 - Hosted by [NTU Business Solutions Club](https://clubs.ntu.edu.sg/businesssolutions/)")
            st.write("Proposed solutions to help increase competitiveness of BreadTalk after performing market research and analysis on the F&B industry")
            #st.write("[Pitch Deck](https://drive.google.com/file/d/1kLgbBVuth4KvfhjaK00n30xlr4bmn-iM/view)")
            mention(label="Pitch Deck", icon="🪧", url="https://drive.google.com/file/d/1kLgbBVuth4KvfhjaK00n30xlr4bmn-iM/view",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_runes)
        with text_column:
            st.subheader("Contest 2.2 Beautiful Runes - CS1010S Programming Methodology")
            st.write("Awarded 1st Place for 2D Runes category out of over 600 students enrolled in the module for Academic Year 2020/21 Semester 1")
            st.write("2D pixel art created using Pillow (PIL) Library in Python")
            #st.write("[Github Repo](https://github.com/harrychangjr/runes)")
            mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/runes",)
elif choose == "Leadership and Volunteering":
    lv = [
        {
            'Position': 'Technical Writer',
            'Organization': "VIT Google Developer's Club",
            'Description': "Created comprehensive guides and tutorials on software development and coding best practices. Collaborated with student developers to ensure accuracy and clarity in documentation.",
            'image_url': 'images/gdg.png',
            'org_url': ''
        },
        {
            'Position': 'Team Lead and PR Head',
            'Organization': 'VIT Dance Club',
            'Description': "Led a contingent of 150 members across 14 teams in the club inlcluding a street dancing team of 17 members to compete and win several cultural fests including Asia's biggest college festival - Mood Indigo",
            'image_url': 'images/dc.jpg',
            'org_url': ''
        },
        {
            'Position': 'Contributor',
            'Organization': 'Aket Foundation',
            'Description': "Supported the cause Village Development Program (Virtual Adoption of a child). Through the concept of virtual adoption, I was able to contribute financial resources to ensure the well-being, education, and overall development of a specific child within a village.",
            'image_url': 'images/aket.jpg',
            'org_url': 'org_url'
            
        },
        {
            'Position': 'Volunteer for the K-12 Program',
            'Organization': 'Smile Foundation',
            'Description': 'Organized campaigns to raise funds and awareness for the education of underprivileged children. Alongside this, I also volunteered as a meal server on the weekends.',
            'image_url': 'images/smilef.jpg',
            'org_url': ''
        }
    ]
    for i in range(0, len(lv), 2):
        with st.container():
            cols = st.columns(2)
            for idx, col in enumerate(cols):
                if i + idx < len(lv):
                    exp = lv[i + idx]
                    with col:
                        st.image(exp['image_url'], width=300)
                        st.subheader(exp['Position'])
                        st.markdown(f"**{exp['Organization']}**")
                        st.markdown(f"- {exp['Description']}")
    
elif choose == "Blog":
    st.header("Blog")
    selected_options = ["Overview", "Article & Essay List",
    #"“It’s not pink, it’s salmon” – Why I returned to my previous start-up for FREE", 
                        "Mayans MC – Season 5 Detailed Preview",
                        "Finding success as an outlier (Extracted Using Wordpress REST API)",
                        "Finding success as an outlier (Formatted Version)", 
                        "Should the statue of Sir Stamford Raffles disappear for good?",
                        "Should the Women's Charter replace one of the existing ten objects in the module?", 
                        "Does gender inequality still have a place in Singapore's society today?", 
                        "Reflections on Organising an 850-participant Data Analytics Competition (Extracted Using Google Sites REST API)",
                        "Reflections on Organising an 850-participant Data Analytics Competition (Formatted Version)",
                        "Worsened health disparities based on ethnicity and gender due to COVID-19",
                        "Obstacles in promoting healthy eating habits",
                        "Role of healthcare data analytics in managing COVID-19",
                        "Evaluating 'Chinese Privilege' in Singapore: Special Assisted Plan Schools",
                        "Analysing usefulness of word clouds in mental health studies",
                        "Investigating the relationship between culture and sweet-sour taste interactions",
                        "Timing vaccination campaign to reduce measles infections"
                        ]
    selected = st.selectbox("Which section or write-up would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Overview":
        st.subheader("Overview")
        st.markdown("""
        I must admit - I hated reading books as a kid, and in turn, I disliked writing essays or expressing my thoughts as well. However, throughout my time in university, I have gradually picked up the essence of writing, to the extent of making use of it as a destressor from my technical modules.

        Although my writing skills were novice at best when I was a freshman, I eventually got better at it (in my opinion), even to the extent of writing content articles as a regular hobby! It is indeed an asset to pick up as many skills as possible when still young, as you never know when you may need to utilise a particular skill whenever necessary.

        In this section, you will be able to read some of my finest write-ups from my university experiences, based on topics varying from science to politics. For those looking forward to a good read, enjoy!
        """)

    elif selected == "Article & Essay List":
        st.subheader("Article & Essay List")
        #with st.container():
            #text_column, image_column = st.columns((3,1))
            #with image_column:
                #st.image(img_qb)
            #with text_column:
                #st.subheader("“It’s not pink, it’s salmon” – Why I returned to my previous start-up for FREE")
                #st.write("*May 21, 2023* | [*Article*](https://antcabbage.wordpress.com/2023/05/21/its-not-pink-its-salmon-why-i-chose-to-return-to-my-previous-start-up-for-free/)")
                #st.write("A personal reflection explaining why I returned to my former start-up to diversify my experiences")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_mayans)
            with text_column:
                st.subheader("Mayans MC - Season 5 Detailed Preview")
                st.write("*May 13, 2023* | [*Article*](https://antcabbage.wordpress.com/2023/05/13/mayans-mc-season-5-detailed-preview/)")
                st.write("A preview of the fifth and final season Mayans MC, along with its similarities with Sons of Anarchy")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_outlier)
            with text_column:
                st.subheader("Finding success as an outlier")
                st.write("*April 12, 2023* | [*Article*](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
                st.write("A personal reflection of my tumultous undergraduate journey so far - and how I finally found my resolve")
                #st.write("[Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")       
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_raffles)
            with text_column:
                st.subheader("Essays for Final Test - GES1037: A History of Singapore in Ten Objects")
                st.write("*April 29, 2022* | [*Essays*](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Take%20Home%20Test.pdf)")
                st.markdown("""
                Essays written within 24-hour window in Academic Year 2021/22 Semester 2:
                - Q4: Should the statue of Sir Stamford Raffles disappear for good?
                - Q6: Should the Women's Charter replace one of the existing ten objects in the module? 
                """)       
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_gender)
            with text_column:
                st.subheader("Does gender inequality still have a place in Singapore's society today?")
                st.write("*April 2, 2022* | [*Term Paper*](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Term%20Paper.pdf)")
                st.markdown("""
                Term paper submitted for the module GES1037: A History of Singapore in Ten Objects in Academic Year 2021/22 Semester 2
                """)       
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_dac)
            with text_column:
                st.subheader("Reflections on Organising an 850-participant Data Analytics Competition")
                st.write("*February 18, 2022* | [*Article*](https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0&pli=1)")
                st.markdown("""
                A personal reflection of organising a large-scale online competition over the course of 6 months - co-written with [Axel Lau](https://www.linkedin.com/in/axel-lau/)
                """)
                #st.write("[Article](https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0&pli=1)")
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_covid)
            with text_column:
                st.subheader("Essays for Final Assignment - GEH1049: Public Health in Action")
                st.write("*November 12, 2021* | [*Essays*](https://github.com/harrychangjr/geh1049/blob/main/GEH1049%20Final%20Assignment.pdf)")
                st.markdown("""
                Essays written in Academic Year 2021/22 Semester 1:
                - Q1: Worsened health disparities based on ethnicity and gender due to COVID-19
                - Q2: Obstacles in promoting healthy eating habits
                - Q3: Role of healthcare data analytics in managing COVID-19
                """)
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_hci)
            with text_column:
                st.subheader("Evaluating 'Chinese Privilege' in Singapore - Special Assisted Plan Schools")
                st.write("*April 29, 2021* | [*Final Essay*](https://github.com/harrychangjr/ges1010/blob/main/GES1010%20Final%20Essay%20A0201825N.pdf)")
                st.markdown("""
                Final essay submitted for the module GES1010: Nation-building in Singapore in Academic Year 2020/21 Semester 2
                """)      
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_wordcloud)
            with text_column:
                st.subheader("Analysing usefulness of word clouds in mental health studies")
                st.write("*March 5, 2021* | [*Essay*](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20GET1030%20Individual%20Assignment%20Final.pdf)")
                st.markdown("""
                Individual assignment submitted for the module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2
                """)
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_taste)
            with text_column:
                st.subheader("Investigating the relationship between culture and sweet-sour taste interactions")
                st.write("*October 31, 2020* | [*Article*](https://github.com/harrychangjr/sp1541-nlp/blob/main/Originals/SP1541%20NA2.pdf)")
                st.write("*Are we correct to stereotype taste perceptions and preferences based on different cultures?*")
                st.write("Science news article submitted for the module SP1541: Exploring Science Communication through Popular Science in Academic Year 2020/21 Semester 1")      
        with st.container():
            text_column, image_column = st.columns((3,1))
            with image_column:
                st.image(img_measles)
            with text_column:
                st.subheader("Timing vaccination campaign to reduce measles infections")
                st.write("*September 30, 2020* | [*Article*](https://github.com/harrychangjr/sp1541-nlp/blob/main/Originals/SP1541%20NA1.pdf)")
                st.write("*Despite having a vaccine that is readily accessible, measles cases and deaths are still surging worldwide, especially in recent years. Why is this so and are there any long-term solutions to resolve this?*")
                st.write("Science news article submitted for the module SP1541: Exploring Science Communication through Popular Science in Academic Year 2020/21 Semester 1")
    elif selected == "Mayans MC – Season 5 Detailed Preview":
        with st.echo(code_location="below"):
            import streamlit as st
            import requests
            from bs4 import BeautifulSoup

            def arrange_images_side_by_side(html_content):
                soup = BeautifulSoup(html_content, "html.parser")
                images = soup.find_all("img")

                i = 0
                while i < len(images) - 1:
                    current_image = images[i]
                    next_image = images[i + 1]

                    current_figure = current_image.find_parent("figure")
                    next_figure = next_image.find_parent("figure")

                    # Check if the next image is an immediate sibling
                    if current_figure and next_figure and current_figure.find_next_sibling() == next_figure:
                        container = soup.new_tag("div", style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center;")
                        current_figure.wrap(container)
                        next_figure.wrap(container)

                        # Set the same height for both images and add a little margin for better centering
                        current_image['style'] = "height: 400px; margin: auto;"
                        next_image['style'] = "height: 400px; margin: auto;"

                        # Update the images list
                        images = soup.find_all("img")
                    i += 1

                return str(soup)

            def get_post_by_id(url, post_id):
                site_url = url.replace("https://", "").replace("http://", "")
                response = requests.get(f"https://public-api.wordpress.com/wp/v2/sites/{site_url}/posts/{post_id}?_embed")
                response.raise_for_status()
                return response.json()

            url = "https://antcabbage.wordpress.com"
            post_id = 83
            post = get_post_by_id(url, post_id)

            post_title = post["title"]["rendered"]
            post_content = post["content"]["rendered"]
            soup = BeautifulSoup(post_content, "html.parser")
            clean_post_content = soup.get_text()
            st.subheader(post_title)
            st.write("May 13, 2023 | [Article](https://antcabbage.wordpress.com/2023/05/13/mayans-mc-season-5-detailed-preview/)")
            st.write("*The content of this article was extracted using `requests` and `BeautifulSoup`, along with the Worpress REST API. Thus, there may be some formatting and alignment issues, especially for the images and/or video featured. A code block will also be shown at the bottom of this article to demonstrate how the REST API was used with the respective libraries to extract the content from the Wordpress site*")
            modified_content = arrange_images_side_by_side(post_content)
            st.markdown(modified_content, unsafe_allow_html=True)
    elif selected == "Finding success as an outlier (Extracted Using Wordpress REST API)":
        with st.echo(code_location="below"):
            import streamlit as st
            import requests
            from bs4 import BeautifulSoup

            def arrange_images_side_by_side(html_content):
                soup = BeautifulSoup(html_content, "html.parser")
                images = soup.find_all("img")

                i = 0
                while i < len(images) - 1:
                    current_image = images[i]
                    next_image = images[i + 1]

                    current_figure = current_image.find_parent("figure")
                    next_figure = next_image.find_parent("figure")

                    # Check if the next image is an immediate sibling
                    if current_figure and next_figure and current_figure.find_next_sibling() == next_figure:
                        container = soup.new_tag("div", style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center;")
                        current_figure.wrap(container)
                        next_figure.wrap(container)

                        # Set the same height for both images and add a little margin for better centering
                        current_image['style'] = "height: 400px; margin: auto;"
                        next_image['style'] = "height: 400px; margin: auto;"

                        # Update the images list
                        images = soup.find_all("img")
                    i += 1

                return str(soup)

            def get_post_by_id(url, post_id):
                site_url = url.replace("https://", "").replace("http://", "")
                response = requests.get(f"https://public-api.wordpress.com/wp/v2/sites/{site_url}/posts/{post_id}?_embed")
                response.raise_for_status()
                return response.json()

            url = "https://antcabbage.wordpress.com"
            post_id = 72
            post = get_post_by_id(url, post_id)

            post_title = post["title"]["rendered"]
            post_content = post["content"]["rendered"]
            soup = BeautifulSoup(post_content, "html.parser")
            clean_post_content = soup.get_text()
            st.subheader(post_title)
            st.write("April 12, 2023 | [Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
            st.write("*The content of this article was extracted using `requests` and `BeautifulSoup`, along with the Worpress REST API. Thus, there may be some formatting and alignment issues, especially for the images and/or video featured. A code block will also be shown at the bottom of this article to demonstrate how the REST API was used with the respective libraries to extract the content from the Wordpress site*")
            modified_content = arrange_images_side_by_side(post_content)
            st.markdown(modified_content, unsafe_allow_html=True)
        
        
    elif selected == "Finding success as an outlier (Formatted Version)":
        st.subheader("Finding success as an outlier (Formatted Version)")
        st.write("April 12, 2023 | [Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
        st.write("*The content of this article was manually copied and pasted from the original site, along with manually embeedded media and captions for formatting purposes*")
        st.markdown("""
        > Outlier – a person or thing differing from all other members of a particular group or set.

        This was what one of my recent interviewers defined himself as, when I asked him more about his experiences before working at his current position. He elaborated that he has been working at his current company for over 20 years upon graduation, an achievement he takes pride in which also exemplifies his undying passion for his job. This is something that most employees do not normally do, as it is common to switch job environments after every few years to revitalize their careers.

        The conversation that I had with him really hit me that day – because in some way, I would also define myself as an outlier, especially in my university life. Having originally intended to graduate this semester, I would say that I have experienced many ups and downs throughout these past 4 years. From my many mistakes that have resulted in tumultuous phases, to particular happy moments and achievements that I should have cherished more dearly, perhaps it was indeed fate that has shaped me to who I am today.

        Blessed with the privilege of good academics throughout junior college, I originally intended to pursue a degree in chemical engineering, particularly due to my initial fascination for pharmaceuticals and how they could enhance our bodies. During my national service, however, a new course for pharmaceutical science was launched in my school, and given my interest back then, I took a leap of faith and applied for a switch before I formally commenced my university education. 

        Fast forward to my first semester, and I gradually realized that I had made one of the biggest mistakes of my life. I discovered that I was merely blinded by the potential career prospects of this new degree, which has yet to prove itself with a tenured track record. Without seriously considering the pros and cons, I would dare say that I foolishly embarked on this journey without prior preparation and research, resulting in me eventually flunking that semester altogether.

        “But you have all the potential in the world” – said some of my peers and mentors, who were then envious of me being in this prestigious course. Regardless of whether I was merely being motivated to complete a particular task, or that someone genuinely identified the potential in me, I eventually realized that this quote alone made me hate a lot about myself back then, especially whenever I flunked. I would often feel an overwhelming sense of disappointment whenever I felt that I fell short of my own (high) expectations, which were imposed by this “potential” I thought I had. 

        In a way, I was humbled by the experience. Thinking that the competition in junior college was tough enough, having the opportunity to meet different varieties of students changed the game for me. Working and interacting with many youths who came from different backgrounds – including student entrepreneurs, future researchers and national athletes, I realized that they were much more driven, passionate and hardworking at their craft than me, and for the right reasons. Unlike me, it was clear that they had long term plans in mind to hone their skills in order to pursue their ideal careers in the future.

        And so, after taking my second semester off with a leave of absence, I decided to embark on another journey, this time restarting as a data science undergraduate. Knowing that this would delay my graduation and my tuition fees would be higher for my extended final year, I prayed that the journey would be smoother this time round. Although this was definitely not the case due the vastly different disciplines between the 2 degrees, I was privileged to be able to experience a certain degree of success over the next 2 years, even though my academic results signified otherwise. With my expectations being lowered this time round, I felt that at the very least, I was enjoying myself more in whatever I was pursuing.

        Unfortunately, I made the mistake of succumbing to peer pressure once again, this time pursuing too many commitments that I eventually could not handle, resulting in dire consequences both in my academics and interpersonal relationships. Being blinded by greed and ego once more, I knew that I had to take a step back and reflect on what really went wrong, having made the same life mistake multiple times now, which was what I have been doing throughout this semester.

        This was when I truly understood who I really am – one who merely wants to experience life without any comparison to others. I have discovered that the only real critic that I need to value is myself, and develop the self-awareness of whether I am truly enjoying whatever I am doing, or at least fully commit to the purpose of my actions. Not saying that I should downright ignore constructive criticism and opinions against me, but rather question myself from time to time whether their opinions really matter at any particular moment. In addition, self-care is also what I am trying to prioritize, where I should learn to take breaks when necessary.

        As Israel Adesanya said after his most recent bout against Alex Pereira, a mixed martial artist who he lost to 3 times (in both MMA and kickboxing) beforehand to regain the UFC Middleweight Championship:

        > “I hope every one of you — behind the screen and in this arena — can feel this level of happiness, just one time in your life. But guess what, you will never feel this level of happiness if you don’t go for something in your own life. When they knock you down, when they try and sh*t on you… and try and put their foot on your neck. If you stay down, you will never ever get that resolve. Fortify your mind!”

        > **Israel Adesanya**""")
        with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.video("https://www.youtube.com/watch?v=ZNoODFgTq3c")
            with col3:
                st.empty()
        st.markdown("""
        Likewise, I have learnt not to harp on my mistakes for too long, otherwise this would impede me in the long run, and I would never be able to bounce back from what I have done. It is indeed important to forgive yourself and try to strive for the better, even though others may doubt so.

        So who am I – really? To answer this, I would compare myself to 2 characters that I have enjoyed following on television. The first would be Alex Moran, the protagonist of sitcom Blue Mountain State. His character is that of a second-string quarterback for the majority of the show, only aiming to be an “Average Joe” after he graduates from college. The second would be Orange Cassidy, a professional wrestler whose gimmick is based on being the “King of Sloth Style”, otherwise only trying to win when necessary, but doesn’t bother otherwise.
        """)
        with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.image(img_bmsaew, caption = "From left to right: Alex Moran (played by Darin Brooks in Blue Mountain State), Orange Cassidy", width=600, )
            with col3:
                st.empty()
        st.markdown("""
        Drawing inspiration from these two characters, I would say I have now lowered the expectations that I have set for myself, and have learnt to be more appreciative for the opportunities that I have instead. It’s not wrong to be surrounded by driven and passionate people in your circle, but at the end of the day, I feel it’s not worth putting in exceptional efforts if that means sacrificing your own personal well-being.

        And back to my self-reflection this semester: even though I’m not graduating within the next few weeks, it was still satisfying to live as though I was – with minimal commitments, barely dropping by physical lessons, and even finishing a final paper within one-third of the allocated duration before leaving early. It was indeed a breath of fresh air that I needed to rebuild myself for the better in the long run. It felt lonely at times, but when you can find happiness and contentment in being alone, what’s there to stop you from enjoying yourself in better scenarios?

        Throughout this time, it was only recently that I finally figured out what my career goals are. Many may have realized this way before me – but it’s okay, because everyone takes their own time to figure their lives out gradually. Given my unorthodox undergraduate life, I would say I’m more than grateful to be more clear about what I want in the end. I wish I graduated now, but perhaps this was a blessing in disguise.

        > “Success is not defined by either wealth or status. Success is about relations, friends, family and your belief in stewardship. Those will bring you to many places.”

        Those were the parting words from my boss in national service. Although his intentions are good, I would say that I define success a bit differently – being content with whatever you have at the present moment. 

        With that being said, I’ve learnt that there’s nothing wrong being an outlier – in fact, we are all outliers in our own right, because we are the protagonists in our own story that makes us unique. As my GP teacher in junior college once said, you need to develop yourself with an interesting story and cannot be boring – and I hope whatever that I have written here illustrates an engaging narrative that can be enjoyed by all.

        To end off, I’d like to dedicate this write-up to those graduating soon, as well as others like myself, who had an unconventional journey during university for one reason or another. Even with multiple mishaps along the way, I believe that everyone can eventually find their own success as an outlier.
        """)
    elif selected == "Should the statue of Sir Stamford Raffles disappear for good?":
        st.subheader("Should the statue of Sir Stamford Raffles disappear for good?")
        st.write("April 29, 2022 | [Essays](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Take%20Home%20Test.pdf)")
        st.markdown("""
        Sir Stamford Raffles is often credited as the true founder of modern Singapore,
        having “transformed Singapore from an obscure fishing village to a great seaport and
        modern metropolis”. To commemorate his legacy, a statue of Raffles was erected by the
        Singapore government to acknowledge British colonialism as part of the country’s history.
        As we are now living in the post-colonial era, however, many citizens do not see the need
        to commemorate this, especially since most of them did not live in the colonial era. Thus,
        I would agree with the standpoint that the Raffles statue should be taken down for good.

        Firstly, the statue should be taken down due to the possible standpoint that citizens
        recognise Sang Nila Utama as the true founder of modern Singapore, instead of Sir
        Stamford Raffles. While Raffles had first landed in Singapore in 1819 that helped shape
        Singapore to what it is today, Sang Nila Utama had already stepped foot in the country
        as early as 1299, founding the nation as the Kingdom of Singapura back then. It is
        important to recognise the story behind how the Malay prince first landed on the land
        known as Temasek before renaming the land as Singapura. This is especially true
        considering that the indigenous people in the country were Malays, and it would be a
        better idea to credit more of Singapore’s history to its geographical neighbours rather than
        to British colonialism. The introduction of the Singapore Bicentennial in 2019 also
        acknowledges this, citing that not many Singaporeans knew about the existence of Sang
        Nila Utama, believing that Raffles was the true founder instead. Given that the Singapore
        government would want its citizens to better understand Singapore’s history especially
        before 1819, it would be in its best interest to remove the statue instead, to avoid overacknowledging
        Raffles’ influence in Singapore’s history.
        
        Secondly, the statue should be taken down to avoid misinterpretations that
        Singapore is still being influenced by British colonialism. While Singapore is no longer a
        British colony, it still establishes a diplomatic relationship with the United Kingdom,
        forming various trade and political partnerships between the two countries in the process.
        Furthermore, Singapore is also a part of the Commonwealth, where many of the member
        nations are former British colonies. Member nations of this political association enjoy
        exclusive diplomatic partnerships with one another to boost each other’s economies.
        However, having the Raffles statue being erected still in Singapore may give an
        impression that the country still acknowledges the former British empire as its benefactor.
        This is certainly not the case in today’s context, especially if Singapore wishes to be seen
        as an independent nation, it should be recognised as an equal to a country such as the
        United Kingdom, and not as an underling of the latter. As such, removing the statue would
        help to avoid that misconception.

        Thirdly, by removing the statue of Raffles, I believe that this would truly signify
        Singapore’s growth from an economic beneficiary in the colonial era to an economic
        powerhouse in the modern world today. As mentioned in the article attached to this
        question, Singapore has transformed into a global trading port, experiencing volumes of
        economic growth every year. While Singapore used to benefit as a trading hub in the past
        largely due to British rule, the country can now take the next step and help its
        neighbouring countries to prosper economically together through mutually beneficial
        trade partnerships. Singapore’s status as an independent and prospering nation can
        indeed potentially promote the economic growth of the entire Southeast Asian region as
        well, filling in the shoes of its previous colonial ruler. Thus, removing the statue could be
        a symbol of Singapore finally emerging from its previous colonial ruler, in order to step up
        as a strong economic power moving forward.

        To sum up, while Raffles did set the precedent for Singapore to eventually prosper
        as an economic trading port, it is not necessary for his statue to remain erected in our
        soil. To many of our ancestors, the colonial era may signify long bouts of hardships and
        poverty, especially under the rule of the British, which may contribute to local sentiments
        that the statue is not necessary. Furthermore, almost all Singaporean citizens in our
        society today did not actually live in the colonial era, making it difficult for them to
        personally relate to Raffles and his rule back in the 1800s. Therefore, I believe that it is
        indeed essential for the statue to be eventually removed, so that we can move forward
        from being recognised as merely a former British colony and write the next chapter in our
        history as a growing economic power.
        """)
    elif selected == "Should the Women's Charter replace one of the existing ten objects in the module?":
        st.subheader("Should the Women's Charter replace one of the existing ten objects in the module?")
        st.write("April 29, 2022 | [Essays](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Take%20Home%20Test.pdf)")
        st.markdown("""
        In 1961, the Women’s Charter was passed in Singapore Parliament, with the
        intention to improve and protect the legal rights of women in Singapore. While it was
        initially designed to ensure greater equality in legal matters such as marriage and
        housing, this Act has left behind a legacy by inspiring more similar initiatives to be set up
        in Singapore, including the formation of AWARE to further promote gender equality. Given
        how the roles of the two genders have evolved throughout the course of our history, I
        strongly support the idea of including the Women’s Charter as one of the ten featured
        objects in the future iterations of this module.

        For starters, we should first understand why this Act was introduced in the first
        place. During the colonial era in Singapore, females were confined to the role of
        housewife and caregiver, given the traditional religious and socio-cultural norms at that
        point of time. An example of this would be the membership system in the Singapore
        Recreation Club, with females only being allowed to register as members in 1956 (73
        years after the club’s founding) to participate in its various sporting and social activities,
        which were initially only catered to men. In contrast, males were seen to be the more
        dominant gender especially due to the prevalence of polygamy, reiterating the stance that
        women were indeed inferior to men at that point of time. Later in the colonial era, the
        British government introduced the Chinese Protectorate, which mainly focused on
        protecting women from illegal prostitution. While this only served to preserve the basic
        human rights of women in the country, this was an acknowledgement that more can be
        done for women to be treated more equally to men. In a sense, introducing the Women’s
        Charter could be seen as a step forward from the Chinese Protectorate, as it no longer
        merely focuses on basic human rights of women, but rather to introduce more legal rights
        in favour of women, especially in important aspects such as housing, marriage and
        children.

        While the introduction of the Women’s Charter was indeed successful in eventually
        banning polygamy by the 1960s, there was a declining interest in sustaining this women’s
        rights movement afterwards, as its introduction had already achieved its main purpose
        and there was no incentive to further promote gender equality at that point of time. As a
        result, an all-male Parliament was eventually formed from 1970 to 1984, with patriarchal
        policies being introduced once again. These included the announcement of a quota to
        restrict female medical students, as well as the compulsory offering of home economics
        as a subject for lower secondary girls. Such acts eventually led to the formation of
        AWARE in 1985, which set to undo such discriminatory policies against women and
        promote greater gender equality once again. The introduction of AWARE was indeed a
        big success, making use of its vision to provide support on various problems largely faced
        by women, including domestic violence, sexual assault, single parenthood and workplace
        harassment. As such, I believe that the Women’s Charter, as well as its accompanying
        history of emphasising the importance of gender equality in the long run, should indeed
        be an object for this module, so that students recognise its value especially in today’s
        ever-changing society.

        With regards to which current object should be replaced in favour of the Women’s
        Charter, however, I believe that the Sound Blaster should be removed as an object of the
        module. Given the more economic nature of the topic, I feel that the idea of discussing a
        Singaporean invention does not fit as well as the other objects, especially when this is a
        module offered by the Department of History in the National University of Singapore.
        If we were to look back at all the other objects that were taught in this module, be
        it an artefact from the pre-colonial era (Singapore Stone), a club established during the
        colonial era (Singapore Recreation Club), or modern objects such as the Kallang Roar
        and the movie ‘I Not Stupid’, what they have in common is that they have played a
        significant role in Singapore’s history, and have contributed in forging the Singaporean
        identity in the process. Looking at the ‘I Not Stupid’ movie for example, it has established
        a legacy of revamping the current educational system, proving that such filmmaking can
        be influential in establishing Singapore’s history as a progressing society if done right.
        While I recognise and applaud the efforts of Sim Wong Hoo and how his innovation
        of the Sound Blaster technology had contributed to our economy, I feel that this invention
        is not unique enough to be recognised as an ‘object’ of Singapore’s history. Such
        advancements in technology are less distinguishable between the different countries in
        our global economy, especially with many people around the world possibly having the
        misconception that these inventions largely only occur in larger countries such as the
        USA and China. In summary, this invention does not seem as impactful in influencing
        Singapore’s history compared to the other objects, which explains my decision to exclude
        this object in favour of the Women’s Charter if possible.

        To conclude, the story of the Women’s Charter and the subsequent formation of
        AWARE should indeed be included as an object in this module. This has taught us the
        importance of supporting the movement of gender equality, as well as the consequences
        of not sustaining such movements in the long run. I believe that this is an important lesson
        that Singaporeans can learn from, especially with the rising prevalence of women in our
        local workforce, including those in professional, managerial, executive and technical
        professions, which is a testament of the changing gender roles in our society today.

        *For context, this module is offered by the Department of History, Faculty of Arts and Social Sciences at the National University of Singapore. The ten objects that exemplify Singapore's rich history are:*
        1. Singapore Stone
        2. White Sand
        3. Abdullah's Story
        4. Singapore Recreation Club
        5. Old Ford Factory
        6. Majulah Singapura
        7. Block 45, Stirling Road
        8. Kallang Roar
        9. Sound Blaster
        10. I Not Stupid
        """)
    elif selected == "Does gender inequality still have a place in Singapore's society today?":
        st.subheader("Does gender inequality still have a place in Singapore's society today?")
        st.write("April 2, 2022 | [Term Paper](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Term%20Paper.pdf)")
        st.markdown("""
        On April 24, 2021, a new resolution was passed for women in the Singapore
        Recreation Club (SRC) to be entitled with the same rights and privileges as male
        members. With this new resolution, women now have voting rights, and can be elected
        to the club’s management committee. On top of this, they may assume the membership
        of either their spouse or their male next-of-kin. This news was announced after several
        failed attempts to amend the club’s constitution over the course of its 137 year history
        since its founding.

        This made me wonder: as one of Singapore’s most well-established clubs, what
        took it so long to amend this constitution and allow for female members to have equal
        rights? Furthermore, to what extent was gender inequality prevalent over the course of
        Singapore’s history? Therefore, this term paper intends to explore the history of gender
        inequality in Singapore, and whether it still has a place in our society today.
        For starters, we first need to understand the history of SRC. Originating as a
        crickets’ club for Eurasian players in 1883, the club gradually expanded to allow for more
        sports including football and hockey to be played, with various matches held against
        fellow clubs such as the Penang and Malacca Recreation Clubs. However, SRC
        membership was initially restricted to Eurasian males, with memberships only being made
        open to non-Europeans from 1955 onwards. Furthermore, European females were only
        formally allowed as guests in 1927, before subscription memberships were open to
        women of all races by 1956 as well, about one year after memberships were open to non-
        Eurasian men. With drinking as a main social activity and occasional tea parties as SRC’s
        non-sport social activities, it was no surprise that the club had only catered to men, which
        reinforced the stereotype against women as stay-at-home caregivers who did not enjoy
        such activities, especially before World War II.

        From a more macro perspective, the above-mentioned restriction of women’s
        enjoyment of such activities was also representative of the attitude towards women in
        colonial Singapore. With Singapore under British rule, women were “subjected to sociocultural
        and religious pressures to conform to the roles of wife and mother and to lead a
        more secluded life”. This had contrasted with men, whose gender was viewed to be more
        dominant based on the traditions of different cultures in Singapore. In addition, men were
        allowed to have multiple female partners, solidifying the perspective that women were
        inferior to men at that point of time.

        From the 1950s however, there was an increase in female leaders emerging in
        Singapore’s politics, leading the charge to pursue gender equality in the country. For
        instance, the establishment of the Women’s Charter by the Singapore government in
        1961 had aimed to provide equal rights to both genders. Clauses in the Charter include
        the compulsory registration of all marriages as well as providing women with the rights to
        their own housing, marriage and children if applicable. This was a big improvement from
        the Chinese Protectorate that was established during the colonial era, which mainly
        targeted at tackling the illegal prostitution of women. This showed that the local
        government did try to push for women to be treated as equals to men, instead of merely
        taking care of their basic human needs.

        In terms of job opportunities, more Singaporean women are seeking full-time
        employment by either pursuing higher education or entering the workforce, especially
        over the recent years. This breaks the traditional norm of women as stay-at-home
        caregivers, as more women aim to live independently as well. This is evident in the rise
        of the female labour force participation rate from 60.8% in 2018 to 61.2% in 2020.
        Furthermore, the increase in Professionals, Managers, Executives and Technicians from
        50% in 2010 to 59% in 2020 amongst female employees shows that women, just like
        men, are capable of upskilling themselves and contributing meaningfully to the Singapore
        economy when given the opportunity. While a pay gap still exists between employed
        males and females in Singapore, the inclusion of more women especially in higher
        positions within the local workforce has helped to decrease this gender pay gap, paving
        the way towards gender equality based on the employment aspect.

        To answer the question that I posed earlier: I believe that gender inequality should
        not have a place in Singapore’s society today. While there is still more that can be done
        to ensure equal opportunities for both men and women in the long run, we have to
        recognise that the local government today is indeed trying to advocate for women’s rights
        in Singapore. Its efforts in setting up the Women’s Charter and encouraging more women
        to take up higher positions in the workforce, for example, have likewise spurred similar
        initiatives amongst external organisations. This includes the founding of organisations
        such as AWARE for women to seek assistance against physical and emotional abuse, as
        well as the recent news of allowing women to take up management committee positions
        as well as have voting rights in SRC.

        As mentioned by Law and Home Affairs Minister Shanmugam in February 2021,
        perhaps one way to promote gender equality more in Singapore is for employees of both
        genders to be entitled to equal parental leave, as observed in certain European countries.
        This would grant men the opportunity to experience the caregiver role as normally
        experienced by their spouses. In fact, encouraging such role reversals between both
        genders would allow mutual understanding of each other’s roles, strengthening internal
        familial ties in the process.

        Alternatively, gender equality can be introduced in one’s education at a young age,
        such that this would be well ingrained in our future generations, gradually discouraging
        the idea of gender discrimination over time. Hopefully, these current initiatives and
        suggestions would allow women to realise their full potential and ensure that they are not
        seen as inferior compared to men. Furthermore, by having more diverse perspectives
        from both genders, this would allow for improved and balanced decisions to be made, in
        order to boost productivity in the workforce.

        References:

        1. Low, Y. (2021, April 24). After 137 years, Singapore Recreation Club votes to grant
        female members same rights and privileges as males. TODAY. Retrieved
        February 22, 2022, from https://www.todayonline.com/singapore/singaporerecreation-
        club-passes-resolution-allow-female-members-enjoy-same-rights-and

        2. Infopedia, National Library Board. (n.d.). Singapore Recreation Club. Retrieved
        February 23, 2022, from
        https://eresources.nlb.gov.sg/infopedia/articles/SIP_1041_2010-05-07.html

        3. Koh, T. (2019, February 18). Women's Quest for Justice and equality - A short
        history. The Straits Times. Retrieved February 24, 2022, from
        https://www.straitstimes.com/opinion/by-invitation-womens-quest-for-justice-andequality-
        a-short-history

        4. Ministry of Manpower, Singapore. (2021, October 12). Article: A gender-inclusive
        workforce. Retrieved February 24, 2022, from https://stats.mom.gov.sg/Pages/agender-
        inclusive-workforce.aspx

        5. Yuen-C, T. (2021, June 3). Men wanted: All need to play a part in pushing for
        gender equality, says Shanmugam. The Straits Times. Retrieved April 2, 2022,
        from https://www.straitstimes.com/singapore/politics/men-wanted-all-need-toplay-
        a-part-in-pushing-for-gender-equality-says-shanmugam
        """)
    elif selected == "Reflections on Organising an 850-participant Data Analytics Competition (Extracted Using Google Sites REST API)":
        with st.echo(code_location="below"):
            def fetch_google_site_article(url):
                response = requests.get(url)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")
                content = soup.find('div', class_='UtePc RCETm')  # You may need to inspect the Google Site source and adjust the class name

                return str(content)
            def arrange_images_side_by_side(html_content):
                soup = BeautifulSoup(html_content, "html.parser")
                images = soup.find_all("img")

                i = 0
                while i < len(images) - 1:
                    current_image = images[i]
                    next_image = images[i + 1]

                    # Check if the next image is an immediate sibling
                    if current_image.find_next_sibling() == next_image:
                        container = soup.new_tag("div", style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center;")
                        current_image.wrap(container)
                        next_image.wrap(container)

                        # Set the same height for both images and add a little margin for better centering
                        current_image['style'] = "height: 200px; margin: auto;"
                        next_image['style'] = "height: 200px; margin: auto;"

                        # Update the images list
                        images = soup.find_all("img")
                    i += 1

                return str(soup)
            url = "https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0"
            content = fetch_google_site_article(url)
            modified_content = arrange_images_side_by_side(content)
            st.write("*The content of this article was extracted using `requests` and `BeautifulSoup`, along with the Google Sites REST API. Thus, there may be some formatting and alignment issues, especially for the images and/or video featured. A code block will also be shown at the bottom of this article to demonstrate how the REST API was used with the respective libraries to extract the content from the Google Sites webpage*")
            st.markdown(modified_content, unsafe_allow_html=True)
    elif selected == "Reflections on Organising an 850-participant Data Analytics Competition (Formatted Version)":
        st.subheader("Reflections on Organising an 850-participant Data Analytics Competition (Formatted Version)")
        st.write("February 18, 2022 | [Article](https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0&pli=1)")
        st.write("*The content of this article was manually copied and pasted from the original site, along with manually embeedded media and captions for formatting purposes*")
        st.markdown("""
        **Overview**

        *What is DAC2022?*

        Serving as the annual flagship event of NUS SDS, this year’s Data Analytics Competition attracted over 850 participants across 230 teams from our 6 local universities. Originating as a Data Science Competition a few years ago, our organising team opted for a new format this year, choosing to focus on exploratory data analysis instead to make it more beginner-friendly. This year’s competition was a great success, which ultimately led to over 100 submissions and 5 top teams over the course of a week’s efforts. This year’s competition featured a geospatial dataset graciously sponsored by Grab and participants got to work with real-life transport data across countries in the region. This allowed them to practice their technical skills that they have learnt in class, giving them a glimpse of working as data analysts over a span of four days.

        To view the submissions made by our top 5 teams, you may check them out [here](https://drive.google.com/drive/u/0/folders/18O4XvIVAyTqtcXWM-v27vt8nDEpc5uIL)!

        **Background**

        With the success of last year’s Data Science Competition hosted by the previous organising team, we wanted to ensure that this year’s competition was similarly successful to reach a wider audience base. When we initially started planning the competition back in August 2021, we wanted to find a reputable sponsor for the event. Thanks to the Career Advisors at NUS Centre for Future-Ready Graduates (CFG), we were given the chance to pitch to Grab the idea of collaborating for our annual datathon event. Given the impromptu opportunity, we swiftly customised a pitch deck for Grab to explain the benefits of working with us for DAC 2022 such as raising awareness of Grab’s job/internship opportunities for students in NUS. It is not often that we get the opportunity to put our personal presentation skills to good use and convince an external party to host an event that would be beneficial for both parties.
        """)
        with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.image(img_dac1, caption = "A screenshot of our Opening Ceremony, featuring the introduction video of the dataset by Grab", width=600, )
            with col3:
                st.empty()
        st.markdown("""
        **Learnings**

        1. A smooth sea has never made a skilled sailor

        Organising such a large-scale datathon isn’t easy and will never be. There isn’t much information online as to what you need to have and what key points that you will need to take note of. Fortunately, NUS SDS does have previous experience hosting these kinds of events that we could tap into while we were planning for DAC 2022. Previous batches’ proper documentation of past planning mistakes and general competition guidelines helped us to gain a bigger picture of the event that we wanted to host and visualise the roles that we needed to fill.

        When we had first received the dataset from Grab, our organising team was stumped at extracting insights from it as no one on the team had prior experience with geospatial data. Our Workshop Team members, who were supporting the organising team, kindly volunteered to do more research on handling geospatial datasets. Their eagerness and confidence in dealing with the dataset allowed the organising team to confidently move forward with planning the rest of the competition.

        One major issue that we had faced midway through the planning of the competition was that we had underestimated the amount of work the organising team had to do to get the event up and running. There were indeed many administrative matters to resolve, which included the collation of Non-Disclosure Agreement forms as well as confirming the schedules of our judges to ensure their participation in our event. Handling all these processes in the right manner was indeed crucial to ensure the smooth operations of this event.

        On top of this, our initial plan was to host DAC 2022 on the 2nd week of January, when NUS students just started the semester in hopes of getting more teams to sign up. Yet, by the middle of December 2021, the organising team had not much to work with yet, with merely a skeletal structure of the event flow.

        After assessing the situation that we were in, where much of the event was not planned yet and the Grab personnel were currently on leave for the holidays, we decided to postpone the event to the start of February, right after the Chinese New Year celebrations to give ourselves more time to plan for the event. The main thought process behind this decision was that a delayed event will always be better than a rushed barely planned event.

        2. Communication is key (by Axel)

        It is one thing to have a vision for the competition and another to execute it. For myself, I tend to keep my ideas to myself and prefer to execute simple tasks by myself to not inconvenience others. However, in the scenario that I was in, having to juggle internship and planning of DAC, communicating my ideas to the team for them to execute was becoming increasingly important. After all, hosting DAC is a team effort and not an individual effort.

        Delegating tasks to the Events Team allowed for planning to occur even when I was occupied by my internship’s tasks. Delegating tasks to my team members also had a positive effect, as I was more able to focus on the big picture of the event and realise which areas of planning that we had neglected. Giving freedom to team members to resolve their own tasks at their own prerogative gave them a greater sense of ownership and an incentive to seek out innovative solutions.

        One thing that I’m really proud of in this competition came out of our member’s initiatives. One of them suggested using Discord as a central hub for disseminating information about the competition and providing a common platform for groups to discuss their projects. Discord has lots of useful bots and functions for running hackathons, such as user-defined roles and room assignment for teams. With Discord, we were also able to allow for Q&A questions to be publicly viewed and referenced by other teams. Using Discord did immensely help to streamline competition communication and I would wholeheartedly recommend other competition organisers to use it as well.

        Continuously communicating about what had not been done and what could be improved also helped us to assess the current situation that we were in. This really helped to smooth out the planning process and ensure that we covered any blind spots that we had failed to consider at first.

        Fortunately, our efforts paid off in the end, as there was an increase in the number of signups overall. This was particularly impressive, considering that we hosted our competition at a much later period compared to last year and were in fact expecting a decrease in participation rates. In fact, one of our main considerations of planning this event was to reinvigorate student life given the current COVID-19 situation. We were indeed glad to see that the large number of signups was a testament of this.

        Of course, this would not have been possible without the help of our Publicity Team members, who reached out to nearly 40 other student clubs to help us increase our outreach for the event. Other NUS departments such as CFG, Faculty of Science and School of Computing also helped us to publicise our event, which was much appreciated. Indeed, we’ve learnt that it’s vital for us to maintain good relations with other like-minded student organisations to ensure the success of organising such events.

        3. Failure is the key to success (by Prekshi)

        Similar to Axel, I gave my Marketing Team members the liberty to identify potential sponsors that could support our event. Doing this would allow them to learn more about the data/tech industry in general before we would proceed to shortlist our prospective partners and/or sponsors. Our team had managed to identify many different companies from various industries, but had faced rejections in the process. Worst still, many companies did not respond to our sponsorship emails, which felt demoralising at times.

        With multiple waves of attempts however, we managed to secure enough sponsors to support our event. Furthermore, we even exceeded our own sponsorship target in the end, leading to an overall increase in the prize pool compared to last year’s competition. The addition of having sponsored t-shirts from an external company was also a nice touch, given that this would entice participants to send in a valid submission to us for the competition.

        In summary, pursuing sponsorships was indeed an eye-opening experience for our team. This has taught us to be resilient when facing hardships or dejections, which would only make us mentally stronger over time. Without experiencing prior failures, achieving small successes like these would not be as enjoyable as one would expect. 
        """)
        with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.image(img_dac2, caption = "Jet New, President of NUS SDS, making his Closing Speech to thank all parties involved in DAC2022 during our Closing Ceremony", width=600, )
            with col3:
                st.empty()
        st.markdown("""
        4. Playing to each other's strengths

        Managing DAC 2022 was more than just handling a dataset, as there were a lot of tasks that we needed to complete to make it seem enticing for participants to join. The success of this event would not have been possible without the help and guidance from our fellow members in NUSSDS who excelled at their different roles:

        - Our President Jet and Vice-President of Events Ananya, for helping to look through our draft event proposals and giving constructive criticism of certain aspects of the event to make it better.

        - Our Events Team members Fang Ling, Shreya, Yi Fu and Madeline, for working together with Grab to plan out the timeline and problem statement for the competition. The team’s efforts were indeed vital in ensuring that everything operated smoothly without major hiccups throughout the competition week.

        - Our Marketing Team members: Gordon and Chenxiao for securing sponsors for DAC 2022; as well as Hannah and Aengus, for helping to manage a “Team Finder” feature of the event. This Team Finder matches people to form a team and was a rather important feature that we wanted to have. As most lessons are still taught virtually, we wanted to use DAC 2022 as a chance to connect data enthusiasts together to work on a meaningful project and from this experience hopefully build new friendships. Keeping to the theme of making the competition beginner-friendly, we wanted to make it as inclusive as possible to individuals who might not know many people interested in the field of data analytics. Hence, the Team Finder was important as it helps participants to make new friends and network with fellow data enthusiasts.

        - Stephen and Rui En, along with their Workshops Team members Keith, Javier and Wei Liang, for helping us to better understand the dataset and were integral in helping us to word the problem statement for the competition. Having them around to work on understanding the dataset really helped to lighten the load on the Events Team. During the actual competition, they assisted to get participants started on the provided dataset by hosting an introductory workshop.

        - Ethan and his Publicity Team members Briana, Tze Lynn and Yi Xuan, for helping to design cool slides and social media posts to make DAC 2022 look appealing! Their efforts in contributing appealing visuals and increasing social media outreach were also a major contributing factor to the success of this event.
        """)
        with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.image(img_dac, caption = "A screenshot from our Closing Ceremony, featuring our organising team, judges and participants", width=600, )
            with col3:
                st.empty()
        st.markdown("""
        **Conclusion**

        All in all, while organising DAC 2022 was a pretty stressful experience, we felt that this has helped us to achieve some form of personal growth and develop our leadership skills. We would both agree that this was indeed one of our toughest experiences in university so far. 

        **Acknowledgements**

        To commemorate the success of this event, we would also like to thank the following for their support:

        - Our main sponsor, Grab and its Data Science Team (consisting of Victor, Kenrex and Keru), for providing us with the dataset, prizes and expertise as judges;

        - Our other sponsors, AI Singapore and Quest Ventures, for providing us with prizes for our participants;

        - The NUS Department of Statistics and Data Science, for partially sponsoring the cash prizes for this event;

        - Gregory He and Emily Tan, our Career Advisors from NUS CFG who assisted us with onboarding Grab to support our event;

        - Jackie Tan, Head of Tribe Academy, for supporting our flagship event for the second consecutive year through his advanced technical workshop that was vital to the competition;

        - Prof Carol Hargreaves, Director of NUS Data Analytics Consulting Centre, for accepting our invitation as one of our judges;

        - And last but not least, the undergraduate population amongst our local universities for either participating actively in our competition or helping to spread the word about our event through various social media platforms.

        We hope that all parties involved have enjoyed their experience throughout the competition and had fun in the process. Our society looks forward to organising this flagship event again next year, so that more students will be inspired by the applications of data science and analytics in the real world.

        If this post has inspired you and you are keen to take on the challenge of hosting the next iteration of our flagship datathon event, do look out for our next recruitment cycle over the summer holidays.

        To find out more about Data Analytics Competition 2022, do check out the recordings of the following online events and workshops from the competition below:
        """)
        st.subheader("Opening and Closing Ceremonies")
        with st.container():
            col1, col2 = st.columns((2,2))
            with col1:
                st.video("https://www.youtube.com/watch?v=j0yvVP5XvTk")
            with col2:
                st.video("https://www.youtube.com/watch?v=goSAydRaOjY")
        st.subheader("Beginner and Advanced Workshops")
        with st.container():
            col1, col2 = st.columns((2,2))
            with col1:
                st.video("https://www.youtube.com/watch?v=6n3uQFZdN9g")
            with col2:
                st.video("https://www.youtube.com/watch?v=UlUU_WW3H_0")
        st.markdown("""
        *Axel Lau is the Events Director of the NUS Statistics and Data Science Society (AY21/22)*

        *Harry Chang is the Marketing Director of the NUS Statistics and Data Science Society (AY21/22)*       
        """)

    elif selected == "Worsened health disparities based on ethnicity and gender due to COVID-19":
        st.subheader("Worsened health disparities based on ethnicity and gender due to COVID-19")
        st.write("November 12, 2021 | [Essays](https://github.com/harrychangjr/geh1049/blob/main/GEH1049%20Final%20Assignment.pdf)")
        st.markdown("""
        COVID-19 has worsened health disparities within countries based on ethnicity, as the latter often corresponded to socioeconomic status (SES) levels. In general, lower-income minorities are more prone to chronic illnesses and would require more care. This is especially true for illegal immigrants who tend to avoid local healthcare facilities altogether to prevent future deportation. For instance, in the US, African-American and Hispanic minorities are more probable in living in congested environments and working in blue-collar jobs compared to the Caucasian majority. These minorities tend to travel by bus or train with large crowds, as many of them do not own private vehicles. By considering such conditions, these individuals would be more likely to fall ill and even contract airborne illnesses, including COVID-19 (Lopez, 2021). Furthermore, recent COVID-19 data has shown that mortality and hospitalisation rates have an association with Black or Brown ethnicities, also commonly described as the “ethnicity effect”. US hospitalisation rates were much higher amongst the African-Americans (1.8) and Hispanics (1.6) compared to the Whites (0.5) when considering these ethnicities’ prevalence ratios (Hughes et al., 2021). It was also reported in July 2020 that 1.6 million Hispanics in the US were deprived of their healthcare coverage due to COVID-19 (Gangopadhyaya et al., 2020). As the aforementioned argument demonstrated that ethnicity is often stereotyped as an SES indicator, it is proven that ethnic minorities within countries generally have poorer health outcomes. Therefore, COVID-19 has indeed widened the health disparities in terms of ethnicity within countries, particularly when comparing the Whites and the Blacks/Browns.
        
        COVID-19 has also widened health disparities within countries based on gender. Traditionally, women would tend to be at a physical disadvantage compared to males, often leading to a greater risk of undergoing various health problems for the former. Based on biological research, women have a higher chance of experiencing musculoskeletal diseases including osteoporosis, and subsequently cardiovascular health problems as compared to men. This gender health disparity is further exacerbated especially with the introduction of lockdowns and travel restrictions due to COVID-19, limiting the healthcare required for treatment, especially amongst females (Guerrina, 2021). Besides physical well-being, the mental health aspect has also been adversely affected especially amongst women as compared to men. In a 2020 Jordan study, research has revealed that almost 40% of locals have experienced anxiety from COVID-19 related quarantines. Amongst these individuals, data has showed “that psychological stress levels were significantly higher in women, especially in unmarried or younger than 50 years” (Massad et al, 2020). In the UK, it was also discovered that domestic violence rates have more than doubled due to the COVID-19 pandemic. The typical pre-pandemic death rate of about 6 deaths (of women and children) per month due to such violence peaked at 16 during the first month of lockdown in the country (Bambra et al., 2021). Again, this increased domestic violence is often attributed to social isolations which have aggregated the mental well-being of families during the pandemic. In summary, case studies have shown that women are likely to experience more long-term physical and mental health problems than men, and this gender health disparity has evidently increased due to COVID-19.
        
        To conclude, the worsening gender health disparity due to COVID-19 is more serious as compared to that of ethnicity. Women, often appointed the role of caregivers to children, are essential in growing our global population of future generations. However, given the fact that approximately 70% of healthcare workers are female worldwide (Salles, 2021), the latter is at a much higher risk of exposure to COVID-19, which would be detrimental to human reproduction in order to maintain or grow the global population due to the lives of females lost to the pandemic. On the other hand, the worsening ethnic health disparity due to COVID-19 would be considered relatively less serious as many governments worldwide are experiencing related issue(s) that are either similar or exactly the same. They can collaborate with each other in an international forum and come up with a general solution, before tweaking them based on their respective contexts to help close this ethnic gap in their individual countries.

        References:

        1. Lopez, L., III MD. (2021). Racial and Ethnic Health Disparities Related to COVID-19. Health Disparities | JAMA | JAMA Network. https://jamanetwork.com/journals/jama/fullarticle/2775687 
        2. Hughes, G. D., Mbamalu, O. N., Okonji, C. O., & Puoane, T. R. (2021). The Impact of Health Disparities on COVID-19 Outcomes: Early Findings from a High-Income Country and Two Middle-Income Countries. Journal of racial and ethnic health disparities, 1–8. Advance online publication. https://doi.org/10.1007/s40615-021-00999-5 
        3. Gangopadhyaya, A., Karpman, M., & Aarons, J. (2020). As the COVID-19 Recession Extended Into the Summer of 2020, More Than 3 Million Adults Lost Employer-Sponsored Health Insurance Coverage and 2 Million Became Uninsured. RWJF. https://www.rwjf.org/en/library/research/2020/09/as-covid-19-recession-extended-into-summer-2020-more-than-3-million-lost-employer-sponsored-health-insurance.html 
        4. Guerrina, R. (2021). Health and Gender Inequalities of the COVID-19 Pandemic: Adverse Impacts on Women’s Health, Wealth and Social Welfare. Frontiers. https://www.frontiersin.org/articles/10.3389/fgwh.2021.670310/full#B29 
        5. Massad, I., Al-Taher, R., Massad, F., Al-Sabbagh, M. Q., Haddad, M., & Abufaraj, M. (2020). The impact of the COVID-19 pandemic on mental health: early quarantine-related anxiety and its correlates among Jordanians. Eastern Mediterranean Health Journal, 26(10), 1165-1172. https://doi.org/10.26719/emhj.20.115
        6. Bambra, C., Albani, V., & Franklin, P. (2021). COVID-19 and the gender health paradox. Scandinavian Journal of Public Health, 49(1), 17-26. https://journals.sagepub.com/doi/pdf/10.1177/1403494820975604 
        7. Salles, A. (2021). COVID has worsened gender disparities, especially for women of color. The Clayman Institute for Gender Research. https://gender.stanford.edu/news-publications/gender-news/covid-has-worsened-gender-disparities-especially-women-color-heres 
        """)
    
    elif selected == "Obstacles in promoting healthy eating habits":
        st.subheader("Obstacles in promoting healthy eating habits")
        st.write("November 12, 2021 | [Essays](https://github.com/harrychangjr/geh1049/blob/main/GEH1049%20Final%20Assignment.pdf)")
        st.markdown("""
        An obstacle that may undermine national efforts aimed at reducing childhood obesity in high-income countries would be the lack of support by parents to cultivate healthy eating habits amongst children. As children are deemed rationally unprepared to make their own decisions at a young age, the actions of their parents are imperative in influencing their children’s behaviours. This is especially the case when children view their parents as their role models who they would like to develop similar traits with when they grow up in the future. In a 2019 Singaporean study, parents conveyed various difficulties in trying to promote healthy eating habits to their children. Parents preoccupied with work and other commitments do not have adequate time to prepare healthy food for their children. They would often opt to eat outside or order takeaways instead of consuming home-cooked meals, which increases the likelihood of fast food consumption instead. Furthermore, they cited the dietary preferences for less healthy food by either their spouse or their own parents that would compromise their own efforts in promoting healthy eating to their children (Chong, 2021). These observations are also similar in other high-income countries in the European Union (EU), including Germany and Italy. In a 2018 online survey targeted at 187 policy-makers and stakeholders from 12 EU member states, 67.6% of the respondents agreed that the lack of parental support contributed to the prevention of childhood obesity, ranking it amongst the top three reasons from a possible nine listed in the survey (Abu-Omar et al., 2018).
    
        Another obstacle that may hinder national efforts to reduce childhood obesity in high-income countries would be the difficulty in enforcing regulations against unhealthy food marketing. As most food companies aim to generate profits by maximising revenue and minimising costs, they may not necessarily be obliged to promote healthier foods, especially when the latter may not be as popular amongst citizens compared to fast foods and sugary beverages. In fact, eating healthily is considered a more costly option due to the higher cost required to farm fresh fruits and vegetables, even in high-income countries such as the USA (Sotirovska & Philip, 2018). Moreover, promoting healthier foods is considered high-risk, especially when competing firms choose to continue marketing their less healthy yet popular products instead. To illustrate, PepsiGo had unsuccessfully attempted to market healthier products in the past, resulting in a fall in revenue and market share. It had to recenter its focus to its main products (e.g Cheetos, Doritos and Pepsi) to gradually regain its position in the food industry (Fleming-Milici & Harris, 2020). Even with increasing regulations against unhealthy food marketing in different countries, the wide usage of social media platforms especially amongst today’s children is a loophole constantly exploited by food companies to maximise their outreach and promote the sale of their products. As such, the difficulty in regulating unhealthy food marketing deters national efforts to reduce childhood obesity, particularly due to firms’ common aim to maximise profits by any means necessary, even at the possible expense of their consumers’ long-term health.
    
        In my personal opinion, the lack of parental support to promote healthy eating habits is a more difficult obstacle to overcome compared to the difficulty in regulating unhealthy food marketing when it comes to reducing childhood obesity in high-income countries. Given the fast pace of living in metropolitan areas, it is understandable that citizens living in such conditions may not necessarily afford the luxury of time to prepare healthy meals diligently for their children, especially when they are working. In addition, parents would struggle to constantly find the motivation to impose a healthy diet on their children or themselves all the time. A sudden slip-up in maintaining such efforts may lead to a rebound towards unhealthy food consumption once again, which is especially detrimental for parents as their children would likely be influenced to follow suit. On the other hand, tackling unhealthy food marketing may be an easier problem to overcome. As online media is often referred to as a double-edged sword, it can either be used by firms to positively promote healthy eating habits or encourage unhealthy food consumption instead. Therefore, it would ultimately be up to the individual’s self-control to decide which form of influence to follow when it comes to making eating decisions.

        References:

        1. Abu-Omar, K., Messing, S., Sarkadi-Nagy, E., Kovács, V. A., Kaposvari, C., Brukało, K., ... & World Health Organization. (2018). Barriers, facilitators and capacities for childhood obesity prevention in 12 European Union member states: results of a policy-maker survey. Public health panorama, 4(03), 360-367. https://apps.who.int/iris/bitstream/handle/10665/324940/php-4-3-360-367-eng.pdf 
        2. Chong, M. (2021). Commentary: Why do some children choose unhealthy food when they get older? CNA. https://www.channelnewsasia.com/commentary/children-fast-food-healthy-eating-parents-research-1883946 
        3. Sotirovska, D., & Philip, E. (2018). Why eating healthy is so expensive in America. Vox. https://www.vox.com/videos/2018/3/22/17152460/healthy-eating-expensive 
        4. Fleming-Milici, F. & Harris, J. (2020). Food marketing to children in the United States: Can industry voluntarily do the right thing for children's health?. Physiology & Behavior. 227. 113139. https://doi.org/10.1016/j.physbeh.2020.113139   
        """)

    elif selected == "Role of healthcare data analytics in managing COVID-19":
        st.subheader("Role of healthcare data analytics in managing COVID-19")
        st.write("November 12, 2021 | [Essays](https://github.com/harrychangjr/geh1049/blob/main/GEH1049%20Final%20Assignment.pdf)")   
        st.markdown("""
        Contact tracing was one method which demonstrated the usage of healthcare data analytics to help tackle the pandemic. The idea behind contact tracing revolves around the usage of mobile applications for users to transmit their localisation data as unchangeable time-stamped records into a common database. This database will then be used as an investigation system by governments to trace persons who either had contact with newly infected patients or had frequented high-risk areas. Collecting such data also ensures that users suspected of contracting COVID-19 are not contravening self-isolation protocols, as their locations are constantly monitored to deter them from doing so (Benreguia et al., 2020). Moreover, Asian countries such as Taiwan and South Korea have resorted to tracking their citizens’ movements without the latter’s consent to maximise the effectiveness of contact tracing efforts (Nageshwaran et al., 2021). In particular, the TraceTogether mobile application, developed in Singapore, has greatly assisted the country in identifying suspected and confirmed COVID-19 cases. Using this application involves the exchange of Bluetooth signals between phones within range of each other to discover nearby users. With the increasing number of confirmed cases in Singapore, the usage of TraceTogether application was eventually made compulsory for users to check-in when visiting high traffic areas such as shopping centres and workplaces using the in-built SafeEntry system within the application for them to monitor their whereabouts. The local authorities commended TraceTogether for helping to “reduce the average time taken to contact trace from four days to less than 1.5 days” (Low, 2021), indicating its usefulness in Singapore’s battle against COVID-19.
        
        Data analytics also contributed to healthcare decision-making by helping countries to “evaluate the effectiveness of COVID-19 control measures'' (Alsunaidi et al., 2021). To illustrate, a study on China published in March 2020 concluded that restricting and relaxing quarantine measures at different timings greatly impacts the trend in the number of daily cases in the subsequent stages of the outbreak (Chen et al., 2020). Using the data of daily confirmed cases reported in Hubei, the researchers ran a simulation using the C-SEIR mathematical model (Zhang et al., 2005) to predict different peak periods of the pandemic in the region. The simulation revealed that adjusting the lockdown start date earlier or later by two days could have decreased or increased the number of confirmed cases by almost twice the actual amount respectively. Furthermore, the study showed that the relaxation of such restrictive measures should occur in a more controlled manner to minimise the number of infections and avoid experiencing subsequent large waves of infections. In correspondence to the study’s results, China has adopted a “zero tolerance policy” as its main public health approach, as its main priority remains in preserving the good health of its citizens and minimising deaths (Ning et al., 2020). Strict lockdowns are enforced whenever clusters occur in certain regions, which includes the restriction of inter-city movements such as workplace closures and transport bans. The daily cases in China remain negligible compared to other countries such as Britain and USA, both which have adopted the endemic approach of living with the virus instead (Feng, 2021). While China’s approach is effective in minimising daily infections, this may come at a high economic cost, especially when the country relies on the international market to boost its economy, which is hindered by travel restrictions. 
        
        While both above-mentioned applications of healthcare data analytics have their respective merits, contact tracing is a more successful contribution in comparison to the control of the COVID-19 restrictive measures. With reference to the Socio-Ecological Model, the main focus of contract tracing is at the individual level. Individuals would be more conscious to only leave their houses whenever necessary, or at the very least monitor their whereabouts to minimise the risk of infection during the pandemic. On the other hand, the control of restrictive measures focuses at the policy level, since the decision making by governments on such measures affects its citizens’ livelihoods, which may not be agreeable by all members of the local community especially when the country’s economy would be affected in the long run. As such, contact tracing would be deemed more successful in its contribution against COVID-19, especially when the individual belief of exercising social responsibility has the potential to relieve the burden borne by governments to tackle the virus. After all, the prevention of more cases is indeed better than cure.

        References:
        1. Alsunaidi, S. J., Almuhaideb, A. M., Ibrahim, N. M., Shaikh, F. S., Alqudaihi, K. S., Alhaidari, F. A., Khan, I. U., Aslam, N., & Alshahrani, M. S. (2021). Applications of Big Data Analytics to Control COVID-19 Pandemic. Sensors (Basel, Switzerland), 21(7), 2282. https://doi.org/10.3390/s21072282 
        2. Nageshwaran, G., Harris, R. C., & Guerche-Seblain, C. E. (2021). Review of the role of big data and digital technologies in controlling COVID-19 in Asia: Public health interest vs. privacy. DIGITAL HEALTH. https://doi.org/10.1177/20552076211002953 
        3. Benreguia, B., Moumen, H., & Merzoug, M.A. (2020). Tracking COVID-19 by Tracking Infectious Trajectories. IEEE Access, 8, 145242-145255. https://doi.org/10.1109/ACCESS.2020.3015002 
        4. Low, Z. (2021). Mandatory TraceTogether-only SafeEntry brought forward to May 17. CNA. https://www.channelnewsasia.com/singapore/covid19-tracetogether-safeentry-may-17-brought-forward-token-app-1358126 
        5. Chen, B., Shi, M., Ni, X., Ruan, L., Jiang, H., Yao, H., ... & Ge, T. (2020). Visual data analysis and simulation prediction for COVID-19. https://doi.org/10.18562/IJEE.055
        6. Zhang. J., Lou, J., Ma. Z., et al. (2005). A compartmental model for the analysis of SARS transmission patterns and outbreak control measures in China. Applied Mathematics and Computation, 162(2), 909-924.
        7. Feng, E. (2021). China Is Imposing Strict Lockdowns To Contain New COVID Outbreaks. But There’s A Cost. NPR. https://choice.npr.org/index.html?origin=https://www.npr.org/sections/goatsandsoda/2021/09/02/1033396323/china-is-imposing-strict-lockdowns-to-contain-new-covid-outbreaks-but-theres-a-c 
        8. Ning, Y., Ren, R., & Nkengurutse, G. (2020). China's model to combat the COVID-19 epidemic: a public health emergency governance approach. Global health research and policy, 5, 34. https://doi.org/10.1186/s41256-020-00161-4 
        """)
    elif selected == "Evaluating 'Chinese Privilege' in Singapore: Special Assisted Plan Schools":
        st.subheader("Evaluating 'Chinese Privilege' in Singapore - Special Assisted Plan Schools")
        st.write("April 29, 2021 | [Final Essay](https://github.com/harrychangjr/ges1010/blob/main/GES1010%20Final%20Essay%20A0201825N.pdf)")
        st.markdown("""
        In 1979, the Special Assistance Plan (SAP) was established in order to preserve the heritage of top Chinese schools, nurture traditional Chinese values in students and promote bilingualism. Today, critics question the relevance of SAP schools, as they claim that these schools no longer fulfil their original goals. Instead, they cite these schools as an example of “Chinese privilege” in Singapore, which is defined as a scenario where “Chinese-Singaporeans, unlike minority Malays, Indians, or Eurasians, enjoy exclusive racial advantages that position them as Singapore’s cultural, economic, political, and social core”. In my opinion, SAP has reinforced “Chinese privilege” in Singapore as it has been perceived by Singaporeans to promote racial segregation and social inequality instead.

        For starters, the admission criteria required to enrol in these schools heavily favour the top Chinese students, which may encourage “Chinese elitism”, where they deem themselves to be superior compared to their non-Chinese peers due to their enrolment in SAP schools. SAP students are not only required to take Chinese as a subject in the Primary School Leaving Examinations (PSLE), but also at the secondary level. Furthermore, SAP schools are only open to the top 30% of students in each PSLE cohort. In fact, some SAP schools are more stringent with their admission requirements, including Hwa Chong Institution, which admits only the top 3% of PSLE graduates annually. While this is partly due to historical prestige, government policies were also introduced to boost the elite status of the SAP schools. When educational streaming was first introduced in Singapore, only the nine SAP schools at the time were banded as “Special”, which formally branded them as the cream of the crop amongst all Singapore schools. Subsequently, the Integrated Programme (IP) was later introduced, allowing top secondary school students to skip the GCE ‘O’ Level examination and proceed to take a national pre-university examination after six years of secondary education. As SAP schools were among the first to pilot the programme, about 35% of the IP schools also benefit from SAP today. Enrolling in such prestigious institutions would indeed be a “Chinese privilege”, particularly due to the compulsory prerequisite of studying Mandarin, which would disadvantage the students from minority races who are mostly unable to do so. 

        In addition, the lack of daily interaction with people of other races may discourage multiracialism amongst SAP students, which arises from the inadequate ethnic sensitivities of other racial groups. While SAP schools are open to all eligible students regardless of race, they are required to be highly proficient in Mandarin as it is the only mother tongue offered. This, along with the strong Chinese tradition of SAP schools, have greatly discouraged students of minority races from enrolling. As such, the minimal inter-ethnic interaction experienced by SAP students results in them having “less ethnically diverse social networks than their non-SAP peers.” To support this, a 2012 Straits Times survey conducted amongst the top 5 schools (of which 2 are in SAP) revealed that 82% of SAP students reported a lack of close friends from other races, compared to 12% for the non-SAP schools. In a RICE Media interview, a Malay SAP alumnus elaborated that certain SAP students lack cultural knowledge of other races, citing quotes such as “I can’t differentiate between Malay and Indian” and being asked “if water was halal”. This shows that minorities who enrol in SAP schools would find it nearly impossible to avoid racist jokes and insensitive comments from their Chinese peers in SAP schools, suggesting the latter’s inability to interact meaningfully with other races. In fact, students from minority races would find it challenging to represent their own races and cultures to face the predominantly Chinese cohort of SAP students. This would ultimately lead to an increased racial segregation between the Chinese and the minority races, as xenophobic sentiments may arise especially from the former, believing that their status as the majority race is indeed a social privilege in Singapore. Despite the government’s attempts to alleviate this through Racial Harmony Day celebrations and weekly conversational Malay lessons, this may be insufficient to encourage inter-racial understanding between students of different races. A possible suggestion to rectify this would be to abolish the SAP system. By eliminating the prerequisite of studying Mandarin in these Chinese schools, this would allow the minority races to be better represented in each school. Also, this provides more opportunities for daily interactions between the different races to better promote multiracialism in all schools.

        Furthermore, students in SAP schools are provided an “unequal access to educational resources” compared to their peers in other public schools, which reinforces the idea of “Chinese privilege” in Singapore. As a reward for performing well under Singapore’s meritocratic system, students in SAP schools experience multiple advantages over their counterparts in other schools. For instance, SAP schools enjoyed additional funding in the form of annual grants and interest-free loans, including a per capita government funding for SAP school students that was up to over 50% higher than other secondary school students during the programme’s initial years. In 2019, then Education Minister Ong Ye Kung updated that each SAP student receives an additional S\$300 “to develop their proficiency and interest in Chinese language-related studies.” SAP schools often receive donations from alumni working in top organisations and firms to repay their alma mater for contributing to their educational success. These schools also have a lower student-teacher ratio, as attributed in their additional funding used to improve both the quality and quantity of their teaching staff. In particular, selected SAP schools offer the Bicultural Studies Programme (BSP), which provides its top students with unrivalled opportunities to visit China and learn more about Chinese culture and values through daily interactions with the mainland Chinese. As BSP is not offered to non-SAP schools, this signifies the increased government funding that is invested in nurturing the SAP elites. Again, these privileges are only offered to students that take Chinese as an examinable subject, which mostly excludes the minority races. As such, the advantages that are offered to SAP schools reinforces the idea that “Chinese privilege” exists, given that the SAP students are mostly Chinese. To alleviate this, a “donation cap” can be imposed by the government on SAP schools to prevent them from receiving excessive financial support for additional facilities and exclusive programmes. Under this framework, donations should be declared and checked annually by the government. SAP schools which exceed this “donation cap” would then incur a decrease in additional funding per student, down from S\$300 to S\$150 for example.

        Moreover, SAP “perpetuates social inequality by instilling cultural capital in its students that enables them to thrive in a world where China is an emerging economy of opportunities”. To justify the relevance of SAP, Ong Ye Kung explained in 2019 that the rapid development of China, as Singapore’s largest trading partner, raises the importance of helping students to amass Chinese cultural capital. Doing so could reap economic benefits when doing business with China, especially when one possesses Chinese cultural knowledge that is essential in facilitating access and building strong professional ties with China’s market, which serves as a key motivation behind SAP. As mentioned earlier, the introduction of BSP to selected SAP schools exemplifies this belief, as top students are offered the opportunity to visit China and learn the Chinese culture, language and values directly from daily interactions with the mainland Chinese. Pierre Bourdieu’s concept of capital suggests that by having a deeper understanding of Chinese culture and values, SAP students could be well-versed with the “knowledge, skills and abilities to pursue further opportunities professionally and maintain or advance their social positions,” provided that they seize the opportunities to make these connections. These include either working or studying in China, as well as building professional ties with Chinese firms and individuals. By restricting such opportunities to a handful of students from a particular racial group, this widens the inequality gap between the SAP and non-SAP students since the latter do not have access to such overseas immersion programmes. To resolve this, the government can consider expanding BSP to Malay and Tamil-speaking students, especially in the form of overseas immersion programmes for non-SAP public schools.

        Given that Singapore boasts a population that is nearly 75% Chinese, the SAP is a prime example of how “Chinese privilege” is deemed prevalent in the country today. The government should explore solutions to minimise the unfair advantages enjoyed by the SAP schools. As previously mentioned, it can reduce the additional funding to resolve the unfair allocation of resources that favours the SAP schools. Alternatively, SAP can be expanded by creating similar programmes that cater to Malay and Tamil-speaking students and offered to all schools in Singapore to close the inequality gap between the Chinese and the minority races. Better still, SAP should be abolished to ensure a more equal representation of all races in every school and encourage multiracialism amongst students through inter-racial interactions. These suggestions would align with the Ministry of Education’s vision that “every school is a good school”.

        References:

        1.	Gien, Si Yun (2019). Time To Rethink? SAP Schools and Chineseness: The Millennial Experience. ScholarBank@NUS Repository. Retrieved from https://scholarbank.nus.edu.sg/handle/10635/157979  
        2.	Saharudin, Hydar (2016). Confronting ‘Chinese privilege’ in Singapore. New Mandala. Retrieved from https://www.newmandala.org/brief-history-chinese-privilege-singapore/  
        3.	Zhuo, Tee (2017). The Special Assistance Plan: Singapore’s own bumiputera policy. Equality & Democracy (Yale-NUS College). Retrieved from https://equalitydemocracy.commons.yale-nus.edu.sg/2017/12/07/the-special-assistance-plan-singapores-own-bumiputera-policy/  
        4.	Koh Jhai Leng, Shammah (2018). A Fruitful Graft: Examining the Localisation of 'White Privilege' as 'Chinese Privilege' in Singapore. ScholarBank@NUS Repository. Retrieved from https://scholarbank.nus.edu.sg/handle/10635/144416  
        5.	Ong, Ye Kung (2019). Funding to Special Assistance Plan Schools and non-Special Assistance Plan schools. Parliament Sitting No. 96, Volume 94. Singapore: Parliament of Singapore: No. 13. Retrieved from https://sprs.parl.gov.sg/search/sprs3topic?reportid=written-answer-4643  
        6.	Yong, Charissa., & Zaccheus, Melody (2012). Top schools’ students tend to have friends like themselves: Poll. The Straits Times, Retrieved from https://www.asiaone.com/News/Latest%2BNews/Edvantage/Story/A1Story20121117-384060.html  
        7.	Pang, Ethel (2019). As Long As SAP Schools Exist, ‘Chinese Elitism’ in Singapore Will Exist. RICE Media. Retrieved from https://www.ricemedia.co/current-affairs-opinion-sap-schools-chinese-elitism-singapore/ 
        8.	Ngu Li Xuan, Geraldine (2020). Sapping Resources? The Ineffectiveness and Inequalities of SAP School Education. ScholarBank@NUS Repository. Retrieved from https://scholarbank.nus.edu.sg/handle/10635/170314  
        9.	Bourdieu, Pierre (1986). “The Forms of Capital.” Pp. 241-258 in Handbook of Theory and Research for the Sociology of Education, edited by J. G. Richarson. New York: Greenwood Press

        """)
    elif selected == "Analysing usefulness of word clouds in mental health studies":
        st.subheader("Analysing usefulness of word clouds in mental health studies")
        st.write("March 5, 2021 | [Essay](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20GET1030%20Individual%20Assignment%20Final.pdf)")
        st.markdown("""
        For this assignment, I will be analysing word clouds from a research article published in
        2019, which aimed to understand and measure psychological stress levels based on social
        media posts.

        In today’s digital age, people are increasingly using social media platforms to inform others
        of their mental states, garner social support, as well as to record their daily activities.
        Despite previous studies which investigate the underlying factors behind stresses in our
        daily lives, many researchers believe that there is still a gap in the scientific understanding of
        how psychological stress is expressed on social media. In particular, they believe that mental
        health conditions, such as depression and anxiety, can be predicted from the social media
        language of its users.

        In 2019, a study was implemented to explore how to differentiate high-stress users from
        low-stress users by performing natural language processing methods on text in social media
        posts.

        To facilitate data collection, the study’s researchers deployed a survey on Qualtrics, which
        consisted of several demographic questions (age, gender, race, education, income) and the
        Perceived Stress Scale questionnaire. Each item in the scale is scored from 0 to 4, with an
        absolute maximum summing to 40. The stress scores for each survey participant range from
        6 to 39, with a mean value of 30.

        Interestingly, the researchers chose to obtain their data from Facebook and Twitter, as they
        are amongst the most widely used social media platforms worldwide. Survey participants
        were invited to share access to their Facebook and/or Twitter posts. Among the
        participants, 601 users completed the survey and had active accounts with more than 900
        words on Facebook and Twitter. Their social media posts were then downloaded by using
        the Facebook Graph and Twitter APIs. All participants who completed the survey were
        based in the United States.

        The posts were then processed using the HappierFunTokenizer available with the DLATK
        package in Python. The language of each user and county is then represented as a set of
        features. In the dictionary-based method, social media language is transformed into
        numerical features representing percentage proportions of lexical categories in an existing
        dictionary. In the data-driven method, the language is morphed into numerical features
        which represent the proportions of word clusters that are statistically similar according to
        their frequency distributions.

        Afterwards, 1-,2-, and 3-grams were extracted from all posts to analyse significant
        associations between words & phrases and stress. As seen above, the word clouds are
        visualizations of the Pearson correlations of words and phrases with stress scores obtained
        from the survey. The word clouds were generated by uploading the dataset containing the
        processed Facebook posts onto Wordle.net, a free online word cloud creator that no longer
        exists today. The red word cloud represents words commonly used by users with high stress
        levels while the blue word cloud represents words from Facebook posts of low-stress users.
        The size of each word indicates the correlation strength while the colour intensity indicates
        frequency (darker being more frequent).

        Based on the researchers’ analysis, the language of high stress users is made prevalent
        either by expressions of perceived lack of control, expressions of a need state or a lack of
        resources, along with a negative-angry sentiment. Also, high stress language seems to be
        comorbid with mental health conditions. Indeed, it is intriguing to see how these words
        reflect the adverse effects that stress can have on health. On the other hand, the language
        of low stress users has prominent positive affect, which include discussions of meals as well
        as feelings of social inclusion.

        Most of the time, the size of each word in a word cloud corresponds to the relative
        frequency of that particular word in a corpus. In the case of this visualization, however, the
        Pearson correlation coefficient between words & phrases and stress score is used as the
        metric that affects word size in a word cloud. On the other hand, the colour intensity of
        each word is used to measure frequency instead. In short, the researchers have attempted
        to address the common limitation of size misinterpretation by adding another metric when
        generating each word cloud.

        Although word clouds are simple to visualize and interpret, there are certain limitations that
        come with them. For instance, word clouds do not categorise words that have similar or the
        exact same meaning. In the context of my chosen visualisation, pairs of words such as
        “depressed” and “depression”, as well as “I” and “me”, are almost equal in size when
        compared in their own pairs. Having such synonyms as duplicated could omit out other
        unique words from appearing in the word cloud, which could affect the researchers’ analysis
        of identifying the words with the highest Pearson correlation values within the processed
        dataset.

        Another limitation of the visualisations discussed is that only Facebook data was used,
        despite also gaining access to the users’ Twitter updates during the data collection phase.
        To improve the results of the analysis, separate sets of word clouds can be generated using
        posts from other popular social media platforms, such as Twitter, Instagram, LinkedIn and
        Reddit. These different sets of word clouds, representing each social media platform, can
        then be compared against each other for further analysis to evaluate if the words with the
        highest Pearson correlation values are consistent across all sets. This is especially important
        since the social media language used in each platform may vary.

        To reiterate, word clouds are simple to use and were popularized in the early 2000s, when
        the photo sharing site Flickr first introduced their usage to display commonly used tags on
        its website. Being one of the most widely used forms of information visualization today,
        critics believe that word clouds can often be misinterpreted by the general public, primarily
        due to the issue of word size and the lack of context. However, the word clouds discussed
        above are generally appropriate in my opinion, as it has been made clear that the clouds
        were generated for academic research purposes to supplement the findings of a mental
        health study.

        References:

        1. Guntuku, Sharath Chandra, Anneke Buffone, Kokil Jaidka, Johannes C. Eichstaedt,
        and Lyle H. Ungar. "Understanding and measuring psychological stress using social
        media." In Proceedings of the International AAAI Conference on Web and Social
        Media, vol. 13, pp. 214-225. 2019.
        2. Viégas, F. B., & Wattenberg, M. “Timelines tag clouds and the case for vernacular
        visualization.” Interactions, 15(4), 49-52. 2008.
        """)
    elif selected == "Investigating the relationship between culture and sweet-sour taste interactions":
        st.subheader("Investigating the relationship between culture and sweet-sour taste interactions")
        st.write("October 31, 2020 | [Article](https://github.com/harrychangjr/sp1541-nlp/blob/main/Originals/SP1541%20NA2.pdf)")
        st.write("*Are we correct to stereotype taste perceptions and preferences based on different cultures?*")
        st.markdown("""
        Imagine that you are drinking a glass of margarita. After that first sip, you find that your drink is too sour. You then lick some of the salt from the rim of the glass before taking a second sip. You find that now, the margarita tastes less sour! This is a perfect example of a taste interaction between different taste qualities. 
        
        When two or more taste qualities interact, they affect the perception of one another. The taste qualities involved can either enhance or suppress one another, which is dependent on their concentrations.
        
        Previous studies have shown that cultural differences do affect taste sensitivities and taste interactions amongst different individuals. For instance, a US study discovered that taste sensitivities across all five taste qualities are lower amongst individuals of African-American and Hispanic origin compared to Caucasians. Another study also revealed that Taiwanese students tend to have higher sweetness sensitivity compared to their American counterparts.
        
        Thus, a new study has sought to validate the above-mentioned findings. Conducted by a group of Danish and Chinese researchers earlier this year, this cross-cultural study suggested that culture does affect taste interactions to a certain degree. In particular, Danish consumers experienced a smaller extent of sourness suppression by the sweetness of sucrose as compared to their Chinese counterparts.
        
        To the researchers’ surprise, they discovered that the vice versa does not prove to be true. As they could not establish a relationship between culture and the extent of sourness suppressing sweetness, this suggests that the differences in taste perception may need to be further classified at the individual level. 
        
        So, in the first place, how does the suppression between sweetness and sourness occur?
        
        Sucrose, widely known as table sugar, undergoes hydrolysis to be further decomposed to glucose and fructose. This process can be quickened by introducing acids such as citric acid, commonly present in fruit juices. As such, hydrolysis reduces the formation of sugar crystals, explaining how sourness can suppress sweetness.
        
        Let us now try to break down this process from another perspective. Citric acid, for instance, has an estimated pH of 2.2, which exemplifies its relatively high acidity to its sourness. On the other hand, sucrose is known to be slightly alkaline – and a bit bitter, given its higher pH value of 8. However, when citric acid is introduced to sucrose, the resultant solution will have a pH range between 4 to 7. Simply put, we can also make use of the same reaction to explain how sweetness suppresses sourness.
        
        To further appreciate the findings of the study, we should also understand how taste sensitivities relate to taste preferences. 
        
        In a separate study conducted by Canadian researchers in 2019, there is evidence of a relationship between certain taste sensitivities of consumers and their taste preferences. In particular, sweetness and saltiness were revealed to be less preferred by consumers who recorded higher sensitivities in these two taste qualities.
        
        As such, the study sought to investigate how these taste interactions vary between both cultures. The Danish and Chinese test subjects evaluated six liquid mixtures: namely water, sucrose, tartaric acid, citric acid, a mixture of sucrose with tartaric acid and sucrose mixed with citric acid. Both citric and tartaric acids were used as samples to exhibit the taste of sourness, while sucrose was used to exhibit sweetness.
        
        Participants were tasked to taste one sample at a time, with a 30 second break in between after rinsing their mouth with water. For each sample, the taste sensitivity was evaluated on a 9-point scale, with 1 being ‘not at all’ and 9 rated as ‘extremely’ sweet or sour, depending on the sample.
        
        For samples containing a mixture of sweetness and sourness, they were evaluated with an additional ‘Just About Right’ (JAR) scale to measure the appropriate concentrations of sucrose and acids based on each individual. Together with the taste sensitivities, the JAR ratings for each sample were recorded using a questionnaire. Data collected from this questionnaire was later used for further analysis.
        
        On average, the Danish consumers consistently recorded higher sweetness sensitivities than their Chinese counterparts. This further explains how the researchers concluded that sucrose had managed to suppress tartaric acid to a greater extent in Chinese consumers compared to the Danish consumers.
        
        The researchers added that based on their research on similar studies, a Caucasian population generally tends to have a lower taste sensitivity for sweetness, sourness, saltiness and bitterness than an Asian population. Since an inverse relationship between taste sensitivity and taste preference has been established from the Canadian study, comparing the taste sensitivities of these Chinese and Danish consumers may therefore not be entirely representative of the ‘East vs. West’ comparison.
        
        In addition, the researchers could not conclude if culture had a role in sweetness suppression by sourness. This is because the results had varied between each individual, regardless of whether they were Chinese or Danish.
        
        Upon obtaining the necessary readings, the test subjects were later divided into three different clusters based on their relative sensitivities to sourness. For instance, consumers with similarly low sourness sensitivity were grouped together under the same category. This may be due to the high suppression of sourness by sweetness.
        
        This same method of classification based on sweetness was also performed on these customers. Likewise, each cluster comprised of both Chinese and Danish consumers. While there were certain trends that may imply a relationship between culture and taste interactions, the researchers could not affirm this conclusion upon further analysis.
        
        Overall, beverage manufacturers stand to benefit most from the results of the study. In order to boost their sales revenue, they would need to re-evaluate their product segmentation strategies to diversify their target consumer range. Instead of focusing on culture, these companies may wish to explore other variables such as age and gender instead.
        
        With this stereotype debunked, do we now expect people of different cultures to appreciate unique drinks such as sugarcane juice with lemon the same way? Only time and experience will tell. 
        
        References:
        1. Bertino, M., Beauchamp, G. K., & Jen, K. L. C. (1983). Rated taste perception in two cultural groups. Chemical senses, 8(1), 3-15. Also available from https://academic.oup.com/chemse/article-abstract/8/1/3/271785 
        2. Chamoun, E., Liu, A. A., Duizer, L. M., Darlington, G., Duncan, A. M., Haines, J., & Ma, D. W. (2019). Taste sensitivity and taste preference measures are correlated in healthy young adults. Chemical senses, 44(2), 129-134. Also available from https://pubmed.ncbi.nlm.nih.gov/30590512/ 
        3. Hydrolysis. (n.d). In Wikipedia. Retrieved from https://en.wikipedia.org/wiki/Hydrolysis 
        4. Junge, J.Y.; Bertelsen, A.S.; Mielby, L.A.; Zeng, Y.; Sun, Y.-X.; Byrne, D.V.; Kidmose, U. Taste Interactions between Sweetness of Sucrose and Sourness of Citric and Tartaric Acid among Chinese and Danish Consumers. Foods 2020, 9, 1425. Also available from https://www.mdpi.com/2304-8158/9/10/1425 
        5. Williams, J. A., Bartoshuk, L. M., Fillingim, R. B., & Dotson, C. D. (2016). Exploring ethnic differences in taste perception. Chemical senses, 41(5), 449-456. Also available from https://academic.oup.com/chemse/article/41/5/449/2366044 
        """)
    elif selected == "Timing vaccination campaign to reduce measles infections":
        st.subheader("Timing vaccination campaign to reduce measles infections")
        st.write("September 30, 2020 | [Article](https://github.com/harrychangjr/sp1541-nlp/blob/main/Originals/SP1541%20NA1.pdf)")
        st.write("*Despite having a vaccine that is readily accessible, measles cases and deaths are still surging worldwide, especially in recent years. Why is this so and are there any long-term solutions to resolve this?*")
        st.markdown("""
        According to an update from the World Health Organisation (WHO), nearly 10 million cases of measles were reported in the year 2018. During that year, more than 140,000 people worldwide have died from the disease. In addition, reported measles cases have surged internationally in devastating outbreaks across different regions.

        Besides the mild symptoms of fever, runny nose and body rashes, this highly contagious disease may also lead to long term effects on the immune systems of those affected. For instance, as many as 1 in 20 children with measles will contract pneumonia, which is the leading cause of death amongst young children. In addition, about 1 in every 1000 who contract measles will develop encephalitis - or brain infection - which can result in the child being deaf or developing intellectual disability. This raises the importance of vaccinating children so that they will not have to live with such complications in the long run.

        Despite the long existence of an effective and cost-efficient vaccine, the outbreak of measles remains a pressing global health issue particularly for developing countries. These nations have often been identified to lack access to vaccinations and high-quality health infrastructure.
        
        As such, a study on the measles outbreak in Pakistan has predicted that optimising the timing of a vaccination campaign plays an important role in reducing the total infections of measles.

        The study, led by senior researcher Niket Thakkar from the Institute for Disease Modelling (based in the USA), was conducted in response to the sudden increase in measles cases within the span of a year. From 2016 to 2017, the number of cases in Pakistan have more than doubled, as confirmed by local laboratories.

        Prior to the study, measles vaccination coverage in toddlers aged under 2 was estimated to be 61% nationwide, as cited from Pakistan’s Demographic and Health Survey (DHS) in 2012 – 2013. With Pakistan being identified as one of the top countries with the most unvaccinated infants, the need to improve this rate was therefore essential, as suggested by Thakkar and his team of researchers.

        The researchers came up with a mathematical model which uses linear regression to predict the severity of future outbreaks. Using case data from Pakistan that contains the number of new measles cases per month, they predicted the number of cases of subsequent months within the next three years. This data was also categorised by province level to compare the severity of the measles outbreak between different regions in Pakistan. 

        To understand how linear regression works, let us think of this example. If you spent \$10 on a Monday, \$20 on a Tuesday, \$30 on a Wednesday, how much would you win on Thursday? If your answer is $40, you’ve just performed linear regression - this method thus makes use of available information to constantly make predictions.

        This model assisted researchers in understanding when and where the vaccine should be distributed within the country. Their results show that holding a vaccination campaign in November has the greatest impact, with an estimated 440,000 more infections that could be prevented in comparison to a January campaign. These results were later used by the Pakistani government in vaccination planning, which led to the implementation of the campaign in November 2018.

        According to the study, less cases were confirmed from May to October as compared to the rest of the year. This suggests a low transmission season during this period, reiterating why the campaign is best implemented in November, when cases start to surge again. As a result of this implementation, the estimated measles vaccination coverage in infants aged under 2 had improved to 73% nationwide. This statistic was reported in 2017 – 2018’s iteration of Pakistan’s DHS, which was published in January 2019.

        On the other hand, if the campaign was delayed from November 2018 to May 2019, can you guess the number of additional infections that would have occurred? There would have been more than 600,000 additional infections from 2018 to 2021 - this significant number is sandwiched between the population sizes of Sialkot and Sukkur, the 13th and 14th most densely populated cities in Pakistan respectively (out of 99 cities in total). As such, this further justifies the researchers’ preference for the campaign to be conducted in November.

        Beyond immediate outbreak response, countries should continue investing in high quality immunisation programmes, as well as disease surveillance. This would help to ensure that these outbreaks are detected quickly and stopped as soon as possible.

        It is indeed a tragedy to witness a sudden increase in cases and deaths from a disease that is easily preventable, especially in recent times. Therefore, it is crucial to ensure that even the poorest countries have access to these high-quality vaccination programmes. This would help prevent the unnecessary loss of lives to easily treatable diseases, including measles.
        
        References:

        1. Thakkar, N., Gilani, S. S. A., Hasan, Q., & McCarthy, K. A. (2019). Decreasing measles burden by optimizing campaign timing. Proceedings of the National Academy of Sciences, 201818433. Also available from https://www.pnas.org/content/pnas/116/22/11069.full.pdf 
        2. Patel, M. K., Dumolard, L., Nedelec, Y., Sodha, S. V., Steulet, C., Gacic-Dobo, M., ... & Goodson, J. L. (2019). Progress toward regional measles elimination—worldwide, 2000–2018. Morbidity and Mortality Weekly Report, 68(48), 1105. Also available from https://www.cdc.gov/mmwr/volumes/68/wr/pdfs/mm6848a1-H.pdf 
        3. National Institute of Population Studies (NIPS) [Pakistan] and ICF. 2019. Pakistan Demographic and Health Survey 2017-18. Islamabad, Pakistan, and Rockville, Maryland, USA: NIPS and ICF. Also available from https://dhsprogram.com/pubs/pdf/FR354/FR354.pdf 
        4. Pakistan Bureau of Statistics. Block Wise Provisional Summary Results of 6th Population & Housing Census-2017 [As on January 03, 2018]. Also available from http://www.pbs.gov.pk/content/block-wise-provisional-summary-results-6th-population-housing-census-2017-january-03-2018 
        5. Centers for Disease Control and Prevention. Epidemiology and Prevention of Vaccine-Preventable Diseases. Chapter 10, Measles. 8th Edition, 2004. https://www.cdc.gov/vaccines/pubs/pinkbook/meas.html 
        """)


#elif choose == "Site Analytics":
    #st.header("Site Analytics")
    #with st.container():
      #with streamlit_analytics.track():
            #st.text_input("Enter something below if you'd like!", key="name_input", 
                      #help="Just type something!", 
                      #value="Type something here!", 
                      #max_chars=100, 
                      #type="default",
                      #)
            #st.markdown("""
            #<style>
                #/* Add custom CSS styles for the text input */
                ##name_input input[type=text] {
                    #background-color: #f2f2f2;
                    #border: none;
                    #padding: 8px;
                    #font-size: 16px;
                    #width: 100%;
                #}
            #</style>
            #""", unsafe_allow_html=True)
            #st.button("Click me!")
            #st.write("...and now add `?analytics=on` to the URL to see the analytics dashboard 👀")

elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1CPW5glbrIDu7CwS1kx-CH7EmBzy7vqE8/view"
    st.subheader(f"[Resume]({resume_url})")


elif choose == "Talks": 
      
    st.header("Conferences where I have been a Speaker and an Attendee") 
    with st.container():  
            st.subheader("Airflow Global Summit")
            "Presented at the Airflow 2022 Global Summit, engaging 500+ professionals with a tech talk on efficient workflow orchestration"
            st.markdown("[WATCH HERE !](https://www.youtube.com/watch?v=sPOLGMlL6mo)")
            st.image(img_techtalk)
            
    with st.container():  
            st.subheader("Grace Hopper Conference 2024")
            st.text("Coming Soon!")
# elif choose == "Contact":
# # Create section for Contact
#     #st.write("---")
#     st.header("Contact")
#     def social_icons(width=24, height=24, **kwargs):
#         icon_template = '''
#         <a href="{url}" target="_blank" style="margin-right: 10px;">
#             <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
#         </a>
#         '''

#         icons_html = ""
#         for name, url in kwargs.items():
#             icon_src = {
#                 "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
#                 "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
#                 "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
#             }.get(name.lower())

#             if icon_src:
#                 icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

#         return icons_html
#     with st.container():
#         text_column, mid, image_column = st.columns((1,0.2,0.5))
#         with text_column:
#             st.write("Let's connect! You may either reach out to me at prvyas@seas.upenn.edu or use the form below!")
#             #with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
#                 #st.write('Please help us improve!')
#                 #Name=st.text_input(label='Your Name',
#                                     #max_chars=100, type="default") #Collect user feedback
#                 #Email=st.text_input(label='Your Email', 
#                                     #max_chars=100,type="default") #Collect user feedback
#                 #Message=st.text_input(label='Your Message',
#                                         #max_chars=500, type="default") #Collect user feedback
#                 #submitted = st.form_submit_button('Submit')
#                 #if submitted:
#                     #st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
#             def create_database_and_table():
#                 conn = sqlite3.connect('contact_form.db')
#                 c = conn.cursor()
#                 c.execute('''CREATE TABLE IF NOT EXISTS contacts
#                             (name TEXT, email TEXT, message TEXT)''')
#                 conn.commit()
#                 conn.close()
#             create_database_and_table()

#             st.subheader("Contact Form")
#             if "name" not in st.session_state:
#                 st.session_state["name"] = ""
#             if "email" not in st.session_state:
#                 st.session_state["email"] = ""
#             if "message" not in st.session_state:
#                 st.session_state["message"] = ""
#             st.session_state["name"] = st.text_input("Name", st.session_state["name"])
#             st.session_state["email"] = st.text_input("Email", st.session_state["email"])
#             st.session_state["message"] = st.text_area("Message", st.session_state["message"])


#             column1, column2= st.columns([1,5])
#             if column1.button("Submit"):
#                 conn = sqlite3.connect('contact_form.db')
#                 c = conn.cursor()
#                 c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
#                         (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
#                 conn.commit()
#                 conn.close()
#                 st.success("Your message has been sent!")
#                 # Clear the input fields
#                 st.session_state["name"] = ""
#                 st.session_state["email"] = ""
#                 st.session_state["message"] = ""
#             def fetch_all_contacts():
#                 conn = sqlite3.connect('contact_form.db')
#                 c = conn.cursor()
#                 c.execute("SELECT * FROM contacts")
#                 rows = c.fetchall()
#                 conn.close()
#                 return rows
            
#             if "show_contacts" not in st.session_state:
#                 st.session_state["show_contacts"] = False
#             if column2.button("View Submitted Forms"):
#                 st.session_state["show_contacts"] = not st.session_state["show_contacts"]
            
#             if st.session_state["show_contacts"]:
#                 all_contacts = fetch_all_contacts()
#                 if len(all_contacts) > 0:
#                     table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
#                     table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
#                     markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
#                     st.markdown(markdown_table)
#                 else:
#                     st.write("No contacts found.")


#             st.write("Alternatively, feel free to check out my social accounts below!")

#             linkedin_url = "https://www.linkedin.com/in/prekshi-vyas/"
#             github_url = "https://github.com/prekshivyas"
#             email_url = "mailto:prvyas@seas.upenn.edu"
#             st.markdown(
#                 social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
#                 unsafe_allow_html=True)
#             st.markdown("")
#             st.empty()
        # with image_column:
        #     st.image(img_ifg)
# st.markdown("*Copyright © 2023 Harry Chang*")

