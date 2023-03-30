# sync_folders
This Python script is designed to keep two directories in sync by copying any new or modified files from the source directory to the destination directory, while also deleting any files or folders that have been deleted in the source directory.

The script takes in four command line arguments:

- The source directory to be synced
- The destination directory where changes will be made
- The time interval in seconds for the script to run periodically
- The file path to write logs of the synchronization process

The sync function is responsible for copying files and folders from the source directory to the destination directory and deleting files and folders that no longer exist in the source directory.

The syncInterval function is responsible for running the sync function at a specified interval. It takes in the same arguments as the script itself.

The log function is used to print messages to the console and write messages to the log file specified in the command line arguments.

To use the script, open a terminal or command prompt and navigate to the directory containing the script. Then run the script with the following command:

- python sync_folders.py source_directory destination_directory time_interval log_file_path

Replace source_directory and destination_directory with the absolute paths of the directories you want to sync. Replace time_interval with an integer value representing the time in seconds that you want the script to run periodically. Replace log_file_path with the absolute path of the file where you want to write the log messages.

For example:

- python sync.py /home/user/Documents /home/user/backup 60 /home/user/sync_log.txt

This will sync the Documents directory to the backup directory every 60 seconds and write log messages to sync_log.txt.
