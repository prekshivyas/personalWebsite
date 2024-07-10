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
                "youtube": "https://img.icons8.com/ios-filled/100/000000/youtube-play.png",
                "linkedin": "https://img.icons8.com/ios-filled/100/000000/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/000000/github--v2.png",
                "wordpress": "https://img.icons8.com/ios-filled/100/000000/wordpress--v1.png",
                "email": "https://img.icons8.com/ios-filled/100/000000/filled-message.png"
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
    st.markdown(f'<p style="font-size: 25px; color: black;">{a}</p>', unsafe_allow_html=True)
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
        "container": {"padding": "0!important", "background-color": "#ece2d1"},
        "icon": {"color": "black", "font-size": "20px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#eee", "color": "black"},
    }
    )
    youtube_url = "https://www.youtube.com/@prekshivyas"
    linkedin_url = "https://www.linkedin.com/in/prekshi-vyas/"
    github_url = "https://github.com/prekshivyas"
    email_url = "mailto:prvyas@seas.upenn.edu"
    resume = "https://drive.google.com/file/d/1CPW5glbrIDu7CwS1kx-CH7EmBzy7vqE8/view"
    
    def get_icons(url):
        icons = ""
        icons += social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url)
        icons += f'<a href="{url}" target="_blank" style="text-decoration: none;"><img src="https://img.icons8.com/ios-filled/30/000000/resume.png" alt="CV" title="CV" width="30" height="30"/></a>'
        icons += social_icons(30, 30, Youtube=youtube_url)
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
                     
            st.write("My journey so far also includes delivering talks at global summits and conducting research in Natural Language Processing. I specialize in automating and optimizing processes for enhanced reliability and scalability. I am actively seeking opportunities for Summer 2025 internships.")

            st.write("💃 Beyond tech, I am a competitive street style dancer, pianist and love reading non-fiction!")

            st.write("👨🏼‍💻 Interests: Microservices, Distributed Systems, Cloud, DevOps, MultiModal Large Models, Machine Learning, Natural Language Processing, Computer Vision, Data Orchestration")
            # st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/164EEVH6BmvC89q2M4WsBNF1JyddDAbNY/view?usp=sharing)")
        with middle_column:
            st.empty()

        st.markdown(
            """
            <style>
            .stButton > button {
                background-color: white;
                color: black;
            }
            .stButton > button:hover {
                background-color: white;
                color: black;
            }
            .stButton > button:active {
                background-color: white;
                color: black;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        def slideshow_swipeable(images):
            # Create a unique key for this instance of the slideshow
            key = f"slideshow_{str(images).encode().hex()}"

            # Initialize the index in session state if it doesn't exist
            if key not in st.session_state:
                st.session_state[key] = 0

            # Get the current index from session state
            index = st.session_state[key]

            # Display the current image
            with st.container(height=360):
                st.image(images[index], use_column_width=True)


            # Create two columns for previous and next buttons
            col1, col2, col3, col4 = st.columns(4)

            # Previous button
            with col1:
                if st.button(".<<.", key=f"{key}_prev"):
                    st.session_state[key] = (index - 1) % len(images)
                    st.experimental_rerun()

            # Next button
            with col4:
                if st.button(".>>.", key=f"{key}_next"):
                    st.session_state[key] = (index + 1) % len(images)
                    st.experimental_rerun()
            
        images = ["images/frenz3.jpeg", "images/intro.jpeg", "images/piano.jpeg"]
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
            'description': "- Configured alerts and metrics for storage and service availability, improving fault diagnosis and reducing resolution time by 48%.\n"
            "- Created 12 visually intuitive dashboards for real-time insights into critical metrics, enhancing service health monitoring.\n"
            "- Automated the EKS upgrade process, streamlining the configuration of add-ons and in-cluster EC2 node upgrades, reducing time and labor costs by 75%.\n"
            "- Fixed 74 security vulnerabilities across 12 different docker images in ECR production.\n",
            'skills': "`Python` `AWS` `Prometheus` `Grafana` `Terraform` `Docker` `Git` `Jira` `Confluence`"
        },
        {
            'image_url': img_sg,
            'position': "Software Engineer",
            'duration': "*June 2020 to June 2022*",
            'company_name': "Société Générale",
            'company_url': "https://www.societegenerale.com/en",
            'description': "- Led the full software development life cycle for 5 crucial features using Airflow DAGs and APIs, achieving a 63% reduction in labor costs by implementing auto-remediation, automatic resource scaling, multi AZ-switching, and pre-provisioning.\n"
            "- Built and maintained CI/CD pipelines, enhancing version control, increasing feature testing and rollout efficiency by 70%.\n"
            "- Automated and scaled instance patching process to 1500+ instances, completely eliminating manual efforts and support assistance.\n"
            "- Boosted service availability by delivering capacity planning feature and configuring rolling updates cutting down deployment time by 50%.\n"
            "- Designed and developed a micro-service based, workflow logging, and monitoring system which catalyzed 20% surge in service adoption.\n"
            "- Promoted to QA Representative for leading successful cloud service migration, achieving 99% KPI, and mentoring interns to automate Disaster Recovery in 3 months.\n"
            "- Presented at the Airflow 2022 Global Summit, engaging 500+ professionals with a tech talk on efficient workflow orchestration\n",
            'skills': "`Airflow` `API Development` `Kubernetes` `Jenkins` `Terraform` `Docker`"
        },
        {
            'image_url': img_sg,
            'position': "Software Engineer Intern",
            'duration': "*May to August 2020*",
            'company_name': "Société Générale",
            'company_url': "https://www.societegenerale.com/en",
            'description': "- Spearheaded front line tasks and production support, handling 20+ tickets weekly.\n"
            "- Researched architecture designs, dependency maps, service SLA and SLO for migrating the service to hybrid cloud.",
            'skills': "`Airflow` `API Development` `Docker` `System Architecture` `DevOps`"
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
        st.markdown('---')
        with st.container():
            cols = st.columns(2)
            for idx, col in enumerate(cols):
                if i + idx < len(experiences):
                    exp = experiences[i + idx]
                    with col:
                        st.image(exp['image_url'], width=400)
                        st.subheader(exp['position'])
                        st.write(exp['duration'])
                        st.markdown(f"**[{exp['company_name']}]({exp['company_url']})**")
                        st.markdown(f"- {exp['description']}")
                        st.markdown(f"`Skills:` {exp['skills']}")

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)

elif choose == "Technical Skills":
    # Define skills categories with images and text
    st.markdown('---')
    software_engineering_skills = [
        {"name": "Python", "image_url": "images/skills/python.svg"},
        {"name": "Java", "image_url": "images/skills/java.svg"},
        {"name": "Flask-Restful APIs", "image_url": "images/skills/Flask.svg"},
        {"name": "Firebase", "image_url": "images/skills/firebase.svg"},
        {"name": "Jenkins CI/CD", "image_url": "images/skills/Jenkins.svg"},
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
        {"name": "Microservices", "image_url": "images/skills/microservices.svg"},
         {"name": "JIRA", "image_url": "images/skills/Jira.svg"},
        {"name": "Confluence", "image_url": "images/skills/Confluence.svg"},
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
                            st.image(skills[idx]['image_url'], width=75)
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
            'skills': 'Generative AI, LangChain, LLMs, Oracle Cloud',
            'credential_url': 'https://brm-certview.oracle.com/ords/certview/ecertificate?ssn=OC5078969&trackId=OCI2024GAIOCP&key=abc99789ba478af4aff1515997c13536da339489',
            'image_url': 'images/oci.png'
        },
        {
            'name': 'AWS Certified Solutions Architect',
            'issuer': 'Udemy',
            'date_issued': 'May 2024',
            'credential_url': 'https://www.udemy.com/certificate/UC-3bdd35e3-a356-41eb-b0f4-e94e86d05bd2/',
            'image_url': 'images/aws.png',
            'skills': 'AWS Services'
        },
        {
            'name': 'Microsoft Technology Associate: Software Development Fundamentals (MTA)',
            'issuer': 'Microsoft',
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
                    st.markdown("---")
                    img = Image.open(cert['image_url'])
                    img.resize((200, 200))
                    st.image(img, width=300)
                    st.markdown(f"**[{cert['name']}]({cert['credential_url']})**")
                    st.markdown(f"Issued by {cert['issuer']} in {cert['date_issued']}")
                    if 'skills' in cert:
                        st.markdown(f"Skills: {cert['skills']}")
                    if 'credential_id' in cert:
                        st.markdown(f"Credential ID: {cert['credential_id']}")
# Create section for Education
#st.write("---")
elif choose == "Education":
    st.markdown('---')
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_frenx)
        with text_column:
            st.subheader("Master of Science and Engineering - Computer and Information Science, [University of Pennsylvania](https://www.upenn.edu/) (2023-2025)")
            st.write("GPA: 4.0/4.0")
            st.write("Coursework: Natural Lanaguage Processing, Computer Vision, Analysis of Algorithms, Big Data and Cloud, Artificial Intelligence, Applied Machine Learning")
    st.markdown('---')
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
        # with image_column:
        #     st.image(images_projects[0])
    st.markdown("---")
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
        # with image_column:
        #     st.image(images_projects[1])
    st.markdown("---")

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
        # with image_column:
        #     st.image(images_projects[2])
    

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
    for i in range(1, len(lv), 2):
        with st.container():
            cols = st.columns(2)
            st.markdown('---')
            for idx, col in enumerate(cols):
                if i + idx < len(lv):
                    exp = lv[i + idx]
                    with col:
                        with st.container(height=390):
                            st.image(exp['image_url'])
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


elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1CPW5glbrIDu7CwS1kx-CH7EmBzy7vqE8/view"
    st.subheader(f"[Resume]({resume_url})")


elif choose == "Talks": 
      
    # st.header() 
    st.markdown("---")
    with st.container():  
            st.subheader("Airflow Global Summit")
            "Presented at the Airflow 2022 Global Summit, engaging 500+ professionals with a tech talk on efficient workflow orchestration"
            st.markdown('<a href="https://www.youtube.com/watch?v=sPOLGMlL6mo" style="text-decoration: none; border: 2px solid black; border-radius: 5px; padding: 5px 10px; color: black;">Watch Here!</a>', unsafe_allow_html=True)

            st.image(img_techtalk, width=800)
    st.markdown("---")
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

