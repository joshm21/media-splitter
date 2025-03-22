import os
import csv
import subprocess

# Function to run the ffmpeg command to split the media file
def split_file(input_file, start_time, end_time, output_file):
    # Use subprocess.Popen to allow real-time output display from ffmpeg
    command = [
        'ffmpeg', '-i', input_file, '-ss', str(start_time), '-to', str(end_time), '-c', 'copy', output_file
    ]

    # Run the command and display ffmpeg's output in real time
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Read and print both stdout and stderr streams
    for stdout_line in iter(process.stdout.readline, b''):
        print(stdout_line.decode(), end='')  # Decode and print stdout
    for stderr_line in iter(process.stderr.readline, b''):
        print(stderr_line.decode(), end='')  # Decode and print stderr

    process.stdout.close()
    process.stderr.close()
    process.wait()

# Main function to process all CSV files in the current directory
def process_csv_files():
    folder_path = os.getcwd()

    # Loop through all CSV files in the current directory
    for csv_file in os.listdir(folder_path):
        if csv_file.endswith('_splits.csv'):
            print(f"\033[93mProcessing CSV file: {csv_file}\033[0m")

            # Extract the base name of the CSV (remove the _splits.csv part)
            base_name = csv_file.replace('_splits.csv', '')

            # Open the CSV file and read the first row to get the file extension from the Name field
            with open(csv_file, mode='r') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Read the header row
                first_row = next(csv_reader)  # Read the first data row

                # Extract the extension from the Name field of the first row
                name = first_row[3]  # Assuming the 4th column is the Name field
                input_extension = os.path.splitext(name)[1][1:]  # Get the extension without the dot

                # Define the input file using the base name and the extension from the first row
                input_file = f"{base_name}.{input_extension}"

                # Check if the corresponding input file exists
                if not os.path.exists(input_file):
                    print(f"\033[91mInput file '{input_file}' not found for CSV: {csv_file}\033[0m")
                    continue

                # Now process each row in the CSV
                file.seek(0)  # Go back to the start of the CSV file to process all rows
                next(csv_reader)  # Skip the header row again

                for row in csv_reader:
                    if len(row) >= 4:
                        split_num, start_time, end_time, name = row
                        try:
                            split_num = int(split_num)  # Ensure split_num is an integer
                            start_time = float(start_time)
                            end_time = float(end_time)

                            # Make sure the output file name is valid
                            output_file = os.path.join(folder_path, name)

                            # Run the ffmpeg command to split the file
                            print(f"\033[93mProcessing split #{split_num}: {start_time} to {end_time}, output file: {output_file}\033[0m")
                            split_file(input_file, start_time, end_time, output_file)
                        except ValueError as e:
                            print(f"\033[91mSkipping invalid row: {row} (Error: {e})\033[0m")
                    else:
                        print(f"\033[91mSkipping invalid row: {row} (Row does not have 4 fields)\033[0m")

if __name__ == "__main__":
    process_csv_files()

