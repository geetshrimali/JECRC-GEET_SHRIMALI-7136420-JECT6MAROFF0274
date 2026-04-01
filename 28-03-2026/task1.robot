*** Settings ***
Documentation  handling dropdowns
Library  SeleniumLibrary


*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
handle dropdown
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1

    Page Should Contain List    id=colors

    Mouse Over    id=colors
    Sleep    1

    Select From List By Label    id=colors  Blue  Green
#    Select From List By Label    id=colors  Blue
    
    @{selected}=  Get Selected List Labels    id=colors
    
    Log To Console    ${selected}
    Sleep    2