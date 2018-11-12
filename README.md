# XL Release CloudForms plugin v1.0.0

[![Build Status][xlr-cloudforms-plugin-travis-image]][xlr-cloudforms-plugin-travis-url]
[![License: MIT][xlr-cloudforms-plugin-license-image]][xlr-cloudforms-plugin-license-url]
![Github All Releases][xlr-cloudforms-plugin-downloads-image]

[xlr-cloudforms-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-cloudforms-plugin.svg?branch=master
[xlr-cloudforms-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-cloudforms-plugin
[xlr-cloudforms-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-cloudforms-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-cloudforms-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-cloudforms-plugin/total.svg

## Preface

This document describes the functionality provided by the XL Release CloudForm plugin.

See the [XL Release reference manual](https://docs.xebialabs.com/xl-release) for background information on XL Release and release automation concepts.  

## Overview

## Requirements

Note:  XLD or XLR version should not be lower than lowest supported version.  See <https://support.xebialabs.com/hc/en-us/articles/115003299946-Supported-XebiaLabs-product-versions>.

## Installation

* Copy the latest JAR file from the [releases page](https://github.com/xebialabs-community/xlr-cloudforms-plugin/releases) into the `XL_RELEASE_SERVER/plugins` directory.
* Restart the XL Release server.

## XLRelease Tasks

* Check CFME Service: check if the CloudForm Service is available
* Start Service: Request a new Service from a service template ID and wait for its end.

## References

