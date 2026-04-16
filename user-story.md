# User Stories for Customer Accounts Microservice

## 1. Create Account

**As a** System Administrator  
**I want to** create a new customer account  
**So that** I can manage new customer information in the system.

**Acceptance Criteria:**

- The system should accept name, email, and address.
- The system should return a 201 Created status code upon success.
- Email must be unique.

## 2. Read Account

**As a** Customer Service Rep  
**I want to** retrieve a specific account's details  
**So that** I can provide support to that customer.

**Acceptance Criteria:**

- The system should return account details for a valid ID.
- The system should return 404 Not Found for non-existent IDs.

## 3. Update Account

**As a** Customer  
**I want to** update my personal details  
**So that** my information stays current.

**Acceptance Criteria:**

- The system should allow updating name and address.
- The system should return 200 OK after a successful update.

## 4. Delete Account

**As a** Data Privacy Officer  
**I want to** delete a customer account  
**So that** we comply with data deletion requests.

**Acceptance Criteria:**

- The system should remove the account from the database.
- The system should return 204 No Content upon successful deletion.

## 5. List All Accounts

**As a** Manager  
**I want to** see a list of all customer accounts  
**So that** I can get an overview of our customer base.

**Acceptance Criteria:**

- The system should return an array of all accounts.
- The system should return 200 OK.
