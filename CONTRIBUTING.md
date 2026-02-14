# Contributing to EdcellenceEdPEx

Thank you for your interest in contributing to EdcellenceEdPEx! This document provides guidelines for contributing to the project.

## 🎯 Ways to Contribute

- **Bug Reports**: Submit detailed bug reports via GitHub Issues
- **Feature Requests**: Suggest new features or enhancements
- **Code Contributions**: Submit pull requests for bug fixes or new features
- **Documentation**: Improve documentation, examples, or tutorials
- **Testing**: Write tests or improve test coverage
- **Research**: Contribute to academic validation or case studies

## 🚀 Getting Started

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/EdcellenceEdPEx.git
cd EdcellenceEdPEx

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/EdcellenceEdPEx.git
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

## 📝 Development Guidelines

### Code Style

- **Python**: Follow PEP 8 style guide
- **Formatting**: Use `black` for auto-formatting
- **Linting**: Use `flake8` and `pylint`
- **Type Hints**: Use type annotations where appropriate

```bash
# Format code
black src/ tests/

# Check linting
flake8 src/ tests/
pylint src/
```

### Testing

- Write tests for all new features
- Maintain test coverage > 80%
- Run tests before submitting PR

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_algorithms.py
```

### Documentation

- Add docstrings to all functions/classes (Google style)
- Update README.md if adding new features
- Add examples in docstrings

```python
def compute_score(self, indicators: Dict[str, float]) -> float:
    """
    Compute ADLI score for a process item.

    Args:
        indicators: Dictionary with keys 'P_A', 'P_D', 'P_L', 'P_I'

    Returns:
        ADLI score in range [0, 100]

    Raises:
        ValueError: If indicators are missing or out of range

    Example:
        >>> scorer = ADLIScorer()
        >>> score = scorer.compute_score({'P_A': 0.75, 'P_D': 0.45, 'P_L': 0.60, 'P_I': 0.55})
        >>> print(score)
        59.0
    """
```

### Commit Messages

Follow conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding/updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(adli): Add custom weight validation
fix(api): Resolve database connection timeout
docs(readme): Update installation instructions
test(letci): Add trend normalization tests
```

## 🔄 Pull Request Process

### 1. Update Your Branch

```bash
git fetch upstream
git rebase upstream/main
```

### 2. Pre-submission Checklist

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Commit messages follow conventions

### 3. Submit Pull Request

1. Push your branch to your fork
2. Open PR on GitHub
3. Fill out PR template
4. Link related issues
5. Request review

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

## 🐛 Bug Reports

Use this template for bug reports:

```markdown
**Description**
Clear description of the bug

**To Reproduce**
1. Step 1
2. Step 2
3. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Windows 10]
- Python version: [e.g., 3.9.7]
- Package version: [e.g., 1.0.0]

**Additional Context**
Any other relevant information
```

## 💡 Feature Requests

Use this template for feature requests:

```markdown
**Problem Statement**
Describe the problem this feature would solve

**Proposed Solution**
Describe your proposed solution

**Alternatives Considered**
Other solutions you've considered

**Use Case**
How would you use this feature?

**Additional Context**
Mockups, examples, references
```

## 📚 Academic Contributions

If your contribution relates to academic research:

1. **Methodology Changes**: Submit detailed mathematical justification
2. **Validation Studies**: Include statistical evidence and data
3. **Case Studies**: Follow ethical research guidelines
4. **Citations**: Properly cite related work

## 🤝 Community Guidelines

- **Be respectful**: Treat all contributors with respect
- **Be constructive**: Provide helpful feedback
- **Be patient**: Maintainers are volunteers
- **Be collaborative**: Work together to improve the project

## ❓ Questions

- **General Questions**: Use GitHub Discussions
- **Bug Reports**: Use GitHub Issues
- **Security Issues**: Email maintainers directly
- **Academic Inquiries**: Contact corresponding author

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to EdcellenceEdPEx!** 🎉
