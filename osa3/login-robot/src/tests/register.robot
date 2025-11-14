*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input  kalle
    Input  kalle123!
    Run Application
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User    kalle    esimerkki123
    Input New Command
    Create User    kalle    jokuUusi123
    Run Application
    Output Should Contain    Username already exists


Register With Too Short Username And Valid Password
    Input New Command
    Create User    ka    salasana123!
    Run Application
    Output Should Contain    Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Create User    k@ll#    Salasana123!
    Run Application
    Output Should Contain    Invalid username

Register With Valid Username And Too Short Password
    Input New Command
    Create User    matti    aa
    Run Application
    Output Should Contain    Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Create User    maija    abcdefghij
    Run Application
    Output Should Contain    Password must not contain only letters
