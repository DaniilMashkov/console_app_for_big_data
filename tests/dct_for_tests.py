# import pandas as pd
# import os
#
#
# def read_csv(*args: tuple) -> dict:
#     df = pd.read_csv(f'cache/{args[:2]}.csv').to_dict()
#     return df
#
#
# def read_only_line_csv(file: str) -> dict:
#     df = pd.read_csv(f'data/{file}.csv')
#     df.round({'amount': 2})
#     return df.iloc[3].to_dict()
#
#
# def set_back_only_line(file: str):
#     df = pd.read_csv(f'data/{file}.csv')
#     df.loc[(df['cai'] == 16777225) & (df['region'] == 'Georgia'), 'amount'] = 66242.82
#     df.loc[(df['cai'] == 16777225) & (df['region'] == 'Georgia'), 'last_sale'] = '2022-0331'
#     df.to_csv(f'data/{file}.csv', index=False, mode='w')

#
# region_test_dict = {'region': {0: 'India', 1: 'USA', 2: 'Georgia', 3: 'Germany', 4: 'Russia'},
#                     'amount': {0: 98029786.44, 1: 97523512.28, 2: 97357621.36, 3: 96567609.54, 4: 95792211.46}}
#
# latest_test_dict = {
#     'cai': {0: 16777225.0, 1: 50874489.0, 2: 93352290.0, 3: 75526804.0, 4: 96738449.0, 5: 46462527.0, 6: 96738449.0,
#             7: 1158461.0, 8: 82383540.0, 9: 66697636.0, 10: 8593149.0, 11: 60994538.0, 12: 3522561.0, 13: 8593149.0,
#             14: 3522561.0},
#     'region': {0: 'Georgia', 1: 'Georgia', 2: 'Georgia', 3: 'Georgia', 4: 'USA', 5: 'Germany', 6: 'USA', 7: 'Spain',
#                8: 'India', 9: 'India', 10: 'Georgia', 11: 'Russia', 12: 'China', 13: 'Georgia', 14: 'China'},
#     'last_sale': {0: '2022-1225', 1: '2022-1205', 2: '2022-1205', 3: '2022-1205', 4: '2022-1205', 5: '2022-1205',
#                   6: '2022-1205', 7: '2022-1205', 8: '2022-1205', 9: '2022-1205', 10: '2022-1205', 11: '2022-1205',
#                   12: '2022-1205', 13: '2022-1205', 14: '2022-1205'},
#     'amount': {0: 266242.82, 1: 28918.55, 2: 39688.29, 3: 37366.06, 4: 89577.2, 5: 3028.88, 6: 89577.2, 7: 81966.98,
#                8: 34511.5, 9: 90797.39, 10: 61678.52, 11: 26378.7, 12: 80046.67, 13: 61678.52, 14: 80046.67}}
#
# top_test_dict = {'cai': {0: 16777225.0, 1: 85338224.0}, 'region': {0: 'Georgia', 1: 'India'},
#                  'last_sale': {0: '2022-1225', 1: '2022-0210'}, 'amount': {0: 266242.82, 1: 99986.1}}
