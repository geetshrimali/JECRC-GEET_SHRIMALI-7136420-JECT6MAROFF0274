*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***

Handling Checkbox
    [Documentation]  automation
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Page Should Contain Checkbox     xpath = //input[@id = 'sunday']

    Select Checkbox    xpath = //input[@id = 'sunday']

    Sleep    2s

    Select Radio Button    gender    male

    Sleep    2s


    Close Browser