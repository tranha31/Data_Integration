from crawl_url import get_product_list, crawl_url
from crawl_info import crawl_info
from time import time
from json import dumps
from os.path import dirname, abspath
if __name__ == '__main__':
    start = time()
    product_list = get_product_list()
    urls = crawl_url(product_list)
    data = crawl_info(urls)
    content = dumps(data, ensure_ascii=False)
    path = dirname(abspath(__file__))
    with open(path+'\\fphone.json', 'w', encoding='utf8') as f:
        f.write(content)
    print(f'fptshop.com.vn crawler executed successfully!\nData saved at {path}\\fphone.json')
    print('Total time:',time()-start)
    
