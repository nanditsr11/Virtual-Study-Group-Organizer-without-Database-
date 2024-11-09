## Virtual Study Group Organizer
The Virtual Study Group Organizer is a simple desktop application built with Python and Tkinter. It allows users to create, view, and manage study groups. The app is designed for students or study enthusiasts who want to organize their study groups, track topics, and schedule meetings in an intuitive way.


## Features

Add Study Group: Users can create a new study group by specifying the group name, topic, and meeting time.
View Group Details: Allows users to view the details (topic and meeting time) of any selected study group.
Delete Study Group: Provides an option to remove a study group from the list.
In-Memory Storage: All group data is temporarily stored in memory while the app is running, making it easy to use without setup.

## Prerequisites
To run this app, you need:

Python 3.x installed on your system.
Getting Started

1. Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/your-username/virtual-study-group-organizer.git
cd virtual-study-group-organizer

2. Run the Application
Run the following command to start the application:

python study_group_organizer.py

## Usage

Add Study Group: Click on "Add Study Group" and enter the study group name, topic, and meeting time (in YYYY-MM-DD HH:MM format).
View Details: Select a group from the list and click "View Details" to see more information.
Delete Group: Select a group from the list and click "Delete Study Group" to remove it from the list.
Note: All data is stored in memory, so groups will reset when you close the app.

## Code Overview
study_group_organizer.py: 

Main application file containing the code for the Tkinter GUI and application logic.
groups: Stored in a Python list within the application; each group is represented as a dictionary with fields for group name, topic, and meeting time.
Future Enhancements

## Possible enhancements to this project:

Persistent Storage: Add options to save groups to a file (e.g., CSV or JSON) or integrate with a database.
Calendar Integration: Integrate with Google Calendar API for setting up and viewing study sessions in users' calendars.
Chat Feature: Incorporate a chat feature for group members to communicate.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

