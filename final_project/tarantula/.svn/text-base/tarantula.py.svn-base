###########################################################
# File: Tarantula.py
# Description: Implements a version of tarantula for multipurpose programs.
# 	produces colored output based on the suspiciousness of a line
#	given its presence in failing test cases.
# Interface: import this module and call the run_tarantula() function
#	with an argument that supports a next_test() function returning
#	True when more tests exist and False when not, a get_gcov_file() method that returns the file to gcov, and a run_test() method
#	returning 1 for success or 0 for failure.
###########################################################

import subprocess
import sys

class taran_line:
	def __repr__(self):
		return "line %d: %d, %d\n" % (self.line_no, self.pass_count, self.fail_count)

	def __init__(self, text, line_no, exec_count=0, passed=0, failed=0):
		self.text = text
		self.line_no = int(line_no)
		self.exec_count = exec_count
		self.pass_count = passed
		self.fail_count = failed
	
	def inc_passed(self):
		self.pass_count += 1

	def inc_failed(self):
		self.fail_count += 1

	def set_exec_count(self, exec_count):
		self.exec_count = exec_count

	def get_cmdline_str(self, totalpassed, totalfailed):
		if totalfailed == 0:
			totalfailed = 1
		if totalpassed == 0:
			totalpassed = 1

		if self.pass_count == 0 and self.fail_count == 0:
			# This line contributed nothing
			return ""

		# Determine color
		fail_ratio = float(self.fail_count) / totalfailed
		# print "Fail ratio: ", fail_ratio, " totalpassed: ", totalpassed, " totalfailed: ", totalfailed, " self.passed: ", self.pass_count, " self.failed: ", self.fail_count
		#raw_input("How do those numbers look?")
		suspiciousness = (fail_ratio) / ((float(self.pass_count) / totalpassed) + (fail_ratio))
		get_color = color_default
		if suspiciousness >= 0.75:
			get_color = color_red
		elif suspiciousness >= 0.5:
			get_color = color_yellow
		else :
			get_color = color_green
		
		# Format output
		out_str = "%d: %f (%d, %d)\t-- %s" % (self.line_no, suspiciousness, self.pass_count, self.fail_count, self.text)
		#print out_str
		#raw_input("Does that str have the strange whitespace?")
		out_str = get_color(out_str)
		return out_str

def color_red(input_str):
	return "\x1b[0;31m" + input_str + "\x1b[0m"

def color_yellow(input_str):
	return "\x1b[0;33m" + input_str + "\x1b[0m"

def color_green(input_str):
	return "\x1b[0;32m" + input_str + "\x1b[0m"

def color_default(input_str):
	return "\x1b[0m" + input_str

def run_tarantula(tests):
	src_file = tests.get_gcov_file()

	cmd = "gcov " + src_file
	print "Running '" + cmd + "'"
	if subprocess.call(["gcov", src_file]) == 0:
		print "Gcov returned success!"
	else:
		print "Gcov initial run failed!"
		sys.exit(1)

	# Iterate through the gcov file and record the line of the src
	#	file with line number and 0 failing and passing test cases
	#	and zero coverage counts
	result_file_name = src_file + ".gcov"
	taran_lines = {}
	gcov_lines = interpret_gcov_file(result_file_name)
	for line in gcov_lines:
		taran_lines[line[0]] = taran_line(line[2], line[0], exec_count=line[1])

	#print "taran_lines: ", taran_lines
	#raw_input("How do those lines look?")

	# Run tests
	totalfailed = 0
	totalpassed = 0
	while tests.next_test():
		test_result = tests.run_test()
		if test_result:
			totalpassed += 1
		else:
			totalfailed += 1
		
		subprocess.call(["gcov", src_file])
		gcov_lines = interpret_gcov_file(result_file_name)
		for line in gcov_lines:
			if line[1] > taran_lines[line[0]].exec_count:
				taran_lines[line[0]].set_exec_count(line[1])
				if test_result:
					# Test passed
					#print "Line passed: ", line[2]
					#print "Line no: ", line[0], " exec_count_new: ", line[1], " exec_count_old: ", taran_lines[line[0]].exec_count
					taran_lines[line[0]].inc_passed()

				else:
					# Test failed
					taran_lines[line[0]].inc_failed()

	# Pretty print the results
	for key in taran_lines:
		out_str = taran_lines[key].get_cmdline_str(totalpassed, totalfailed)
		if out_str != "":
			print out_str

# Returns, (line_no, exec_cnt, text)
def interpret_gcov_file(filename):
	result_file = open(filename, "r")
	gcov_lines = []
	for line in result_file:
		gcov_row = line.split(':')
		line_no = 0
		exec_count = 0
		try:
			line_no = int(gcov_row[1].strip())
		except:
			print "Could not convert line number '", gcov_row[1], "'"
			sys.exit(1)

		try:
			exec_count = int(gcov_row[0])
		except:
			# If it's not convertable, set it to zero
			exec_count = 0

		if line_no == 0:
			continue
		# Exclude the newline in the gcov text
		gcov_lines.append((line_no, exec_count, gcov_row[2][:-1]))
	
	return gcov_lines
