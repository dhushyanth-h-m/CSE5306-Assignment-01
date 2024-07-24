# Image Search Application Using Docker

## Overview
This project demonstrates how to build a Dockerized image search application using gRPC for communication between client and server components. The server utilizes a machine learning model to analyze user queries and return relevant images.

## System Architecture
The application consists of two main components:

### Server:
- Deploys a machine learning model for image analysis.
- Responds to client requests with matching images.

### Client:
- Sends image search queries to the server.
- Receives and displays the server's response (image).

## Prerequisites
- Docker installed and running on your system.
- Python 3.9 or higher.

## Installation
**Step 1:** Clone the Repository

Clone this repository to your local machine. Use code with caution.

**Step 2:** Build Docker Images

Navigate into the project's root directory and build the Docker images for both the server and the client.

```bash
cd image-search-docker

# Build server image
docker build -t my-server-image ./server

# Build client image
docker build -t my-client-image ./client
```


## Usage
Step 1: Start the Server

Run the following command to start the server container:


```bash
docker run -d --network=host my-server-image
```
Step 2: Start the Client

Run the following command to start the client container in interactive mode:

```bash
docker run -it --network=host -v $PWD:/app my-client-image
```
Inside the client container, enter a query keyword and press enter. The client will send the query to the server, which will return a matching image. The image will be saved to the client directory as image.jpg.

## Customization
You can modify the following aspects of the application to suit your needs:

Machine Learning Model: The server's model.py script can be updated to use a different machine learning model for image analysis.
Query Logic: The server's server.py script can be modified to implement different query logic.
Docker Images: The Dockerfiles in the server and client directories can be customized to include additional dependencies or configurations.
Next Steps

Explore integrating a more sophisticated machine learning model for improved image analysis.
Add support for multiple clients to send queries to the server concurrently.
Deploy the application to a cloud platform for scalability and availability.
Contributing

Contributions to this project are welcome! Please make sure to read the contributing guidelines before submitting a pull request.

## License
This project is licensed under the MIT License.


<!--
&lt;--- Readme.md Snippet without images Start ---&gt;
## Tech Stack
dhushyanth-h-m/Multi-threaded-Image-Search-Engine is built on the following main stack:

- [Python](https://www.python.org) – Languages
- [Protobuf](https://developers.google.com/protocol-buffers/) – Serialization Frameworks
- [Docker](https://www.docker.com/) – Virtual Machine Platforms & Containers
- [TensorFlow](https://www.tensorflow.org) – Machine Learning Tools

Full tech stack [here](/techstack.md)

&lt;--- Readme.md Snippet without images End ---&gt;

&lt;--- Readme.md Snippet with images Start ---&gt;
## Tech Stack
dhushyanth-h-m/Multi-threaded-Image-Search-Engine is built on the following main stack:

- <img width='25' height='25' src='https://img.stackshare.io/service/993/pUBY5pVj.png' alt='Python'/> [Python](https://www.python.org) – Languages
- <img width='25' height='25' src='https://img.stackshare.io/service/4393/ma2jqJKH_400x400.png' alt='Protobuf'/> [Protobuf](https://developers.google.com/protocol-buffers/) – Serialization Frameworks
- <img width='25' height='25' src='https://img.stackshare.io/service/586/n4u37v9t_400x400.png' alt='Docker'/> [Docker](https://www.docker.com/) – Virtual Machine Platforms & Containers
- <img width='25' height='25' src='https://img.stackshare.io/service/4717/FtFnqC38_400x400.png' alt='TensorFlow'/> [TensorFlow](https://www.tensorflow.org) – Machine Learning Tools

Full tech stack [here](/techstack.md)

&lt;--- Readme.md Snippet with images End ---&gt;
-->
<div align="center">

# Tech Stack File
![](https://img.stackshare.io/repo.svg "repo") [dhushyanth-h-m/Multi-threaded-Image-Search-Engine](https://github.com/dhushyanth-h-m/Multi-threaded-Image-Search-Engine)![](https://img.stackshare.io/public_badge.svg "public")
<br/><br/>
|7<br/>Tools used|07/24/24 <br/>Report generated|
|------|------|
</div>

## <img src='https://img.stackshare.io/languages.svg'/> Languages (1)
<table><tr>
  <td align='center'>
  <img width='36' height='36' src='https://img.stackshare.io/service/993/pUBY5pVj.png' alt='Python'>
  <br>
  <sub><a href="https://www.python.org">Python</a></sub>
  <br>
  <sub></sub>
</td>

</tr>
</table>

## <img src='https://img.stackshare.io/frameworks.svg'/> Frameworks (1)
<table><tr>
  <td align='center'>
  <img width='36' height='36' src='https://img.stackshare.io/service/4393/ma2jqJKH_400x400.png' alt='Protobuf'>
  <br>
  <sub><a href="https://developers.google.com/protocol-buffers/">Protobuf</a></sub>
  <br>
  <sub>v4.24.4</sub>
</td>

</tr>
</table>

## <img src='https://img.stackshare.io/devops.svg'/> DevOps (3)
<table><tr>
  <td align='center'>
  <img width='36' height='36' src='https://img.stackshare.io/service/586/n4u37v9t_400x400.png' alt='Docker'>
  <br>
  <sub><a href="https://www.docker.com/">Docker</a></sub>
  <br>
  <sub></sub>
</td>

<td align='center'>
  <img width='36' height='36' src='https://img.stackshare.io/service/1046/git.png' alt='Git'>
  <br>
  <sub><a href="http://git-scm.com/">Git</a></sub>
  <br>
  <sub></sub>
</td>

<td align='center'>
  <img width='36' height='36' src='https://img.stackshare.io/service/12572/-RIWgodF_400x400.jpg' alt='PyPI'>
  <br>
  <sub><a href="https://pypi.org/">PyPI</a></sub>
  <br>
  <sub></sub>
</td>

</tr>
</table>

## Other (1)
<table><tr>
  <td align='center'>
  <img width='36' height='36' src='https://img.stackshare.io/service/4717/FtFnqC38_400x400.png' alt='TensorFlow'>
  <br>
  <sub><a href="https://www.tensorflow.org">TensorFlow</a></sub>
  <br>
  <sub>v2.13.0</sub>
</td>

</tr>
</table>


## <img src='https://img.stackshare.io/group.svg' /> Open source packages (1)</h2>

## <img width='24' height='24' src='https://img.stackshare.io/service/12572/-RIWgodF_400x400.jpg'/> PyPI (1)

|NAME|VERSION|LAST UPDATED|LAST UPDATED BY|LICENSE|VULNERABILITIES|
|:------|:------|:------|:------|:------|:------|
|[grpcio](https://pypi.org/project/grpcio)|v1.59.0|10/17/23|Dhushyanth |Apache-2.0|N/A|

<br/>
<div align='center'>

Generated via [Stack File](https://github.com/marketplace/stack-file)

