from runabove import Runabove
application_key = '52tSKhS9sdpKJjWS'
application_secret = 'jILFGpLpOnVY3eYb3CMYkCbJzjiqSplP'
consumer_key = 'oDzTPCyynZD1OERdAhAKhNeoui2DsQEc'

# Create the Runabove SDK interface
run = Runabove(application_key,
               application_secret,
               consumer_key=consumer_key)

region = run.regions.list().pop()
print("region:", region)
'''
# Get a region, flavor and image
flavor = run.flavors.list_by_region(region).pop()
image = run.images.list_by_region(region).pop()

# Launch a new instance
instance = run.instances.create(region, 'My instance', flavor, image)

# List instances
print 'Instances:'
for i in run.instances.list():
    print ' - %s (%s)' % (i.name, i.image.name)

# Delete the newly created instance
instance.delete()
print '%s deleted' % instance.name'''
