import subprocess

completed = subprocess.run(
    ["powershell", "-Command", "Get-ChildItem | Format-Table"])
print(type(completed))  # <class 'subprocess.CompletedProcess'>
# args ['powershell', '-Command', 'Get-ChildItem | Format-Table']
print("args", completed.args)
print("returncode", completed.returncode)  # returncode 0
print("stderr", completed.stderr)  # stderr None
print("stdout", completed.stdout)  # stdout None
