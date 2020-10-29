from flask import Flask, send_from_directory, abort, render_template, request, jsonify

app = Flask(__name__, template_folder="C:/Users/jason/Desktop/personal_webpage/html") # __name__

# Test page without using html
@app.route("/test") #Url address http://127.0.0.1:8090/test
def test():
    return "test"

# Homepage display by using html file
@app.route("/") #Url address
def home():
    return render_template("Homepage.html")

# Image
app.config["image"] = "C:/Users/jason/Desktop/personal_webpage/image" #Path of file

@app.route("/get_image/<image_name>") # http://127.0.0.1:8090/get_image/xxx.jpg, can hyperlink this in html
def get_image(image_name):
    try:
        return send_from_directory(app.config["image"], filename=image_name, as_attachment=False) # When attachment is True, will download directly
    except FileNotFoundError: # If file not found give 404 error
        abort(404)


# Pdf
app.config["pdf"] = "C:/Users/jason/Desktop/personal_webpage/pdf" #Path of file

@app.route("/get_pdf/<pdf_name>") # http://127.0.0.1:8090/get_pdf/xxx.pdf, can hyperlink this in html
def get_pdf(pdf_name):
    try:
        return send_from_directory(app.config["pdf"], filename=pdf_name, as_attachment=False) # When attachment is True, will download directly
    except FileNotFoundError: # If file not found give 404 error
        abort(404)



if __name__=="__main__":
    app.run(host="127.0.0.1", port=8090)
    
