FROM python:3.11
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#add this directory in the PATH
ENV PYTHONPATH .anynote
ENV POETRY_VERSION=1.8.3

RUN set -xe \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install virtualenvwrapper poetry==$POETRY_VERSION \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#RUN pip install --upgrade pip && \
#    python -m pip install --no-cache-dir poetry==$POETRY_VERSION \
#    && poetry config virtualenvs.create false \
#    && rm -rf $(poetry config cache-dir)/{cache,artifacts}
#RUN poetry --version
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY anynote anynote

# Expose port 8000
EXPOSE 8000

WORKDIR /app/anynote/

COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

#RUN export PATH=$PATH:$HOME/.local/bin
#ENV PATH="${PATH}:/root/.poetry/bin"

CMD ["/entrypoint.sh"]