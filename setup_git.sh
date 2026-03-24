#!/bin/bash

# Function to log messages with colors
log_info() { echo -e "\033[1;32m[INFO]\033[0m $1"; }
log_warning() { echo -e "\033[1;33m[WARNING]\033[0m $1"; }
log_error() { echo -e "\033[1;31m[ERROR]\033[0m $1"; exit 1; }

# 1️⃣ Check if Git is Installed
if ! command -v git &> /dev/null; then
    log_warning "Git is not installed. Installing Git..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install git || log_error "Failed to install Git!"
    else
        sudo apt update && sudo apt install -y git || log_error "Failed to install Git!"
    fi
else
    log_info "Git is already installed."
fi

# 2️⃣ Configure Git with User's Name and Email
read -p "Enter your full name (for Git commits): " GIT_NAME
read -p "Enter your email (associated with GitHub): " GIT_EMAIL

log_info "Configuring Git with the provided details..."
git config --global user.name "$GIT_NAME"
git config --global user.email "$GIT_EMAIL"

# Verify Git Configuration
log_info "✅ Git is now configured with:"
log_info "   - Username: $(git config --global user.name)"
log_info "   - Email: $(git config --global user.email)"

# 3️⃣ Check if SSH Key Exists, If Not Generate One
SSH_KEY="$HOME/.ssh/id_rsa"
if [[ -f "$SSH_KEY" ]]; then
    log_info "SSH key already exists. Skipping key generation."
else
    log_info "Generating SSH key..."
    ssh-keygen -t rsa -b 4096 -C "$GIT_EMAIL" -f "$SSH_KEY" -N "" || log_error "Failed to generate SSH key!"
    log_info "SSH key generated successfully!"
fi

# 4️⃣ Display SSH Key and Guide User to Add It to GitHub
log_info "Please add the following SSH key to your GitHub account:"
cat "$SSH_KEY.pub"
echo -e "\n👉 Open this link in your browser: https://github.com/settings/keys"
echo "1️⃣ Click 'New SSH Key'"
echo "2️⃣ Paste the copied key"
echo "3️⃣ Click 'Add SSH Key'"
read -p "Press Enter after adding the SSH key to GitHub..."

# 5️⃣ Test SSH Connection to GitHub
log_info "Testing SSH connection to GitHub..."
if ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
    log_info "✅ SSH authentication successful! Your system is now fully configured for GitHub."
else
    log_warning "⚠️ SSH authentication failed! You might need to check your key and try again."
    log_warning "🔹 Run the following command to test SSH manually:"
    echo "   ssh -T git@github.com"
    log_warning "If issues persist, visit: https://docs.github.com/en/authentication/connecting-to-github-with-ssh"
    exit 1
fi

# 6️⃣ Ask User for a Test Repository to Clone
read -p "Enter an existing GitHub SSH repository URL to test cloning (e.g., git@github.com:your-username/test-repo.git): " TEST_REPO

# 7️⃣ Create a Test Directory and Clone the Repository
TEST_DIR="$HOME/git_test"
log_info "Creating test directory: $TEST_DIR"
mkdir -p "$TEST_DIR" || log_error "Failed to create directory!"
cd "$TEST_DIR" || log_error "Failed to navigate to $TEST_DIR!"

log_info "Cloning the test repository: $TEST_REPO..."
if git clone "$TEST_REPO"; then
    log_info "✅ Repository cloned successfully! Your system is ready for Git and GitHub SSH."
else
    log_error "❌ Failed to clone repository. Please check the repository URL or SSH configuration."
fi

# 8️⃣ Final Confirmation
log_info "🎉 Your system is now fully set up for Git and GitHub!"
log_info "🔹 You can now use Git commands like:"
echo -e "\033[1;34m   git clone git@github.com:<your-username>/<repo-name>.git\033[0m"

