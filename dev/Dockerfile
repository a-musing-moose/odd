FROM codercom/code-server:1.621
RUN sudo apt-get update \
    && sudo DEBIAN_FRONTEND=noninteractive apt-get install -yq make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

ARG PYVERSION=3.7.3

RUN cd $HOME && git clone git://github.com/yyuu/pyenv.git .pyenv

ENV PYENV_ROOT /home/coder/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv install $PYVERSION \
    && pyenv global $PYVERSION \
    && pyenv rehash

# Generic Python stuff above, project specific below

RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install -yq libpq-dev
RUN pip install isort invoke black