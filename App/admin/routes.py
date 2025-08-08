from flask import Blueprint, request, redirect, url_for, render_template, current_app
from . import admin

@admin.route('/', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        current_app.posts.append({'title': title, 'content': content})
        return redirect(url_for('main.index'))
    return render_template('admin.html')