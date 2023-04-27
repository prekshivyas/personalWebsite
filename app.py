import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64

# Set page title
st.set_page_config(page_title="Harry Chang", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

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

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_utown = Image.open("images/utown.JPG")
img_quest = Image.open("images/quest.jpg") #unused
img_ifg = Image.open("images/ifg.jpg")
#Assets for competitions
img_lifehack = Image.open("images/lifehack.jpg")
img_he4d = Image.open("images/he4d.jpg")
img_shopee = Image.open("images/shopee.png")
img_sbcc = Image.open("images/sbcc.png")
img_runes = Image.open("images/runes.png")
# Assets for education
img_sji = Image.open("images/sji.jpg")
img_tpjc = Image.open("images/tpjc.jpg")
img_nus = Image.open("images/nus.jpeg")
img_poc = Image.open("images/poc.jpg")
img_gmss = Image.open("images/gmss.jpg")
img_sjij = Image.open("images/sjij.jpg")
# Assets for experiences
img_questlogo = Image.open("images/questlogo.jpg")
img_scor = Image.open("images/scor.jpg")
img_sephora = Image.open("images/sephora.jpg")
img_iasg = Image.open("images/iasg.jpg")
img_sshsph = Image.open("images/sshsph.jpg")
img_yll = Image.open("images/yll.jpg")
img_saf = Image.open("images/saf.jpg")
# Assets for projects
img_chatgpt = Image.open("images/chatgpt.jpg")
img_anime = Image.open("images/anime.jpg")
img_biopics = Image.open("images/biopics.jpg")
img_cellphone = Image.open("images/cellphone.jpg")
img_spotify = Image.open("images/spotify.jpg")
img_videogames = Image.open("images/videogames.jpg")
img_word2vec = Image.open("images/word2vec.jpg")
img_fob = Image.open("images/fob.jpg")
img_map = Image.open("images/map.png")
img_gephi = Image.open("images/gephi.png")
# Assets for articles and essays
img_outlier = Image.open("images/outlier.png")
img_dac = Image.open("images/dac.png")
img_raffles = Image.open("images/raffles.jpg")
img_covid = Image.open("images/covid.jpg")
img_gender = Image.open("images/gender.jpg")
img_hci = Image.open("images/hci.jpg")
img_wordcloud = Image.open("images/wordcloud.jpg")
img_taste = Image.open("images/taste.jpg")
img_measles = Image.open("images/measles.jpeg")
# Assets for gallery
# 2019
img_2019_1 = Image.open("gallery/2019_1.jpg")
img_2019_2 = Image.open("gallery/2019_2.jpg")
img_2019_3 = Image.open("gallery/2019_3.jpg")
img_2019_4 = Image.open("gallery/2019_4.jpg")
img_2019_5 = Image.open("gallery/2019_5.jpg")
img_2019_6 = Image.open("gallery/2019_6.jpg")
img_2019_7 = Image.open("gallery/2019_7.jpg")
img_2019_8 = Image.open("gallery/2019_8.jpg")
img_2019_9 = Image.open("gallery/2019_9.jpg")
#2020
img_2020_1 = Image.open("gallery/2020_1.jpg")
#2021
img_2021_1 = Image.open("gallery/2021_1.jpg")
img_2021_2 = Image.open("gallery/2021_2.jpg")
img_2021_3 = Image.open("gallery/2021_3.jpg")
img_2021_4 = Image.open("gallery/2021_4.jpg")
img_2021_5 = Image.open("gallery/2021_5.jpg")
img_2021_6 = Image.open("gallery/2021_6.jpg")
img_2021_7 = Image.open("gallery/2021_7.jpg")
img_2021_8 = Image.open("gallery/2021_8.jpg")
img_2021_9 = Image.open("gallery/2021_9.jpg")
img_2021_10 = Image.open("gallery/2021_10.jpg")
img_2021_11 = Image.open("gallery/2021_11.jpg")
img_2021_12 = Image.open("gallery/2021_12.jpg")
#2022
img_2022_1 = Image.open("gallery/2022_1.jpg")
img_2022_2 = Image.open("gallery/2022_2.jpg")
img_2022_3 = Image.open("gallery/2022_3.jpg")
img_2022_4 = Image.open("gallery/2022_4.jpg")
img_2022_5 = Image.open("gallery/2022_5.jpg")
img_2022_6 = Image.open("gallery/2022_6.jpg")
img_2022_7 = Image.open("gallery/2022_7.jpg")
img_2022_8 = Image.open("gallery/2022_8.jpg")
img_2022_9 = Image.open("gallery/2022_9.jpg")
img_2022_10 = Image.open("gallery/2022_10.jpg")
img_2022_11 = Image.open("gallery/2022_11.jpg")
img_2022_12 = Image.open("gallery/2022_12.jpg")
img_2022_13 = Image.open("gallery/2022_13.jpg")
img_2022_14 = Image.open("gallery/2022_14.jpg")
img_2022_15 = Image.open("gallery/2022_15.jpg")
img_2022_16 = Image.open("gallery/2022_16.jpg")
img_2022_17 = Image.open("gallery/2022_17.jpg")
img_2022_18 = Image.open("gallery/2022_18.jpg")
img_2022_19 = Image.open("gallery/2022_19.jpg")
img_2022_20 = Image.open("gallery/2022_20.jpg")
img_2022_21 = Image.open("gallery/2022_21.jpg")
img_2022_22 = Image.open("gallery/2022_22.jpg")
img_2022_23 = Image.open("gallery/2022_23.jpg")
img_2022_24 = Image.open("gallery/2022_24.jpg")
img_2022_25 = Image.open("gallery/2022_25.jpg")
img_2022_26 = Image.open("gallery/2022_26.jpg")
img_2022_27 = Image.open("gallery/2022_27.jpg")
img_2022_28 = Image.open("gallery/2022_28.jpg")
img_2022_29 = Image.open("gallery/2022_29.jpg")
img_2022_30 = Image.open("gallery/2022_30.jpg")
#2023
img_2023_1 = Image.open("gallery/2023_1.jpg")
img_2023_2 = Image.open("gallery/2023_2.jpg")
img_2023_3 = Image.open("gallery/2023_3.jpg")
#img_lottie_animation = Image.open("images/lottie_animation.gif")
# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

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
    choose = option_menu(
                        "Harry Chang", 
                        ["About Me", "Site Overview", "Experience", "Technical Skills", "Education", "Projects", "Competitions", "Articles & Essays", "Gallery", "Site Analytics", "Resume & CV", "Contact"],
                         icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'pencil square', 'image', 'activity', 'paperclip', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#f5f5dc"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )

# Sidebar: If using streamlit_on_hover_tabs - not mobile friendly
#with st.sidebar:
#    choose = on_hover_tabs(tabName=["About Me", "Experience", "Technical Skills", "Education", "Projects", "Competitions", "Articles & Essays", "Site Analytics", "Contact"], 
#                         iconName=['person', 'schedule', 'construction', 'book', 'assignment', 'work', 'edit', 'dashboard', 'mail'], default_choice=0,
#                         styles = {'navtab': {'background-color':'#5a5a5a',
#                                                  'color': 'beige',
#                                                  'font-size': '18px',
#                                                  'transition': '.2s',
#                                                  'white-space': 'nowrap',
#                                                  'text-transform': 'uppercase'},
#                                       'tabOptionsStyle': {':hover :hover': {'color': 'darkorange',
#                                                                      'cursor': 'pointer'}},
#                                       'iconStyle':{'position':'fixed',
#                                                    'left':'7.5px',
#                                                    'text-align': 'left'},
#                                       'tabStyle' : {'list-style-type': 'none',
#                                                     'margin-bottom': '30px',
#                                                     'padding-left': '30px'}},
#                             key="1")

# Create header
if choose == "About Me":
    with st.container():
        left_column, right_column = st.columns((1,0.55))
        with left_column:
            st.title("Harry Chang")
            st.subheader("Aspiring Data Analyst/Data Scientist")
            st.write("👋🏻 Hi, I'm Harry! I'm a data science and analytics undergraduate based in Singapore. Having prior relevant experiences in tech, reinsurance and consulting sectors, I am constantly seeking unique internships to broaden my horizons before embarking on my data career upon graduation.")
            st.write("💼 With the COVID-19 pandemic behind us, I believe there is potential for data science to be applied in the retail industry. In response to the increasing demand for data analytics from both online and brick-and-mortar sales, I am thus aiming to enter this industry for my first full-time job.")
            st.write("🏋🏻 In addition, I like to exercise in the gym, run, write, play video games and... eat good food in my free time.")
            st.write("👨🏼‍💻 Academic interests: Data Visualization, Market Basket Analysis, Recommendation Systems, Natural Language Processing")
            st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, Data Engineer, Business Intelligence Analyst, Product Manager")
            st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/13CHoDfb-mYr9F8YSA4ZDV3tZPpNF6eck/view?usp=sharing) | [CV (2 pages)](https://drive.google.com/file/d/1-aubNVEKkgmHdeCtlp_O1M99tVChXfYs/view?usp=sharing)")
        with right_column:
            st.image(img_utown)
elif choose == "Site Overview":
    st.header("Site Overview")
    st.markdown("""
    Initally creating this as a portfolio website in the form of an extended resume, I came to discover the uniqueness of Streamlit as compared to typical front-end frameworks such as Angular and Bootstrap. Even though Streamlit is primarily used as a web application for dashboarding, its extensive features make it more aesthetically appealing to explore with as compared to alternatives such as Plotly and Shiny.
    
    With the convenience of using Python as a beginner-friendly programming language, I have now decided to evolve this personal project into a time capsule - documenting key moments and achievements that I have attained since commencing my formal education at 7 years old. In addition, should I be successful in completing this project, I intend to provide my codes as open-source, so that other students can document their educational journey in a similar manner.

    A video will also be embedded in this section to provide a detailed tour of this entire web application and its features.

    *Video to be released*
    """)
# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_sephora)
        with text_column:
            st.subheader("Product Data Analyst Intern, [Sephora](https://sephora.sg)")
            st.write("June to December 2023 (Upcoming)")
            #st.markdown("- Built, documented and hosted SQL queries and processes to enable reproducible and effective pipelines, analysis and dashboards using BigQuery")
            #st.markdown("- Utilised Domo to create dataflows and visualizations that provide quick insights into product health and performance of e-commerce features (web and mobile)")
            #st.markdown("- Implemented A/B testing to measure potency of new e-commerce features before reporting results")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_questlogo)
        with text_column:
            st.subheader("Marketing Intern, [Quest](https://quest-inc.co)")
            st.write("April to June 2023 (Ongoing)")
            st.markdown("""
            - Launched marketing ad campaigns using Google Ads to target businesses to visit company's landing page
            - Drafted content articles on Wordpress for search engine optimisation (SEO)
            - Performed weekly reporting of user acquisition metrics from various marketing channels, including [TikTok](https://www.tiktok.com/@questhireahero?lang=en) and [Instagram](https://www.instagram.com/questhireahero/)
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_scor)
        with text_column:
            st.subheader("Actuarial Intern, [SCOR](https://scor.com)")
            st.write("May to August 2022 | [Testimonial](https://drive.google.com/file/d/1seUP5OcXV5irA1Y1qt0cKnd7uQnLJLzw/view?usp=share_link)")
            st.markdown("""
            - Performed actuarial analysis of reinsurance treaties in various APAC markets, including entry of client portfolio and loss data into xAct (treaty pricing system)
            - Regularly updated and analysed risk profiles and claims databases for insurance markets in Pakistan, Thailand and Vietnam
            - Trained machine learning models (logistic regression, random forest) to predict insurance claims, with an average accuracy of 80% for each model
            """)
            #st.write("[Testimonial](https://drive.google.com/file/d/1seUP5OcXV5irA1Y1qt0cKnd7uQnLJLzw/view?usp=share_link)")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_questlogo)
        with text_column:
            st.subheader("Data Analytics Intern, [Quest](https://quest-inc.co)")
            st.write("February to May 2022")
            st.markdown("""
            - Conducted cohort analysis to optimise user acquisition and retention rates
            - Collected, analysed and interpreted trends within user data to improve company’s growth and marketing strategies
            - Built visualizations and dashboards using RStudio and Tableau to report monthly key metrics of company’s mobile application
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_sshsph)
        with text_column:
            st.subheader("Public Health Intern, [Saw Swee Hock School of Public Health](https://sph.nus.edu.sg/)")
            st.write("January to May 2021")
            st.markdown("""
            - Conducted literature reviews and summarized papers related to public health
            - Drafted case study report on British population health system, including impacts from COVID-19
            - Collaborated with other students to compare successes and challenges of Britain, Canada and New Zealand’s healthcare systems
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_iasg)
        with text_column:
            st.subheader("Data Migration Intern, [Immigration@SG LLP](https://iasg.com.sg/)")
            st.write("October 2020 to January 2021 | [Testimonial](https://drive.google.com/file/d/11qFI-9TMfjOk1OxuyQ9ho9A7D6KuIsXp/view?usp=sharing)")
            st.markdown("""
            - Cleaned over 30,000 records using Pandas to facilitate smooth data migration into new CRM system
            - Derived customer segmentation models using regression models and market basket analysis (association rule mining) to improve company’s marketing strategies
            - Completed time series analysis using past sales data to forecast future monthly revenue
            """)
            #st.write("[Testimonial](https://drive.google.com/file/d/11qFI-9TMfjOk1OxuyQ9ho9A7D6KuIsXp/view?usp=sharing)")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_yll)
        with text_column:
            st.subheader("Temporary Management Support Staff, [Yong Loo Lin School of Medicine](https://medicine.nus.edu.sg/)")
            st.write("February to June 2019")
            st.markdown("""
            - Answered up to 100 different queries daily regarding undergraduate admissions
            - Managed venue preparations for admissions interviews involving over 1,000 candidates over the span of 2 weeks
            - Supported set-up of faculty booth for NUS Open House, with an estimated attendance of 30,000 visitors in one day
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_saf)
        with text_column:
            st.subheader("Administrative Support Assistant, [Singapore Armed Forces](https://www.mindef.gov.sg/web/portal/mindef/home)")
            st.write("January 2017 to January 2019 | [Testimonial](https://drive.google.com/file/d/1O6Yu0P65dU8LCSDuXkf9BvlQJoz_5mRW/view?usp=sharing)")
            st.markdown("""
            - Assisted in organising division-level In-Camp Trainings, conferences and welfare events
            - Handled daily administration of Operations Branch, including indentation of office equipment, budget management and food rations
            - Promoted to Corporal First Class (CFC) for outstanding efforts
            """)
            #st.write("[Testimonial](https://drive.google.com/file/d/1O6Yu0P65dU8LCSDuXkf9BvlQJoz_5mRW/view?usp=sharing)")
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages","`R`, `Python`, `SQL`, `Java`, `Stata`, `MATLAB`")
    txt3("Academic Interests","`Data Visualization`, `Market Basket Analysis`, `Recommendation Systems`, `Natural Language Processing`")
    txt3("Data Visualization", "`ggplot2`, `matplotlib`, `seaborn`, `Folium`, `Gephi`, `Tableau`, `Power BI`, `Google Data Studio`, `Domo`, `Google Analytics`")
    txt3("Database and Cloud Systems", "`MySQL`, `PostgreSQL`, `BigQuery`, `Cloud Firestore`, `Google Cloud Platform`, `Amazon Web Services`")
    txt3("Version Control", "`Git`, `Docker`")
    txt3("Design and Front-end Development", "`Canva`, `Figma`, `HTML`, `CSS`, `Streamlit`, `Wordpress`")
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `Association Rules Mining`, `Random Forest`, `Decison Trees`, `Principal Components Analysis`, `Text Classification`, `Sentiment Analysis`, `Matrix Factorisation`, `Collaborative Filtering`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`, `JAX`, `NLTK`")
    txt3("Task Management Tools", "`Asana`, `Notion`, `ClickUp`, `Slack`")
    txt3("Miscellaneous", "`Google Firebase`, `Microsoft Office`, `Retool`, `Google Ads`")

#st.subheader("Programming Languages")
#st.write("R, Python, SQL, Java, Stata")
#st.subheader("Academic Interests")
#st.write("Data Visualization, Market Basket Analysis, Recommendation Systems, Natural Language Processing")
#st.subheader("Data Visualization")
#st.write("ggplot2, matplotlib, seaborn, Gephi, Tableau, Power BI, Looker (Google Data) Studio, Domo, Google Analytics")
#st.subheader("Database and Cloud Systems")
#st.write("MySQL, PostgreSQL, BigQuery, Cloud Firestore, Google Cloud Platform, Amazon Web Services")
#st.subheader("Version Control")
#st.write("Git, Docker")
#st.subheader("Design and Front-end Development")
#st.write("Canva, Figma, HTML, CSS, Streamlit, Wordpress")
#st.subheader("Data Science Techniques")
#st.write("Regression, Clustering, Association Rules Mining, Random Forest, Decison Trees, Principal Components Analysis, Natural Language Processing, Matrix Factorisation, Collaborative Filtering")
#st.subheader("Machine Learning Frameworks")
#st.write("TensorFlow, Keras, JAX, NLTK")
#st.subheader("Task Management Tools")
#st.write("Asana, Notion, ClickUp, Slack")
#st.subheader("Miscellaneous")
#st.write("Google Firebase, Microsoft Office, Retool, Google Ads")

#st.write("##")

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_nus)
        with text_column:
            st.subheader("Bachelor of Science - [Data Science and Analytics](https://www.stat.nus.edu.sg/wp-content/uploads/sites/8/2022/12/NUS-CHS-DSA-Print-FA.pdf), [National University of Singapore](https://nus.edu.sg) (2020-2024)")
            st.write("Relevant Coursework: Computers and the Humanities, Convex Optimization, Data Science in Practice, Data Structures and Algorithms, Data Visualization, Database Technology and Management, Linear Algebra, Multivariable Calculus, Optimization for Large-Scale Data-Driven Inference, Probability, Programming Tools for Economics, Regression Analysis, Statistical Learning")
            st.markdown("""
            - [NUS Statistics and Data Science Society](https://sites.google.com/view/nussds/home) - President (2022), Marketing Director (2021-22)
            - [Google Developer Student Clubs NUS](https://dsc.comp.nus.edu.sg/) - Deputy Head of Finance (2021-22)
            - [NUS Inter-Faculty Games](https://ifg.nussportsclub.org/) - Track and Field (Science) Captain (2022)
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_poc)
        with text_column:
            st.subheader("Bachelor of Science - Pharmaceutical Science, [National University of Singapore](https://nus.edu.sg) (2019)")
            st.write("Coursework: Foundations of Medicinal Chemistry, Pharmaceutical Biochemistry, Statistics for Life Sciences, Human Anatomy and Physiology, Quantitative Reasoning")
            st.markdown("""
            Withdrew from course in 2020, before performing a clean slate transfer to pursue a Bachelor's Degree in Data Science and Analytics
            - [NUS Students' Science Club](https://www.nussciencelife.com/) - Marketing Executive, Welfare Subcommittee
            - Pharmaceutical Science (Class of 2023) - Assistance Class Representative
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_tpjc)
        with text_column:
            st.subheader("GCE A Level - [Tampines Junior College](https://www.tmjc.moe.edu.sg/our-heritage/tampines-jc/) (2015 - 2016)")
            st.write("Coursework: H2 Chemistry, H2 Economics, H2 Mathematics, H1 Project Work, H1 Chinese, H1 History")
            st.markdown(""" 
            - Track and Field - 100m (2016 A Division Semi-finalist), 200m, 4x100m
            - TPJC Economics and Financial Literacy Fair 2015 - Games Facilitator
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_sji)
        with text_column:
            st.subheader("GCE O Level - [Saint Joseph's Institution](https://www.sji.edu.sg/) (2012 - 2014)")
            st.write("Coursework: English, Mathematics, Additional Mathematics, Physics, Chemistry, History, Geography Elective, Chinese")
            st.markdown(""" 
            - Track and Field (Long Jump, 100m)
            - [Business Design Thinking](https://www.sp.edu.sg/sp/news/sp/Secondary-students-learn-to-innovate)
            - Josephian International Experience Programme (Siem Reap, Cambodia)
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_gmss)
        with text_column:
            st.subheader("Secondary One - [Geylang Methodist School (Secondary)](https://www.geylangmethodistsec.moe.edu.sg/) (2011)")
            st.write("Coursework: English, Mathematics, Science, History, Geography, Literature, Chinese, Design & Technology, Home Economics")
            st.markdown(""" 
            - Volleyball
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(img_sjij)
        with text_column:
            st.subheader("Primary School Leaving Examination - [Saint Joseph's Institution Junior](https://www.sjijunior.moe.edu.sg/) (2005 - 2010)")
            st.write("Coursework: English, Mathematics, Science, Chinese, Higher Chinese")
            st.markdown(""" 
            - Art Club
            """)
#st.write("##")

elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Optimising article quality using ChatGPT and NLP")
            st.write("Self-initiated project using past articles written for module SP1541: Exploring Science Communication in Popular Science in Academic Year 2020/21 Semester 1")
            st.markdown("""
            - Preliminary analysis - comparing word counts, readability scores and sentiment (compound) scores of all 6 article variants using NLTK and Textstat
            - Generated word clouds to highlight frequently used words in each article variant
            - Identified top 10 most commonly used words between variants of the same article to assess suitability of ChatGPT in enhancing article quality
            """)
            st.write("[Github Repo](https://github.com/harrychangjr/sp1541-nlp) | [Github Code (Backend)](https://github.com/harrychangjr/sp1541-nlp/blob/main/backend.ipynb)")
        with image_column:
            st.image(img_chatgpt)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Statistical Learning: Analysis on Video Game Sales")
            st.write("Completed project within 48 hours for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2")
            #st.write("Methods performed on [Kaggle dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings):")
            st.markdown("""
            - Utilised multiple regression to investigate impact of publishers on global sales by regression coefficient, including performing one-hot encoding on 'Publisher' categorical variable
            - Compared performances of multiple linear regression, random forest and XGBoost to predict global sales using critic scores and user scores from Metacritic
            - Trained linear mixed-effects model to investigate impact of publishers, platform and genres in global sales
            """)
            st.write("[Term Paper](https://github.com/harrychangjr/st4248-termpaper/blob/main/ST4248%20Term%20Paper%20(A0201825N)%20v5.pdf) | [Github Repo](https://github.com/harrychangjr/st4248-termpaper)")
        with image_column:
            st.image(img_videogames)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data Science Project on Biopics Dataset from Kaggle")
            st.write("Self-initiated project using various machine learning methods on [biopics dataset](https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-biopics-dataset)")
            st.markdown("""
            - Ran regression models to predict box office revenue (linear regression, random forest, support vector machines)
            - Used k-means clustering with principal components analysis to identify similar types of movies
            - Built content-based recommendation system using cosine similarity to recommend similar movies based on input title
            """)
            st.write("[RPubs](https://rpubs.com/harrychangjr/biopics) | [Github Repo](https://github.com/harrychangjr/biopics)")
        with image_column:
            st.image(img_biopics)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Optimisation for Large-Scale Data-Driven Inference: Anime Recommendation System")
            st.write("Completed assignment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2")
            st.markdown("""
            - Built recommendation system using various non-factor models, including content-based collaborative filtering and clustering
            - Utilised matrix factorisation (single value decomposition) to optimise performance of recommendation system with lower test MSE
            - Provided optional recommendations to further optimise performance e.g scraping additional data, using deep learning methods
            """)
            st.write("[Github Repo](https://github.com/harrychangjr/dsa4212) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%202%20Group%2039%20Report.pdf)")
        with image_column:
            st.image(img_anime)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Optimisation for Large-Scale Data-Driven Inference: Word Embedding")
            st.write("Completed assigmment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2")
            st.markdown("""
            - Trained Word2Vec model on 20 Newsgroups dataset from scikit-learn package in Python, which provides a number of similar words based on input word
            - Evaluated usefulness of model by applying model to text classification (46% accuracy) and sentiment analysis (86.4% accuracy)
            """)
            st.write("[Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039%20Report.pdf) | [Github Code](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb)")
        with image_column:
            st.image(img_word2vec)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data-Driven Marketing: Exploration on 3 datasets related to cellphone billing and subscriber data")
            st.write("Self-initiated project based on past assignment from module BT4211: Data-Driven Marketing")
            st.markdown("""
            - Performed preliminary churn analysis, customer segmentation and descriptive analysis to understand more about dataset
            - Trained logit and probit models, as well as providing model estimations for duration models
            - Utilised random forest classifier to predict customer churn
            """)
            st.write("[RPubs](https://rpubs.com/harrychangjr/cellphone) | [Github Repo](https://github.com/harrychangjr/cellphone-billing)")
        with image_column:
            st.image(img_cellphone)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data Visualization: Analysis on Spotify Dataset from [tidytuesday](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-21)")
            st.write("Completed group project for module DSA2101: Essential Data Analytics Tools: Data Visualization in Academic Year 2021/22 Semester 2")
            st.markdown("""
            - Investigated variables that differentiates songs of different genres, which could be useful in designing recommendation systems
            - Explored how do the four seasons affect number of songs produced in each period
            - Visualizations used: ridgeline faceted density plot, boxplot, line chart, faceted donut chart
            """)
            st.write("[Github Code](https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd) | [RPubs](https://rpubs.com/harrychangjr/dsa2101-groupb)")
        with image_column:
            st.image(img_spotify)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Computers and the Humanities: Chloropleths using Google Sheets and Folium in Python")
            st.write("Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2")
            st.markdown("""
            - Visualized the total number of performances of A Doll's House by country, using a chloropleth from Google Sheets
            - Drafted scatterplots and boxplots using seaborn to investigate relationship between number of events per country and number of years these plays have been performed
            - Created chloropleth using Folium to compare total performance counts in China, categorised by province
            """)
            st.write("[Google Sheets](https://docs.google.com/spreadsheets/d/1NBlGM7Sjcybbpl1Esa55qLRJw-Seti1LhC93EhV_68w/edit?usp=sharing) | [Google Colab](https://colab.research.google.com/drive/1RHqtb5XC7PkJDpNEb-BY3tO-8mI2j32E?usp=sharing)")
        with image_column:
            st.image(img_map)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Computers and the Humanities: Network Analysis on Harry Potter Film Database")
            st.write("Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2")
            st.markdown("""
            - Utilised custom Python file based on NetworkX and Glob to create networks using Harry Potter film database
            - Drafted visualizations using matplotlib and seaborn to compare densities and weighted degree values of nodes from generated networks
            - Customised network visualization using Gephi to investigate relationship between various Harry Potter film directors
            """)
            st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N_GET1030_Tutorial_4.ipynb)")
        with image_column:
            st.image(img_gephi)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Computers and the Humanities: Text Processing and Analysis on Song Lyrics")
            st.write("Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2")
            st.markdown("""
            - Utilised NLTK to process 10 sets of song lyrics from Fall Out Boy across 2 albums (Folie à Deux, Save Rock and Roll)
            - Drafted visualizations using matplotlib and seaborn to compare proportions of nouns and verbs between different songs
            - Analysed type/token ratios of songs from both albums to evaluate which album produced better quality songs based on words used
            """)
            st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb)")
        with image_column:
            st.image(img_fob)
elif choose == "Competitions":
    # Create section for Competitions
    #st.write("---")
    st.header("Competitions")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lifehack)
        with text_column:
            st.subheader("[NUS LifeHack 2022](https://lifehack-2022.vercel.app/) - Hosted by [NUS Students' Computing Club](https://nuscomputing.com/)")
            st.write("Awarded Theme Best - Safety and Overall 2nd Place out of 117 team submissions")
            st.write("Ideated and developed Drive Woke! - a Flutter-based mobile application that aims to keep drivers awake by simulating conversations")
            st.write("[Devpost](https://devpost.com/software/quest-busters) | [Github Repo](https://github.com/yuechen2001/LifeHack2022) | [Pitch Deck](https://www.canva.com/design/DAFGF_nbyZ8/noJnq3IGDdX6nvu7M_2pXQ/view?utm_content=DAFGF_nbyZ8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Demo Video](https://www.youtube.com/watch?v=su3_Y3yzeh8)")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_he4d)
        with text_column:
            st.subheader("NUS Fintech Month Hackathon 2021 - Hosted by [NUS Fintech Society](https://fintechsociety.comp.nus.edu.sg/)")
            st.write("Awarded Overall 2nd Place")
            st.write("Ideated a multi-pronged approach using blockchain and machine learning methods to improve fraud detection amongst complex entities in a digital or hybrid (digital and manual) operating environment")
            st.write("[Pitch Deck](https://www.linkedin.com/feed/update/urn:li:ugcPost:6761489595420037120/)")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_shopee)
        with text_column:
            st.subheader("[Shopee Product and Design Challenge 2021](https://careers.shopee.sg/event-detail/396)")
            st.write("Redesigned user interface of Shopee mobile app using Figma to reduce clutter and increase user utilization of in-app rewards")
            st.write("[Pitch Deck](https://drive.google.com/file/d/12qnveB-SMjG_gF_gwNj3Nr-JsKeyKd6g/view) | [Figma Prototype](https://www.figma.com/proto/3UXT29N1RgVGDUlSBeWcPN/UI-Prototype-1?node-id=18-3&viewport=-675%2C231%2C0.32458001375198364&scaling=scale-down)")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_sbcc)
        with text_column:
            st.subheader("Singapore Business Case Competition 2020 - Hosted by [NTU Business Solutions Club](https://clubs.ntu.edu.sg/businesssolutions/)")
            st.write("Proposed solutions to help increase competitiveness of BreadTalk after performing market research and analysis on the F&B industry")
            st.write("[Pitch Deck](https://drive.google.com/file/d/1kLgbBVuth4KvfhjaK00n30xlr4bmn-iM/view)")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_runes)
        with text_column:
            st.subheader("Contest 2.2 Beautiful Runes - CS1010S Programming Methodology")
            st.write("Awarded 1st Place for 2D Runes category out of over 600 students enrolled in the module for Academic Year 2020/21 Semester 1")
            st.write("2D pixel art created using Pillow (PIL) Library in Python")
            st.write("[Github Repo](https://github.com/harrychangjr/runes)")
#st.write("##")

elif choose == "Articles & Essays":
    st.header("Articles & Essays")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with image_column:
            st.image(img_outlier)
        with text_column:
            st.subheader("Finding success as an outlier")
            st.write("April 12, 2023 | [Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")
            st.write("A personal reflection of my tumultous undergraduate journey so far - and how I finally found my resolve")
            #st.write("[Article](https://antcabbage.wordpress.com/2023/04/12/finding-success-as-an-outlier/)")       
    with st.container():
        text_column, image_column = st.columns((3,1))
        with image_column:
            st.image(img_raffles)
        with text_column:
            st.subheader("Essays for Final Test - GES1037: A History of Singapore in Ten Objects")
            st.write("April 29, 2022 | [Essays](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Take%20Home%20Test.pdf)")
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
            st.write("April 2, 2022 | [Term Paper](https://github.com/harrychangjr/ges1037/blob/main/GES1037%20Term%20Paper.pdf)")
            st.markdown("""
            Term paper submitted for the module GES1037: A History of Singapore in Ten Objects in Academic Year 2021/22 Semester 2
            """)       
    with st.container():
        text_column, image_column = st.columns((3,1))
        with image_column:
            st.image(img_dac)
        with text_column:
            st.subheader("Reflections on Organising an 850-participant Data Analytics Competition")
            st.write("February 18, 2022 | [Article](https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0&pli=1)")
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
            st.write("November 12, 2021 | [Essays](https://github.com/harrychangjr/geh1049/blob/main/GEH1049%20Final%20Assignment.pdf)")
            st.markdown("""
            Essays written in Academic Year 2021/22 Semester 1:
            - Q1: Worsened health disparities based on ethnicity and gender due to COVID-19
            - Q3: Obstacles in promoting healthy eating habits
            - Q4: Role of healthcare data analytics in managing COVID-19
            """)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with image_column:
            st.image(img_hci)
        with text_column:
            st.subheader("Evaluating 'Chinese Privilege' in Singapore - Special Assisted Plan Schools")
            st.write("April 29, 2021 | [Final Essay](https://github.com/harrychangjr/ges1010/blob/main/GES1010%20Final%20Essay%20A0201825N.pdf)")
            st.markdown("""
            Final essay submitted for the module GES1010: Nation-building in Singapore in Academic Year 2020/21 Semester 2
            """)      
    with st.container():
        text_column, image_column = st.columns((3,1))
        with image_column:
            st.image(img_wordcloud)
        with text_column:
            st.subheader("Analysing usefulness of word clouds in mental health studies")
            st.write("March 5, 2021 | [Essay](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20GET1030%20Individual%20Assignment%20Final.pdf)")
            st.markdown("""
            Individual assignment submitted for the module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2
            """)
    with st.container():
        text_column, image_column = st.columns((3,1))
        with image_column:
            st.image(img_taste)
        with text_column:
            st.subheader("Investigating the relationship between culture and sweet-sour taste interactions")
            st.write("October 31, 2020 | [Article](https://github.com/harrychangjr/sp1541-nlp/blob/main/Originals/SP1541%20NA2.pdf)")
            st.write("*Are we correct to stereotype taste perceptions and preferences based on different cultures?*")
            st.write("Science news article submitted for the module SP1541: Exploring Science Communication through Popular Science in Academic Year 2020/21 Semester 1")      
    with st.container():
        text_column, image_column = st.columns((3,1))
        with image_column:
            st.image(img_measles)
        with text_column:
            st.subheader("Timing vaccination campaign to reduce measles infections")
            st.write("September 30, 2020 | [Article](https://github.com/harrychangjr/sp1541-nlp/blob/main/Originals/SP1541%20NA1.pdf)")
            st.write("*Despite having a vaccine that is readily accessible, measles cases and deaths are still surging worldwide, especially in recent years. Why is this so and are there any long-term solutions to resolve this?*")
            st.write("Science news article submitted for the module SP1541: Exploring Science Communication through Popular Science in Academic Year 2020/21 Semester 1")
elif choose == "Gallery":
    st.header("Gallery")
    st.subheader("Some of my highlights throughout my educational years!")
    selected_options = ["Overview", "2023", "2022", "2021", "2020", "2019"]
    selected = st.selectbox("Which year would you like to explore?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Overview":
        st.subheader("Overview")
        st.markdown("""
        > "Photos are always the greatest gifts, because the memories from them will remain forever."
        
        My sister said this to me when I was in primary school. Having an immature and materialistic mindset back then, I was disappointed when I did not receive a present from her back then.

        The quote that she shared that day - was something that I failed to appreciate only until recently. Over the course of these past few years, I have made many memories - both good and bad - which I will fondly remember.

        Thus, this section is a compilation of highlights from my educational years, starting from primary school (7 years old), until the recent day (*in progress*). These images are not only meant to remind myself of the good times that I once had with long lost friends who I hardly keep in touch with nowadays due to our busy schedules, but also serve to show potential viewers a glimpse of what my life was like beyond academics.

        In particular, I hope to be able to refer to this time and time again, especially upon graduating from university and when I formally commence my full-time career.

        To those viewing my website and this section in particular, enjoy the pictures!

        *Note: Photos filed under each year are not necessarily posted in any particular order, as I may have forgotten the exact dates of some photos that were taken.*
        """)
    elif selected == "2019":
        st.subheader("2019")
        st.write("*So many things to explore, yet so little time*")
        # Define the list of image files
        images_2019 = [img_2019_1, img_2019_2, img_2019_3, img_2019_4, img_2019_5, img_2019_6, img_2019_7, img_2019_8, img_2019_9]
        # Display the images in a grid
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(images_2019[0], use_column_width=True)
        with col2:
            st.image(images_2019[1], use_column_width=True)
        with col3:
            st.image(images_2019[2], use_column_width=True)
        
        col4, col5, col6 = st.columns(3)
        with col4:
            st.image(images_2019[3], use_column_width=True)
        with col5:
            st.image(images_2019[4], use_column_width=True)
        with col6:
            st.image(images_2019[5], use_column_width=True)
        
        col7, col8, col9 = st.columns(3)
        with col7:
            st.image(images_2019[6], use_column_width=True)
        with col8:
            st.image(images_2019[7], use_column_width=True)
        with col9:
            st.image(images_2019[8], use_column_width=True)

    elif selected == "2020":
        st.subheader("2020")
        st.write("*Intro to Zoom University*")
        # Create a container for the image
        container = st.container()
        # Display the image in the container
        with container:
            st.image(img_2020_1, width = 500)
    elif selected == "2021":
        st.subheader("2021")
        st.write("*Boomer in a zoomer's body*")
        # Define the list of image files
        images_2021 = [img_2021_1, img_2021_2, img_2021_3, img_2021_4, img_2021_5, img_2021_6, img_2021_7, img_2021_8, img_2021_9, img_2021_10, img_2021_11, img_2021_12]
        # Display the images in a grid
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(images_2021[0], use_column_width=True)
        with col2:
            st.image(images_2021[1], use_column_width=True)
        with col3:
            st.image(images_2021[2], use_column_width=True)
        
        col4, col5, col6 = st.columns(3)
        with col4:
            st.image(images_2021[3], use_column_width=True)
        with col5:
            st.image(images_2021[4], use_column_width=True)
        with col6:
            st.image(images_2021[5], use_column_width=True)
        
        col7, col8, col9 = st.columns(3)
        with col7:
            st.image(images_2021[6], use_column_width=True)
        with col8:
            st.image(images_2021[7], use_column_width=True)
        with col9:
            st.image(images_2021[8], use_column_width=True)

        col10, col11, col12 = st.columns(3)
        with col10:
            st.image(images_2021[9], use_column_width=True)
        with col11:
            st.image(images_2021[10], use_column_width=True)
        with col12:
            st.image(images_2021[11], use_column_width=True)
    elif selected == "2022":
        st.subheader("2022")
        st.write("*Highlights, lowlights, learnings, help sought, and kudos to everyone!*")
        # Define the list of image files
        images_2022 = [img_2022_1, img_2022_2, img_2022_3, 
        img_2022_4, img_2022_5, img_2022_6, 
        img_2022_7, img_2022_8, img_2022_9, 
        img_2022_10, img_2022_11, img_2022_12,
        img_2022_13, img_2022_14, img_2022_15,
        img_2022_16, img_2022_17, img_2022_18,
        img_2022_19, img_2022_20, img_2022_21,
        img_2022_22, img_2022_23, img_2022_24,
        img_2022_25, img_2022_26, img_2022_27,
        img_2022_28, img_2022_29, img_2022_30
        ]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(images_2022[0], use_column_width=True)
        with col2:
            st.image(images_2022[1], use_column_width=True)
        with col3:
            st.image(images_2022[2], use_column_width=True)
        
        col4, col5, col6 = st.columns(3)
        with col4:
            st.image(images_2022[3], use_column_width=True)
        with col5:
            st.image(images_2022[4], use_column_width=True)
        with col6:
            st.image(images_2022[5], use_column_width=True)
        
        col7, col8, col9 = st.columns(3)
        with col7:
            st.image(images_2022[6], use_column_width=True)
        with col8:
            st.image(images_2022[7], use_column_width=True)
        with col9:
            st.image(images_2022[8], use_column_width=True)

        col10, col11, col12 = st.columns(3)
        with col10:
            st.image(images_2022[9], use_column_width=True)
        with col11:
            st.image(images_2022[10], use_column_width=True)
        with col12:
            st.image(images_2022[11], use_column_width=True)

        col13, col14, col15 = st.columns(3)
        with col13:
            st.image(images_2022[12], use_column_width=True)
        with col14:
            st.image(images_2022[13], use_column_width=True)
        with col15:
            st.image(images_2022[14].rotate(180), use_column_width=True)
        
        col16, col17, col18 = st.columns(3)
        with col16:
            st.image(images_2022[15], use_column_width=True)
        with col17:
            st.image(images_2022[16], use_column_width=True)
        with col18:
            st.image(images_2022[17].rotate(180), use_column_width=True)
        
        col19, col20, col21 = st.columns(3)
        with col19:
            st.image(images_2022[18], use_column_width=True)
        with col20:
            st.image(images_2022[19], use_column_width=True)
        with col21:
            st.image(images_2022[20], use_column_width=True)

        col22, col23, col24 = st.columns(3)
        with col22:
            st.image(images_2022[21], use_column_width=True)
        with col23:
            st.image(images_2022[22], use_column_width=True)
        with col24:
            st.image(images_2022[23], use_column_width=True)
        
        col25, col26, col27 = st.columns(3)
        with col25:
            st.image(images_2022[24], use_column_width=True)
        with col26:
            st.image(images_2022[25], use_column_width=True)
        with col27:
            st.image(images_2022[26], use_column_width=True)
        
        col28, col29, col30 = st.columns(3)
        with col28:
            st.image(images_2022[27], use_column_width=True)
        with col29:
            st.image(images_2022[28], use_column_width=True)
        with col30:
            st.image(images_2022[29], use_column_width=True)
    elif selected == "2023":
        st.subheader("2023")
        st.write("*Success - being content at the present moment*")
        # Define the list of image files
        images_2023 = [img_2023_1, img_2023_2, img_2023_3, 
        ]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(images_2023[0], use_column_width=True)
        with col2:
            st.image(images_2023[1], use_column_width=True)
        with col3:
            st.image(images_2023[2], use_column_width=True)
        st.write("...and more to come!")
elif choose == "Site Analytics":
    st.header("Site Analytics")
    with st.container():
      with streamlit_analytics.track():
            st.text_input("Enter something below if you'd like!", key="name_input", 
                      help="Enter your full name", 
                      value="Type something here!", 
                      max_chars=100, 
                      type="default",
                      )
            st.markdown("""
            <style>
                /* Add custom CSS styles for the text input */
                #name_input input[type=text] {
                    background-color: #f2f2f2;
                    border: none;
                    padding: 8px;
                    font-size: 16px;
                    width: 100%;
                }
            </style>
            """, unsafe_allow_html=True)
            st.button("Click me!")
            st.write("...and now add `?analytics=on` to the URL to see the analytics dashboard 👀")  
elif choose == "Resume & CV":
    st.header("Resume & CV")
    def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    st.subheader("Resume (1 page)")
    show_pdf("Harry Chang Resume2024.pdf")
    st.subheader("CV (2 pages)")
    show_pdf("Harry Chang CV2023.pdf")

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
        text_column, image_column = st.columns((1,0.55))
        with text_column:
            st.write("Let's connect! You may reach out to me at harrychang.work@gmail.com")
            st.write("Alternatively, feel free to contact me using any of the social media icons below!")
            linkedin_url = "https://www.linkedin.com/in/harrychangjr/"
            github_url = "https://github.com/harrychangjr"
            email_url = "mailto:harrychang.work@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
            st.write("© 2023 Harry Chang")
            #st.write("[LinkedIn](https://linkedin.com/in/harrychangjr) | [Github](https://github.com/harrychangjr) | [Linktree](https://linktr.ee/harrychangjr)")
        with image_column:
            st.image(img_ifg)
#st.write("##")
