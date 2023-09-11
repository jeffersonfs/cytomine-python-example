FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["cytomine_python_example"]
