*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/login_pg_loc.robot

*** Keywords ***
login
    [Arguments]  ${email}  ${pwd}

    Input Text    ${mail}    ${email}
    Log    entering mail

    Input Text    ${pass}    ${pwd}
    Log    entering password

    Wait Until Element Is Enabled    ${button}
    Sleep    2
    Click Element    ${button}
    Log    Submit
