```markdown
### Test Cases

#### TCI-001
- **Title**: Successful login with valid credentials
- **Steps**:
  1. Navigate to the login page.
  2. Enter valid username and password.
  3. Click on the login button.
- **Expected Result**: User should be redirected to the dashboard.
- **Severity**: High

#### TCI-002
- **Title**: Login with invalid username and password
- **Steps**:
  1. Navigate to the login page.
  2. Enter invalid username and password.
  3. Click on the login button.
- **Expected Result**: User should see an error message indicating invalid credentials.
- **Severity**: High

#### TCI-003
- **Title**: Login with empty username and password
- **Steps**:
  1. Navigate to the login page.
  2. Leave both username and password fields empty.
  3. Click on the login button.
- **Expected Result**: User should see an error message prompting to fill in both fields.
- **Severity**: Medium

#### TCI-004
- **Title**: Login with valid username and empty password
- **Steps**:
  1. Navigate to the login page.
  2. Enter a valid username and leave the password field empty.
  3. Click on the login button.
- **Expected Result**: User should see an error message indicating password is required.
- **Severity**: Medium

#### TCI-005
- **Title**: Login with valid password and empty username
- **Steps**:
  1. Navigate to the login page.
  2. Enter a valid password and leave the username field empty.
  3. Click on the login button.
- **Expected Result**: User should see an error message indicating username is required.
- **Severity**: Medium

#### TCI-006
- **Title**: Login with locked account
- **Steps**:
  1. Simulate multiple failed login attempts to lock the account.
  2. Try to login with the locked account.
- **Expected Result**: User should see an error message indicating the account is locked.
- **Severity**: High
```