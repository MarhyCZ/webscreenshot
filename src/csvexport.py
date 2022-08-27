import io
import csv
from pprint import pprint


def generate_csv_cookies(cookies: list[dict[str, list]]):
    headers = ['name', 'value', 'expiry', 'domain']
    return generate_file(cookies, headers)


def generate_csv_storage(local_storage):
    headers = ['name', 'value']
    return generate_file(local_storage, headers)


def generate_file(data, headers):
    file = io.StringIO()
    rows_data = []
    for item in data:
        row = []
        for header in headers:
            value = item.get(header, "")
            row.append(value)
        rows_data.append(row)

    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows_data)
    return file.getvalue()
