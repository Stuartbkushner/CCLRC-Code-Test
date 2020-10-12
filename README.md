
# CCLRC-Code-Test

This is a project takes the XML from the following streams, outputs the data in JSON format, and renders
the results to a front-end created with Python and Flask.

```
http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=109-02-088
```
```
http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=136-18-117
```
```
http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=109-21-100
```
```
http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=672-06-054
```
```
http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=673-12-062
```

## Installing / Getting started

1. Clone the repo

```shell
git clone https://github.com/Stuartbkushner/CCLRC-Code-Test
cd CCLRC-Code-Test
```
2. Initialize and activate a virtualenv:
```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

3. Install the dependencies:
```
$ pip install -r requirements.txt
```

5. Run the development server:
```
$ python app.py
```

6. Navigate to [http://localhost:5000](http://localhost:5000)

## Licensing

One really important part: Give your project a proper license. Here you should
state what the license is and how to find the text version of the license.
Something like:

"The code in this project is licensed under MIT license."

