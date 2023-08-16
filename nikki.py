from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return 'Happy Independence Day'

@FAI.route('/first')
def first():
    return render_template('first.html',name='nikhitha',age=24)

FAI.run(debug=True)