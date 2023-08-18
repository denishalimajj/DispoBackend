# DispoBackend

Dipso Backend Setup

This README provides step-by-step instructions on how to install and start the Dipso backend using Docker Compose.

Prerequisites

Docker and Docker Compose should be installed on your system. You can download and install them from the official Docker website: 
		
  	Get Docker : https://www.docker.com/get-started/

Getting Started

Clone the Repository:

Clone the Dipso repository to your local machine:

 	git clone https://github.com/your-username/dipso.git

	cd dipso


Environment Variables:

Create a .env file in the root directory of the project and set the required environment variables. Replace the placeholders with actual values:

	DB_USER=your_db_username

	DB_PASSWORD=your_db_password

	DB_NAME=your_db_name

	PGADMIN_EMAIL=your_pgadmin_email

	PGADMIN_PASSWORD=your_pgadmin_password

Build and Start the Backend:

Run the following command to build and start the backend services defined in the docker-compose.yml file:

	docker-compose up -d

This will create and start the PostgreSQL database, PgAdmin interface, and the Dipso application.

Access the Application:

Dipso API: The Dipso API should be accessible at:  

	http://localhost:8000

PgAdmin Interface: You can access the PgAdmin web interface at 

	http://localhost:5050 
 
Use the credentials you provided in the .env file.

Stopping the Services:

To stop the services, run the following command:

	docker-compose down

This will stop and remove the containers while preserving your data.

Troubleshooting

If you encounter any issues during setup, please check the Docker Compose logs for any error messages:

	docker-compose logs

If you need further assistance, please refer to the official Docker documentation or seek help from the Dipso community.

Conclusion

You have successfully set up and launched the backend of your application! This guide covered installation, configuration, and starting the backend server. Moving forward, you can expand your application's functionality by adding routes, controllers, and additional features.
For further assistance, consult the project documentation or seek support from our team. Happy coding! 

