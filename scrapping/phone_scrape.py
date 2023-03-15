import requests
from csv import writer

#used due to unknown number of pages with phone data
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
s = requests.Session()
s.headers.update(headers)
counter = 1

with open('mobile_phones.csv', 'w', encoding='utf8', newline='') as f:
    file_writer = writer(f)
    top_header = ['PHONE_TYPE', 'RAM_STORAGE', 'NAIRA_PRICE', 'CITY','STATE', 'PHONE_CONDITION']
    file_writer.writerow(top_header)
    while True:
        try:
            url = f'https://jiji.ng/api_web/v1/listing?slug=mobile-phones&init_page=true&page={counter}&webp=true'

            data = s.get(url).json()['adverts_list']['adverts']
            if len(data) < 1:
                break
            for x in data:
                phone_name = x['title']
                for t in data:
                    ram_storage = ''
                    st = [a['value'] for a in t['attrs']]
                    if len(st) == 3:
                        ram_storage += st[2]
                    else:
                        ram_storage += "NA"

                price_naira = x['price_obj']['value']
                city = x['region_name']
                state = x['region_parent_name']
                condition = x['attrs'][0]['value']
                phone_info = [phone_name, ram_storage,
                            price_naira, city, state, condition]

                file_writer.writerow(phone_info)

            counter = counter + 1
        except Exception as e:
            break
