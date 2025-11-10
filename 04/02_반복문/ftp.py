def help():
    help_msg = """
Commands may be abbreviated.  Commands are:

!               debug           mdir            sendport        site
$               dir             mget            put             size
account         disconnect      mkdir           pwd             status
append          exit            mls             quit            struct
ascii           form            mode            quote           system
bell            get             modtime         recv            sunique
binary          glob            mput            reget           tenex
bye             hash            newer           rstatus         tick
case            help            nmap            rhelp           trace
cd              idle            nlist           rename          type
cdup            image           ntrans          reset           user
chmod           lcd             open            restart         umask
close           ls              prompt          rmdir           verbose
cr              macdef          passive         runique         ?
delete          mdelete         proxy           send
    """
    print(help_msg)

def ls():
    pass

while True:
    cmd = input('ftp> ')
    if cmd == 'quit':
        break
    elif cmd == 'help':
        help()
    elif cmd == 'ls':
        ls()
    elif cmd == '':
        pass
    else:
        print("?Invalid command")