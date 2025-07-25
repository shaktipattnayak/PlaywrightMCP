# Manual Test Cases for OrangeHRM Login Suite

This document describes the manual test cases corresponding to the automated tests implemented in the project so far.

---

## 1. Login Success
**Automated Test:** `test_login_success`

- **Description:** Verify that a user can log in with valid credentials.
- **Steps:**
  1. Navigate to the OrangeHRM login page.
  2. Enter a valid username in the username field.
  3. Enter a valid password in the password field.
  4. Click the Login button.
- **Expected Result:**
  - User is redirected to the dashboard page.

---

## 2. Login with Invalid Username
**Automated Test:** `test_login_from_csv` (row: invalid_user, admin123)

- **Description:** Verify that login fails with an invalid username and valid password.
- **Steps:**
  1. Navigate to the OrangeHRM login page.
  2. Enter an invalid username in the username field.
  3. Enter a valid password in the password field.
  4. Click the Login button.
- **Expected Result:**
  - An error message "Invalid credentials" is displayed.

---

## 3. Login with Invalid Password
**Automated Test:** `test_login_from_csv` (row: Admin, invalid_pass)

- **Description:** Verify that login fails with a valid username and invalid password.
- **Steps:**
  1. Navigate to the OrangeHRM login page.
  2. Enter a valid username in the username field.
  3. Enter an invalid password in the password field.
  4. Click the Login button.
- **Expected Result:**
  - An error message "Invalid credentials" is displayed.

---

## 4. Login with Empty Fields
**Automated Test:** `test_login_from_csv` (row: empty username and password)

- **Description:** Verify that login fails when both username and password fields are empty.
- **Steps:**
  1. Navigate to the OrangeHRM login page.
  2. Leave the username and password fields empty.
  3. Click the Login button.
- **Expected Result:**
  - A validation message "Required" is displayed for the empty fields.

---

## 5. Forgot Password Link
**Automated Test:** `test_forgot_password_link`

- **Description:** Verify that clicking the "Forgot your password?" link navigates to the password reset page.
- **Steps:**
  1. Navigate to the OrangeHRM login page.
  2. Click the "Forgot your password?" link.
- **Expected Result:**
  - The user is navigated to the password reset page (URL contains `requestPasswordResetCode`).

---

## 6. Data-Driven Login Tests
**Automated Test:** `test_login_from_csv`

- **Description:** Verify multiple login scenarios using data from `data/test_users.csv`.
- **Steps:**
  1. For each row in `data/test_users.csv`, perform login with the specified username and password.
  2. Verify the expected error/result as specified in the CSV.
- **Expected Result:**
  - The result matches the expected value in the CSV for each scenario.

---

**Note:** All automated tests are implemented in `tests/test_orangehrm_login.py` and are mapped to the above manual test cases. 