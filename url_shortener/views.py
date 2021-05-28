from flask import Blueprint, render_template, redirect,request
from .models import Link


short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.objects(short=short_url).first_or_404()
    if link is not None:
        print(f'this is link:{link.visits}')
        link.visits+=1
        link.save()
        return redirect(link.url)
    

@short.route('/add_link',methods=['GET', 'POST'])

def add_link():
    original_url = request.form['original_url']
    link = Link(url=original_url)
    link.save()
    return render_template('link_added.html', 
        new_link=link.short, original_url=link.url)
@short.route('/')
def index():
    return render_template('index.html') 

@short.route('/stats')
def stats():
    links = Link.objects.all()
    return render_template('stauts.html', links=links)

@short.errorhandler(404)
def page_not_found(e):
    return 'link not found',404