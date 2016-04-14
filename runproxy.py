from flask import Flask, request
app = Flask(__name__)

@app.route("/run")
def proxy():
    filename = request.args.get('filename')
    if filename is None:
      filename = "./demo.py"
    variables = {}
    filename_arr = filename.split(';')
    #print filename_arr[0]
    for item in filename_arr:
    	if item is not None and item != "":
    		execfile(item)
    	#print item
    return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)