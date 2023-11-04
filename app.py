from flask import Flask, render_template, request
from predict import predict_parkinsons  # Import the predict function from predict.py

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render your HTML template

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        # Get user inputs from the form
        number = float(request.form['number'])
        no_strokes_st = float(request.form['no_strokes_st'])
        no_strokes_dy = float(request.form['no_strokes_dy'])
        speed_st = float(request.form['speed_st'])
        speed_dy = float(request.form['speed_dy'])
        magnitude_vel_st = float(request.form['magnitude_vel_st'])
        magnitude_horz_vel_st = float(request.form['magnitude_horz_vel_st'])
        magnitude_vert_vel_st = float(request.form['magnitude_vert_vel_st'])
        magnitude_vel_dy = float(request.form['magnitude_vel_dy'])
        magnitude_horz_vel_dy = float(request.form['magnitude_horz_vel_dy'])
        magnitude_vert_vel_dy = float(request.form['magnitude_vert_vel_dy'])
        magnitude_acc_st = float(request.form['magnitude_acc_st'])
        magnitude_horz_acc_st = float(request.form['magnitude_horz_acc_st'])
        magnitude_vert_acc_st = float(request.form['magnitude_vert_acc_st'])
        magnitude_acc_dy = float(request.form['magnitude_acc_dy'])
        magnitude_horz_acc_dy = float(request.form['magnitude_horz_acc_dy'])
        magnitude_vert_acc_dy = float(request.form['magnitude_vert_acc_dy'])
        magnitude_jerk_st = float(request.form['magnitude_jerk_st'])
        magnitude_horz_jerk_st = float(request.form['magnitude_horz_jerk_st'])
        magnitude_vert_jerk_st = float(request.form['magnitude_vert_jerk_st'])
        magnitude_jerk_dy = float(request.form['magnitude_jerk_dy'])
        magnitude_horz_jerk_dy = float(request.form['magnitude_horz_jerk_dy'])
        magnitude_vert_jerk_dy = float(request.form['magnitude_vert_jerk_dy'])
        ncv_st = float(request.form['ncv_st'])
        ncv_dy = float(request.form['ncv_dy'])
        nca_st = float(request.form['nca_st'])
        nca_dy = float(request.form['nca_dy'])
        in_air_stcp = float(request.form['in_air_stcp'])
        on_surface_st = float(request.form['on_surface_st'])
        on_surface_dy = float(request.form['on_surface_dy'])

        # Create a feature list
        features = [
            number,no_strokes_st, no_strokes_dy, speed_st, speed_dy, magnitude_vel_st,
            magnitude_horz_vel_st, magnitude_vert_vel_st, magnitude_vel_dy,
            magnitude_horz_vel_dy, magnitude_vert_vel_dy, magnitude_acc_st,
            magnitude_horz_acc_st, magnitude_vert_acc_st, magnitude_acc_dy,
            magnitude_horz_acc_dy, magnitude_vert_acc_dy, magnitude_jerk_st,
            magnitude_horz_jerk_st, magnitude_vert_jerk_st, magnitude_jerk_dy,
            magnitude_horz_jerk_dy, magnitude_vert_jerk_dy, ncv_st, ncv_dy,
            nca_st, nca_dy, in_air_stcp, on_surface_st, on_surface_dy
        ]

        # Call the prediction function
        prediction_result = predict_parkinsons(features)

        if prediction_result == 1:
            result = "PERSON HAS BEEN DIAGNOSED WITH PARKINSON'S DISEASE"
        else:
            result = "PERSON IS SAFE FROM PARKINSON'S DISEASE"

        return render_template('result.html', prediction=result)  # Render the result in an HTML template

if __name__ == '__main__':
    app.run(debug=True)
