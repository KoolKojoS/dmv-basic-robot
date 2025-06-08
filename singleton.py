#Using this to define Singleton for generic buffers. 
# Singleton will force new buffers to exist as single instance. 
class Singleton(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'): #If class exists, skip line below
      cls.instance = super(Singleton, cls).__new__(cls) #When instance doesn't exist, create new instance. Super refers to Object. 
    return cls.instance