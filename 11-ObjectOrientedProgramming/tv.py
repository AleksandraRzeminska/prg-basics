# tv.py file
# class definition
class TV:
   def __init__(self,channel_no):
      self.is_on = False
      self.channel_no = channel_no 
   def turn_off(self):
      self.is_on =False
   def turn_on(self):
      self.is_on= True
   #def set_channel(new_channel_no):
   def show_status(self):
        if self.is_on:
            print(f"TV is on channel", self.channel_no)
        else:
            print("TV is off")


