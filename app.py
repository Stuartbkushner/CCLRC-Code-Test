import json
import pprint
import xmltodict
from urllib.request import urlopen
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/house1')
def house1():
  with urlopen("http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=109-02-088") as url:
    http_info = url.info()
    raw_data = url.read().decode(http_info.get_content_charset())
    raw_data = "".join(raw_data.split()).replace("<?xmlversion='1.0'?>", "<?xml version='1.0'?>")
    parsed_xml_object = xmltodict.parse(raw_data)
    json_result = json.dumps(parsed_xml_object)
    loaded_json = json.loads(json_result)
    return render_template('house1.html', raw_data=loaded_json)


@app.route('/house2')
def house2():
  with urlopen("http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=136-18-117") as url:
    http_info = url.info()
    raw_data = url.read().decode(http_info.get_content_charset())
    raw_data = "".join(raw_data.split()).replace("<?xmlversion='1.0'?>", "<?xml version='1.0'?>")
    parsed_xml_object = xmltodict.parse(raw_data)
    json_result = json.dumps(parsed_xml_object)
    loaded_json = json.loads(json_result)
    return render_template('house2.html', raw_data=loaded_json)

@app.route('/house3')
def house3():
  with urlopen("http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=109-21-100") as url:
    http_info = url.info()
    raw_data = url.read().decode(http_info.get_content_charset())
    raw_data = "".join(raw_data.split()).replace("<?xmlversion='1.0'?>", "<?xml version='1.0'?>")
    parsed_xml_object = xmltodict.parse(raw_data)
    json_result = json.dumps(parsed_xml_object)
    loaded_json = json.loads(json_result)
    return render_template('house3.html', raw_data=loaded_json)

@app.route('/house4')
def house4():
  with urlopen("http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=672-06-054") as url:
    http_info = url.info()
    raw_data = url.read().decode(http_info.get_content_charset())
    raw_data = "".join(raw_data.split()).replace("<?xmlversion='1.0'?>", "<?xml version='1.0'?>")
    parsed_xml_object = xmltodict.parse(raw_data)
    json_result = json.dumps(parsed_xml_object)
    loaded_json = json.loads(json_result)
    return render_template('house4.html', raw_data=loaded_json)

@app.route('/house5')
def house5():
  with urlopen("http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=673-12-062") as url:
    http_info = url.info()
    raw_data = url.read().decode(http_info.get_content_charset())
    raw_data = "".join(raw_data.split()).replace("<?xmlversion='1.0'?>", "<?xml version='1.0'?>")
    parsed_xml_object = xmltodict.parse(raw_data)
    json_result = json.dumps(parsed_xml_object)
    loaded_json = json.loads(json_result)
    return render_template('house5.html', raw_data=loaded_json)


if __name__ == '__main__':
  app.run(debug=True)
