*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2

    Mouse Over    xpath=//button[@onclick="return popup()"]

    Click Button    xpath=//button[@onclick="myFunctionAlert()"]
    Handle Alert
    ${text}=    Get Text    xpath=//p[@id='demo']
    Page Should Contain    ${text}
    Log To Console    ${text}
    Sleep    2

    Click Button    xpath=//button[@onclick="myFunctionConfirm()"]
    Handle Alert
    ${text}=    Get Text    xpath=//p[@id='demo']
    Page Should Contain    ${text}
    Log To Console    ${text}


    Click Button    xpath=//button[@onclick="myFunctionPrompt()"]
    
    Input Text Into Alert    hueeue
    ${text}=    Get Text    xpath=//p[@id='demo']
    Page Should Contain    ${text}
    Log To Console    ${text}

    Close Browser


