# -*- encoding: utf-8 -*-

import ovh

# Instantiate. Visit https://api.ovh.com/createToken/index.cgi?GET=/me
# to get your credentials
# 3237bd1306c00f4574b392118b43efbeec8f0b58
# 1420802713
client = ovh.Client(
    endpoint='runabove-ca',
    application_key='52tSKhS9sdpKJjWS',
    application_secret='jILFGpLpOnVY3eYb3CMYkCbJzjiqSplP',
    consumer_key='CFQ4v7mLeyELP3RTpBXi2LefBHpSpE41',
)

# Print nice welcome message
print "Welcome", client.get('/me')['firstname']
