from flask import Flask, escape, request, jsonify
from ncclient import manager
import json
from xml.etree.ElementTree import fromstring
from flask_cors import CORS

import xmltodict

connection = manager.connect(
    host='127.0.0.1',
    port=17830,
    hostkey_verify=False
)

netconf_config = open("config-ietf-interfaces.xml").read()
netconf_payload = netconf_config.format(
    int_name="Berk",
    int_desc="a",
    ip_address="0.0.0.0",
    subnet_mask="255.255.255.255"
)
netconf_reply = connection.edit_config(netconf_payload, target="running")

app = Flask(__name__)
CORS(app)

@app.route('/connect')
def connect():
    global connection
    connection = manager.connect(
        host='127.0.0.1',
        port=17830,
        hostkey_verify=False
    )

    netconf_config = open("config-ietf-interfaces.xml").read()
    netconf_payload = netconf_config.format(
        int_name="Berk",
        int_desc="a",
        ip_address="0.0.0.0",
        subnet_mask="255.255.255.255"
    )
    netconf_reply = connection.edit_config(netconf_payload, target="running")
    return connection.get_config(source="running").xml


@app.route('/config', methods=["GET", "POST", "DELETE"])
def config():

    if request.method == "GET" :
        return connection.get_config(source="running").xml

    if request.method == "POST" :
        json = request.get_json(silent=True)
        xml = json.get('data')
        connection.edit_config(f'<config> {xml} </config>')
        return connection.get_config(source="running").xml


@app.route('/lock')
def lock():
    connection.lock(target="running")
    response = app.response_class(
        response='OK',
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/unlock')
def unlock():
    connection.unlock(target="running")
    response = app.response_class(
        response='OK',
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/close')
def close():
    connection.close_session()
    response = app.response_class(
        response='OK',
        status=200,
        mimetype='application/json'
    )
    return response
