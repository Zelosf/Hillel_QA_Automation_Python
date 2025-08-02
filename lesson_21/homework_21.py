from datetime import datetime
import re


def analyze_heartbeat(log_path: str, result_path: str, key: str = "TSTFEED0300|7E3E|0400"):
	time_sample = r"Timestamp (\d{2}:\d{2}:\d{2})"
	timestamps = []

	with open(log_path, "r") as file:
		for line in file:
			if key in line:
				match = re.search(time_sample, line)
				if match:
					timestamp_str = match.group(1)
					timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")
					timestamps.append((timestamp_str, timestamp))

	log_output = []
	for i in range(len(timestamps) - 1):
		curr_str, curr = timestamps[i]
		next_curr_str, next_curr = timestamps[i + 1]
		delta = (curr - next_curr).total_seconds()

		if 31 < delta < 33:
			log_output.append(f"In the interval from {curr_str} to {next_curr_str} - WARNING: Heartbeat delta {delta:.0f} sec\n")
		elif delta >= 33:
			log_output.append(f"In the interval from {curr_str} to {next_curr_str} - ERROR: Heartbeat delta {delta:.0f} sec\n")

	with open(result_path, "w") as out_file:
		out_file.writelines(log_output)

	print(f"Завершено.")


log_file = "hblog.txt"
output_file = "hb_test.log"
#key = "TSTFEED0015|7E3E|0400"
analyze_heartbeat(log_file, output_file)
