import logging

from flask import request, render_template

from unblocker import app

@app.route('/')
def home():
    return "home"


@app.route('/incoming_call.xml', methods=['GET', 'POST'])
def incoming_call():
    """ Route that handles incoming calls
    """
    logging.debug(request.form)

    if request.form.get('Unblocked', False):
        # This was a withheld number - lets forward the call
        ctx = {
            'to': '+447449967482',
            'callerId': request.form.get('From'),
            'record': "true"
        }
        out = render_template('call_passthrough.xml', **ctx)
    else:
        out = render_template('call_reject.xml')
    logging.debug(out)
    return out
