*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${down}  C:\\Users\\GEET SHRIMALI\\Downloads\\file.txt

*** Test Cases ***
File Upload
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href="/upload"]
    Sleep    2s
    ${path}  Normalize Path    ${CURDIR}/sample.text
    Choose File    id=file-upload    ${path}
    Sleep    3s
    Click Button    id=file-submit
    Sleep    3s
    Close Browser

File Download
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/download"]
    Sleep    2s

    Click Element    xpath=//a[@href="download/file.txt"]

    Wait Until Created    ${down}  timeout=10s

    File Should Exist    ${down}
    Log To Console    it downloaded successfully

    Close Browser
