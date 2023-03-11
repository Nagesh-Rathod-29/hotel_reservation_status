from flask import Flask,jsonify,render_template,request
import config
from utils import ReservationClass
import traceback


app = Flask(__name__)
@app.route('/')
def home():
    #print("This is Home Page")
    #return jsonify({"Result":"This is home page"})
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def outcome():
    try:
        if request.method == 'GET':
            data = request.args.get

            print("Data:::",data)

            adults = eval(data('no_of_adults'))
            children = eval(data('no_of_children'))
            weekend_nights = eval(data('no_of_weekend_nights'))
            week_nights = eval(data('no_of_week_nights'))
            meal_plan = data('type_of_meal_plan')
            car_parking_space = eval(data('required_car_parking_space'))
            room_type = data('room_type_reserved')
            time = eval(data('lead_time'))
            year = eval(data('arrival_year'))
            month = eval(data('arrival_month'))
            date = eval(data('arrival_date'))
            segment_type = data('market_segment_type')
            repeated = eval(data('repeated_guest'))
            previous_cancellations = eval(data('no_of_previous_cancellations'))
            previous_bookings_not_canceled = eval(data('no_of_previous_bookings_not_canceled'))
            avg_price = eval(data('avg_price_per_room'))
            special_requests = eval(data('no_of_special_requests'))

            test = ReservationClass()
            
            prediction = test.result(adults,
                                    children,
                                    weekend_nights,
                                    week_nights,
                                    meal_plan,
                                    car_parking_space,
                                    room_type,
                                    time,
                                    year,
                                    month,
                                    date,
                                    segment_type,
                                    repeated,
                                    previous_cancellations,
                                    previous_bookings_not_canceled,
                                    avg_price,
                                    special_requests)

            result = ''

            if prediction[0] == 1:
                result = 'Confirmed'
            else:
                result = 'Not Confirmed'
            #print(f"Your hotel reservation status is {result}")
            #return jsonify({"Result":f"Your hotel reservation status is {result}"})
            return render_template('index.html',predict=result)
        else:
            data = request.form.get

            print("Data:::",data)

            adults = eval(data('no_of_adults'))
            children = eval(data('no_of_children'))
            weekend_nights = eval(data('no_of_weekend_nights'))
            week_nights = eval(data('no_of_week_nights'))
            meal_plan = data('type_of_meal_plan')
            car_parking_space = eval(data('required_car_parking_space'))
            room_type = data('room_type_reserved')
            time = eval(data('lead_time'))
            year = eval(data('arrival_year'))
            month = eval(data('arrival_month'))
            date = eval(data('arrival_date'))
            segment_type = data('market_segment_type')
            repeated = eval(data('repeated_guest'))
            previous_cancellations = eval(data('no_of_previous_cancellations'))
            previous_bookings_not_canceled = eval(data('no_of_previous_bookings_not_canceled'))
            avg_price = eval(data('avg_price_per_room'))
            special_requests = eval(data('no_of_special_requests'))

            test = ReservationClass()
            
            prediction = test.result(adults,
                                    children,
                                    weekend_nights,
                                    week_nights,
                                    meal_plan,
                                    car_parking_space,
                                    room_type,
                                    time,
                                    year,
                                    month,
                                    date,
                                    segment_type,
                                    repeated,
                                    previous_cancellations,
                                    previous_bookings_not_canceled,
                                    avg_price,
                                    special_requests)
            result = ''

            if prediction[0] == 1:
                result = 'Confirmed'
            else:
                result = 'Not Confirmed'

            #print(f"Your hotel reservation status is {result}")
            #return jsonify({"Result":f"Your hotel reservation status is {result}"})
            return render_template('index.html',predict=result)
    except:
        print("Error is ",traceback.print_exc())

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=config.PORT,debug=True)
