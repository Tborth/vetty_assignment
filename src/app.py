from flask import Flask, send_file,render_template




# from route import *
# app.register_blueprint(form_blueprint)
app = Flask(__name__)
import codecs

@app.route('/')
def index():
    try:
        with codecs.open(f"static/files/file1.txt", 'r', encoding="ascii",
                    errors='ignore') as fdata:
            data1=f1.read().split("\n")
            return render_template('index.html',data=data1 ).encode( "utf-8" )
    except Exception as e:
        print(e)
 
    
@app.route('/<filename>')
def filename(filename):
    try:
        with codecs.open("static/files/"+filename, "r", encoding='utf-8',
                    errors='ignore') as fdata:
            data1=fdata.read().split("\n")
            return data1 
    except Exception as e:
        return e
@app.route('/<filename>/<int:startindex>/<int:lastindex>')
def filename_filter(filename,startindex,lastindex):
    try:
        with codecs.open("static/files/"+filename, "r", encoding='utf-8',
                    errors='ignore') as fdata:
            data1=fdata.read().split("\n")
            data1=data1[startindex:lastindex]
            return data1 
    except Exception as e:
        return e
        
        
        
    with open("static/files/"+filename, "r") as f1:
        # print(my_file.read())
        
        data1=f1.read().split("\n")
        return render_template('index.html',data=data1 )
    # f2 = open("static/files/file2.txt", "r")
    # data2=f2.read().split("\n")
    # f3 = open("static/files/file3.txt", "r")
    # data3=f3.read().split("\n")
    # f4 = open("static/files/file4.txt", "r")
    # data4=f4.read().split("\n")
    # return render_template('index.html',data=data1 )

if __name__ == '__main__':
    app.run(debug=True)

