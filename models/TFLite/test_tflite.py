
import numpy as np
import tensorflow as tf
import sys
import traceback
# Load TFLite model and allocate tensors.f
try:
	interpreter = tf.lite.Interpreter(model_path="mobilenet.tflite")
	interpreter.allocate_tensors()
	# Get input and output tensors.
	input_details = interpreter.get_input_details()
	output_details = interpreter.get_output_details()
	print(input_details)
	print(output_details)
except:
	traceback.print_exc()