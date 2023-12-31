# nice_coding_challenge


To execute the code, follow these steps:

     1. Save the code in a file named NiceTestApp.py on your computer (Windows/linux).
     2. Open a command prompt or terminal window.
     3. Navigate to the directory where you saved NiceTestApp.py
     4. Run the script by typing 'python NiceTestApp.py' and press Enter.

 You can also pass the command-line arguments. For example:

     # To display the information on the screen and log it to a file, use: 'python NiceTestApp.py -logInfo'
     # To display the information on the screen without logging, use: 'python NiceTestApp.py'
     # To display the help message, use: 'python NiceTestApp.py -help'

Prerequisites: Make sure you have Python installed on your system and the necessary dependencies (argparse and psutil) installed. If not, you can install them using pip:
```
pip install argparse psutil
```
The script will create a log file named NiceTestApp.log in the same directory as the NiceTestApp.py file if the -logInfo argument is specified.

NOTE: The fetch_top_cpu_processes() function works for linux machines only. \n
To test top processes consuming high resources you can use below command on your test linux environment. Running this command can consume significant CPU resources and generate a large amount of output since it generates MD5 hashes continuously. Be cautious when executing commands like this, as they may impact system performance and produce a large amount of output data.
```
nproc | xargs seq | xargs -n1 -P2 md5sum /dev/zero
```


SAMPLE OUPUT:
$ python3 NiceTestApp.py
```
Computer Name: WS-19860
Total Physical Memory: 12 Gb
Total Number of Physical Processors: 4
Total Number of Cores: 8
Total Number of Hard Disks: 5
Top 5 processes in terms of CPU:
        md5sum: 98.9%
        md5sum: 98.9%
        python3: 7.0%
        init: 0.0%
        init: 0.0%
```
