FROM python:3.10

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Install python packages
COPY requirements.txt /feast/requirements.txt
RUN pip --disable-pip-version-check --no-cache-dir install -r /feast/requirements.txt

# Copy source files
COPY definitions /feast/definitions
COPY scripts /feast/scripts

# Switch back to dialog
ENV DEBIAN_FRONTEND=dialog

# Start application
CMD [ "/bin/bash"]