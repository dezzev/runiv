# Модули


from flask import Flask, render_template, send_from_directory, Response, jsonify, redirect, request

import urllib

import random

import config

from peewee import *

# Модели

db = SqliteDatabase('runiv.db')

class Short(Model):
    url = CharField()
    short = CharField()

    class Meta:
        database = db


# Приложение

ip_to_use = ""

if config.localhost:
    ip_to_use = "127.0.0.1"
else:
    ip_to_use = config.ip

app = Flask(__name__, static_url_path="/lib", static_folder="lib")


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/link_gen", methods=['POST'])
def urlshort():
    geturl = request.form.get("url")

    print(geturl)

    genid = "".join(random.sample("abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ", random.randrange(4,6)))

    if Short.select().where(Short.url == geturl):
        return jsonify({"tourl": generate, "warn": "this url exists"})
    else:
        u = Short(url=geturl, short=genid)
        u.save()
        return jsonify({"tourl": genid})

@app.route("/<tourl>")
def redirecturl(tourl):
    print(tourl)
    potanceval = Short.select().where(Short.short == tourl)
    if potanceval:
        return redirect("http://" + potanceval.get().url, code="302")
    else:
        return redirect("/", code="302")


if __name__ == "__main__":
    app.run(host=ip_to_use, port=config.port)
