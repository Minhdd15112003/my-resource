import requests
from requests.auth import HTTPBasicAuth

class ddnsDynu():
    def __init__(self, first):
        self.name = first.name
        self.token = first.token
        self.domain = first.domain
        self.username = first.username
        self.password = first.password
        self.status = first.status
        self.hosts = {
            "noip.com":"https://dynupdate.no-ip.com/nic/update",
            "dynu.com":"https://api.dynu.com/nic/update",
            "duckdns.org":"https://api.dynu.com/nic/update"
        }

    def update_ip(self, myip=None):
        if self.domain and self.username and self.password and self.status:
            params={'hostname': self.domain}
            if myip:
                params["myip"] = myip
            return requests.get(
                self.hosts[self.name],
                params=params,
                auth=HTTPBasicAuth(self.username, self.password),
                timeout=10
            )
            
    
    