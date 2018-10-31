# Модули


from flask import Flask, render_template, send_from_directory, Response, jsonify, redirect

import urllib

import random

import config


# Приложение

ip_to_use = ""

if config.localhost == True:
    ip_to_use = "127.0.0.1"
else:
    ip_to_use = config.ip

app = Flask(__name__, static_url_path="/lib", static_folder="lib")


@app.route("/")

def main_page():
    return render_template("index.html")


@app.route("/link_gen/<path:geturl>")

def urlshort(geturl):
    
    geturl = urllib.parse.unquote(geturl).replace("https%3a//", "").replace("https://","").replace("http://","").replace("http%3a//","")
    
    print(geturl)
    
    generate = ""
    
    urlread = open("links.txt", "r")
    
    readurl = urlread.read()
    
    urlread.close()
    
    arurl = readurl.split("\n")
    
    for strokes in arurl:
        if len(strokes.split(","))>0:
            if strokes.split(",")[0]=="url:" + geturl:
                generate = strokes.split(",")[1].replace("short:","")
                return jsonify({"tourl":generate,"warn":"this url exists"})
            
    if generate == "":
        writeurl = open("links.txt","w")
        genid = "".join(random.sample("abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ", random.randrange(4,6)))
        writeurl.write(readurl+"url:" + urllib.parse.unquote(geturl) + ",short:" + genid + "\n")
        writeurl.close()
        return jsonify({"tourl":genid})
        
    
@app.route("/<tourl>")

def redirecturl(tourl):
    
    broughtto = ""
    
    urlread = open("links.txt", "r")
    
    readurl = urlread.read()
    
    urlread.close()
    
    arurl=readurl.split("\n")
    
    for strokes in arurl:
        if len(strokes.split(","))>0:
            if strokes.split(",")[1]=="short:" + urllib.parse.quote(tourl):
                broughtto = strokes.split(",")[0].replace("url:","")
                return redirect("http://" + broughtto, code="302")
            
    if broughtto == "":
        return redirect("/", code="302")


if __name__ == "__main__":
    app.run(host=ip_to_use, port=config.port)

