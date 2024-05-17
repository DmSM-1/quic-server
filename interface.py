import subprocess
from src.myjson import *
import json
from time import sleep

program = "client.py"
process = None

class Interface():
    def __init__(self):
        self.process = subprocess.Popen(
                ['python', program, "d", "d", "d"], 
                stdin=subprocess.PIPE, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True)

    def send_and_get(self,input_json):
        self.process.stdin.write(input_json.to_json().decode() + '\n')
        self.process.stdin.flush()
        output_data = self.process.stdout.readline().strip()
        print(output_data)
        output_json = Frame(data=output_data).from_json()
        return output_json
    
# inter = Interface()
# sig  = Sig(name='1', password='1')
# con = ControlFrame(chat_id=10, user_id= 3)
# print(inter.send_and_get(Sig(name='1', password='1')))
