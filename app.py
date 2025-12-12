import streamlit as st
# Safe fallback for sticky_header (module removed from streamlit-extras)
def sticky_header(*args, **kwargs):
    return None

from streamlit_extras.colored_header import colored_header


st.set_page_config(page_title="Sathana S | Portfolio", layout="wide")

# ------------------------------------------
# Custom CSS for smooth scrolling & styling
# ------------------------------------------
st.markdown("""
<style>

html {
    scroll-behavior: smooth;
}

.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: #0a0a0a;
    z-index: 1000;
    padding: 15px 0;
    text-align: center;
    box-shadow: 0 2px 10px rgba(255,255,255,0.1);
}

.nav-item {
    display: inline-block;
    margin: 0 20px;
}

.nav-item a {
    color: white;
    text-decoration: none;
    font-size: 18px;
    font-weight: 500;
}

.nav-item a:hover {
    color: #00c2ff;
}

.section {
    padding: 90px 0;
}

.hero-text {
    font-size: 48px;
    font-weight: 900;
}

.subtext {
    font-size: 22px;
    color: #bbbbbb;
}

.skill-box {
    padding: 20px;
    background: #111111;
    margin: 10px;
    border-radius: 10px;
    border: 1px solid #333;
    text-align: center;
}

.timeline-item {
    padding: 15px;
    margin: 10px;
    border-left: 4px solid #00c2ff;
    background: #161616;
    border-radius: 5px;
}

footer {
    text-align: center;
    padding: 30px;
    background: #000;
    color: #aaa;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------
# Fixed Navbar
# ------------------------------------------
st.markdown("""
<div class="navbar">
    <span class="nav-item"><a href="#home">Home</a></span>
    <span class="nav-item"><a href="#about">About</a></span>
    <span class="nav-item"><a href="#skills">Skills</a></span>
    <span class="nav-item"><a href="#projects">Projects</a></span>
    <span class="nav-item"><a href="#workshops">Workshops</a></span>
    <span class="nav-item"><a href="#timeline">Education</a></span>
    <span class="nav-item"><a href="#contact">Contact</a></span>
</div>
""", unsafe_allow_html=True)

st.write("")  
st.write("")  
# ============================================================
# HERO SECTION
# ============================================================
st.markdown('<div id="home" class="section"></div>', unsafe_allow_html=True)

# Create two columns (left for text, right for photo)
col1, col2 = st.columns([1.2, 1])

# Left column: text, title, subtitle, download resume button
with col1:
    # small vertical spacing so navbar doesn't overlap content
    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

    st.markdown(
        "<h1 class='hero-text'>Hi, I'm <span style='color:#00c2ff;'>SATHANA S</span></h1>",
        unsafe_allow_html=True,
    )
    st.markdown("<p class='subtext'>Engineering Student (BE.)</p>", unsafe_allow_html=True)

    st.write(
        "Enthusiastic learner with a passion for new technologies and problem solving. "
        "Aspiring to secure an entry-level role where I can use my skills and knowledge "
        "to contribute to organizational success."
    )

    # Safe resume download button (shows info if file missing)
    try:
        with open("assets/resume.pdf", "rb") as f:
            resume_bytes = f.read()
        st.download_button(
            label="📄 Download Resume",
            data=resume_bytes,
            file_name="Sathana_Resume.pdf",
            mime="application/pdf",
        )
    except Exception:
        st.info("Resume not found at assets/resume.pdf — put your resume there to enable download.")

# Right column: profile image (safe fallback if file missing)
with col2:
    try:
        st.image("assets/photo.jpg", width=300, caption="Sathana S")
    except Exception:
        # show placeholder text if image fails to load
        st.markdown("<div style='height:300px; display:flex; align-items:center; justify-content:center; "
                    "border-radius:8px; background:#111; color:#ddd;'>Profile image missing</div>",
                    unsafe_allow_html=True)


# ============================================================
# ABOUT SECTION
# ============================================================
st.markdown('<div id="about" class="section"></div>', unsafe_allow_html=True)
st.header("👨‍💻 About Me")
st.write("""
I am an enthusiastic and dedicated engineering student with a keen interest in technology, programming, and problem-solving.  
I enjoy learning new concepts, exploring modern tools, and building real-world applications.
""")

# ============================================================
# SKILLS SECTION
# ============================================================
st.markdown('<div id="skills" class="section"></div>', unsafe_allow_html=True)
st.header("🛠 Skills")

skills = ["Python", "C", "HTML", "CSS", "MySQL", "Power BI"]

cols = st.columns(3)
for i, skill in enumerate(skills):
    with cols[i % 3]:
        st.markdown(f"<div class='skill-box'><b>{skill}</b></div>", unsafe_allow_html=True)




# ============================================================
# PROJECTS SECTION
# ============================================================
st.markdown('<div id="projects" class="section"></div>', unsafe_allow_html=True)
st.header("📁 Projects")

st.subheader("1. Banking Console App")
st.write("A Python + MySQL-based console banking management system.")
st.write("[🔗 GitHub Link](https://github.com/sathana0205/SQL-training/blob/main/banksql.py)")

st.subheader("2. Medical Appointment Scheduler")
st.write("Python + MySQL project for scheduling patient appointments.")
st.write("[🔗 GitHub Link](https://github.com/sathana0205/SQL-training/blob/main/PSM.py)")

# ============================================================
# WORKSHOPS SECTION
# ============================================================
st.markdown('<div id="workshops" class="section"></div>', unsafe_allow_html=True)
st.header("📚 Workshops & Certifications")

st.write("""
### Completed Workshops:
- UI & UX – Workshop  
- Database and Data Analytics – Workshop  
- Data Analytics with Python – NPTEL (63%)  
- Internet of Things – NPTEL (73%)

### Topics Explored:
- Data Preprocessing & Cleaning  
- Exploratory Data Analysis (EDA)  
- Statistical Methods  
- Data Visualization (Pandas, Matplotlib)  
- Basics of Machine Learning  
- Hands-on Projects with Real-world Datasets  
""")

# ============================================================
# TIMELINE / EDUCATION SECTION
# ============================================================
st.markdown('<div id="timeline" class="section"></div>', unsafe_allow_html=True)
st.header("🎓 Education Timeline")

st.markdown("""
<div class='timeline-item'>
    <h4>BE. (2026)</h4>
    <p>Engineering Student with strong interest in software development and analytics.</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CONTACT SECTION
# ============================================================
st.markdown('<div id="contact" class="section"></div>', unsafe_allow_html=True)
st.header("📞 Contact")

st.write("**Email:** sathana0205@gmail.com")  
st.write("**Phone:** 9025939353")  
st.write("[🔗 GitHub](https://github.com/sathana0205?tab=repositories)")  
st.write("[🔗 LinkedIn](https://www.linkedin.com/in/sathana-s-124658387/)")

# ============================================================
# FOOTER
# ============================================================

