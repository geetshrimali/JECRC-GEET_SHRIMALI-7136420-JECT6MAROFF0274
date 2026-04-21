*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/home_pg_loc.robot

*** Keywords ***
account_tab
    Wait Until Element Is Visible    ${account}
    Click Element    ${account}
    Sleep    3
    Log    account button clicked

search_hmpg
    Wait Until Element Is Visible    ${search}
    Click Element    ${search}
    Sleep    3
    Log    search button clicked