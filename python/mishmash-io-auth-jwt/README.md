# Mishmash io authentication jwt plugin
Mishmash io jwt authentication plugin allows you to authenticate to Mishmash io server.


# Prerequisites
Python 3.6 or greater

# Installation

Install using pip:

``` pip install mishmash-io-auth-jwt```

To upgrade the package to its latest version:

``` pip install mishmash-io-auth-jwt --upgrade ```


# Configuration
Mishmash io authentication jwt plugin needs some configuration variables.

## MISHMASHIO_AUTH_PRIVATE_KEY 

A private key to sign the token - This private key must be unique and never be revealed. 
To add the private key you should set environment variable called  MISHMASHIO_AUTH_PRIVATE_KEY or add it to config file

## MISHMASHIO_AUTH_SERVER

authentication server endpoint

## MISHMASHIO_APP_ID

registered mishmash app id in mishmash server 
