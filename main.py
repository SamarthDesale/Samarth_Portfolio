from fasthtml.common import *

# FastHTML app initialization
# (Reloading again for the footer styling)
css = Style(open("static/styles.css").read())
app, rt = fast_app(
    pico=False, # Disable pico to use our custom CSS entirely
    hdrs=(css,)
)

@rt("/")
def get():
    # Header Navigation
    header = Header(
        Nav(
            Div(
                Div("</>", cls="logo-icon"),
                Div(
                    Strong("Samarth Desale"),
                    Span("AI/ML & Data Science Portfolio"),
                    cls="logo-text"
                ),
                cls="nav-logo"
            ),
            Ul(
                Li(A("Home", href="#home", cls="active")),
                Li(A("Skills", href="#skills")),
                Li(A("Projects", href="#projects")),
                Li(A("Experience", href="#experience")),
                Li(A("Contact", href="#home")),
                cls="nav-links"
            ),
            cls="container"
        ),
        cls="navbar"
    )

    # Hero Section
    hero = Section(
        id="home",
        cls="hero container hero-grid"
    )(
        Div(
            Div(
                Span("", cls="status-badge"),
                cls="badge-wrapper"
            ),
            
            H1("Samarth ", Span("Desale", cls="gradient-text")),
            H2("AI/ML Engineer \n& Data Scientist", cls="hero-subtitle"),
            
            Div(
                Span("🌐 AI/ML Engineer", cls="role-badge"),
                cls="role-wrapper"
            ),
            
            P("Building intelligent systems at the intersection of AI, machine learning, and data engineering — from predictive churn models to CNN-based disease classifiers.", cls="hero-desc"),
            
            Div(
                Span("📍 Dhule, Maharashtra", cls="info-badge"),
                Span("🎓 CGPA 7.26 till date", cls="info-badge"),
                cls="info-badges"
            ),
            
            Div(
                A("Explore Work ↓", href="#projects", cls="btn btn-primary"),
                A("Contact ✉", href="mailto:samarthdesale739@gmail.com", cls="btn btn-secondary"),
                cls="hero-buttons"
            ),
            
            Div(
                A("GitHub", href="https://github.com/Samarthdesale", target="_blank", cls="social-icon-btn"),
                A("LinkedIn", href="https://linkedin.com/in/samarthdesale", target="_blank", cls="social-icon-btn"),
                cls="hero-socials"
            ),
            cls="hero-content"
        ),
        Div(
            Div(
                Img(src="/static/profile.jpg?v=2", alt="Samarth Jitendra Desale", cls="profile-img"),
                cls="img-container"
            ),
            cls="hero-image-wrapper"
        )
    )

    # About Section
    about = Section(
        id="about",
        cls="container"
    )(
        H2("About Me"),
        Div(
            P("Hello! I am an aspiring Data Scientist and AI/ML enthusiast currently pursuing my B.Tech in Information Technology at SVKM Institute of Technology. I am deeply passionate about the entire data lifecycle—from engineering robust data pipelines and building predictive machine learning models, to transforming complex raw data into clear, actionable business intelligence."),
            P("My core interests lie in Artificial Intelligence, Machine Learning, and Data Analytics. While my primary focus is on extracting valuable insights from data and creating intelligent systems using tools like Python, TensorFlow, and Power BI, I also possess a strong foundation in full-stack web development. This versatile skill set allows me to not only analyze data but also build end-to-end interactive dashboards and seamlessly deploy ML models into production environments."),
            cls="glass-card"
        ),
        cls="container"
    )

    # Education Section
    education = Section(
        id="education",
        cls="container"
    )(
        H2("Education"),
        Div(
            Div(
                Span("2023 – Present", cls="timeline-date"),
                H3("B.Tech Information Technology (CGPA: 7.26)"),
                P("SVKM Institute of Technology, Dhule (DBATU)"),
                cls="timeline-item"
            ),
            Div(
                Span("2021 – 2023", cls="timeline-date"),
                H3("HSC (72.17%)"),
                P("Z.B.Patil Jr. College, Dhule"),
                cls="timeline-item"
            ),
            Div(
                Span("2020 – 2021", cls="timeline-date"),
                H3("SSC (85.40%)"),
                P("Chavara High School, Dhule"),
                cls="timeline-item"
            ),
            cls="timeline glass-card"
        ),
        cls="container"
    )

    # Skills Section
    ds_ai_skills = [
        "Machine Learning", "Python", "PyTorch", "TensorFlow", "Keras", "Scikit-learn", "NLP"
    ]
    bi_analytics_skills = [
        "Power BI", "Tableau", "SQL", "Pandas", "NumPy", "Data Visualization"
    ]
    de_mlops_skills = [
        "Data Engineering", "ETL Pipelines", "MLOps", "Docker", "MySQL", "MongoDB"
    ]
    web_skills = [
        "Node.js", "Express.js", "React.js", "FastAPI", "Flask", "Java"
    ]
    
    ds_tags = [Span(skill, cls="skill-tag") for skill in ds_ai_skills]
    bi_tags = [Span(skill, cls="skill-tag") for skill in bi_analytics_skills]
    de_tags = [Span(skill, cls="skill-tag") for skill in de_mlops_skills]
    web_tags = [Span(skill, cls="skill-tag") for skill in web_skills]
    
    skills = Section(
        id="skills",
        cls="container"
    )(
        H2("Technical Skills"),
        Div(
            H3("Data Science & AI/ML"),
            Div(*ds_tags, cls="skills-container"),
            
            H3("Data Analysis & Business Intelligence"),
            Div(*bi_tags, cls="skills-container"),
            
            H3("Data Engineering & MLOps"),
            Div(*de_tags, cls="skills-container"),
            
            H3("Web Development"),
            Div(*web_tags, cls="skills-container"),
            cls="glass-card"
        ),
        cls="container"
    )

    # Experience Section
    experience = Section(
        id="experience",
        cls="container"
    )(
        H2("Experience"),
        Div(
            Div(
                Span("Jul 2026 – Present", cls="timeline-date"),
                H3("Virtual Data Science Apprentice Intern"),
                P("Yuva Intern by Henry Harvin"),
                P("Working on MLOps pipelines, machine learning model development, and applied data analysis. Built the E-Commerce Retention Engine."),
                cls="timeline-item"
            ),
            Div(
                Span("Jun 2025 – Jul 2025", cls="timeline-date"),
                H3("Java Programming Intern"),
                P("VaultofCodes"),
                P("Built practical Java applications, reinforcing OOP principles and professional coding standards in a team environment."),
                cls="timeline-item"
            ),
            cls="timeline glass-card"
        ),
        cls="container"
    )

    # Projects Section
    projects = Section(
        id="projects",
        cls="container"
    )(
        H2("Featured Projects"),
        Div(
            Div(
                H3("E-Commerce Retention Engine"),
                P("AI-powered E-commerce retention engine. Features real-time churn prediction via a Random Forest model, served through a FastAPI backend and a beautiful Flask business dashboard."),
                A("View on GitHub", href="https://github.com/SamarthDesale/Ecommerce-Retention-Engine", target="_blank", cls="btn"),
                cls="glass-card"
            ),
            Div(
                H3("Plant Disease Detection"),
                P("CNN-based plant disease classifier trained on 26,000+ images across 7 categories, achieving 97% training accuracy. Deployed as a Streamlit app."),
                A("View on GitHub", href="https://github.com/SamarthDesale/ML-Based-Plant-Disease-Detection-System", target="_blank", cls="btn"),
                cls="glass-card"
            ),
            Div(
                H3("E-Ration Seva"),
                P("Anti-corruption ration platform with role-based access for Citizens, Shopkeepers, and District Officers. Features dynamic verification and Twilio SMS alerts."),
                A("View on GitHub", href="https://github.com/SamarthDesale/Smart_Ration_Management_System", target="_blank", cls="btn"),
                cls="glass-card"
            ),
            cls="grid"
        ),
        cls="container"
    )

    # Certifications Section
    certifications = Section(
        id="certifications",
        cls="container"
    )(
        H2("Training & Certifications"),
        Div(
            Div(
                Span("Oct 2024", cls="timeline-date"),
                H3("NPTEL Elite Certification: The Joy of Computing Using Python"),
                P("IIT Madras"),
                cls="timeline-item"
            ),
            Div(
                Span("Jun 2026", cls="timeline-date"),
                H3("Prime AI/ML Program"),
                P("Apna College (Machine Learning & Agentic AI)"),
                cls="timeline-item"
            ),
            Div(
                Span("Jun 2026", cls="timeline-date"),
                H3("Databases for Developers: Foundations"),
                P("Oracle"),
                cls="timeline-item"
            ),
            Div(
                Span("Jun 2026", cls="timeline-date"),
                H3("SQL and Relational Databases 101"),
                P("IBM"),
                cls="timeline-item"
            ),
            Div(
                Span("Oct 2025", cls="timeline-date"),
                H3("Data Analytics Job Simulation"),
                P("Deloitte"),
                cls="timeline-item"
            ),
            cls="timeline glass-card"
        ),
        cls="container"
    )

    # Achievements Section
    achievements = Section(
        id="achievements",
        cls="container"
    )(
        H2("Achievements"),
        Div(
            Div(
                H3("MumbaiHacks 2025"),
                P("Agentic AI Hackathon: Built 'PayAgent,' an AI financial agent with automated invoice parsing and PIN-verified transfers, in 24 hours."),
                cls="timeline-item"
            ),
            Div(
                H3("Avishkar 2025"),
                P("Institute Research Competition Presenter. Presented the ML-Based Plant Disease Detection System."),
                cls="timeline-item"
            ),
            cls="timeline glass-card"
        ),
        cls="container"
    )

    # Footer
    footer = Footer(
        P("© 2026 Samarth Jitendra Desale"),
        P("Email: ", A("samarthdesale739@gmail.com", href="mailto:samarthdesale739@gmail.com"), " | Phone: 8459444084"),
        style="text-align: center; padding: 2rem; color: var(--text-muted);"
    )

    # Assemble Page
    return Title("Samarth Desale | Portfolio"), Body(
        header,
        hero,
        about,
        education,
        skills,
        experience,
        projects,
        certifications,
        achievements,
        footer
    )

if __name__ == "__main__":
    serve()
