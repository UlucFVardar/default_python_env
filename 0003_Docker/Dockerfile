# python3.8 lambda base image
#FROM public.ecr.aws/lambda/python:3.8
FROM python:3.8


# Copy function code to container
COPY ./1000_Platform/* ./

COPY ./0001_Dependents_Codes/* ./
COPY ./0001_Dependents_Files/* ./

# copy requirements.txt to container
COPY ./0003_Docker/requirements.txt .
# installing dependencies
RUN pip3 install -r requirements.txt

#CMD ["python", "app.py"] 