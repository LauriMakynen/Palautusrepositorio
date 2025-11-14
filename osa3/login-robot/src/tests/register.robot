*** Settings ***
Resource    resource.robot
Test Setup    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    kalle    kalle123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    Markus    Makke123
    Output Should Contain    Username already exists

Register With Too Short Username And Valid Password
    Input Credentials    ka    salasana123!
    Output Should Contain    Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    k@ll#    Salasana123!
    Output Should Contain    Username contains special characters which are not allowed

Register With Valid Username And Too Short Password
    Input Credentials    matti    aa
    Output Should Contain    Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    maija    abcdefghij
    Output Should Contain    Password must contain at least one number or special character