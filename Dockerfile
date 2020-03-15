########################################################################
# Dockerfile to execute the palindrome program and to run the testcases
########################################################################

# Set the base image to ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER Prajeesh Cheruvath

# Update the repository and install the required packages
RUN apt-get update -y && \
 apt-get install python -y && \ 
 mkdir -p /home/ubuntu/assignment/

# Copy a configuration file from the current directory
ADD palindrome.py /home/ubuntu/assignment/ 
ADD test_palindrome.py /home/ubuntu/assignment/

ENTRYPOINT ["python", "/home/ubuntu/assignment/test_palindrome.py"]

CMD ['eYe']
