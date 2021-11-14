from flask import Blueprint, redirect, render_template, request, url_for

bp = Blueprint('clt_main', __name__, url_prefix="/")


@bp.route('/', methods=('GET','POST'))
def index():
    if request.method == 'POST':
        num_draws = request.form["draws"]
        num_samples = request.form["samples"]
        #num_draws = 25
        #num_samples = 25
        return render_template('clt_main/index.html', draws=num_draws, samples=num_samples)

    num_draws = 'Not Given'
    num_samples = 'Not Given '

    return render_template('clt_main/index.html', draws=num_draws, samples=num_samples)
