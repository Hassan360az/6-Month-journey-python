class District():
    def watch_camera(self, user_name , user_id):
        self.user_name = user_name
        self.user_id = user_id

        if user_name == "Ali" and user_id == 7656:
            print("Access Granted!")
        else:
            print("name or id is wrong")

Lahore = District()

Lahore.watch_camera("Ali", 7656) 

