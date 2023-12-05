import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

questions = [
    "What is the Italian word for PIE? /n a.Mozzarella/n b.Pastry/n c.Patty",
    "How many wonders are in the world? /n a.7/n b.3/n c.5"
]   
nicknames = []

print("Server has started...")

def clientthread(conn, addr):
    score = 0
    conn.send("Welcome to this quiz!".encode('utf-8'))
    conn.send("You will receive a random question".encode('utf-8'))
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score +=1
                    conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect".encode('utf-8'))
                
            else:
                remove_question(index)
                remove_nickname(nickname)
                index, question, answer = get_random_question_answer(conn)
        except:
            continue

def get_random_question(conn):
    random_index = random.randint(0, len(questions) - 1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer
    
def remove_question(index):
    questions.pop(index)
    answers.pop(index)
def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)
        
while True:
    conn, addr = server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    list_of_clients.append(conn)
    nicknames.append(nickname)
    print (nickname + " connected")
    new_thread = Thread(target= clientthread,args=(conn,nickname))
    new_thread.start()
