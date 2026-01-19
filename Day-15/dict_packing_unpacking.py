# DICT PACKING AND UNPACKING

# Function demonstrating dictionary packing using **kwargs

def save_user_info(**user_data):
    """Stores and displays user information."""
    print(f'User information: {user_data}')

save_user_info(name='Bob', age=40, location='NYC')

# FUNCTION ARGUMENT UNPACKING WITH **

def connect_to_server(ip, port, username, password):
    """Connects to server."""
    print(f'Connecting to {ip}:{port} as {username}')

server_info = {
    'ip': '192.168.0.1',
    'port': 22,
    'username': 'admin',
    'password': 'ysdgfayd'
}

connect_to_server(**server_info)

