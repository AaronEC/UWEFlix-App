
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
  <h3 align="center">UWEFlix</h3>

  <p align="center">
    An online cinema booking and ticket sales portal.
    <br />
    <a href="https://www.youtube.com/watch?v=K8lKLx9CCwY"><img src="https://aaroncardwell.dev/images/flix/video_template.jpg" width="412" alt="VideoLogo"></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributors">Contributors</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The system is an online portal, for a university cinema, which allows tickets for specific screenings to be purchased by individual students, or in bulk by university clubs or societies.

Films, screenings and ticket price etc can be managed by staff accounts with elevated access levels.

Built with a web based frontend, linked to a Python backend via the Django API. Tickets, screenings and films are dynamically generated from entries, added by cinema staff with specific access levels, in an SQL database.

The web portal features full user account registration and authorisation, including password strength checks, valid email checks and much more. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

The UWEFlix project was built by an agile team of three members, over a 12 week period, using the scrum methodology. The following tools and frameworks were used.

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![HTML][HTML]][HTML-url]
* [![Docker][Docker]][Docker-url]
* [![JS][JS]][JS-url]
* [![sql][sql]][sql-url]
* [![AllAuth][AllAuth]][AllAuth-url]

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/python-3.9.8-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Django]: https://img.shields.io/badge/Django-4.0.7-000000?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[HTML]: https://img.shields.io/badge/HTML-5.0-000000?style=for-the-badge&logo=appveyor&logoColor=white
[HTML-url]:https://www.w3schools.com/html/
[sql]: https://img.shields.io/badge/SQL-20_c_R3-000000?style=for-the-badge&logo=appveyor&logoColor=white
[sql-url]: https://angular.io/
[Docker]: https://img.shields.io/badge/Docker-20.10.11-000000?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[AllAuth]: https://img.shields.io/badge/AllAuth-0.50.0-000000?style=for-the-badge&logo=django&logoColor=white
[AllAuth-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-5.2.1-000000?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JS]: https://img.shields.io/badge/JavaScript-ES2022-000000?style=for-the-badge&logo=javascript&logoColor=white
[JS-url]: https://www.javascript.com/

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy of the app up and running and try it for yourself, follow these simple steps.

### Prerequisites

* Django
* Django AllAuth
 ```sh
pip install Django
pip install django-allauth
  ```

### Installation

1. Clone the repo
   ```sh
	git clone https://github.com/AaronEC/UWEFlix-App.git
   ```
2. Install packages
   ```sh
	pip install Django
	pip install django-allauth
   ```
3. Navigate terminal to webapp directory
   ```js
   cd webapp
   ```
4. Run local Django server
   ```js
   python manage.py runserver
   ```
5. Open server in your browser
   ```js
   http://localhost:8000/
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Please see the project in action using the screenshots below.

<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20181459.jpg?raw=true" width="412" alt="Screenshot">
<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20181518.jpg?raw=true" width="412" alt="Screenshot">
<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20181545.jpg?raw=true" width="412" alt="Screenshot">
<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20181556.jpg?raw=true" width="412" alt="Screenshot">
<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20182828.jpg?raw=true" width="412" alt="Screenshot">
<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20181612.jpg?raw=true" width="412" alt="Screenshot">
<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20181626.jpg?raw=true" width="412" alt="Screenshot">
<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20181936.jpg?raw=true" width="412" alt="Screenshot">
<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20181951.jpg?raw=true" width="412" alt="Screenshot">
<img src="https://github.com/AaronEC/Portfolio/blob/main/images/flix/Screenshot%202022-09-02%20182000.jpg?raw=true" width="412" alt="Screenshot">


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributors

Also contributed to this project:

Ollie Latham (Developer) <br />
Charlie Saunders (Developer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Aaron Cardwell - [LinkedIn](https://www.linkedin.com/in/aaronecardwell/) - aaron_cardwell@hotmail.com

Project Link: [https://github.com/AaronEC/UWEFlix-App](https://github.com/AaronEC/UWEFlix-App)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
