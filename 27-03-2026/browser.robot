*** Settings ***
Documentation
Library   SeleniumLibrary
*** Variables ***
${url}  https://www.cricbuzz.com/   #scalar var

@{bikes}  ktm  kawasaki  honda  pulsar   #list var

&{cars}   nissan=gtr  honda=civic  bmw=m4   #dict var




*** Test Cases ***
Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke
    Open Browser  ${url}  headlesschrome
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    ${bikes}[1]&${bikes}[2]          #navigated to cricbuzz
    Log To Console    ${cars.bmw}
    Sleep    3s

    Close Browser


Opening firefox Browser
    [Documentation]   firefox browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  firefox
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s

    Close Browser


#Opening edge Browser
#    [Documentation]  edge browser navigating to https://www.cricbuzz.com/
#    Open Browser  https://www.cricbuzz.com/  edge
#    Maximize Browser Window
#
#    Log    navigated to cricbuzz
#    Log To Console    navigated to cricbuzz
#    Sleep    3s
#    Close Browser


open cricbuzz in edge
    [Tags]  req
    Opening edge Browser


*** Keywords ***
Opening edge Browser
    [Documentation]  edge browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  edge
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s

#robot -d reports -t "Opening Chrome Browser" browser.robot
#robot -d reports -i "smoke" browser (grouping)
