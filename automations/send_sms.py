import requests
def send_sms(message, sender, number):
    url = "https://www.intouchsms.co.rw/api/sendsms/.json"
    username = "rugema3"
    password = "pass123"
    data =	{'recipients':number,'message'	: message,'sender': sender}
    r	=	requests.post(url, data, auth=(username, password))
    print(r.json(),	r.status_code)

if __name__ == '__main__':
    message = input("please enter the message.: ")
    sender = input("Please enter the name of the sender: ")
    number = input("Please enter the number to send to: ")
    send_sms(message, sender, number)
