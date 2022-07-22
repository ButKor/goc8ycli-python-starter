ARG VARIANT="buster"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# Install go-c8y-cli
RUN sudo apt-get install -y curl gnupg2 apt-transport-https
RUN curl https://reubenmiller.github.io/go-c8y-cli-repo/debian/PUBLIC.KEY | gpg --dearmor | sudo tee /usr/share/keyrings/go-c8y-cli-archive-keyring.gpg >/dev/null
RUN sudo sh -c "echo 'deb [signed-by=/usr/share/keyrings/go-c8y-cli-archive-keyring.gpg] http://reubenmiller.github.io/go-c8y-cli-repo/debian stable main' >> /etc/apt/sources.list"
RUN sudo apt-get update
RUN sudo apt-get install go-c8y-cli
RUN echo 'source "/etc/go-c8y-cli/shell/c8y.plugin.zsh"' >> ~/.zshrc

# Some helper tools
RUN apt install jq -y
RUN sudo apt-get -y install coreutils
