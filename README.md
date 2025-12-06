# DevTest & Deployment Engineer - Interview Preparation

4-day intensive technical preparation covering core technologies for DevTest Engineer and Deployment Engineer roles.

---

## Day 1: Python, Testing & QA

### Python Fundamentals
- Variables, data types, f-strings
- Lists, dictionaries, loops
- Functions with parameters and return values
- Conditionals (if/elif/else)

### pytest
- Test functions with `assert`
- Fixtures: setup/teardown with `@pytest.fixture`
- `yield` for cleanup after test
- `@pytest.mark.parametrize` for multiple test cases

### REST APIs
- HTTP methods: GET (read), POST (create), PUT (replace), PATCH (update), DELETE
- Status codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error
- `requests` library for API calls
- API testing with pytest

### QA Methodology
- Test types: Unit, Integration, E2E, Smoke, Sanity, Regression, Performance
- Test Plan (TP): scope, test cases, edge cases, expected results
- Edge cases: empty values, boundaries, invalid formats, duplicates

---

## Day 2: Containers, Orchestration & CI/CD

### Docker
- Image: template for containers (built from Dockerfile)
- Container: running instance of an image
- Dockerfile commands: FROM, WORKDIR, COPY, CMD, EXPOSE
- Commands: `docker build`, `docker run`, `docker ps`, `docker images`
- Volumes (`-v`): persistent storage, shared between host and container
- Port mapping (`-p`): expose container ports to host

### Kubernetes
- Cluster → Node → Pod → Container
- Pod: smallest deployable unit
- Deployment: manages replicas, self-healing, rolling updates
- Service: exposes pods, load balancing (NodePort, ClusterIP)
- Commands: `kubectl apply -f`, `kubectl get pods/deployments/services`, `kubectl delete`

### CI/CD
- CI (Continuous Integration): automated tests on every push
- CD (Continuous Delivery): automated deployment after tests pass
- GitHub Actions: workflow files in `.github/workflows/`
- Pipeline triggers: push, pull_request

### Linux
- Processes: `ps aux`, `top`, `kill PID`
- Network: `ifconfig`, `ping`, `lsof -i :PORT`, `nslookup`
- Permissions: `ls -la`, `chmod 755` (rwx=7, r-x=5, r--=4)
- Logs: `tail`, `tail -f`, `grep`
- Filesystem: `/etc` (config), `/var/log` (logs), `/home` (users)

---

## Day 3: Messaging, Databases & Distributed Systems

### Kafka
- Message broker / event streaming platform
- Producer → Topic → Consumer
- Topics contain partitions for parallelism
- Messages persist with TTL (default 7 days)
- Use cases: event-driven architecture, logs aggregation, microservices decoupling

### RPC & gRPC
- RPC: Remote Procedure Call - call functions on remote machines
- gRPC: Google's RPC framework using Protobuf (binary, fast)
- REST: JSON, readable, external APIs
- gRPC: Protobuf, fast, internal microservices communication

### Temporal
- Workflow orchestration platform
- Manages long-running processes with state persistence
- Automatic retries on failure
- Components: Workflow, Activity, Worker

### Databases
- SQL (relational): tables, rows, columns, joins
- NoSQL: flexible schema, documents (MongoDB), key-value (Redis)
- ACID: Atomicity, Consistency, Isolation, Durability
- Basic SQL: SELECT, INSERT, UPDATE, DELETE
- Index: speeds up queries

### Distributed Systems Testing
- Challenges: network failures, race conditions, consistency
- Fault tolerance: system survives component failures
- Chaos engineering: intentionally cause failures to test resilience
- Testing approach: Docker Compose environment, simulate failures, verify recovery

---

## Day 4: Virtualization, Cloud & Scripting

### Virtualization
- Hypervisor: software that runs VMs
- Type 1 (bare metal): ESXi, Hyper-V, KVM - runs on hardware
- Type 2 (hosted): VirtualBox, VMware Workstation - runs on OS
- ESXi: VMware hypervisor
- vCenter: centralized management for multiple ESXi hosts
- vMotion: live VM migration between hosts

### VM vs Container
- VM: full OS, GBs, minutes to start, full isolation
- Container: shared kernel, MBs, seconds to start, partial isolation
- VMs for infrastructure, different OS requirements
- Containers for microservices, CI/CD, fast scaling

### AWS
- EC2: virtual machines
- S3: object storage
- IAM: users, roles, permissions
- VPC: virtual network (subnets, security groups, route tables)
- Security Group: instance-level firewall, stateful
- RDS: managed databases
- Lambda: serverless functions

### Azure
- Virtual Machines (= EC2)
- Blob Storage (= S3)
- Azure AD / RBAC (= IAM)
- VNet (= VPC)
- Resource Group: logical container for resources

### Bash Scripting
- Shebang: `#!/bin/bash`
- Variables: `name="value"`, usage: `$name`
- Input: `read variable`
- Conditions: `if [ $x -gt 5 ]; then ... fi`
- Comparisons: `-eq`, `-gt`, `-lt`, `-le`, `-ge`
- Loops: `for i in 1 2 3; do ... done`
- Functions: `func() { echo $1; }`

---

## Key Interview Topics

### DevTest Engineer
- pytest fixtures and parametrize
- REST API testing
- Unit vs Integration vs E2E tests
- Kafka: when and why
- gRPC vs REST
- Distributed systems testing approach

### Deployment Engineer
- Docker: images, containers, volumes, ports
- Kubernetes: pods, deployments, services
- VM vs Container differences
- ESXi, vCenter, Hyper-V
- Linux commands and permissions
- AWS/Azure core services
- Bash scripting basics

---

## Repository Structure
```
DevTest_Deployment/
├── day1/
│   ├── basics.py
│   ├── lists_loops.py
│   ├── dicts.py
│   ├── functions.py
│   ├── conditionals.py
│   ├── test_basics.py
│   ├── test_fixtures.py
│   ├── test_parametrize.py
│   ├── test_api.py
│   └── test_plan_example.md
├── day2/
│   ├── Dockerfile
│   ├── app.py
│   ├── pod.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── linux_cheatsheet.md
├── day4/
│   ├── hello.sh
│   ├── variables.sh
│   ├── conditions.sh
│   ├── loops.sh
│   └── functions.sh
├── .github/
│   └── workflows/
│       └── ci.yaml
└── README.md
```