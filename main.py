from flask import Flask, redirect, url_for, request, render_template
from montecarlo import montecarlo
from stockdata import getStockData, getCurrentPrice
import pandas as pd
import plotly.express as px
from jinja2 import Template


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def home():
    return redirect('/montecarlo')

@app.route('/montecarlo')
def montecarlopage():
    company = 'MSFT'
    data = getStockData(company)
    df = montecarlo()
    
    output_html_path=r"templates/montecarlo.html"
    input_template_path = r"templates/montecarlotemplate.html"
    fig = px.line(df, x='Date', y='Averaged Stock Price', title="Monte Carlo Simulation") 
    fig.update_layout(title_x=0.5, font_color="Black", font_family="Sans Serif")

    plotly_jinja_data=fig.to_html(full_html=False)
    currentprice=getCurrentPrice(company)

    with open(output_html_path, "w", encoding="utf-8") as output_file:
        with open(input_template_path) as template_file:
            j2_template = Template(template_file.read())
            output_file.write(j2_template.render(brand=company, currentstockprice=currentprice, fig=plotly_jinja_data))
            # output_file.write(j2_template.render(plotly_jinja_data))
            
    return render_template('montecarlo.html')


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)