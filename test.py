import requests



def main():
    print(requests.get('http://127.0.0.1:5000/schedule/tasks').text)

if __name__ == '__main__':
    main()
