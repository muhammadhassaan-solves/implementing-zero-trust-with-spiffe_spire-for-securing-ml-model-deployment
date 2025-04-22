<h1>Implementing Zero Trust with SPIFFE/SPIRE for Securing ML Model Deployment</h1>


<h2>Description</h2>
This project demonstrates the integration of SPIFFE and SPIRE for secure communication in a Flask-based machine learning service. I implemented mutual TLS (mTLS) to ensure both the client and server authenticate each other using certificates. This approach boosts security and trust for data exchanges. It also enables secure API calls for machine learning predictions while ensuring data integrity and privacy.
<br />


<h2>Utilities Used</h2>

- SPIFFE/SPIRE
- Python
- Flask
- mTLS
- numpy, scikit-learn, joblib
- Docker


<h2>Project Walk-through</h2>

<p align="center">
Set Up SPIRE Server <br />
<img src="https://i.imgur.com/dCtJVjE.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Configure the SPIRE Agent <br/>
<img src="https://i.imgur.com/sONQLkD.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Create SPIFFE Entry for the Service <br/>
<img src="https://i.imgur.com/8eh43U0.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Certificate Generation for Mutual TLS (mTLS) <br/>
<img src="https://i.imgur.com/znijD5P.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Flask API Implementation and Containerization <br/>
<img src="https://i.imgur.com/X4BGVIz.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Secure API Call with Curl After Another Certificate Generation <br/>
<img src="https://i.imgur.com/1XHdIdZ.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />

</p>


