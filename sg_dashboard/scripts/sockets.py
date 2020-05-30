from socket_server.namespace import EventNamespace


class Namespace(EventNamespace):

    def client_connected(self, client):
        super(Namespace, self).client_connected(client)
        print('Sending hello')
        self.emit_to(client, 'hello')

    def register_callbacks(self):
        return {
            'hey': self.hey
        }

    def hey(self, client, **kwargs):
        print('Received "hello" event.')
