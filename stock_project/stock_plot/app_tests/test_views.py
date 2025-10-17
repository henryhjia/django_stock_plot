from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
import pandas as pd

class StockPlotViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_index_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock_plot/index.html')

    @patch('stock_plot.views.yf.download')
    def test_index_post(self, mock_download):
        # Create a sample DataFrame to be returned by the mock
        data = {
            'Open': [100, 102, 101],
            'High': [103, 104, 102],
            'Low': [99, 101, 100],
            'Close': [102, 103, 101],
            'Adj Close': [102, 103, 101],
            'Volume': [1000, 1200, 1100]
        }
        df = pd.DataFrame(data, index=pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']))
        mock_download.return_value = df

        response = self.client.post(self.url, {
            'ticker': 'AAPL',
            'start_date': '2023-01-01',
            'end_date': '2023-01-03'
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn('plot_url', response.context)
        self.assertIn('min_price', response.context)
        self.assertIn('max_price', response.context)
        self.assertIn('mean_price', response.context)
        self.assertIn('data_table', response.context)
