# Install the IBM Cloud Controller for TJBot

## Registration on IBM Cloud

* [Register IBM Cloud](http://ibm.biz/austria)

## Install the TjBot-Cloud-Controller

1. Install TjBot IoT Environment in the Cloud using IoT Boilerplate
    * [IoT Starter](https://console.bluemix.net/catalog/starters/internet-of-things-platform-starter)

This Boilerplate will install as a runtime base

* [Node-Red in NodeJS](https://console.bluemix.net/catalog/starters/node-red-starter) Runtime
* the [IoT Foundation](https://console.bluemix.net/catalog/services/internet-of-things-platform)
* [Cloudant DB](https://console.bluemix.net/catalog/services/cloudant)

2. Install additional services for the TjBot functionality

The following services are used by the TjBot full implemented version

* [Visual Recognition](https://console.bluemix.net/catalog/services/visual-recognition)
* [Watson Assistant](https://console.bluemix.net/catalog/services/watson-assistant-formerly-conversation)
* [Text to Speech](https://console.bluemix.net/catalog/services/text-to-speech)
* [Speech to Text](https://console.bluemix.net/catalog/services/speech-to-text)
* [Language Translator](https://console.bluemix.net/catalog/services/language-translator)
* [Object Storage](https://console.bluemix.net/catalog/services/cloud-object-storage)
* [Watson Studio](https://console.bluemix.net/catalog/services/watson-studio)
* [Watson Machine Learning](https://console.bluemix.net/catalog/services/machine-learning)
* [Weather Company Service](https://console.bluemix.net/catalog/services/weather-company-data)

Optional Services are

* [Apache Spark](https://console.bluemix.net/catalog/services/apache-spark)
* [Watson Knowledge Catalog](https://console.bluemix.net/catalog/services/knowledge-catalog)
* [Watson Discovery](https://console.bluemix.net/catalog/services/knowledge-catalog)

4. Create Credentials on each service

For each of the created services check if there is a credential for access and managing the instance existing. Go to each of the services from the cloud dashboard (services section), click on each service,, go to the "Service Credential" Tab on the left, click on "New Credential" to create a credential_1 asset.

3. Bind all services to TjBot IoT Controller

    * restart the controller application after binding all of these services to get access to all of the credentials

## Configuration

1. Configure Watson Assist
    * load workspaces of Watson-Conversation as a base
    * write down the Workspace ID for DE/EN

2. Setup IoT Foundation
    * Create Device Classs
    * Create Device (tjbot-xxx)
    * write down the credentials or give well known name

3. Import Flows for TjBot Controller
    * Take Flows from TjBot-Cloud-Controller-Flows and Import each file as a new TAB
    * Deploy

4. Export all credentials into a Textfile - for later configuration (raspi)

5. Setup the TjBot on Raspberry PI

* [Install TjBot Raspi](Documents/Install-TjBot-Raspi.md)

## See also the IBM Cloud Catalog

* [Watson/AI](https://console.bluemix.net/catalog/?category=ai)
