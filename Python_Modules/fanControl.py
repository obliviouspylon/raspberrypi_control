from gpiozero import PWMLED
from time import sleep, time, strftime, localtime
from subprocess import check_output
from re import findall

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode()   
    temp = float(findall('\d+\.\d+', temp)[0])                   
    return(temp)

fan = PWMLED(15)
low = 25 #Start fan
high = 50 #Full Speed

try:
	while True:
		sleep(5)
		temperature = get_temp()
		if (temperature < low):
			fan.value = 0
		elif (temperature < high):
			fan.value = (temperature-low)/(high-low)
		else:
			fan.value = 1
		with open(r"/home/pi/Desktop/Python_Modules/fanTemp.txt","r+") as fp:
			lines = fp.readlines()
			if (len(lines) > 16):
				# move file pointer to the beginning of a file
				fp.seek(0)
				#truncate the file
				fp.truncate()
				lines.append(strftime('%Y-%m-%d %H:%M:%S %Z',localtime(time())) + "\n")
				lines.append("Temperature : " + str(temperature) + "°C\n")
				lines.append("  Fan Speed : " + str(round(fan.value*100,1)) + "%\n")
				lines.append("---\n")
				# start writing lines except the first line
				# lines[1:] from line 2 to last line
				fp.writelines(lines[4:])
				
			else:
				fp.seek(0)
				fp.truncate()
				lines.append(strftime('%Y-%m-%d %H:%M:%S %Z',localtime(time())) + "\n")
				lines.append("Temperature : " + str(temperature) + "°C\n")
				lines.append("  Fan Speed : " + str(round(fan.value*100,1)) + "%\n")
				lines.append("---\n")
				fp.writelines(lines)
			fp.close()
except KeyboardInterrupt:
	print("Exit pressed Ctrl+C")
