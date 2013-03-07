import requests

r = requests.get("http://updates.puppetlabs.com:9091/?email=austin.dubina%40gmail.com")
print "Answer Header:", r.headers['X-Answer']

