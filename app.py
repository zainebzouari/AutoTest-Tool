import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from automative import connect_db, get_vehicle_data
from metadata import metadata
from test_automative import test_vehicle_attributes

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return connect_db()

@app.route('/')
def index():
    return render_template('index.html')


USERNAME = os.getenv('APP_USERNAME', 'primatec')
PASSWORD = os.getenv('APP_PASSWORD', 'changeme')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('test'))
        else:
            error = "Invalid username or password. Please try again."

    return render_template('login.html', error=error)

@app.route('/test', methods=['GET', 'POST'])
def test():
    vehicle_data = None
    test_results = []
    message = None

    if request.method == 'POST':
        vehicle_id = request.form.get('vehicle_id')

        if vehicle_id:
            db_connection = connect_db()
            vehicle_data = get_vehicle_data(db_connection, vehicle_id)
            db_connection.close()

            if vehicle_data:
                selected_tables = request.form.getlist('fields')
                if selected_tables:
                    for table in selected_tables:
                        try:
                            test_vehicle_attributes(vehicle_data, table)
                            test_results.append({
                                'table': table,
                                'result': 'Pass',
                                'error_messages': []
                            })
                        except AssertionError as e:
                            test_results.append({
                                'table': table,
                                'result': 'Fail',
                                'error_messages': str(e).split('\n')
                            })
                    return render_template('results.html', 
                                           vehicle_id=vehicle_id, 
                                           selected_tables=selected_tables, 
                                           test_results=test_results)
                else:
                    message = "Please select fields to test."
            else:
               
                message = "No vehicle found with the provided ID."
        else:
            message = "Please enter a vehicle ID."

    return render_template('test.html', metadata=metadata, vehicle_data=vehicle_data, message=message)


if __name__ == '__main__':
    app.run(debug=True)





