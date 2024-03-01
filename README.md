# AgriTrack
AgriTrack is a remote soil fertility monitoring and control system designed to address the challenges faced by farmers in maintaining fertile soil. This project aims to provide farmers with a solution that allows them to remotely and automatically monitor and regulate their soil fertility levels.
## Motivation/Why?
Growing up in rural areas where agriculture is the primary source of livelihood, the struggles faced by farmers due to the depletion of soil fertility were witnessed. The decline in soil quality has led to decreased crop yields and increased farming difficulties. Inspired by these challenges, AgriTrack was developed to empower farmers with a modern solution that helps them effectively manage and improve soil fertility.
## Goal
The primary goal of AgriTrack is to enable farmers to regain control over their soil fertility. By providing real-time data and insights, the system allows farmers to make informed decisions and take proactive measures to optimize their farming practices. Ultimately, the aim is to promote sustainable agriculture and enhance crop productivity.
## Usage
To utilize AgriTrack, farmers will eventually need to purchase the hardware kit and install it on their farms. The hardware components, such as Arduino Uno and ESP32, are responsible for collecting and transmitting data to the backend endpoints. This data is then made accessible to farmers through the web app, where they can view live data and visualizations related to soil fertility.

Currently, AgriTrack is still in progress, and the hardware kit is not yet available for purchase. The development team is actively working on finalizing the hardware design and ensuring its compatibility with the system. We anticipate that the hardware kit will be released in the near future, allowing farmers to fully experience the benefits of AgriTrack.

Once the hardware is available, farmers will be able to connect to the web app, which provides a secure data transmission and guarantees privacy. The web app features a user-friendly interface that enables farmers to monitor essential soil fertility parameters, including nutrient levels, pH balance, and moisture content. Furthermore, the system will provide recommendations and alerts based on data analysis and historical trends, empowering farmers to make informed decisions and optimize their farming practices.

## Contributing

To contribute to the project, please follow the steps below:

1. Fork the repository by clicking on the "Fork" button at the top right corner of this page. This will create a copy of the project in your GitHub account.
2. Clone the forked repository to your local machine using the following command:

   ```
   git clone https://github.com/Nolulamo/AgriTrack.git
   ```

3. Navigate to the project's directory:

   ```
   cd AgriTrack
   ```

4. Create a virtual environment to isolate the dependencies for the project. Run the following command based on your operating system:

   - For Windows:

     ```
     python -m venv env
     ```

   - For macOS and Linux:

     ```
     python3 -m venv env
     ```

5. Activate the virtual environment:

   - For Windows (Command Prompt):

     ```
     env\Scripts\activate
     ```

   - For Windows (Git Bash or PowerShell):

     ```
     source env/Scripts/activate
     ```

   - For macOS and Linux:

     ```
     source env/bin/activate
     ```

6. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

7. Apply the database migrations:

   ```
   python manage.py migrate
   ```

8. Start the development server:

   ```
   python manage.py runserver
   ```

   The server should now be running locally at `http://localhost:8000/`.

9. Make the necessary changes or improvements to the codebase.
10. Test your modifications thoroughly to ensure they do not introduce any issues.
11. Commit your changes and push them to your forked repository.
12. Create a pull request by navigating to the original repository and clicking on the "New Pull Request" button.
13. Clearly describe the changes you have made and their purpose in the pull request. Provide any additional information or context that may be helpful.
14. Submit the pull request, and our team will review your contribution as soon as possible.

We appreciate your interest in contributing to AgriTrack!
