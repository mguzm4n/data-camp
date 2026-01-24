

1. Locate the dockerfile
2. Build the image: `docker build . -t py-it-bash`
3. Create the container in interactive mode: `docker run -it py-it-bash`
4. Run `pip --version``
5. You should see: `pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)`