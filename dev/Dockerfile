FROM codercom/code-server:1.621
RUN sudo apt-get update \
    && sudo DEBIAN_FRONTEND=noninteractive apt-get install -yq make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

ARG PYVERSION=3.7.3

RUN curl https://pyenv.run | bash \
    && echo "export PATH=\"/home/coder/.pyenv/bin:\$PATH\"" >> ~/.bashrc \
    && echo "eval \"\$(pyenv init -)\"" >> ~/.bashrc \
    && echo "eval \"\$(pyenv virtualenv-init -)\"" >> ~/.bashrc \
    && /home/coder/.pyenv/bin/pyenv install $PYVERSION \
    && /home/coder/.pyenv/bin/pyenv global $PYVERSION
    
