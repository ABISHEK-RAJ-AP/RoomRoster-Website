from flask import Flask, render_template, request, send_file
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def allocate_rooms(group_df, hostel_df):
    # Placeholder for room allocation logic
    # Modify this according to your actual allocation logic
    # For example: merging dataframes, calculating room allocation, etc.
    return group_df, hostel_df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        group_file = request.files['group_file']
        hostel_file = request.files['hostel_file']

        if group_file and hostel_file:
            group_filename = os.path.join(app.config['UPLOAD_FOLDER'], group_file.filename)
            hostel_filename = os.path.join(app.config['UPLOAD_FOLDER'], hostel_file.filename)

            group_file.save(group_filename)
            hostel_file.save(hostel_filename)

            # Load CSV files into DataFrames
            group_df = pd.read_csv(group_filename)
            hostel_df = pd.read_csv(hostel_filename)

            # Allocate rooms (dummy example function)
            group_df, hostel_df = allocate_rooms(group_df, hostel_df)

            # Prepare HTML table for rendering
            tables = hostel_df.to_html(classes='data', index=False)

            return render_template('index.html', tables=tables)

    return render_template('index.html')

@app.route('/download')
def download_file():
    allocations_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'allocations.csv')
    return send_file(allocations_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
