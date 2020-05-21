# NETCONF Workaround

Simple NETCONF protocol workaround implemented with [ncclient](https://github.com/ncclient/ncclient) library.

## System requirements

This application must have these prerequisites with its minimum versions denoted to run the application:

<ul>
    <li>
        Java Runtime Environment 8
    </li>
    <li>
        Python 3.7.4
    </li>
    <li>
        npm 6.13.7
    </li>
</ul>

## Get Started

The workaround is consisting of 3 fundamental application layers: Client, Server and Test Device. In order to use the application properly, all 3 layers must be running and stable.

### Test Device

Test Device is one of the most important fundamental application layer of the workaround, this is a simple executable Java .jar file which located on `./netconf-device` folder and runs a ready-to-use virtual NETCONF device simulator created by [OpenDaylight Project](https://docs.opendaylight.org/projects/netconf/en/latest/testtool.html)

In order to start the simulator, make sure to have JRE 8 or higher version is currently installed, then run:

```
cd ./netconf-device
java -jar netconf-testtool-1.7.2-executable.jar
```

Device is currently active and ready-to-use on port 17830 if the executable logs like this:

```
00:56:41.205 [main] INFO  o.o.n.t.tool.NetconfDeviceSimulator - Starting 1, SSH simulated devices starting on port 17830
00:56:41.231 [main] INFO  o.o.n.t.tool.NetconfDeviceSimulator - Custom module loading skipped.
00:56:42.119 [main] INFO  o.o.n.t.tool.NetconfDeviceSimulator - using OperationsProvider.
00:56:42.630 [main] WARN  io.netty.bootstrap.ServerBootstrap - Unknown channel option 'SO_BACKLOG' for channel '[id: 0xab0aaddd]'
00:56:42.790 [main] INFO  o.o.n.t.tool.NetconfDeviceSimulator - All simulated devices started successfully from port 17830 to 17830
```

### Server

Server layer is a simple [Flask](https://flask.palletsprojects.com/en/1.1.x/) application which is responsible for connecting the test device and providing some backend operations on that.

Before starting to develop, I was searching for proper library of NETCONF protocol to perform some NETCONF specific operations, then I found a Java library, [`netconf-java`](https://github.com/Juniper/netconf-java), which has been developed by Juniper development community. After I analyzed the library, I decided to implement backend application in Java so I could easily import the library and complete my backend job without pain. Unfortunately, it's not happen like I expected, the library was not even able to connect the test device so I decided to keep searching. After a detailed searching, I encountered a solution in Python way! [`ncclient`](https://github.com/ncclient/ncclient) is a Python library that facilitates client-side scripting and application development around the NETCONF protocol. I immediately started to develop backend in Flask and did it!

In order to start the backend, all project libraries/dependencies must be installed with:

```
pip3 install ncclient Flask flask_cors xmltodict
```

To start backend, run:
```
$ export FLASK_APP=app.py
$ flask run
```

To start backend with VSCode, `Run and Debug > Start`

### Client

Client layer is a simple UI layer of the application which is responsible for fetching data from backend and render them on a web application. It's implemented in [Vue.js](https://vuejs.org/)

In fact, I see this type of assignments as a new opportunity to improve my skill set so this is the main reason why I chose developing a web application to visualize the data and prefer Vue.js.

Before running the application, node dependencies should be installed with:
```
npm install
```

To start client, run:
```
npm run serve
```
To build and obtain ready-to-use deploy of the project, run:
```
npm run build
```