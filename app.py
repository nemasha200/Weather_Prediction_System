from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# --------------------------
# Home Dashboard
# --------------------------
@app.route('/')
def home():
    return render_template('index.html')

# API: Weather for Dashboard
@app.route('/api/weather')
def weather_data():
    data = {
        "temperature": 28,
        "rainfall": 10,
        "humidity": 76,
        "wind_speed": 16,
        "forecast": {
            "days": ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"],
            "temperature": [20, 10, 21, 11, 16, 24, 17],
            "rainfall": [8, 7, 10, 7, 8, 6, 9]
        }
    }
    return jsonify(data)

# --------------------------
# Agriculture Tips Page
# --------------------------
@app.route('/agriculture-tips')
def agriculture_tips():
    return render_template('first.html')

# API: Tips for Agriculture Tips Page
@app.route('/api/tips')
def get_tips():
    data = {
        "weather": {
            "temperature": 28,
            "rainfall": 20,
            "humidity": 85,
            "wind_speed": 12,
            "forecast": {
                "days": ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"],
                "rainfall": [20, 25, 18, 10, 5, 12, 8],
                "temperature": [28, 27, 29, 30, 31, 29, 28]
            }
        },
        "crop": "Paddy",
        "recommendations": [
            "Heavy rain expected: delay irrigation to prevent waterlogging.",
            "High humidity may cause fungal diseases — inspect fields daily.",
            "Ideal time to apply nitrogen fertilizer after rain subsides.",
            "Prepare drainage channels to avoid crop damage."
        ]
    }
    return jsonify(data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # You can implement email sending or DB storage here
        print(f"Contact Form Submitted: Name={name}, Email={email}, Message={message}")
        
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html')


# --------------------------
# Business Planning Page
# --------------------------
@app.route('/business-planning')
def business_planning():
    return render_template('second.html')

# API: Business Data
@app.route('/api/business')
def get_business_data():
    data = {
        "weather": {
            "temperature": 28,
            "rainfall": 15,
            "humidity": 70,
            "wind_speed": 14,
            "forecast": {
                "days": ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"],
                "temperature": [28, 29, 27, 30, 31, 29, 28],
                "rainfall": [15, 12, 10, 8, 5, 7, 6]
            }
        },
        "recommendations": [
            "Expect moderate rain: stock up indoor goods.",
            "Plan deliveries in the morning to avoid afternoon showers.",
            "Increase marketing for rain gear and umbrellas.",
            "Monitor supply chains for possible delays due to weather."
        ]
    }
    return jsonify(data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/historical-trends')
def historical_trends():
    return render_template('history.html')

# API: Historical Data
@app.route('/api/historical')
def historical_data():
    region = request.args.get('region', 'Colombo')
    start_year = int(request.args.get('start', 2020))
    end_year = int(request.args.get('end', 2025))

    # Example dummy data (replace with DB query!)
    years = list(range(start_year, end_year + 1))
    temperature = [28 + i % 3 for i in range(len(years))]
    rainfall = [200 + i * 10 for i in range(len(years))]

    insights = f"In {region}, avg temperature ranged from {min(temperature)}°C to {max(temperature)}°C. Total rainfall trend is increasing."

    return jsonify({
        "years": years,
        "temperature": temperature,
        "rainfall": rainfall,
        "insights": insights
    })

# --------------------------
# Run the app
# --------------------------
if __name__ == '__main__':
    app.run(debug=True)
