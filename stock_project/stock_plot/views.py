from django.shortcuts import render
import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import io
import urllib, base64
import pandas as pd
import numpy as np

def index(request):
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        try:
            data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)
            if data.empty:
                error = "No data found for the given ticker and date range."
                return render(request, 'stock_plot/index.html', {'error': error})

            close_prices = data['Close']
            min_price = np.min(close_prices)
            max_price = np.max(close_prices)
            mean_price = np.mean(close_prices)

            fig = plt.figure(figsize=(10, 6))
            plt.plot(data.index, close_prices, marker='o', markersize=4)
            plt.title(f'{ticker} Stock Price')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.grid(axis='both', linestyle='--', alpha=0.7)

            ax = plt.gca()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            fig.autofmt_xdate() # Auto-formats and rotates the date labels
            plt.xticks(rotation=90) # Force 90-degree rotation

            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = urllib.parse.quote(string)

            return render(request, 'stock_plot/index.html', {
                'plot_url': uri,
                'min_price': min_price,
                'max_price': max_price,
                'mean_price': mean_price,
                'data_table': data.sort_index(ascending=False).head(20).to_html(classes='table table-striped'),
            })
        except Exception as e:
            error = f"An error occurred: {e}"
            return render(request, 'stock_plot/index.html', {'error': error})

    return render(request, 'stock_plot/index.html')
