*** Settings ***
Library  SeleniumLibrary
Library  ../config/env_loader.py
Library  env_loader

*** Variables ***
${BROWSER}  chrome
${ENV}  qa

*** Keywords ***

Load Environment
    Load Env  ${ENV}

    ${url}=  Get Env    baseurl
    ${mail}=  Get Env    user_email
    ${pwd}=  Get Env    user_password

    Set Global Variable  ${BASE_URL}  ${url}
    Set Global Variable  ${USER_EMAIL}  ${mail}
    Set Global Variable  ${USER_PWD}  ${pwd}

open app
    [Documentation]  opens the application
    Open Browser  ${BASE_URL}  ${BROWSER}
    Maximize Browser Window

close app
    Close All Browsers