# hpat874_364_A2

## How to install the code

The following must be installed:
- OpenSSL
- Python 3.7 or higher
> Note:
> If ```python``` or ```python3``` is an alias for a different version, you should use ```python3.7```.

### 1. Cloning the reposittory
- Clone the repository using this command
```
git clone https://github.com/HamishPatel/364_A2
```
### 2. Change directory into project folder
- Use this command
```
cd .\364_A2\
```
### 3. Configure and generate the SSL Certificate
- Use this command
```
openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem
```
- Follow the pormpts and enter in the information as the screenhot below
![image](https://github.com/user-attachments/assets/dfeec521-971b-48c8-9144-533c802d9bc9)

## How to run the code
> Note:

>a.You should already be in the **364_A2** directiory

>b.If ```python``` or ```python3``` is an alias for a different version, you should use ```python3.7```.

### 1. Run the Server
- In the **364_A2** directory run the following command
```
python chat_server.py --port=9988
```

### 2. Run the Client
- In another terminal but still in the **364_A2** dreictory run the following command
```
python chat_client.py --port=9988
```
- It will ask you to register and login, enter a username to register and log in


>* For any further help, email me at : hpat874@aucklanduni.ac.nz




