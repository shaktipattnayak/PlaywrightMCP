Feature: Login

  Scenario: Successful login
    Given I am on the login page
    When I fill "username" with "Admin"
    And I fill "password" with "admin123"
    And I click "Login"
    Then I should see "dashboard"

  Scenario: Invalid login
    Given I am on the login page
    When I fill "username" with "invalid_user"
    And I fill "password" with "wrongpass"
    And I click "Login"
    Then I should see "Invalid credentials" 