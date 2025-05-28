# Django Chaos Engineering Experiment Plan

## 📁 Directory Structure

```
chaos-engineering/
├── README.md                    # This overview file
├── setup/
│   ├── install.sh              # Tool installation script
│   ├── docker-health-check.yml # Enhanced Docker Compose with health checks
│   └── requirements.txt        # Python dependencies for chaos scripts
├── experiments/
│   ├── 01-gunicorn-kill/
│   │   ├── experiment.sh       # Kill Gunicorn process
│   │   ├── verify.sh          # Verification script
│   │   └── README.md          # Experiment documentation
│   ├── 02-db-restart/
│   │   ├── experiment.sh       # Restart PostgreSQL
│   │   ├── verify.sh          # Verification script
│   │   └── README.md          # Experiment documentation
│   ├── 03-cpu-stress/
│   │   ├── experiment.sh       # CPU stress test
│   │   ├── verify.sh          # Verification script
│   │   └── README.md          # Experiment documentation
│   └── 04-network-delay/
│       ├── experiment.sh       # Network latency injection
│       ├── verify.sh          # Verification script
│       └── README.md          # Experiment documentation
├── monitoring/
│   ├── health-check.py         # Health check script
│   ├── monitor.sh             # Real-time monitoring during experiments
│   └── log-analyzer.py        # Post-experiment log analysis
├── automation/
│   ├── run-all-experiments.sh  # Run all experiments sequentially
│   ├── ci-chaos-test.yml      # CI/CD integration example
│   └── slack-notification.py  # Alert integration
└── reports/
    ├── experiment-template.md  # Report template
    └── results/               # Directory for experiment results
```

## ⚙️ Project Context

**Your Stack:**
- Django backend (via Gunicorn)
- Nginx as reverse proxy
- PostgreSQL database
- All containerized with Docker Compose

**Goal:** Test system resilience when components fail

---

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Clone or create the chaos-engineering directory
mkdir chaos-engineering && cd chaos-engineering

# Run setup script
chmod +x setup/install.sh
./setup/install.sh
```

### 2. Run Single Experiment
```bash
# Example: Test Gunicorn failure
cd experiments/01-gunicorn-kill
./experiment.sh
```

### 3. Run All Experiments
```bash
# Run complete chaos test suite
./automation/run-all-experiments.sh
```

---

## 🧪 EXPERIMENT DETAILS

### 🎯 Steady State Hypothesis
**"The system should serve requests normally with a 200 response for /health/ endpoint."**

Verification command:
```bash
curl -I http://localhost:8081/health/
```

### ✅ Pre-requisites
- [ ] Docker + Docker Compose installed
- [ ] System running in staging/test environment
- [ ] Health check endpoint configured (`/health/`)
- [ ] Monitoring/logging enabled
- [ ] Team notified of chaos testing

---

## 🧪 Experiment #1 – Kill Gunicorn Process

**Objective:** Test Docker restart behavior and recovery time

**Files:**
- `experiments/01-gunicorn-kill/experiment.sh`
- `experiments/01-gunicorn-kill/verify.sh`

**Expected Results:**
- Nginx returns 502 temporarily
- Gunicorn restarts automatically (if configured)
- Service recovers within configured timeout

---

## 🧪 Experiment #2 – Restart PostgreSQL

**Objective:** Check Django DB connection resilience

**Files:**
- `experiments/02-db-restart/experiment.sh`
- `experiments/02-db-restart/verify.sh`

**Expected Results:**
- Temporary DB connection errors
- Django should retry and recover
- Connection pool behavior observation

---

## 🧪 Experiment #3 – CPU Stress Test

**Objective:** Test performance under high CPU load

**Files:**
- `experiments/03-cpu-stress/experiment.sh`
- `experiments/03-cpu-stress/verify.sh`

**Expected Results:**
- Increased response times
- Resource limit behavior
- Load balancer response

---

## 🧪 Experiment #4 – Network Delay

**Objective:** Test network latency tolerance

**Files:**
- `experiments/04-network-delay/experiment.sh`
- `experiments/04-network-delay/verify.sh`

**Expected Results:**
- DB query timeouts
- Connection pool exhaustion
- Graceful degradation

---

## 📊 Monitoring & Analysis

### Real-time Monitoring
```bash
# Monitor system during experiments
./monitoring/monitor.sh
```

### Health Checks
```bash
# Continuous health verification
python monitoring/health-check.py --interval 5 --duration 300
```

### Log Analysis
```bash
# Analyze logs post-experiment
python monitoring/log-analyzer.py --experiment gunicorn-kill --date 2024-01-15
```

---

## 📝 Post-Experiment Checklist

- [ ] **Error Visibility:** Did logs show clear error messages?
- [ ] **User Impact:** Were users affected? How did UI behave?
- [ ] **Monitoring:** Did monitoring systems detect the failure?
- [ ] **Recovery:** Did service recover automatically?
- [ ] **Alerting:** Were appropriate alerts triggered?
- [ ] **Documentation:** Results documented in `reports/results/`

---

## 🤖 CI/CD Integration

### GitLab CI Example
```yaml
# Include in .gitlab-ci.yml
chaos-test:
  stage: test
  script:
    - cd chaos-engineering
    - ./automation/run-all-experiments.sh
  only:
    - staging
  allow_failure: true
```

### GitHub Actions Example
```yaml
# .github/workflows/chaos-test.yml
name: Chaos Engineering Tests
on:
  push:
    branches: [staging]
jobs:
  chaos-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Chaos Tests
        run: |
          cd chaos-engineering
          ./automation/run-all-experiments.sh
```

---

## 🛡️ Safety Guidelines

### ⚠️ IMPORTANT SAFETY RULES
1. **Never run in production** without proper approval and safeguards
2. **Always use staging/test environments** first
3. **Start small** - single service, short duration
4. **Have rollback plans** ready
5. **Monitor recovery time** and set reasonable timeouts
6. **Involve the whole team** - Devs, DevOps, QA

### 🚨 Emergency Procedures
```bash
# Stop all chaos experiments immediately
docker-compose down && docker-compose up -d

# Check system status
./monitoring/health-check.py --quick-check

# View recent logs
docker-compose logs --tail=50
```

---

## 📈 Advanced Scenarios

### Multi-Component Failures
```bash
# Test cascading failures
./experiments/advanced/multi-component-failure.sh
```

### Load + Chaos
```bash
# Combine load testing with chaos
./experiments/advanced/load-plus-chaos.sh
```

### Scheduled Chaos
```bash
# Add to crontab for regular chaos testing
0 2 * * 1 /path/to/chaos-engineering/automation/weekly-chaos.sh
```

---

## 📚 Resources & References

- [Principles of Chaos Engineering](https://principlesofchaos.org/)
- [Pumba Documentation](https://github.com/alexei-led/pumba)
- [Docker Health Checks](https://docs.docker.com/engine/reference/builder/#healthcheck)
- [Django Production Deployment](https://docs.djangoproject.com/en/stable/howto/deployment/)

---

## 🤝 Contributing

1. Add new experiments in `experiments/` directory
2. Follow naming convention: `##-experiment-name/`
3. Include README.md, experiment.sh, and verify.sh
4. Update main README.md with experiment details
5. Test thoroughly in safe environment

---

## 📞 Support & Contact

- **Emergency Contact:** [Your Team Lead]
- **Slack Channel:** #chaos-engineering
- **Documentation:** [Internal Wiki Link]
- **Incident Response:** [Runbook Link]

---

*Remember: Chaos Engineering is about building confidence in your system's resilience. Start small, learn continuously, and always prioritize safety!* 🛡️