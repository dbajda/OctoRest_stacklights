# OctoREST industrial stack light controller
# using 4 channel relay for triggering lights
# It's alpha and I'm total newbie in python

#Using OctoREST and GPIOzero
from octorest import OctoRest
from gpiozero import LED
from time import sleep

# here you define outputs on your Raspberry pi
rele1 = LED(17)
rele2 = LED(22)
rele3 = LED(10)

# here you define your octopi instance and api key
octopi = "octopi.local"
api = "random api key"

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
            rele1.on()
            rele2.on()
            rele3.off()
            sleep(1)
            rele3.on()
            sleep(1)
       # else:
           # rele3.on()
        if cancelling == True and printing == True:
            rele1.on()
            rele3.on()
            rele2.off()
        #else:
            #rele2.on()
        if ready == True:
            rele1.on()
            rele2.on()
            rele3.off()
        #else:
           # rele3.on()
        if error == True:
            rele3.on()
            rele2.on()
            rele1.off()
        #else:
         #   rele1.on()
        if paused == True:
            rele1.on()
            rele3.on()
            rele2.off()
            sleep(1)
            rele2.on()
            sleep(1)
       
        #if operational == True:
        #    rele2.off()
        #else:
         #   rele2.on()
        if finishing == True:
            rele2.off()
            rele3.off()
            sleep(1)
            rele3.on()
            sleep(1)
        #else:
           # rele3.on()

        return status
    except Exception as e:
        #print(e)
        i=0

def main():
    c = make_client()
    while True:
        print(get_printer_info())


"""
    while True:
     if get_printer_info() == False:
        rele2.on()
        sleep(1)
        rele1.on()
        print("Waiting for printing")
        sleep(1)
        rele1.off()
    else:
        rele1.on()
        rele2.off()
        print("Printing")
"""
    

if __name__ == "__main__":
    main()
