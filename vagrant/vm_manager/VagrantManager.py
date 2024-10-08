import vagrant

v = vagrant.Vagrant()
out = v.up(vm_name="task2", stream_output=True)
for s in out:
    if "Flag:" in s:
        flag = s[s.find("Flag:") + len("Flag: "):]
        print("Flag: ", flag, end="")
    if "Generated password for vagrant:" in s:
        passw = s[s.rfind("Generated password for vagrant:") + len("Generated password for vagrant: "):]
        print("Password: ", passw, end="")

print(v.status())
