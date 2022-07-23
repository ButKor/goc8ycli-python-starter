import json
import subprocess
import os


# Redirect go-c8y to your tenant via ENVVARs
os.environ["C8Y_HOST"] = "https://example.cumulocity.com"
os.environ["C8Y_TENANT"] = "t1234"
os.environ["C8Y_USER"] = "korbinian.butz@softwareag.com"
os.environ["C8Y_PASSWORD"] = "secret-password"
os.environ["C8Y_SETTINGS_CI"] = "TRUE"


# OPTION 1: A simple GET command using subprocess.run()
output = subprocess.run(["c8y", "devices", "list"], capture_output=True)
print('return code: ', output.returncode)
print('stdout: ', output.stderr.decode("utf-8") )
print('stderr: ', output.stdout.decode('utf-8'))


# OPTION 2: Chain a command with static text using subprocess.Popen (e.g. echo 'device_a\ndevice_b' | c8y devices create --dry')
cmd = 'c8y devices create --dry'
cmd_call = subprocess.Popen(cmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, errors = cmd_call.communicate(input="device_a\ndevice_b\n")
cmd_call.wait()
print('return code: ', cmd_call.returncode)
print('stdout: ', output)
print('stderr: ', errors)


# OPTION 3: Run any chained command using Popen
cmd = 'seq -f "device_%05g" 1 2 | c8y devices create --dry'
with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as process:
    output, error = process.communicate()
    print('return code: ', process.returncode)
    print('stdout: ', 'none' if output == '' else output.decode('utf-8'))
    print('stderr: ', 'none' if error == '' else error.decode('utf-8') )
    
