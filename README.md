# Salary_Prediction_AWS_EC2
Deployed in AWS EC2 directly from local environment by puttygen



# Deployed in AWS EC2

### High Level steps:

	1) Flask Code
	2) Run and Check in Local
	3) Create AWS account
	4) Create EC2 Instance
	5) Download Putty and putty gen, Winscp
	6) Generate Private with help of puttygen
	7) Update the port in Flask app.py
	8) Install the libraries by connecting through Putty
	9) Run python3 app.py in putty
	10. Execution URL/Web url from EC2 instance and verify it.
11) Disable Instance

### Deployment main files:
		app.py
		MLDemoTesting.pem (This req to generate .ppk file)
		MLDemoTesting.ppk
		model.pkl
		procfile
		requirements.txt
		templates folder with home.html
		static folder with css folder with style file (Depends)


1) Login to AWS --> Search EC2 (Its a virtual server in cloude)--> Running Instance --> Launch Instance

2) Create AWS EC2 Instance:
  Now we are creating a cloud server, here we deploy our model and create api outof it
	Here we have many free tier server to create in cloud 

	--> Search Ubantu free tier and select(Any freeone can select) --> t2.micro (Free tier eligible) --> Review and Launch  --> Launch

	--> Select New key pair (Keypair pop up comes) (Whenever new instance create new keypair) --> Type 'MLDemoTest' (Key pair name) --> Press Download keypair

	--> Copy that downloaded file (MLDemoTesting.pem) in our project file(This helps us tocreate the private key via puttygen, this private key help us to interact with Linux env)
	
	--> Launch Instance(We can type any name (TestPrabha) while its lauching)

3) Make this instances accessable from everywhere. Make this setting in EC2

###	Select the instance and then in leftside list  
		--> Networks & Security --> Security Group --> Create a Security Group
			--> Security Groupname as "FullAccess" 
			--> Description as "FullAccess" 
		--> Click add rule
		In "INBOUND"
		--> Type as "All Traffic " (This is the various protocal to communicate with this api)
		--> Source as "Anywhere"
	--> Now select Create

4) Now we need to link this security group to EC2:
	Goto --> Networks & Security --> Networks Interfaces --> Right click on 1st interface id --> Select "Change security group"
		--> In Associated security groups selct "FullAccess" Named newly created security Group --> Save
		--> Now we can see security groups as "FullAccess" 


5) In Puttygen: To create Private Key using pem file
	--> Convert .ppk version 3 to 2 , else it will fail later(One time)
		Inside Puttygen --> Key -->Parameter for saving Keys  -->vesrion change 3 to 2
		
	--> Select Load --> Load our MLDemoTesting.pem file  --> Open 
		--> OK(Successfull imported privatekey ) --> Save Private Key --> Without Pharser
		--> Give name as 'MLDemoTesting' and provide our location--> It saves from pem file as .ppk fileSave Private key in .ppk  (This is a privatekey)

6) In EC2 Copy the Public DNS:
	--> Now goto EC2 instance newly created(Testprabha) instance --> ActionS --> Connect  ( to your instance, there we will get out winscp required hostname. Which is Public DNS)
		--> In 'SSH Client' tab copy Hostname / (Connect to your instance using its Public DNS:) ec2-13-229-242-115.ap-southeast-1.compute.amazonaws.com

7) Connect to EC2 via Winscp:
	--> Winscp helps to deploy code in EC2 instance just like connecting to server and drag and drop

	-->Inside Winscp Copy above Public DNS as Hostname here -->Username Default as 'ubuntu' --> in  Advanced select Authentication-->
		--> selct the uploading option to selct private key file "MLDemoTesting.ppk" file(this is a private key to connect with ubuntu ec2 server)
		--> Ok -->Login -->yes
  		--> Now it coonects to AWS EC2 and shows empty folder in winscp (/home/ubuntu)


	--> Now drag drop all our code from local to winscp AWS ec2 folder
		app.py  
		model.pkl  
		requirements.txt  
		folder: templates

8) Connect to EC2 via putty:
	--> Copy above Public DNS as Hostname here --> Type "MLDemoTest" as saved session and save
	--> Goto SSH -->Goto Auth --> Privatekeyfor authantication select "MLDemoTest.ppk" ---> Press Open
	--> Now putty Command Prompt opens --> Type 'ubuntu' as login as
	--> Now it connects to EC2 server : ubuntu@ip-172-31-45-206:~$
	--> Type pwd shows our directory (/home/ubuntu)

9) We need to install few libraries in ec2, so we connected to putty command prompt (All the library available in requirement.txt , we need to install)

	pip3 install panda   
		--> This shows error, so type below lines (coz version are not sync)
	sudo apt-get update && sudo apt-get install python3-pip

	#This to install all libraries in req.txt file in unbuntu ec2 
	pip3 install -r requirements.txt

10) Deploy now in putty
	Write below command in putty 
		python3 app.py

	Now it will execute in 8080 portal and show message " Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)"

11) EC2 Deployed and checking via URL
	In our instance Status check shows as passed
	select our instance -->Connect --> There we will get our URL(Public DNS)  ec2-13-229-242-115.ap-southeast-1.compute.amazonaws.com
	
	URL:
		Copy this in google and write :8080 at the end
		 ec2-13-229-242-115.ap-southeast-1.compute.amazonaws.com:8080

