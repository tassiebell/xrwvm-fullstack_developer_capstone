# Deployment Steps:

# Clone Repo
git clone https://github.com/tassiebell/xrwvm-fullstack_developer_capstone.git
# Create Superuser
cd /home/project/xrwvm-fullstack_developer_capstone/server
pip install virtualenv
cd /home/project/xrwvm-fullstack_developer_capstone/server
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
python3 -m pip install -U -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser
# Alternatively register after deploymnent, new users are recordet to SQL
# Cleaning
deleting the db.sqlite3 file from the server directory, and also delete the __pycache__ folder and __init__.py file (if present) from the djangoapp directory. 
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb

# Launch Mongo
cd /home/project/xrwvm-fullstack_developer_capstone/server/database
docker build . -t nodeapp
docker-compose up

# Build Frontend
cd /home/project/xrwvm-fullstack_developer_capstone/server/frontend
npm install
npm run build
# Set Sentimentanalyzer
* Set Up Mongo
cd /home/project/xrwvm-fullstack_developer_capstone/server/database
docker build . -t nodeapp
docker-compose up
* SetUp Django
* cd /home/project/xrwvm-fullstack_developer_capstone/server
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
python3 -m pip install -U -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

* Set Up Code Engine
Create Project
New CLI tab
cd xrwvm-fullstack_developer_capstone/server/djangoapp/microservices
docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000
sentiment_analyzer_url=your code engine deployment url

# Kubernetes deployment


Add a base image.
Add the requirements.txt file.
Install and update Python.
Change the working directory.
Expose port.
Run the command to start the application.

Create a Dockerfile in the server
entrypoint.sh. Create this file in the server
new terminal cd /home/project/xrwvm-fullstack_developer_capstone/server
MY_NAMESPACE=$(ibmcloud cr namespaces | grep sn-labs-)
echo $MY_NAMESPACE
docker build -t us.icr.io/$MY_NAMESPACE/dealership .
docker push us.icr.io/$MY_NAMESPACE/dealership
kubectl apply -f deployment.yaml
kubectl port-forward deployment.apps/dealership 8000:8000

