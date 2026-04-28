*** Settings ***
Library           RequestsLibrary
Library           Collections
Library           JSONLibrary

*** Variables ***
${base_url}    https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
    [Documentation]    Add a new pet to the store
    Create Session    petapi    ${base_url}  verify=True
    ${payload}=   Load Json From File    ${CURDIR}/../data/add_pet.json
    ${response}=    Post On Session    petapi    /pet  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}
    Log To Console    ${body}
    Log To Console    ${response.status_code}

Update existing pet
    [Documentation]    Add a new pet to the store
    Create Session    petapi    ${base_url}  verify=True
    ${payload}=   Load Json From File    ${CURDIR}/../data/update_pet.json
    ${response}=    PUT On Session    petapi    /pet  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}
    Log To Console    ${body}
    Log To Console    ${response.status_code}

    Set Suite Variable    ${pet_id}    ${body}[id]

Find pet by ID
    [Documentation]    Find pet by ID
    Create Session    petapi    ${base_url}  verify=True
    ${response}=    GET On Session    petapi    /pet/${pet_id}
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    Log To Console    ${body}
    Log To Console    ${response.status_code}

Find pet by Status
    [Documentation]    Find pet by ID
    Create Session    petapi    ${base_url}  verify=True
    ${qp}=   Create Dictionary    status=available
    ${response}=    GET On Session    petapi    /pet/findByStatus  params=${qp}
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    Log To Console    ${body}
    Log To Console    ${response.status_code}

Upload an image
    [Documentation]    Upload an image
    Create Session    petapi    ${base_url}  verify=True

    ${form_data}=   Create Dictionary    additionalMetadata=Pillu img

    ${file_path}=  Set Variable  ${CURDIR}/../data/New_Courage.jpg
    ${file}=  Create Dictionary    file=${file_path}

    ${response}=    POST On Session    petapi    /pet/${pet_id}/uploadImage  data=${form_data}  files=${file}
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    Log To Console    ${body}
    Log To Console    ${response.status_code}

Update with form data
    [Documentation]    Update pet with form data
    Create Session    petapi    ${base_url}  verify=True

    ${form_data}=   Create Dictionary    name=NewPillu status=sold

    ${response}=    POST On Session    petapi    /pet/${pet_id}  data=${form_data}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    pet updated

Delete pet by ID
    [Documentation]    Delete pet by ID
    Create Session    petapi    ${base_url}  verify=True
    ${response}=    DELETE On Session    petapi    /pet/${pet_id}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    pet deleted

