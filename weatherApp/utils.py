

def clothes(temp):
        
    if temp <= -30:
        clothes = "On the street severe frost put on your warm jacket and hat with earflap."
    elif temp <= -20 and temp > -30:
        clothes = "On the street frost put on your winter jacket and hat."
    elif temp <= -10 and temp > -20:
        clothes = "On the street cold put on your jacket."
    elif temp <= 0 and temp > -10: 
        clothes = "On the street chilly put on your coat."
    elif temp <= 10 and temp > 0:
        clothes = "On the street warm put on your hoodie."
    elif temp <= 20 and temp > 10: 
        clothes = "On the street Very warm put on your denim jacket."
    elif temp <= 30 and temp > 20:
        clothes = "On the street heat put on your shirt."
    elif temp > 30:
        clothes = "On the street Very hot put on your t-shirt and shorts."

    return clothes

def speedInfo(speed):
    if speed <= 2:
        speedInf = " Light breeze "
    elif speed > 2 and speed <= 7:
        speedInf = "Have Wind "
    elif speed > 7 and speed <= 12:
        speedInf = " High wind "
    elif speed > 12:
        speedInf = " Hurricane-Force winds "

    return speedInf

def humidityInfo(humidity):
    if humidity <= 50:
        humidityInf = "and dry."
    elif humidity > 50 and humidity <=70:
        humidityInf = "and humidity normal."
    elif humidity > 70 and humidity <=80:
        humidityInf = "and humidity."
    elif humidity > 80:
        humidityInf = " and humidity:Saint Petersburg."
    return humidityInf