FROM datajoint/miniconda3:4.10.3-py3.9-debian
COPY --chown=anaconda:anaconda ./setup.py /main/
COPY --chown=anaconda:anaconda ./toolbox /main/toolbox
COPY --chown=anaconda:anaconda ./pip_requirements.txt /tmp/
RUN \
    /entrypoint.sh echo "STATUS: Installed dependencies." && \
    rm -R /main/toolbox /main/setup.py /tmp/pip_requirements.txt
