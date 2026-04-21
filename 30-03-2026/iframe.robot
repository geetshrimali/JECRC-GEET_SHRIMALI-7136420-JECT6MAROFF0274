*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling iframes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2
    Click Element    xpath=//a[text() = "Iframe with in an Iframe"]

    Select Frame    xpath=//iframe[@src='MultipleFrames.html']
    Select Frame    xpath=//iframe[@src='SingleFrame.html']

    Input Text    xpath=//input[@type="text"]    Knight
    Sleep    3
    Unselect Frame

    Close Browser