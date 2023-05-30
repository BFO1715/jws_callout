<strong><u>JWS Callout Request</u></strong>

npm install -g heroku<br>
heroku login -i<br>
check env.py

Admin/WeighingCompany<br>
Weigh1715<br>
bethan@johnwhiteandson.com<br>
APi Key

python3 manage.py makemigrations<br>
python3 manage.py migrate<br>
python3 manage.py runserver

import os

os.environ["DATABASE_URL"]="postgres://altiihsq:Vecuor_Jvir81c122tOv3w-qRkmRBnXN@lucky.db.elephantsql.com/altiihsq"
os.environ["SECRET_KEY"]="my-jws-secret-key"
os.environ["CLOUDINARY_URL"]="cloudinary://798566658129613:ExOirMglR8aUVwNJdFs86BDFk6U@diplwfbus"
