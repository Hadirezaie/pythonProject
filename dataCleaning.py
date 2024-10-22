dupFile_path = 'E:/dup.txt'  # Values to remove
newFile_path = 'E:/1M.txt'    # File to filter

# Read values from dup.txt, ignoring the header
with open(dupFile_path, 'r') as file1:
    # Skip the header and read only the iccid values
    next(file1)  # Skip the header line
    values_to_remove = set(line.split(',')[0].strip() for line in file1)

# Read values from 1M.txt and filter out the duplicates
with open(newFile_path, 'r') as file2:
    # Skip the header line in 1M.txt as well
    header = next(file2)  # Read and store the header line
    filtered_values = [header]  # Start with the header
    filtered_values += [line for line in file2 if line.strip() not in values_to_remove]

# Write the filtered values back to 1M.txt
with open(newFile_path, 'w') as file2:
    file2.writelines(filtered_values)

print("Values removed successfully.")
