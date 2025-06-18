Feature: Product Management

  Background:
    Given the following products
      | name   | description      | price | available | category  |
      | Wrench | Handy tool       | 19.99 | true      | TOOLS     |
      | Apple  | Fresh and crisp  | 0.99  | true      | FOOD      |
      | Drill  | Power tool       | 89.99 | false     | TOOLS     |

  Scenario: Read a product by ID                # Task 6a
    When I visit "/products/1"
    Then the response status should be "200"
    And the response should contain "Wrench"

  Scenario: Update a product                    # Task 6b
    When I PUT "/products/1" with:
      """
      {
        "name": "Updated Wrench",
        "description": "Updated",
        "price": 20.00,
        "available": true,
        "category": "TOOLS"
      }
      """
    Then the response status should be "200"
    And the response should contain "Updated Wrench"

  Scenario: Delete a product                    # Task 6c
    When I DELETE "/products/1"
    Then the response status should be "204"

  Scenario: List all products                   # Task 6d
    When I visit "/products"
    Then the response status should be "200"
    And the response should contain "Apple"
    And the response should contain "Wrench"

  Scenario: Search by category                  # Task 6e
    When I visit "/products?category=FOOD"
    Then the response status should be "200"
    And the response should contain "Apple"
    And the response should not contain "Wrench"

  Scenario: Search by availability              # Task 6f
    When I visit "/products?available=true"
    Then the response status should be "200"
    And the response should contain "Apple"
    And the response should not contain "Drill"

  Scenario: Search by name                      # Task 6g
    When I visit "/products?name=Drill"
    Then the response status should be "200"
    And the response should contain "Drill"
