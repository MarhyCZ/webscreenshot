import io
import csv
from pprint import pprint


def generate_csv_cookies(cookies: list[dict]) -> str:
    headers = ['name', 'value', 'expiry', 'domain']
    return generate_file(cookies, headers)


def generate_csv_local_storage(local_storage: list[dict]) -> str:
    pprint(local_storage)
    headers = ['name', 'value']
    return generate_file(local_storage, headers)


def generate_file(data, headers) -> str:
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
