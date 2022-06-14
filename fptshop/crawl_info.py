from yarl import URL
from crawl_url import get_product_url
async def get_product_info(url, session,is_variant=False):
    url = URL(url, encoded=True)
    resp = await session.get(url)
    resp = await resp.json()
    resp = resp['datas']['model']['product']
    variants = resp['listProductGroupDetail']
    if is_variant == False and len(variants) > 0:
        items = []
        for v in variants:
            item = await get_product_info(get_product_url(v['productNameAscii']), session, True)
            items.append(item)
        return items
    else:
        item = {}
        item['name'] = resp['name']
        item['brand'] = resp['brand']['name']
        for a in resp['listAttrDetailShort']:
            if a['attributeName'] == 'Màn hình':
                item['display'] = a['specName']
        for a in resp['productAttributes']:
            if a['attributeName'] == 'Bộ nhớ trong':
                item['ROM'] = a['specName']
            elif a['attributeName'] == 'Phiên bản CPU':
                item['CPU'] = a['specName']
            elif a['attributeName'] == 'RAM':
                item['RAM'] = a['specName']
            elif a['attributeName'] == 'Dung lượng pin':
                item['battery'] = a['specName']
            elif a['attributeName'] == 'Chuẩn màn hình':
                item['display_resolution'] = a['specName']
            elif a['attributeName'] == 'Kích thước màn hình':
                item['display_size'] = a['specName']
            elif a['attributeName'] == 'Camera Selfie':
                item['front_camera'] = a['specName']
            elif a['attributeName'] == 'Camera sau':
                item['rear_camera'] = a['specName']
            elif a['attributeName'] == 'Hệ điều hành':
                item['OS'] = a['specName']
            elif a['attributeName'] == 'Loại SIM':
                item['sim_card'] = a['specName']
            elif a['attributeName'] == 'Thời điểm ra mắt':
                item['release_date'] = a['specName']
            elif a['attributeName'] == 'Loại PIN':
                item['battery_type'] = a['specName']
            elif a['attributeName'] == 'CPU':
                item['CPU'] = a['specName']
        prefix_img = 'https://images.fpt.shop/unsafe/fit-in/800x800/filters:quality(90):fill(white):upscale()/fptshop.com.vn/Uploads/Originals/'
        item['variants'] = []
        for a in resp['listProductVariant']:
            var = {'color': a['colorName'],
                'price': a['price'],
                'priceMarket': a['priceMarket'],
                'image': prefix_img + a['gallery']['url']}
            item['variants'].append(var)
        item['more_image'] = [prefix_img+i['url'] for i in resp['productVariant']['listGallery']]
        return [item,]

import asyncio
import aiohttp

async def asyncrawl(urls):
    tasks = []
    session = aiohttp.ClientSession()
    for url in urls:
        tasks.append(asyncio.ensure_future(get_product_info(url, session)))
    return await asyncio.gather(*tasks)

def crawl_info(urls):
    data = asyncio.get_event_loop().run_until_complete(asyncrawl(urls))
    data = [i for sublis in data for i in sublis]
    return data
