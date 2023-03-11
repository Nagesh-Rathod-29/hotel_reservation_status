import numpy as np
import pickle
import json
import config
import artifacts
class ReservationClass():

    def __init__(self):
        #print("This is init method of Resevation class")

        with open(r"artifacts//model.pkl",'rb') as file:
            self.model = pickle.load(file)

        
        with open(r"artifacts//scaler.pkl",'rb') as file:
            self.scaler = pickle.load(file)

       
        with open(r"artifacts//model_data.json",'r') as file:
            self.model_data = json.load(file)

    def result(self,no_of_adults,
                no_of_children,
                no_of_weekend_nights,
                no_of_week_nights,
                type_of_meal_plan,
                required_car_parking_space,
                room_type_reserved,
                lead_time,
                arrival_year,
                arrival_month,
                arrival_date,
                market_segment_type,
                repeated_guest,
                no_of_previous_cancellations,
                no_of_previous_bookings_not_canceled,
                avg_price_per_room,
                no_of_special_requests,):

        test_array = np.zeros(self.model.n_features_in_)

        test_array[0] = no_of_adults
        test_array[1] = no_of_children
        test_array[2] = no_of_weekend_nights
        test_array[3] = no_of_week_nights
        test_array[4] = self.model_data['type_of_meal_plan'][type_of_meal_plan]
        test_array[5] = required_car_parking_space
        test_array[6] = self.model_data['room_type_reserved'][room_type_reserved]
        test_array[7] = lead_time
        test_array[8] = arrival_year
        test_array[9] = arrival_month
        test_array[10] = arrival_date
        test_array[11] = repeated_guest
        test_array[12] = no_of_previous_cancellations
        test_array[13] = no_of_previous_bookings_not_canceled
        test_array[14] = avg_price_per_room
        test_array[15] = no_of_special_requests

        ind = self.model_data['features'].index('market_segment_type_'+market_segment_type)
        test_array[ind] = 1


        scaled_array = self.scaler.transform([test_array])

        output = self.model.predict(scaled_array)

        
        #print(f"Your hotel reservation status is {output}")

        return output
#if __name__ == "__main__":
#    test = ReservationClass()
#    test.result(2,0,1,1,'Not Selected',0,'Room_Type 3',48,2018,4,11,'Corporate',0,0,0,94.5,0)



