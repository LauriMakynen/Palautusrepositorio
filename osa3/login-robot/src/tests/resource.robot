*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login
    
Input New Command
    Input  new

Input New Command And Create User
    Create User  kalle  esimerkki123
    Input New Command        

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
