This project automates the process of retrieving the Raspberry Pi’s IP address for SSH access.
When the Raspberry Pi boots up, it runs a script that automatically sends you a message with its IP address via a Telegram bot, eliminating the need for manual checking.
I wrote it in Python for the automation process, then I edited the cron job to run the script by scheduling the task.

< Here's the overall process >

1. If you haven't installed the dependencies, install them.
   
   "pip install requests"
   
2. Write the automation script in Python and keep it in your Raspberry Pi.
   
   -> You'll need your own Telegram Bot Token and chat ID.

3. Edit the cron job to execute it initially.
   
   "crontab -e"
   
   -> In the last line, write "@reboot /usr/bin/python3 /path_to_your_script"

4. Execute the script to check if it works as expected.

   "python your_script.py"
