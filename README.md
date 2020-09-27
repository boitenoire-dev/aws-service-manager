# aws-service-manager
CLI Tool used to manage a variety of AWS resources

#About

This project is a way to manage various AWS resources using the boto3 library

#Configuring

Uses the configuration file created by the AWS CLI E.G

`aws configure --profile=servicemanagerapp`

# To run application

`pipenv run "python serviceapp/servicemanager.py <command>
<--project=PROJECT>"`

*command* is list, start, or stop
*project is option
