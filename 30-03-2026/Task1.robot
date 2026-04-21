*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling windows
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2
    Scroll Element Into View    xpath=//button[@id="PopUp"]
    Wait Until Element Is Visible    xpath=//button[@id = "PopUp"]
    Click Element    xpath=//button[@id = "PopUp"]
    Sleep    2

    @{windows}  Get Window Handles

    Switch Window    NEW
    @{titles}  Get Window Titles
    Log To Console    ${titles}

    Switch Window  ${windows}[0]
    @{titles}  Get Window Titles
    Log To Console    ${titles}

    Page Should Contain   Automation Testing Practice

    Sleep    2

