*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input New Command
    Input   new   

Input Register Command
    Input   Register

Input New Command And Create User
    Create User  kalle  esimerkki123 
    Input Register Command      

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
