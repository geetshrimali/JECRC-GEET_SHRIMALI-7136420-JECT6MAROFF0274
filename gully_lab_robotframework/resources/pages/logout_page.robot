*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/logout_pg_loc.robot
Resource  ../../locators/home_pg_loc.robot

*** Keywords ***
logout
    Wait Until Element Is Visible    ${account}
    Click Element    ${account}
    Sleep    3
    Wait Until Element Is Visible    ${logout}
    Click Element    ${logout}
    Sleep    3
    Log    logout button clicked