import base64
from io import BytesIO
from flask import Flask, render_template
from matplotlib.figure import Figure
import sqlite3

conn=sqlite3.connect('Data.db', check_same_thread=False)
curs=conn.cursor()

app = Flask(__name__)

def getHistData (numSamples):
	curs.execute("SELECT * FROM Solpanel ORDER BY Date DESC LIMIT "+str(numSamples))
	data = curs.fetchall()
	dates = []
	temps = []
	for row in reversed(data):
		dates.append(row[1])
		temps.append(row[2])
	return dates, temps

def plotTemp():
    times, temps = getHistData(15)
    # Generate the figure **without using pyplot**.
    print("times :",times)
    ys = temps
    xs = times
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3) 
    ax.tick_params(axis="x", which="both", rotation=30)
    ax = fig.subplots()
    ax.set_facecolor("#F5F5DC") # inner plot background color HTML black
    fig.patch.set_facecolor('#000') # outer plot background color HTML black
    ax.plot(xs, ys, linestyle = 'dashed', c = '#00ff00', linewidth = '1.5',
     marker = 'o', mec = 'blue', ms = 10, mfc = 'blue' )
    ax.set_xlabel('X-axis ')
    ax.set_ylabel('Y-axis ')
    ax.xaxis.label.set_color('blue') #setting up X-axis label color to hotpink
    ax.yaxis.label.set_color('blue') #setting up Y-axis label color to hotpink
    ax.tick_params(axis='x', colors='white') #setting up X-axis tick color to white
    ax.tick_params(axis='y', colors='white') #setting up Y-axis tick color to white
    ax.spines['left'].set_color('green') # setting up Y-axis tick color to blue
    ax.spines['top'].set_color('green') #setting up above X-axis tick color to blue
    ax.spines['bottom'].set_color('green') #setting up above X-axis tick color to blue
    ax.spines['right'].set_color('green') #setting up above X-axis tick color to blue
    fig.subplots_adjust(bottom=0.3) 
    ax.tick_params(axis="x", which="both", rotation=30) 
   
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    #print(data)
    return data

@app.route("/")
def home():
    temp = plotTemp() 
    return render_template('index.html', temp = temp)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
169.254.143.4169.254.143.4169.254.143.4169.254.143.4169.254.143.4169.254.143.4169.254.143.4169.254.143.4169.254.143.4
