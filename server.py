from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)


@app.route('/')
def html_temp():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_dynamic(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database_plain.txt',mode='a') as database:
        email=data['name']
        subject=data['email']
        message=data['message']
        file=database.write(f'\n {email},{subject},{message}')

def write_to_file2(data):
    with open('database2.csv',mode='a',newline='') as database2:
        email=data['name']
        subject=data['email']
        message=data['message']
        csv_writter=csv.writer(database2,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email,subject,message])





@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
         data = request.form.to_dict()
         write_to_file(data)
         write_to_file2(data)
         return redirect('/Thankyou.html')
        except:
            return 'did not save to db'

    else:
        return 'Please try again'
