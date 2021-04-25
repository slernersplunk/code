# requires dockerhub login
sudo docker build . -f dockerfile-python-print -t python-print && \
# sudo docker tag python-print stevelerner/python-print && \
# sudo docker push stevelerner/python-print