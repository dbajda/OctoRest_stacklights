# OctoREST industrial stack light controller
# using 4 channel relay for triggering lights
# It's alpha and I'm total newbie in python

#Using OctoREST and GPIOzero
from octorest import OctoRest
from gpiozero import LED
from time import sleep

# here you define outputs on your Raspberry pi
relay1 = LED(17)
relay2 = LED(22)
relay3 = LED(10)

# here you define your octopi instance and api key
octopi = "octopi.local"
api = "api key"

def make_client():
    try:
        client = OctoRest(url=octopi, apikey=api)
        return client
    except Exception as e:
        print(e)
        
def get_printer_info():
    try:
        client = OctoRest(url=octopi, apikey=api)
        message = ""
        
        printing = client.printer()['state']['flags']['printing']
        cancelling = client.printer()['state']['flags']['cancelling']
        ready = client.printer()['state']['flags']['ready']
        error = client.printer()['state']['flags']['error']
        paused = client.printer()['state']['flags']['paused']
        operational = client.printer()['state']['flags']['operational']
        finishing = client.printer()['state']['flags']['finishing']
        status = client.printer()['state']['flags']

        if printing == True and cancelling == False:
            relay1.on()
            relay2.on()
            relay3.off()
            sleep(1)
            relay3.on()
            sleep(1)
       # else:
           # relay3.on()
        if cancelling == True and printing == True:
            relay1.on()
            relay3.on()
            relay2.off()
        #else:
            #relay2.on()
        if ready == True:
            relay1.on()
            relay2.on()
            relay3.off()
        #else:
           # relay3.on()
        if error == True:
            relay3.on()
            relay2.on()
            relay1.off()
        #else:
         #   relay1.on()
        if paused == True:
            relay1.on()
            relay3.on()
            relay2.off()
            sleep(1)
            relay2.on()
            sleep(1)
       
        #if operational == True:
        #    relay2.off()
        #else:
         #   relay2.on()
        if finishing == True:
            relay2.off()
            relay3.off()
            sleep(1)
            relay3.on()
            sleep(1)
        #else:
           # relay3.on()

        return status
    except Exception as e:
        #print(e)
        relay1.off()
        relay2.off()
        relay3.off()
        sleep(1)
        relay3.on()
        sleep(1)
def main():
    c = make_client()
    while True:
        print(get_printer_info())

if __name__ == "__main__":
    main()
