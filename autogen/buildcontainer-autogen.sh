# requires dockerhub login
sudo docker build . -f dockerfile-python-autogen -t python-autogen && \
sudo docker tag splk-python-autogen stevelerner/python-autogen && \
sudo docker push stevelerner/python-autogen