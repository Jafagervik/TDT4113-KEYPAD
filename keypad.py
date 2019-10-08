import time


class Keypad:
    """

    """

    def __init__(self):
        self.key_rows = [18, 23, 24, 25]
        self.key_column = [17, 27, 22]
        self.keypad_dict = {
            "0,0": 1,
            "0,1": 2,
            "0,2": 3,
            "1,0": 4,
            "1,1": 5,
            "1,2": 6,
            "2,0": 7,
            "2,1": 8,
            "2,2": 9,
            "3,0": "*",
            "3,1": 0,
            "3,2": "#"

        }

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for row in self.key_rows:
            GPIO.setup(row, GPIO.OUT)

        for col in self.key_column:
            GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def do_polling(self):
        location = ""
        """
        for i in range(len(self.key_rows)):
            GPIO.output(self.key_rows[i], GPIO.HIGH)
            for j in range(len(self.key_column)):
                k = 0
                for t in range(20):
                    if GPIO.input(self.key_column[j]) == GPIO.HIGH:
                        k += 1
                    time.sleep(10)
                if k == 20:
                    location = str(i) + str(j)
        return location
        """
        KEY_PRESS = 0
        while True:
            KEY_PRESS = 0
            for out in self.key_rows:






    def get_next_signal(self):
        location = ""
        while location == "":
            location = self.do_polling()
            if location != "":
                return location
            time.sleep(10)



if __name__ == '__main__':
    # startup function
    pass

"""
KEY_PRESS=0
try:
#####################################
# MAIN LOOP 
######################################
	while True:

		KEY_PRESS=0
		##############################################
		# we want to make sure that all outputs are low
		# Because we just want to detect which row is being accessed
		#
		##############################################
		for out_id2 in outputs:
			#echo "out id:$out_id2"
			GPIO.output(out_id2, 0)
		##############################################
		# This would be nicer if we were waiting for an interrupt -------------> INTERRUPT HERE <-------------------------
		# Instead of looping, which eats CPU doing nothing.
		##############################################
		while KEY_PRESS==0:
			for in_id in inputs:
				#echo "in id:$in_id"
		 
				VAL1=int(GPIO.input(in_id))
				#print str(VAL1)

				if VAL1 == 0:
					KEY_PRESS=1
					break
		##############################################
		# we know which row ($in_id) is being accessed, 
		# we need to detect the column
		##############################################	
		for out_id in outputs:
				##############################################
				# we want to make sure that all outputs are high 
				# before we attemps to see which key is pressed(active low).
				##############################################	
			for out_id2 in outputs:
				#echo "out id:$out_id2"
				GPIO.output(out_id2, 1)
			GPIO.output(out_id, 0)				
			VAL1=int(GPIO.input(in_id))	
			if VAL1 == 0:	
"""