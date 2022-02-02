# base image
FROM python:3.8-buster
RUN useradd -ms /bin/bash app
USER app
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /home/app
ENV PATH="/home/app/.local/bin:${PATH}"

# add requirements
COPY --chown=app:app requirements.txt /home/app/requirements.txt

# install requirements
RUN pip3 install --upgrade pip && pip3 install --user -r requirements.txt

# add app
COPY . /home/app
