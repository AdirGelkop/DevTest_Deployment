# Test Plan: Add Route API

## Scope
Testing: POST /routes endpoint
Not Testing: GET, DELETE, UI

## Test Cases

### TC-001: Add valid route successfully
- **Description:** add a valid route
- **Steps:** 
  1. Send POST to /routes with prefix="10.0.0.0/24", next_hop="192.168.1.1"
- **Expected Result:** status 201 (updated successfully), route has been added

### TC-002: Add invalid subnet and correct IP
- **Description:** add a valid IP with invalid SM
- **Steps:** 
  1. Send POST to /routes with prefix="10.0.0.0/33", next_hop="192.168.1.1"
- **Expected Result:** status 400 (Bad Request), error message: "Invalid prefix"

### TC-003: self loop
- **Description:** add an entry with same prefix and next hop
- **Steps:** 
  1. Send POST to /routes with prefix="10.0.0.0/24", next_hop="10.0.0.0"
- **Expected Result:** status 400 (Bad Request), error message: "Next hop cannot be within prefix range"

### TC-004: Add existing route
- **Description:** add a valid (yet existing) route
- **Steps:** 
  1. Send POST to /routes with prefix="10.0.0.0/24", next_hop="192.168.1.1"
- **Expected Result:** status 409 (Conflict), error message: "Route already exists"

## Edge Cases
- prefix ריק: ""
- next_hop ריק: ""
- prefix עם אותיות: "abc.0.0.0/24"
- subnet mask קיצוני: /0, /32