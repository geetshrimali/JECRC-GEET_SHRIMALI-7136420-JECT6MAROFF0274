*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/login_pg_loc.robot

*** Keywords ***
login
    [Arguments]  ${email}  ${pwd}

    Input Text    ${mail}    ${email}
    Sleep    1
    Log    entering mail

    Input Text    ${pass}    ${pwd}
    Sleep    1
    Log    entering password

    Wait Until Element Is Enabled    ${button}
    Sleep    2
    Click Element    ${button}
    Log    Submit
