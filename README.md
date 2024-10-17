# Facial Recognition

This repository contains code that allows you to run this facial recognition script locally, or from a client-server model.

## Installation

### dlib Requirements (Windows)

If you are on Mac or Linux you can skip this step...

- Install [Microsoft C++ Build Tools](https://aka.ms/vs/17/release/vs_buildtools.exe)

![Build Tools Install GUI](https://i.stack.imgur.com/jKl2N.png)

dlib can be challenging to install on Windows. If you are having trouble try looking through this [Stack Overflow Issue](https://stackoverflow.com/questions/74476152/error-in-installing-dlib-library-in-python3-11)

### dlib Requirements (Ubuntu/Mac)

Refer to [this guide](https://pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/) for help installing dlib on Mac/Linux:

### Install Python Packages

Start by cloning this repository: `git clone <repo-url>` then `cd <repo-directory>`

To install the required packages ensure you are using Python 3.7+ and run the command:

- `pip install -r requirements.txt` (Windows) or
- `pip3 install -r requirements.txt` (Mac/Linux)

## Running The Code

### Running The Code Locally

Assuming all of the packages are installed correctly you should be able to run the code locally.

- Change directories into the `/tutorial` folder: `cd tutorial`
- Execute the python script `face_rec.py`: `python face_rec.py` or `python3 face_rec.py`
- Wait, and press `q` to quit the window!

If you'd like to change the image the faces are being predicted for simply download a new image and set the path on line 55 from `face_rec.py`:

```python
print(classify_face("test-image.jpg"))
```

### Running With Client/Server

Running the code from the client/server model is slightly more complicated.

- Start by running the flask backend server.
- Change directories to `/server`: `cd server`
- Start the API server: `python main.py` or `python3 main.py` (take note of the port it is running on, default is `5000`)

- Now that the server is running you can change to the `/client` directory: `cd ../client`
- If necessary adjust the URL on line 13 of `client.py` to specify the correct port.
- From the client directory run `client.py`: `python client.py` or `python3 client.py`

If you'd like to change the image the faces are being predicted for simply download a new image and set the path on line 14 from `client.py`:

```python
my_img = {'image': open('test-image.jpg', 'rb')} # feel free to change the image path here
```

## Customization

### Adding Faces

To add more faces to be detected simply add a labelled `.jpg` or `.png` file to the `/faces` directory. If you were to add an image of Tim (me!) you would simply save the image as `tim.png` (or `tim.jpg`).

## Deployment

If you're intersted in deploying the flask server have a look at this [Repository](https://github.com/techwithtim/Flask-App-Hosted-On-VPS) and this [YouTube Video](https://www.youtube.com/watch?v=KgAtZ1LlNiQ)


# 💻 Launch Your Software Development Career Today!  

🎓 **No degree? No problem!** My program equips you with everything you need to break into tech and land an entry-level software development role.  

🚀 **Why Join?**  
- 💼 **$70k+ starting salary potential**  
- 🕐 **Self-paced:** Complete on your own time  
- 🤑 **Affordable:** Low risk compared to expensive bootcamps or degrees
- 🎯 **45,000+ job openings** in the market  

👉 **[Start your journey today!](https://techwithtim.net/dev)**  
No experience needed—just your determination. Future-proof your career and unlock six-figure potential like many of our students have!  
