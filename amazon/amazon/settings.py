import scraper_helper as sh

BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'
ROBOTSTXT_OBEY = False
AUTOTHROTTLE_ENABLED=True
DEFAULT_REQUEST_HEADERS=sh.get_dict(
'''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: max-age=0
cookie: session-id=138-1254697-5658101; session-id-time=2082787201l; i18n-prefs=USD; lc-main=en_US; sp-cdn="L5Z9:IN"; ubid-main=134-3233836-5262610; session-token=blSbsRD0DN5TFOS6Su7yo7SZx5MMnG1dO9KJE/NHua1HRYxYmPqmnboJmAc1j0TQ0vTpTQKoLH+RQQTsiS0buHQoiLVvWleD6TvgNvV2PpbDoFjfDz+Y0ObiG0p5bbiCYZ/kMxlNzJQqN4pbtLuhlfdJdqB7Cg0zAScAoVwsUCtPe4yup7sAjgav9RitWmKK; csm-hit=tb:B5FM3P0P77RVHCB0WTZ0+s-B5FM3P0P77RVHCB0WTZ0|1632297014162&t:1632297014162&adb:adblk_no
dnt: 1
downlink: 10
ect: 4g
rtt: 50
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1
'''
)




