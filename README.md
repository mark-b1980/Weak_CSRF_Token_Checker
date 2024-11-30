
# Weak CSRF token tester

Script to identify weak CSRF tokens based on known values.

## Usage

```
markb@parrot$ ./weak_token_checker.py

░█░█░█▀▀░█▀█░█░█░░░█▀▀░█▀▀░█▀▄░█▀▀░░░▀█▀░█▀█░█▀█░█░█░█▀▀░█▀█░░░▀█▀░█▀▀░█▀▀░▀█▀░█▀▀░█▀▄
░█▄█░█▀▀░█▀█░█▀▄░░░█░░░▀▀█░█▀▄░█▀▀░░░░█░░█░█░█░█░█▀▄░█▀▀░█░█░░░░█░░█▀▀░▀▀█░░█░░█▀▀░█▀▄
░▀░▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░▀░▀░░░░░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀ v.1.0

Enter user ID or leave blank for unknown value: 123  
Enter user loginname or leave blank for unknown value: markb
Enter user email or leave blank for unknown value: ibetyouwould@like-to-have.it
Enter CSRF token: 83e2e9cbbfa2b6b40bea6db1f00a5d3b

[-] TESTING :: ID                                      == FAIL!
[-] TESTING :: loginname                               == FAIL!
[-] TESTING :: email                                   == FAIL!
[-] TESTING :: date('YYYY-MM-DD')                      == FAIL!
[-] TESTING :: ID+loginname                            == FAIL!
[-] TESTING :: ID+' '+loginname                        == FAIL!
[-] TESTING :: ID+','+loginname                        == FAIL!
...
[-] TESTING :: loginname+'-'+ID+'-'+date('YYYY-MM-DD') == FAIL!
[-] TESTING :: loginname+'/'+ID+'/'+date('YYYY-MM-DD') == FAIL!
[+] TESTING :: loginname+'|'+ID+'|'+date('YYYY-MM-DD') == md5(loginname+'|'+ID+'|'+date('YYYY-MM-DD'))
DONE!
```