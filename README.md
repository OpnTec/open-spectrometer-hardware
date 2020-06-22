# DIY Analytics Open Source Spectrometer


[![Build Status](https://travis-ci.com/OpnTec/open-spectrometer-hardware.svg?branch=master)](https://travis-ci.com/OpnTec/open-spectrometer-hardware)
[![Gitter](https://badges.gitter.im/fossasia/pslab.svg)](https://gitter.im/fossasia/pslab?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

This repository provides hardware schematics and list of materials for the open spectrometer project to enable practitioners, students and citizen scientists to collect data with their spectrometer and have a good and fun learning experience. The open spectrometer project consists of a web cam, simple lasercut parts, battery casing and a suitable LED lightning component. The spectrometer connects to a computer via USB, where the user can run the scripts provided in this repository to run experiments and take measurements. Enjoy!

![Open Source Spectrometer](/docs/images/spectrometer_transparent.jpg "Open Source Spetrometer")
A transparent version of the spectrometer for explanation purposes.


## Open Science and Goals

By definition science should be open and reproducible. So, the outcome of an experiment can be verified by anyone. Unfortunately today this is not always the case. In order to be able to verify experiments all components used should be openly accessible. This includes the software and hardware of scientific instruments. Our spectrometer project follows this path. By giving access to all layers of the device used in a scientific experiment users can develop a deep understanding how scientific measurements are taken and practitioners are able to critically understand the limitations of the particular instrument.

The spectrometer consists of a set of materials designed to be available and affordable anywhere in the world. The design's focus is to promote education about spectrometry and analytical chemistry, with the goal of empowering, stimulating and encouraging individuals to learn about their environment applying scientific methodologies. Furthermore, the goal of the tool is to enable practitioners to study open design, scientific programming, physics and to reflect about reproducibility in scientific practices.

## Communication

The spectrometer community is still small. There are overlaps with the Pocket Science Lab team. To stay connected with different community members we continue to use the PSLab Gitter channel for the beginning. We will set up a dedicated channel once the project is more established. Please join us here:
* [Pocket Science Channel](https://gitter.im/fossasia/pslab)

## Features and Implementation Status

- The bill of materials is available in the /components folder.
- The design files for the lasercut files are available in the /schematics folder.

![Open Source Spectrometer Camera Component](/docs/images/spectrometer_cameracomponent.jpg "Open Source Spetrometer Camera Component")
The camera component of the spectrometer in transparent casing.

Roadmap:

- improve the design of the wooden part holding the camera
- redesign the light side, in order to allow CFL light coming in without disassembling the whole spectrometer
- write a script that allows the user to control the spactrometer with a simple offline device
- reduce the size to fit in one 25x50cm board


## Software

To get the data from the spetrometer device practitioners can use the spectrometer Python scripts available in the project. 


## Contributors

Alessandro Volpato is the creator of the project. The work was done by merging concepts of the [Public Lab Spectrometer](https://publiclab.org/notes/abdul/10-13-2016/desktop-spectrometry-starter-kit-3-0-instructions), 
the [GaudiLabs spectrometer](http://www.gaudi.ch/GaudiLabs/?page_id=328) and creating new design features to simplify the assembly of a lasercut spetrometer.

## License

The repository is licenced under CERN Open Hardware Licence v1.2
