import RPi.GPIO as GPIO
from time import sleep

dac = [26,19,13,6,5,11,9,10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    sleep(0.05)

    return signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        n = int(input())
        for j in range (0,n):
         for i in range(0,256): 

              value = i

              if value >= levels:
                  print("ряд переполнен, введите заново")
                  continue
            
              signal = bin2dac(value)
              voltage = value/levels * maxVoltage
              print ("Введённый ряд = {:^3} -> {}, Напряжение = {:.2f}".format(value,signal, voltage))
              i = i+1
        

         for k in range(255,-1,-1): 

              value = k

              if value >= levels:
                  print("ряд переполнен")
                  continue
            
              signal = bin2dac(value)
              voltage = value/levels * maxVoltage
              print ("Введённый ряд = {:^3} -> {}, Напряжение = {:.2f}".format(value,signal, voltage))
              


except KeyboardInterrupt:
    print ("Программа остановленна из-за риска ошибки")
else:
    print("Ошибок нет")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup!")