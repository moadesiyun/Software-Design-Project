profiles = []
class User( UserMixin):
    id = primary_key=True
    email = ""
    password = ""
    first_name = ""
    
class Client:
    
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.profile_info = {
            "first_name": "",
            "last_name": "",
            "address_1": "",
            "address_2": "",
            "city": "",
            "state": "",
            "zip_code": "",
        }
    
        self.quote_history = []
        profiles.append(self)
        
    def update_profile_info(self, fname, lname, address_1, address_2, city, state, zip_code):
        self.profile_info = {
            "first_name": fname,
            "last_name": lname,
            "address_1": address_1,
            "address_2": address_2,
            "city": city,
            "state": state,
            "zip_code": zip_code,
        }
        
    def update_quote_history(self, quote_info):
        self.quote_history.append(quote_info)

