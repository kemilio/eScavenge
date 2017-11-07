import int_user

class Team(int_user.User):
    def __init__(self,username,password):
        self.username = username
        self.password = password
        #self.current_landmark = 0;
    def set_team_username(self,new_username):
        self.username = new_username
        return "Team username changed to " + new_username
    def set_team_password(self,new_password):
        self.password = new_password
        return "Team password changed to " + new_password
    def login(self,database,username,password):
        if database.get_current_user() != None:
            return False
        if username == self.username and password == self.password:
            database.set_current_user(self)
            return True
        return False
    def logout(self,database):
        if database.get_current_user() != self:
            return False
        database.set_current_user(None)
        return True
    def display_menu(self):
        return "Which would you like to do?\nlog out\ndisplay status"