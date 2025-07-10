@regression
Feature: Contact Us form functionality

    Background: Pre-conditions
        Given I am on the Contact Us form


    Scenario Outline: Form submission scenarios
        When I fill in the "first_name" field with "<first_name>"
        And I fill in the "last_name" field with "<last_name>"
        And I fill in the "email" field with "<email>"
        And I fill in the "message" field with "<message>"
        And I click on the "<button>" button
        Then I should see the message "<expected_message>"

        Examples:
            | first_name | last_name | email                  | message                    | button | expected_message                  |
            | Joe        | Blogs     | joe_blogs@example.com  | Please can you contact me? | SUBMIT | Thank You for your Message!555    |
            | Sarah      | Woods     | sarah_woodsexample.com | Hello World                | SUBMIT | Error: Invalid email address      |
            | \n         | \n        | \n                     | \n                         | SUBMIT | Error: all fields are required555 |

    @smoke
    Scenario: Missing fields
        When I click on the "SUBMIT" button
        Then I should see an error message saying "Error: all fields are required"

    @smoke
    Scenario: Using the 'RESET' button
        When I fill in the "first_name" field with "Mia"
        And I fill in the "last_name" field with "Lee"
        And I fill in the "email" field with "mia_lee@example.com"
        And I fill in the "message" field with "Test123 Test321"
        And I click on the "RESET" button
        Then all fields should be cleared