import requests
import json
import csv

def download_image(file_path, file_name):
    response = requests.get(file_path)
    with open(file_name, 'wb') as f:
        f.write(response.content)
        print("downloaded image at: ", file_name)


def write_txt(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        for row in data:
            f.write(row + '\n')
    return True


def read_txt(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
    return data

def write_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return True


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def write_csv(filename, data):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        for row in data:
            csv_writer.writerow(row)
    return True