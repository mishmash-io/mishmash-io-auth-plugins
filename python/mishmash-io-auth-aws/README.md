# Mishmash io aws authentication plugin
Mishmash io aws authentication plugin

# Prerequisites
Python 3.6 or greater

# Installation

Install using pip:

``` pip install mishmash-io-auth-aws```

To upgrade the package to its latest version:

``` pip install mishmash-io-auth-aws --upgrade ```

# Configuration
Mishmash io authentication aws plugin needs some configuration variables.

## AWS_CONFIG_FILE
Specifies the location of the file that the AWS CLI uses to store configuration profiles. If config file is set, authentication plugin will get 
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY from there otherwise we will search  them  as environment variables 

## AWS_ACCESS_KEY_ID 
Specifies an AWS access key associated with an IAM mishmash admin user

# AWS_SECRET_ACCESS_KEY
Specifies the secret key associated with the access key.