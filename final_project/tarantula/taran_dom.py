import sys
import time
import tarantula
import subprocess

class DomTests:
	def __init__(self, test_file_name):
		test_file = open(test_file_name, "r")
		test_lines = test_file.readlines()

		test_text = "".join(test_lines)
		
		test_pieces = test_text.split("END_COMMON_HEADER")
		self.common_header = test_pieces[0]
		self.test_cases = test_text.split("taran_test")[1:]

		self.test_num = -1

	def get_gcov_file(self):
		return "dominion.c"

	def next_test(self):
		self.test_num += 1
		if self.test_num >= len(self.test_cases):
			return False
		return True

	def run_test(self):
		c_file = self.common_header
		c_file += "\n\nint main(int argc, char** argv) {"
		c_file += self.test_cases[self.test_num]
		c_file += "\n}"
		
		test_file_name = self.write_test_file(c_file)
		self.build_test(test_file_name)
		ret = subprocess.call(["./" + test_file_name + ".out"])
		
		subprocess.call(["rm", test_file_name, test_file_name + ".out", test_file_name + ".gcda", test_file_name + ".gcno"])
		if ret == 1:
			return False
		return True

	def write_test_file(self, c_file):
		now = str(int(time.time()))
		test_file_name = "taran_test_" + now + ".c"
		test_file = open(test_file_name, "w")
		test_file.write(c_file)
		test_file.close()

		return test_file_name
		

	def build_test(self, test_file_name):
		ret = subprocess.call(["gcc", "dominion.o", "-lm", "-g", "-fprofile-arcs", "-ftest-coverage", "-Wall", "-std=c99", "rngs.c", test_file_name, "-o",  test_file_name + ".out"])
		if ret == 0:
			print "Compilation for test %d successful!" % self.test_num
		else:
			print "Compilation for test %d failed." % self.test_num
			sys.exit(1)



if __name__ == "__main__":
	tests = DomTests("taran_tests.tt")

	tarantula.run_tarantula(tests)

