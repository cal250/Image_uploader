import os
import time
import subprocess
import shutil

# Configuration
source_folder = r'C:\Users\pc\Desktop\embedded_hm\captured'
uploaded_folder = r'C:\Users\pc\Desktop\embedded_hm\Uploaded'
upload_url = 'https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php'

# Ensure the uploaded folder exists
if not os.path.exists(uploaded_folder):
    os.makedirs(uploaded_folder)

# Monitor folder
while True:
    for filename in os.listdir(source_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Add more extensions if needed
            file_path = os.path.join(source_folder, filename)

            # Wait for 30 seconds
            time.sleep(30)

            # Upload the file using curl with --ssl-no-revoke
            try:
                result = subprocess.run(
                    ['curl', '-X', 'POST', '-F', f'imageFile=@{file_path}', '--ssl-no-revoke', upload_url],
                    check=True,
                    capture_output=True,
                    text=True
                )
                print(f'Successfully uploaded {filename}: {result.stdout}')

                # Move the file to the uploaded folder
                shutil.move(file_path, os.path.join(uploaded_folder, filename))

            except subprocess.CalledProcessError as e:
                print(f'Failed to upload {filename}: {e.stderr}')

    # Sleep for a while before checking the folder again
    time.sleep(10)
