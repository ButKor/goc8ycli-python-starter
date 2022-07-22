import json
import subprocess
import os

# Redirect go-c8y to your tenant via ENVVARs
os.environ["C8Y_HOST"] = "https://example.cumulocity.com"
os.environ["C8Y_TENANT"] = "t1234"
os.environ["C8Y_USER"] = "korbinian.butz@softwareag.com"
os.environ["C8Y_PASSWORD"] = "secret-password"
os.environ["C8Y_SETTINGS_CI"] = "TRUE"

# Send 'c8y devices list' and read output
output = subprocess.run(["c8y", "devices", "list"], capture_output=True)
if output.returncode != 0:
    print('PANIC. Command did not succeed. Stderr:\n', output.stderr.decode("utf-8") )
else:
    print('Command succeeded. Stdout:\n', output.stdout.decode('utf-8'))

