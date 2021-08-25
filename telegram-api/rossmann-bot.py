import pandas as pd
import json
import requests
from flask import Flask, request, Response
# constants
token = '1941843017:AAHJnMAp82jihgY8xxP45BgFvtbfQFp5SnY'

## info about bot
#https://api.telegram.org/bot1941843017:AAHJnMAp82jihgY8xxP45BgFvtbfQFp5SnY/getMe

## get updates
#https://api.telegram.org/bot1941843017:AAHJnMAp82jihgY8xxP45BgFvtbfQFp5SnY/getUpdates

## send message
#https://api.telegram.org/bot1941843017:AAHJnMAp82jihgY8xxP45BgFvtbfQFp5SnY/sendMessage?chat_id=552137461&text=Olá,
#muito bom poder te auxiliar na previsão de vendas :)

def send_message( chat_id, text):
    url = 'https://api.telegram.org/bot{}/'.format( token )
    url = url + 'sendMessage?chat_id={}'.format( chat_id )

    r = requests.post( url, json={'text': text})
    print('Status code {}'.format(r.status_code))

    return None

def load_dataset( store_id):
    # loading test csv
    df10 = pd.read_csv('../data/test.csv')
    df_store_raw = pd.read_csv('../data/store.csv')

    # merge test datase + store
    df_test = pd.merge( df10, df_store_raw, how='left', on='Store')

    # choose store for prediction
    df_test = df_test[df_test['Store'] == store_id]

    if not df_test.empty:
        # remove closed days
        df_test = df_test[df_test['Open'] != 0]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop('Id', axis=1)

        # convert Dataframe to json
        data = json.dumps(df_test.to_dict( orient='records'))
    else:
        data = 'error'

    return data

def predict( data ):
    # Api call
    url = 'https://rosmann-store-sales.herokuapp.com/rossmann/predict'
    header = {'Content-type': 'application/json' }
    data = data

    r = requests.post( url, data=data, headers=header )
    print( 'Status Code {}'.format( r.status_code ) )
    
    d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

    return d1

def parse_message( message ):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']

    store_id = store_id.replace('/','')

    try:
        store_id = int(store_id)

    except ValueError:
        store_id = 'error'

    return  chat_id, store_id

# Initialize API
app = Flask( __name__ )

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        message = request.get_json()

        chat_id, store_id = parse_message( message )

        if store_id != 'error':
            #loading data
            data = load_dataset( store_id)

            if data != 'error':
                #prediction
                d1 = predict(data)

                #calculation
                d2 = d1[['store', 'prediction']].groupby('store').sum().reset_index()

                #send message
                msg = 'Previsão de vendas para a loja {} nas próximos 4 semanas é de R${:,.2f} '.format(
                                                                                        d2['store'].values[0],
                                                                                        d2['prediction'].values[0])
                send_message(chat_id, msg)
                return Response('Ok',status=200)

            else:
                send_message( chat_id, 'O código da loja não existe')
                return Response('Ok', status=200 )

        else:
            send_message(chat_id, 'O código da loja está incorreto')
            return  Response('OK', status=200)

    else:
        return '<h1> Rossmann Telegram BOT </h1>'

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000)
