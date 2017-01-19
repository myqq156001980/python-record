import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('host', 22, 'user', 'password')

stdin, stdout, stderr=ssh.exec_command('command')
