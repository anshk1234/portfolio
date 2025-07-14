import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Set up page
st.set_page_config(page_title="portfolio", page_icon=":tada:", layout="wide")

# ---- DEVICE DETECTION ----
user_agent = st.config.get_option("browser.user_agent").lower()
is_mobile_device = "mobile" in user_agent or "android" in user_agent or "iphone" in user_agent

# Load Lottie from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_study_app = Image.open("images/study_app.png")
img_matrix_calculator = Image.open("images/matrix_calculator.png")
img_music_app = Image.open("images/music_app.png")
img_quote_generator_app = Image.open("images/quote_generator_app.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Ansh :wave:")
    st.title("A Web App Developer and designer from India")
    st.write("I am passionate about working on my ideas and interested in web app development.")
    st.write("[Learn More >](https://share.streamlit.io/user/anshk1234)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I'm a Class 12 student passionate about crafting interactive and visually appealing web applications using Streamlit and Python. I love building projects that strike a balance between usefulness and fun—turning ideas into tools that make life a little easier or more delightful.
            I'm always exploring new ways to blend creativity with functionality.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding", loop=not is_mobile_device)

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_study_app)
    with text_column:
        st.subheader("STUDY APP")
        st.write(
            """
            this is a study app which has many features like "to do list" , "study logs" , "pomodoro" for focus and also your daily ,weekly study "reports" in form of graph.
            It is a simple and easy to use app which helps you to manage your study time and also helps you to focus on your studies.  
            You can also set your daily study goals and track your progress.
            It is a great way to stay organized and motivated in your studies.           
            """
        )
        st.markdown("[See App...](https://study-app-tuxkvrvlrrmqextrtvy4rb.streamlit.app/)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_matrix_calculator)
    with text_column:
        st.subheader("MATRIX CALCULATOR")
        st.write(
            """
            This is a matrix calculator which can perform operations like  adjoint, inverse, transpose, multiplication, determinant value of matrices.
            you can also choose order of matrix.
            It is a simple and easy to use calculator for matrix operations.
            It is a great way to perform matrix operations without any hassle.
            """
        )
        st.markdown("[See App...](https://matrix-app.streamlit.app/)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_music_app)
    with text_column:
        st.subheader("MUSIC APP")
        st.write(
            """
            this is a personalised music app which plays music locally .
            you can also like your favourite songs and also create your own playlist.
            It is a simple and easy to use app
            and you can also search for your favourite songs.
            It is a great way to enjoy your music.
            """
        )
        st.markdown("[See App...](https://music-app-efnnywpco6zhjnqz4nkxkk.streamlit.app/)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_quote_generator_app)
    with text_column:
        st.subheader("AESTHETIC QUOTE GENERATOR APP")
        st.write(
            """
            this is a quote generator app  from which you can generate you own quotes as well as ramdom quotes.
            you can choose the background and font style of the quote according to your choice.
            It is a simple and easy to use app.
            you can also download the quote as an image.
            It is a great way to get inspired and motivated by quotes.
            """
        )
        st.markdown("[See App...](https://aesthetic-quote-generator-app-fmqblazjnmsfhkhzrxn28g.streamlit.app/)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/anshkunwar3009@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
