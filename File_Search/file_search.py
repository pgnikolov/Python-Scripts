import pathlib

# Specify the folder path here
all_files_path = pathlib.Path('Place the folder path here under quotes')
file_paths = []
file_extensions = set()  # Use a set to keep unique extensions

# Traverse files once and collect paths and extensions
for file in all_files_path.rglob('*'):
    if file.is_file():
        file_paths.append(str(file))
        ext = file.suffix.lower()
        if ext:
            file_extensions.add(ext)

# Format output for file paths
formatted_file_paths = '[\n' + ',\n'.join(f'  "{path}"' for path in file_paths) + '\n]'
print(formatted_file_paths)

# Format output for file extensions
formatted_file_extensions = '[\n' + ',\n'.join(f'  "{ext}"' for ext in sorted(file_extensions)) + '\n]'
print(formatted_file_extensions)
