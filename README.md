# ProjectCyberSecurity

## Background
With continuous delivery, our customers want to release their software as fast as possible.
Sometimes this even means releasing on a weekly or even daily basis. This means that someone or something needs to verify the release in the same pace. And as you probably can imagine there is hardly any company that have a large enough pen test team to validate those releases. Therefore, there’s only one way to get out: add security automation. This is done in terms of an application security pipeline and a security pipeline. A security pipeline consists of multiple tools that are started with automation tooling to provide feedback to the security team. An application security pipeline is a CI/CD pipeline that is enriched with security tooling to provide feedback to the application development teams. Both these pipelines use a lot of security tooling that report to an aggregator: a vulnerability manager. The vulnerability manager provides insight into possible vulnerabilities within the infrastructure and within the applications. Next, it helps to identify and suppress false positives found by the tooling.
The actual findings reported by the tools can then result in work-instruction tickets (Jira, etc.) so
that developers and operations-specialists can fix the findings. 

## Assignment
This assignment is about extending an existing open-source vulnerability manager with new
functionalities. The tool is called DefectDojo and can be found here:
https://github.com/OWASP/django-DefectDojo . There are various directions in which you can
start extending the tool, see functional requirements for more details.

## Functional requirements
- There is need for integrating with other work-scheduling tools than Jira (e.g. ServiceNow,
VersionOne, etc.)
- There is need for more tooling support (Clair, Arachni, etc.)
- See the issues of the tool.
Implementation details:
- The extensions need to be written in Python
- The extensions need to be approved by the DefectDojo team, so quality is important.

## Project Scope and Requirements

The group debated about which product would be interesting and challenging to investigate and build. A first idea was pitched to build an additional tool with importer for DefectDojo (Functional requirement:  There is need for more tooling support). We wanted the tool to bring new functionality to DefectDojo. The easiest way seemed to import results from penetration testing tools which are already mainstream, but the team was convinced they could build a new tool with new functionality. The functionality was decided to be a web scraper which could parse al pages from a website follow the links and scan the source of these pages for a given set of keywords. This functionality seemed needed since developers leave comments in code which could leak sensitive information about the inner workings of the web application. 
The following primary requirements were agreed upon.

## Requirements

### Testing tool
-	The tool will be run from CLI
-	For usability the tool must have a menu to configure and run the tool
-	The tool will have a default configuration for the most options
-	The tool must allow the user to check if the correct input was given for a configuration option
-	It must allow the user to configure the URL of the web application.
-	It must allow the user to display the current keywords the application scans for.
-	It must allow the user to add and remove keywords to the test.
-	It must allow the user to run the tool without crawling the full web application.
-	It must allow the user to run the tool with crawling the full web application.
-	The tool must allow the user to export the findings to a result file.

### Importer
-	The tool will be run from CLI
-	For usability the tool must have a menu to configure and run the tool
-	The tool must be able to initiate a connection with a DefectDojo implementation
-	The tool must be able to show the available products
-	The user must be able to select a product
-	The tool must be able to show the available engagements for the product
-	The user must be able to select an engagement
-	The tool must be able to display the current result files 
-	The user must be able to select the correct result for uploading to DefectDojo
-	The user must be able to upload the results to DefectDojo

![architecture](https://github.com/derekhof/ProjectCyberSecurity/blob/master/Software%20architecture.jpg)
