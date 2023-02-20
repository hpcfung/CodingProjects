import re

short_url = 'https://www.youtube.com/shorts/xKlqsv4nCao'
out_url = re.sub(r'www.youtube.com/shorts', r'youtu.be', short_url)

print(out_url)
