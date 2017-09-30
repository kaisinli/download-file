from app import app, db
from flask import render_template, request, redirect, url_for, flash, stream_with_context
from models import Download
from werkzeug.datastructures import Headers
from werkzeug.wrappers import Response
from io import StringIO
from forms import DelayForm
import time
import csv

# Routes
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/records')
def report():
    records = db.session.query(Download).all() 
    return render_template('report.html', records=records)

@app.route('/download', methods=['POST', 'GET'])
def download_file():
    download_form = DelayForm()

    if request.method == 'POST':
        if download_form.validate_on_submit():
            # Get validated data from form
            delay = int(download_form.delay.data)
            client_ip = request.remote_addr

            time.sleep(delay)

            # save user to database
            record = Download(client_ip, "placeholder", delay)
            db.session.add(record)
            db.session.commit()

            return redirect(url_for('report'))

    flash_errors(download_form)
    return render_template('download.html', form=download_form)

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
