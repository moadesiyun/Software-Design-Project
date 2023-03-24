from flask_login import UserMixin
profiles = []
count=3
class User():
    def __init__(self, id, username, active=True):
        self.id = id
        self.username = username
        self.active = active

    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        # return self.active
        # for demo i just return True
        return True 
    
    def is_authenticated(self):
        # for demo i just return True
        return True

    def get_id(self):
        # if you do not use Usermixin, this is important
        # user_loader load_user(id) uses this get_id attribute to load the id
        return self.id
    
class Client:
    
    
    def __init__(self, username, password, logintime):
        self.username = username
        self.password = password
        self.logintime = logintime
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

