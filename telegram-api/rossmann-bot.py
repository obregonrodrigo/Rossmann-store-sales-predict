import pandas as pd
import json
import requests

# constants
token = '1941843017:AAHJnMAp82jihgY8xxP45BgFvtbfQFp5SnY'

# info about bot
https://api.telegram.org/bot1941843017:AAHJnMAp82jihgY8xxP45BgFvtbfQFp5SnY/getMe

# get updates
https://api.telegram.org/bot1941843017:AAHJnMAp82jihgY8xxP45BgFvtbfQFp5SnY/getUpdates

# send message
https://api.telegram.org/bot1941843017:AAHJnMAp82jihgY8xxP45BgFvtbfQFp5SnY/sendMessage?chat_id=552137461&text=Olá,
muito bom poder te auxiliar na previsão de vendas :)

def load_dataset( store_id):
    # loading test csv
    df10 = pd.read_csv('../data/test.csv')
    df_store_raw = pd.read_csv('../data/store.csv')

    # merge test datase + store
    df_test = pd.merge( df10, df_store_raw, how='left', on='Store')

    # choose store for prediction
    df_test = df_test[df_test['Store'] == store_id]

    # remove closed days
    df_test = df_test[df_test['Open'] != 0]
    df_test = df_test[~df_test['Open'].isnull()]
    df_test = df_test.drop('Id', axis=1)

    # convert Dataframe to json
    data = json.dumps(df_test.to_dict( orient='records'))

def predict( data ):
    # Api call
    url = 'https://rosmann-store-sales.herokuapp.com/rossmann/predict'
    header = {'Content-type': 'application/json' }
    data = data

    r = requests.post( url, data=data, headers=header )
    print( 'Status Code {}'.format( r.status_code ) )
    
    d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

    return d1

#    d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

#    for i in range( len( d2 ) ):
#        print( 'Store Number {} will sell R${:,.2f} in the next 4 weeks'.format(
#                                                                            d2.loc[i, 'store'],
#                                                                            d2.loc[i, 'prediction'] ) )