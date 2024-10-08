
How to change the php.ini file using ssh and python with fabric

@startuml
start

:define logindata;
:startsSSH();
if (logindata correct?) then (yes)
    :get keywords from php.ini();
    if (is the keyword string == empty?) then (no)
        if (do the keywords have the correct values) then (yes)
            stop
        else (no)
            :change keywords;
            stop
        endif
    else (yes)
        :throw specific exception;
        stop
    endif
else (no)
    :throw specific exception;
    stop
endif
@enduml