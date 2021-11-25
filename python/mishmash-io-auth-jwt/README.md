# Mishmash io authentication openid connect plugin

This package is intended to be used as part of [*mishamsh-io-client*](https://mishmash.io) for authorization with identity provider implementing openid connect.

*mishmash io* is a distributed and scalable database that allows you to easily implement smart, predictive features in your app.
*Find out more on [mishmash.io](https://mishmash.io)*

# Getting Started

## Installation

*The desired authorization plugin must be installed and used only with [*mishamsh-io-client*](https://mishmash.io)*.

You shoudnt install this package independently


##  Usage

This module is used by [*mishamsh-io-client*](https://mishmash.io) to generate access token signed by identity provider. To be able to work it needs the following configuration:

* MISHMASHIO_SERVERS - list of mishmash servers endpoints
* MISHMASHIO_APP_ID - id of the app using mishmash client
* MISHMASHIO_AUTH_SERVER - the identity provider server endpoint
* MISHMASHIO_AUTH_PRIVATE_KEY - Private key used for authentication with the identity provider


## Dependencies

* Python 3.6 or greater

* PyJwt[crypto] - we are using RS256 algorithm for signing JWT tokens, and using pyjwt as dependency. Creators of PyJwtrecommends to use PyJwt [crypto] in requirements files RS256 algorithm has been used 

* requests 

* pycryptodome

##	Latest releases
- 0.0.1 (Latest)

##	Authors

- Mishmash io

    * <https://mishmash.io/> 
    *  <info@mishmash.io>
    * [github](https://github.com/mishmash-io)

##	License

- This project is licensed under Apache 2.0. Full license text is available in [LICENSE](https://www.apache.org/licenses/LICENSE-2.0).
