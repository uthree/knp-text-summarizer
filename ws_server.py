from websocket_server import WebsocketServer
from datetime import datetime
from summarizer import summarize

def new_client(client, server):
    print(datetime.now().isoformat() + ": new client joined!")
    
def message_received(client, server, message):
    print(datetime.now().isoformat() + ": message received!")
    summary = summarize(message, depth=0)
    print(summary)
    server.send_message(client, summary)

if __name__ == "__main__":
    server = WebsocketServer(host="localhost", port=9999, )
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(message_received)
    server.run_forever()