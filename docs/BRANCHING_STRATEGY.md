# Branching Strategy

## Branch Structure

### Main Branches

- `main` (Production)

  - Represents the production-ready code
  - Protected branch (requires pull request reviews)
  - Only accepts merges from `test` branch
  - Tagged with version numbers

- `test` (Testing/Staging)

  - Represents the staging/testing environment
  - Protected branch (requires pull request reviews)
  - Only accepts merges from `dev` branch
  - Used for integration testing and QA

- `dev` (Development)
  - Main development branch
  - Protected branch (requires pull request reviews)
  - Accepts merges from feature branches
  - Used for continuous integration

### Supporting Branches

- `feature/*` (Feature Branches)

  - Created from `dev`
  - Naming convention: `feature/description-of-feature`
  - Merged back into `dev` via pull request
  - Deleted after merging

- `hotfix/*` (Hotfix Branches)

  - Created from `main`
  - Naming convention: `hotfix/description-of-fix`
  - Merged back into `main` and `dev`
  - Deleted after merging

- `release/*` (Release Branches)
  - Created from `test`
  - Naming convention: `release/vX.Y.Z`
  - Merged back into `main` and `dev`
  - Deleted after merging

## Workflow

1. **Feature Development**

   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feature/new-feature
   # Make changes
   git add .
   git commit -m "feat: description of changes"
   git push origin feature/new-feature
   # Create pull request to dev
   ```

2. **Testing Process**

   ```bash
   # After feature is merged to dev
   git checkout test
   git pull origin test
   git merge dev
   git push origin test
   # Run tests and QA
   ```

3. **Production Release**
   ```bash
   # After testing is complete
   git checkout main
   git pull origin main
   git merge test
   git tag -a vX.Y.Z -m "Release version X.Y.Z"
   git push origin main --tags
   ```

## Branch Protection Rules

### Main Branch

- Requires pull request reviews before merging
- Requires status checks to pass before merging
- Requires branches to be up to date before merging
- No direct pushes allowed

### Test Branch

- Requires pull request reviews before merging
- Requires status checks to pass before merging
- Requires branches to be up to date before merging
- No direct pushes allowed

### Dev Branch

- Requires pull request reviews before merging
- Requires status checks to pass before merging
- Requires branches to be up to date before merging
- No direct pushes allowed

## Version Control Best Practices

1. **Commit Messages**

   - Use conventional commits format
   - Start with type: feat, fix, docs, style, refactor, test, chore
   - Include ticket number if applicable
   - Keep messages clear and concise

2. **Pull Requests**

   - Include description of changes
   - Link related issues
   - Request reviews from team members
   - Ensure CI checks pass

3. **Code Review**

   - Review for functionality
   - Check for code quality
   - Verify test coverage
   - Ensure documentation is updated

4. **Merging**
   - Squash and merge feature branches
   - Create merge commits for release branches
   - Keep commit history clean and meaningful
