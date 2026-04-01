*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/

*** Test Cases ***
Screenshots
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1
    Set Screenshot Directory    ${CURDIR}/Screenshots
    Capture Page Screenshot  ss.jpg
    Sleep    3
    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]  dhurandar.jpg
    Sleep    1
    Close Browser