from flask import Flask, redirect, url_for, request, render_template
from montecarlo import MontecarloAlgo
from stockdata import getCurrentPrice, getURL

import pandas as pd
import plotly.express as px

from jinja2 import Template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        company = request.form['company']
        return redirect(url_for('montecarlopage', company=company))
    else:
        return render_template('home.html')

@app.route('/montecarlo', methods=['GET','POST'])
def montecarlopage():
    company = request.args.get('company', None)

    montecarlo =  MontecarloAlgo(company=company)
    df = montecarlo._dataframe()
    
    output_html_path=r"templates/montecarlo.html"
    input_template_path = r"templates/montecarlotemplate.html"
    fig = px.line(df, x='Date', y='Averaged Stock Price', title="Monte Carlo Simulation") 
    fig.update_layout(title_x=0.5, font_color="Black", font_family="Sans Serif")

    plotly_jinja_data=fig.to_html(full_html=False)
    currentprice=getCurrentPrice(company)
    formatcurrentprice = f"${currentprice:.2f}"
    rawminimum = df.min(axis=0)[1]
    minimum = f"{rawminimum:.2f}"

    rawmaximum = df.max(axis=0)[1]
    maximum = f"{rawmaximum:.2f}"

    corresmindate=df.loc[df['Averaged Stock Price']==rawminimum, 'Date'].values[0]
    corresmaxdate=df.loc[df['Averaged Stock Price']==rawmaximum, 'Date'].values[0]
 
    mean = montecarlo.cumulative_mean()
    standev = montecarlo.standard_deviation()


    with open(output_html_path, "w", encoding="utf-8") as output_file:
        with open(input_template_path) as template_file:
            j2_template = Template(template_file.read())
            output_file.write(j2_template.render(
                brand=company, 
                currentstockprice=formatcurrentprice,
                fig=plotly_jinja_data, 
                minprice=minimum, 
                mindate=corresmindate, 
                maxprice=maximum, 
                maxdate=corresmaxdate,
                mean=mean, 
                standev=standev
            ))
            
    return render_template('montecarlo.html')


if __name__ == '__main__':
    app.run(debug=True)
