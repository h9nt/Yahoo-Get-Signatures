import re
from requests   import get
from user_agent import generate_user_agent
from json       import dumps
from colorama   import init, Fore
from os         import system
# from utils.body import fakeFP

init(autoreset=True)
system('cls')

class Yahoo:
    @staticmethod
    def acrumb() -> str:
        try:
            response = get("https://login.yahoo.com/?.src=ym&lang=de-DE&done=https://mail.yahoo.com/", headers= {
                "host"              : "login.yahoo.com",
                "connection"        : "keep-alive",
                "pragma"            : "no-cache",
                "cache-control"     : "no-cache",
                "user-agent"        : f"{generate_user_agent()}",
                "accept"            : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "x-requested-with"  : "com.email.emailloginallemailconnect",
                "sec-fetch-site"    : "none",
                "sec-fetch-mode"    : "navigate",
                "sec-fetch-user"    : "?1",
                "sec-fetch-dest"    : "document",
                "sec-ch-ua"         : "\"Not)A;Brand\";v=\"99\", \"Android WebView\";v=\"127\", \"Chromium\";v=\"127\"",
                "sec-ch-ua-mobile"  : "?1",
                "sec-ch-ua-platform": "\"Android\"",
                "accept-encoding"   : "gzip, deflate, br, zstd",
                "accept-language"   : "en,null;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6",
                "cookie"            : "GUCS=ATkqqUEg"
            }).text
            acrumb_pat = r'<input[^>]*name="acrumb"[^>]*value="([^"]*)"\s*/?>'
            acr = re.search(acrumb_pat, response).group(1) if acrumb_pat else None
            return acr
        except Exception:
            return
    
    @staticmethod
    def crumb() -> str:
        'Exact the sameeee lmaooo'
        try:
            response = get("https://login.yahoo.com/?.src=ym&lang=de-DE&done=https://mail.yahoo.com/", headers= {
                "host"              : "login.yahoo.com",
                "connection"        : "keep-alive",
                "pragma"            : "no-cache",
                "cache-control"     : "no-cache",
                "user-agent"        : f"{generate_user_agent()}",
                "accept"            : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "x-requested-with"  : "com.email.emailloginallemailconnect",
                "sec-fetch-site"    : "none",
                "sec-fetch-mode"    : "navigate",
                "sec-fetch-user"    : "?1",
                "sec-fetch-dest"    : "document",
                "sec-ch-ua"         : "\"Not)A;Brand\";v=\"99\", \"Android WebView\";v=\"127\", \"Chromium\";v=\"127\"",
                "sec-ch-ua-mobile"  : "?1",
                "sec-ch-ua-platform": "\"Android\"",
                "accept-encoding"   : "gzip, deflate, br, zstd",
                "accept-language"   : "en,null;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6",
                "cookie"            : "GUCS=ATkqqUEg"
            }).text
            crumb_pat = r'<input[^>]*name="crumb"[^>]*value="([^"]*)"\s*/?>'
            cru = re.search(crumb_pat, response).group(1) if crumb_pat else None
            return cru
        except Exception:
            return
    
    @staticmethod
    def get_values() -> dict:
        try:
            return dumps({
                'acrumb': Yahoo().acrumb(),
                'crumb': Yahoo().crumb(),
            }).replace(' ', '')
        except Exception:
            return

if __name__ == '__main__':
    print(f"MADE BY {Fore.RED}H9NT{Fore.RESET} ON GITHUB".center(127))
    print(Yahoo().get_values())


# Its actually just basic, so dont' skid LMAO if yes fuck u
