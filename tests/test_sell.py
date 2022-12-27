from console_app_for_big_data.sell import sell, time
from .dct_for_tests import *
import os.path


# def test_sell():
#     current_date = time.strftime('%Y-%m%d', time.localtime())
#     set_back_only_line('test_data')
#     assert read_only_line_csv('test_data') == {'cai': 16777225.0, 'region': 'Georgia',
#                                                'last_sale': '2022-0331', 'amount': 66242.82}
#     sell(16777225, 'Georgia', 100, 'test_data')
#     assert read_only_line_csv('test_data') == {'cai': 16777225.0, 'region': 'Georgia',
#                                                'last_sale': current_date, 'amount': 66342.82}
