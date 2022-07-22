import json
import subprocess
import os

# Redirect go-c8y to your tenant via ENVVARs
os.environ["C8Y_HOST"] = "https://example.cumulocity.com"
os.environ["C8Y_TENANT"] = "t1234"
os.environ["C8Y_USER"] = "korbinian.butz@softwareag.com"
os.environ["C8Y_PASSWORD"] = "secret-password"
os.environ["C8Y_SETTINGS_CI"] = "TRUE"


# A simple GET command
output = subprocess.run(["c8y", "devices", "list"], capture_output=True)
print('return code: ', output.returncode)
print('stdout: ', output.stderr.decode("utf-8") )
print('stderr: ', output.stdout.decode('utf-8'))


# Chain a command with static text (echo 'device_a\ndevice_b' | c8y devices create --dry')
cmd = 'c8y devices create --dry'
cmd_call = subprocess.Popen(cmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, errors = cmd_call.communicate(input="device_a\ndevice_b\n")
cmd_call.wait()
print('return code: ', cmd_call.returncode)
print('stdout: ', output)
print('stderr: ', errors)

