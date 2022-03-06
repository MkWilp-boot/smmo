from datetime import datetime


def write(data: dict):
    date = datetime.now().strftime('%d_%m_%Y')
    with open('history/{}.txt'.format(date), 'a') as f:
        f.write('======== RUN ========\n')
        f.writelines(['{}: {}\n'.format(k, v) for k, v in data.items()])
