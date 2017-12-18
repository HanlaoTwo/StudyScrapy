from scrapy import cmdline

name = 'advanced_spider'
command_str = 'scrapy crawl {0}'
cmd = command_str.format(name)
cmdline.execute(cmd.split())