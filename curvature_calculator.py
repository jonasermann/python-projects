import math

# curvature_calculator takes three arguments: (a) the height of an observer
# above sea level (including observer height) in km, (b) the height of an 
# object the observer is (trying) to see, also in km, and last but not least
# (H) the distance between (a) and (b), meaning the distance along earth's 
# surface. The calculator will tell the user how far away the horizon is from 
# (a), again meaning along earth's surface. If (b) lies outside the horizon,
# the calculator will tell the user how heigh at least (b) needs to be in order
# for (a) to see (b). It will also tell the user the refraction index needed
# for (a) to see (b) anyways, i.e. even without height adjustments. 

# NOTE: In the latter calculations, (b) height is not taken into consideration.
# This means that, even thou (b) is visible for (a) given (b) height, the 
# calculator will still give a refraction index, which is the index required to
# see (b) entire body. However, the height requirement given for (a) to see (b)
# given that (b) lies outisde (a) horizon only refers to the bar minimum, i.e.
# to see the top of (b).


def curvature_calculator(a, b, H):
    
    r = 6371
    
    Ha = math.acos(1-(a/(a+r))) * r
    
    Hb = math.acos(1-(b/(b+r))) * r
    
    HB = H - Ha
    
    B = (r / math.cos(HB/r)) - r 
    
    print("\nThe horizon is", Ha, "km away from the observer.\n")
    
    if b > B:
        
        Hc = (H - Ha - Hb) / 2
        
        c = (r / math.cos(Hc/r)) - r
        
        hc = math.sqrt((c**2)+(2*c*r))
        
        cb = c + ((c*r)/(c+r))
        
        gamma = math.acos(cb/hc)
        
        v = math.pi - (2*gamma)
        
        v = (v / (2*math.pi)) * 360
        
        print("An object", H, "km away has to be at least", B*1000,"meters "
              "high in order for it's top to be seen by the observer.\n")
        print("In order for the observer to see the entirety of the object, "
              "there needs to be", v, "degrees of refraction.")
    
    