
THIS CODE WILL NOT WORK WITH FLASK'S DEVELOPMENT SERVER (You must use httpd with WSGI or a production web server)

The API takes an image as a byte stream and returns an image as a byte stream

Cython can speed up processing but it must be tailord to each need, running the shell scrip on the Cython directory will build and copy the binary to the environments location otherwise you must remove all "C" like syntax and replace it with python.


![alt text](https://github.com/d3spinoz4/Paramecia/blob/main/png/road-img.png?raw=true)

Parallel processing Top view:

![alt text](https://github.com/d3spinoz4/Paramecia/blob/main/png/top.png?raw=true)

CPU and multiprocessing SharedMemory using python system monitor stats:

![alt text](https://github.com/d3spinoz4/Paramecia/blob/main/png/system.png?raw=true)

Results:

![alt text](https://github.com/d3spinoz4/Paramecia/blob/main/png/road-img-svd.png?raw=true)

Alternative to Matlab's SVD (Singular Value Decomposition https://www.mathworks.com/matlabcentral/fileexchange/48817-svd-eigen-qr-and-lu-texture-transforms?tab=reviews):

![alt text](https://github.com/d3spinoz4/Paramecia/blob/main/png/koala.png?raw=true)

Results will vary (be faster) depending on ROI and image resolution:

![alt text](https://github.com/d3spinoz4/Paramecia/blob/main/png/koala-svd.png?raw=true)
