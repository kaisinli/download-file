"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, make_response
from forms import DelayForm
from datetime import datetime
from models import Download
import csv
# import sqlite3

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/download', methods=['POST'])
def download_file():
    download_form = DelayForm()

    if request.method == 'POST':
        if download_form.validate_on_submit():
            # Get validated data from form
            delay_time = download_form.delay_time.data

            # save now record to database
            new_record = Download('name', 'email', delay_time)
            db.session.add(new_record)
            db.session.commit()

            csv = 'foo,bar,baz\nhai,bai,crai\n'
            response = make_response(csv)
            cd = 'attachment; filename=mycsv.csv'
            response.headers['Content-Disposition'] = cd
            response.mimetype = 'text/csv'

            render_template('home.html')
            return response

    flash_errors(download_form)
    return render_template('home.html', form=download_form)

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
