*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  newuser  validpass123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  validpass123
    Output Should Contain  Username already in use

Register With Too Short Username And Valid Password
    Input Credentials  aa  validpass123
    Output Should Contain  Username should have at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  username!  validpass123
    Output Should Contain  Username can only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  newuser  short
    Output Should Contain  Password should have at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  newuser  eightormore
    Output Should Contain  Password should contain at least one non-letter character
