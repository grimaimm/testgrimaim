# -----------------------------------------------------------------------------------------------------------------------------

# Import Library
import firebase_admin
from flask import render_template, request, session, redirect, url_for, flash
from flask_mail import Message, Mail
from app import app
from app.github_stats import get_contributions_from_github, get_github_contributions
from app.page_speed import build_tabs_structure
from app.remove_number import remove_numbers
from flask_caching import Cache
from firebase_admin import credentials, firestore
import mistune
from flask_markdown import Markdown

Markdown(app)
# -----------------------------------------------------------------------------------------------------------------------------

# Configuration
PAGE_SPEED_API_KEY = 'AIzaSyARfx_A-gCPFd4JwMRb7SCANYote5jgIvE'
# app.secret_key = 'personal-dashboard-grimaimcode'
app.secret_key = 'yRc3ERSZF-ahV9vTZo8hu3YqPZAri25IBa7uddcu8v0='
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# -----------------------------------------------------------------------------------------------------------------------------

# Inisialisasi Firebase Admin
cred = credentials.Certificate("app/static/js/personal-dashboard-grimaimcode-firebase-adminsdk-2338o-ff144be714.json")
firebase_admin.initialize_app(cred, {"projectId": "personal-dashboard-grimaimcode"})
db = firestore.client()

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'muhammadrahim@students.amikom.ac.id'
app.config['MAIL_PASSWORD'] = 'rrgn kbpk wjir gsfu'

mail.init_app(app)

app.jinja_env.filters['remove_numbers'] = remove_numbers

# -----------------------------------------------------------------------------------------------------------------------------

# Route Index
@app.route('/')
def index():
    blog_list = [blog.to_dict() for blog in db.collection("Blogs").stream()]
    service_list = [service.to_dict() for service in db.collection("Services").stream()]
    return render_template('index.html', blogs=blog_list, services=service_list)

# -----------------------------------------------------------------------------------------------------------------------------

# Route Blog
@app.route('/blog')
def blog():
    blogs_collection = db.collection("Blogs")
    blogs = blogs_collection.stream()
    blog_list = [blog.to_dict() for blog in blogs] # Memproses dan mengurutkan dokumen blog
    sorted_blogs = sorted(blog_list, key=lambda x: x['published'], reverse=True)  # Asumsi 'published' adalah timestamp
    return render_template('blog/blog.html', blogs=sorted_blogs)

# -----------------------------------------------------------------------------------------------------------------------------

# Route Projects
@app.route('/projects')
def project():
    projects_collection = db.collection("Projects")
    projects = projects_collection.stream()
    project_list = [projects.to_dict() for projects in projects]
    sorted_projects = sorted(project_list, key=lambda x: x['id'], reverse=True)
    return render_template('project/project.html', projects=sorted_projects)

# -----------------------------------------------------------------------------------------------------------------------------

# Route Learn
@app.route('/learn')
def learn():
    learns_collection = db.collection("Learn")
    learns = learns_collection.stream()
    learn_list = [learns.to_dict() for learns in learns]
    return render_template('learn/learn.html', learns=learn_list)

# -----------------------------------------------------------------------------------------------------------------------------

# Route About
@app.route('/about')
def about():
    return render_template('about/about.html')

# -----------------------------------------------------------------------------------------------------------------------------

# Route Contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        sender_email = request.form['email']
        message = request.form['message']

        # Membuat pesan email
        msg = Message(subject="New Message from Contact Form",
                        sender=(name, sender_email),
                        recipients=['muhammadrahim.mr196@gmail.com'],
                        body=f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}")
        
        try: # Mengirim email
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash('Cannot Send Message Now!', 'error')

        return redirect(url_for('contact'))
    
    return render_template('contact/contact.html')

# -----------------------------------------------------------------------------------------------------------------------------

# Route Dashboard
@app.route('/dashboard')
@cache.cached(timeout=60)
def dashboard():
    github_username = 'grimaimm'
    github_token = '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'
    tabs = build_tabs_structure()
    active_tab = request.args.get('tab', 'home')
    session['active_tab'] = active_tab
    contributions = get_contributions_from_github()
    contributions_last_year, weekly_contributions = get_github_contributions(github_username, github_token)
    return render_template('dashboard/dashboard.html', 
                            tabs=tabs, 
                            contributions=contributions, 
                            active_tab=active_tab, 
                            contributions_last_year=contributions_last_year, 
                            weekly_contributions=weekly_contributions)

# -----------------------------------------------------------------------------------------------------------------------------

# Route Blog Exploring the World of Programming
@app.route('/blog/exploring-the-world-of-programming')
def blogOne():
    blogs_collection = db.collection('Blogs').document('exploring-the-world-of-programming')
    blog_data = blogs_collection.get().to_dict()
    views_count = blog_data.get('views', 0) # Meningkatkan jumlah views
    views_count += 1
    blogs_collection.update({'views': views_count}) # Memperbarui nilai views di Firestore
    markdown_files = [
        'machine-language.md',
        'assembly-language.md',
        'mid-level-language.md',
        'high-level-language.md'
    ]
    html_contents = []
    for file_name in markdown_files: # Merender konten Markdown ke HTML menggunakan Mistune
        file_path = f'app/static/content/blog/one/{file_name}'
        with open(file_path, 'r') as file:
            markdown_content = file.read()
            html_content = mistune.markdown(markdown_content)
            html_contents.append(html_content)
    return render_template('blog/blog-One.html', 
                            blog_data = blog_data, 
                            views = views_count, 
                            html_contents = html_contents)

# Route Blog The 10 Best Programming Languages to Learn in 2024
@app.route('/blog/best-programming-languages-to-learn')
def blogTwo():
    blogs_collection = db.collection('Blogs').document('best-programming-languages-to-learn')
    blog_data = blogs_collection.get().to_dict()
    views_count = blog_data.get('views', 0) # Meningkatkan jumlah views
    views_count += 1
    blogs_collection.update({'views': views_count}) # Memperbarui nilai views di Firestore
    blog_ref = db.collection('Blogs').document('best-programming-languages-to-learn').collection('blog-contents') # Mengambil data dari Firestore
    blogs = blog_ref.stream()
    blog_contents = []
    for blog in blogs:
        blog_dict = blog.to_dict()
        number = int(blog.id.split('.')[0].strip()) # Mengambil nomor urut dari judul dokumen
        blog_dict['number'] = number  # Menambahkan nomor urut ke dalam data
        blog_contents.append(blog_dict)
    sorted_blogs = sorted(blog_contents, key=lambda x: x['number']) # Mengurutkan dokumen berdasarkan nomor urut
    return render_template('blog/blog-Two.html', blog_data=blog_data, views=views_count, blogs=sorted_blogs)

# -----------------------------------------------------------------------------------------------------------------------------

# Route Projects Grimaim Financial Dashboard
@app.route('/projects/grimaim-financial-dashboard')
def projectOne():
    project_ref = db.collection('Projects').document('1. grimaim-financial-dashboard')
    project_data = project_ref.get().to_dict()
    project_contents_ref = project_ref.collection('project-contents')
    project_contents_docs = project_contents_ref.stream()
    project_contents_data = []
    for doc in project_contents_docs:
        project_contents_data.append(doc.to_dict())
    return render_template('project/grimaim-financial-dashboard.html', project_data=project_data, project_contents_data=project_contents_data)

# Route Projects Grimaimcode.com
@app.route('/projects/grimaim-code-com')
def projectTwo():
    project_ref = db.collection('Projects').document('2. grimaimcode.com')
    project_data = project_ref.get().to_dict()
    project_contents_ref = project_ref.collection('project-contents')
    project_contents_docs = project_contents_ref.stream()
    project_contents_data = []
    for doc in project_contents_docs:
        project_contents_data.append(doc.to_dict())
    return render_template('project/grimaimcode-com.html', project_data=project_data, project_contents_data=project_contents_data)

# -----------------------------------------------------------------------------------------------------------------------------

# Route Learn Python Flask Framework
@app.route('/learn/python-flask-framework')
def python_flask_framework():
    doc_ref = db.collection('Learn').document('python-flask-framework')
    doc = doc_ref.get()
    lessons = []
    if doc.exists:
        data = doc.to_dict()
        if 'total_lessons' in data:
            total_lessons_map = data['total_lessons']
            sorted_lessons = sorted(total_lessons_map.items(), key=lambda x: int(x[0].split('-')[1]))
            # Iterasi semua lessons dan tambahkan ke dalam list
            for key, value in sorted_lessons:
                lesson_info = {
                    'title': value['title'].title(),
                    'routes': value['routes'].lower()
                }
                lessons.append(lesson_info)

    return render_template('learn/python-flask-framework.html', lessons=lessons)

@app.route('/learn/python-flask-framework/0-introduction')
def flaskZero():
    learn_ref = db.collection('Learn').document('python-flask-framework')
    learn_contents_ref = learn_ref.collection('lessons').document('0. Introduction')
    lesson_data = learn_contents_ref.get().to_dict() # Mengambil data dari dokumen
    return render_template('learn/python-flask-framework/py-lessons-0.html', lesson_data=lesson_data)

@app.route('/learn/python-flask-framework/1-install-flask')
def flaskOne():
    learn_ref = db.collection('Learn').document('python-flask-framework')
    learn_contents_ref = learn_ref.collection('lessons').document('1. Install Flask')
    lesson_data = learn_contents_ref.get().to_dict() # Mengambil data dari dokumen
    return render_template('learn/python-flask-framework/py-lessons-1.html', lesson_data=lesson_data)

@app.route('/learn/python-flask-framework/2-your-first-flask-application')
def flaskTwo():
    learn_ref = db.collection('Learn').document('python-flask-framework')
    learn_contents_ref = learn_ref.collection('lessons').document('2. Your First Flask Application')
    lesson_data = learn_contents_ref.get().to_dict() # Mengambil data dari dokumen
    markdown_files = ['1.md','2.md','3.md','4.md']
    html_contents = [
        mistune.markdown(open(f'app/static/content/learn/python-flask-framework/less2/{file_name}').read())
        for file_name in markdown_files
    ]
    return render_template('learn/python-flask-framework/py-lessons-2.html', lesson_data=lesson_data, html_contents=html_contents)

@app.route('/learn/python-flask-framework/3-routing-and-views')
def flaskThree():
    learn_ref = db.collection('Learn').document('python-flask-framework')
    lesson_data = learn_ref.get().to_dict() # Mengambil data dari dokumen
    markdown_files = ['1.md']
    html_contents = [
        mistune.markdown(open(f'app/static/content/learn/python-flask-framework/less3/{file_name}').read())
        for file_name in markdown_files
    ]
    return render_template('learn/python-flask-framework/py-lessons-3.html', lesson_data=lesson_data, html_contents=html_contents)

@app.route('/learn/python-flask-framework/4-templates')
def flaskFour():
    learn_ref = db.collection('Learn').document('python-flask-framework')
    lesson_data = learn_ref.get().to_dict() # Mengambil data dari dokumen
    markdown_files = ['1.md','2.md','3.md','4.md','5.md','6.md']
    html_contents = [
        mistune.markdown(open(f'app/static/content/learn/python-flask-framework/less4/{file_name}').read())
        for file_name in markdown_files
    ]
    return render_template('learn/python-flask-framework/py-lessons-4.html', lesson_data=lesson_data, html_contents=html_contents)

# -----------------------------------------------------------------------------------------------------------------------------