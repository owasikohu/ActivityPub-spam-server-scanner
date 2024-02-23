import json
import asyncio
import aiohttp

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception:
        return None

async def main():
    with open('urls.json', 'r') as f:
        urls = json.load(f)
    
    urls = [url + '/api/v1/timelines/public' for url in urls]
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(urls):
            if i % 100 == 0:
                print(f'現在のリクエスト数: {i}')
            task = fetch(session, 'https://' + url)
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    
    output_urls = [url for url, response in zip(urls, responses) if response and response.count('荒らし') >= 10]
    print('\n'.join(output_urls))
    
    with open('output.txt', 'w') as f:
        f.write('\n'.join(output_urls))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
