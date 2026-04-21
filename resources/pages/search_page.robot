*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/search_pg_loc.robot

*** Keywords ***
Search
    Wait Until Element Is Visible    ${search}
    Click Element    ${search}
    Sleep    1s
#    Wait Until Element Is Visible    ${searchbar}
#    Click Element    ${searchbar}
    Input Text    ${searchbar}    red
    Sleep    2s
    Press Keys    ${searchbar}    ENTER
    Sleep   3s
    Page Should Contain    Kumkum Red Socks