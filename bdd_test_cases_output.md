```markdown
### BDD Scenarios

#### Scenario: Successful login with valid credentials
  - **Severity**: High
  Given the user is on the login page
  When the user enters valid username and password
  And clicks on the login button
  Then the user should be redirected to the dashboard

#### Scenario: Login with invalid username and password
  - **Severity**: High
  Given the user is on the login page
  When the user enters invalid username and password
  And clicks on the login button
  Then the user should see an error message indicating invalid credentials

#### Scenario: Login with empty username and password
  - **Severity**: Medium
  Given the user is on the login page
  When the user leaves both username and password fields empty
  And clicks on the login button
  Then the user should see an error message prompting to fill in both fields

#### Scenario: Login with valid username and empty password
  - **Severity**: Medium
  Given the user is on the login page
  When the user enters a valid username and leaves the password field empty
  And clicks on the login button
  Then the user should see an error message indicating password is required

#### Scenario: Login with valid password and empty username
  - **Severity**: Medium
  Given the user is on the login page
  When the user enters a valid password and leaves the username field empty
  And clicks on the login button
  Then the user should see an error message indicating username is required

#### Scenario: Login with locked account
  - **Severity**: High
  Given the account is locked due to multiple failed login attempts
  When the user tries to login with the locked account
  Then the user should see an error message indicating the account is locked
```