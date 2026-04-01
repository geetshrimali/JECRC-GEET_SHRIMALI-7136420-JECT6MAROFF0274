*** Settings ***
Documentation  action-chains
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***

Handling drag & drop
    [Documentation]  action-chains
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath = //a[text() = "Drag and Drop"]
    Sleep    1
    Drag And Drop    id = column-a    id = column-b
    Sleep    2

    Close Browser

Hover
    [Documentation]  Hover
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath = //a[text() = "Hovers"]
    Sleep    1
    Mouse Over    (//img[@alt = 'User Avatar'])[2]
    Sleep    2

    Close Browser

Scroll-To
    [Documentation]  Scroll
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Scroll Element Into View    xpath = //a[text() = "Typos"]
    Sleep    1

    Close Browser