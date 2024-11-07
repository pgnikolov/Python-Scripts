# Automated File Explorer

This Python script searches a specified folder for all files, regardless of file type, within its directory and
subdirectories. It outputs the paths of all files found and also lists all unique file extensions present in the folder.
The script uses Python's pathlib module, which is cross-platform and simplifies working with file paths.

# Features:

File Path Finder: The script scans a folder and lists the file paths of all files it finds within the specified
directory and its subdirectories.
Unique File Extension Lister: The script identifies all unique file extensions present in the folder, displaying them in
lowercase format.
Requirements:
Python 3.x

# How to Use:
Set the Folder Path: Replace 'Place the folder path here under quotes' in the script with the path to the folder you
want to scan:

```bash
all_files_path = pathlib.Path('path/to/your/folder')
```

Save the script as file_finder.py (or another name of your choice).
Open your terminal or command prompt.
Navigate to the folder containing the script and run it with:
```bash
python3 file_finder.py
```
Example Output:
The script will output two lists:

The first list contains the paths of all files found within the specified folder and its subdirectories.
The second list contains all unique file extensions in the folder, displayed in lowercase.
Example output:

plaintext
Copy code
[  
"path/to/folder/document.txt",  
"path/to/folder/image.jpg",  
"path/to/folder/subfolder/script.py"
]
[  
".txt",  
".jpg",  
".py"
]

# Algorithm change

```python
# Current: Two separate loops
file_paths = []
file_extensions = set()

# Loop 1: Collect all file paths
for file in all_files_path.rglob('*'):
    if file.is_file():
        file_paths.append(str(file))

# Loop 2: Collect file extensions
for file in all_files_path.rglob('*'):
    if file.is_file():
        ext = file.suffix.lower()
        if ext:
            file_extensions.add(ext)

# Optimized: Single loop to collect both file paths and extensions
file_paths = []
file_extensions = set()

for file in all_files_path.rglob('*'):
    if file.is_file():
        # Collect file path
        file_paths.append(str(file))
        
        # Collect file extension
        ext = file.suffix.lower()
        if ext:
            file_extensions.add(ext)

# Format and output
formatted_file_paths = '[\n' + ',\n'.join(f'  "{path}"' for path in file_paths) + '\n]'
formatted_file_extensions = '[\n' + ',\n'.join(f'  "{ext}"' for ext in sorted(file_extensions)) + '\n]'
print(formatted_file_paths)
print(formatted_file_extensions)
```
## Explanation:

1. Single Traversal: The optimized version only traverses the directory once, which should yield a performance gain, particularly in directories with a large number of files.
2. Timing Entire Function Execution: By timing the function call itself, we capture the complete execution time, including the traversal and formatting steps.
3. Checking for Zero Division: The code includes a check to avoid dividing by zero if the original version’s time is negligible (although this is rare in practical applications).

# Test

```python
import pathlib
import time

all_files_path = pathlib.Path('/home/pgnikolov/Desktop/github/SoftUni-Advance')

# Function for the original version
def original_version():
    file_paths = []
    for file in all_files_path.rglob('*'):
        if file.is_file():
            file_paths.append(str(file))
    formatted_outputpath = '[\n' + ',\n'.join(f'  "{path}"' for path in file_paths) + '\n]'

    file_extensions = ['md']
    for file in all_files_path.rglob('*'):
        if file.is_file():
            ext = file.suffix.lower()
            if ext and ext not in file_extensions:
                file_extensions.append(ext)
    formattedd_outputext = '[\n' + ',\n'.join(f'  "{ext}"' for ext in file_extensions) + '\n]'

    return formatted_outputpath, formattedd_outputext

# Function for the optimized version
def optimized_version():
    file_paths = []
    file_extensions = set()
    for file in all_files_path.rglob('*'):
        if file.is_file():
            file_paths.append(str(file))
            ext = file.suffix.lower()
            if ext:
                file_extensions.add(ext)

    formatted_file_paths = '[\n' + ',\n'.join(f'  "{path}"' for path in file_paths) + '\n]'
    formatted_file_extensions = '[\n' + ',\n'.join(f'  "{ext}"' for ext in sorted(file_extensions)) + '\n]'

    return formatted_file_paths, formatted_file_extensions

# Timing and executing both versions
start_time = time.time()
original_result = original_version()
original_duration = time.time() - start_time
print(f"Original version took: {original_duration:.4f} seconds")

start_time = time.time()
optimized_result = optimized_version()
optimized_duration = time.time() - start_time
print(f"Optimized version took: {optimized_duration:.4f} seconds")

# Compare the performance
if original_duration > 0:
    improvement = ((original_duration - optimized_duration) / original_duration) * 100
    print(f"Performance improvement: {improvement:.2f}% faster")
else:
    print("Performance improvement could not be calculated (division by zero).")

```
Additional Considerations:
Multithreading: If the directory structure is very large and you want to speed things up even more, you could divide the work across multiple threads. Here’s an example of using the concurrent.futures module to achieve parallelism:

```python
import concurrent.futures

def find_files_in_directory(path):
    file_paths = []
    file_extensions = set()
    for file in pathlib.Path(path).rglob('*'):
        if file.is_file():
            file_paths.append(str(file))
            ext = file.suffix.lower()
            if ext:
                file_extensions.add(ext)
    return file_paths, file_extensions

# Using a ThreadPoolExecutor for parallel processing
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_dir = {executor.submit(find_files_in_directory, dir_path): dir_path for dir_path in all_files_path.iterdir()}
    for future in concurrent.futures.as_completed(future_to_dir):
        file_paths, file_extensions = future.result()
```

