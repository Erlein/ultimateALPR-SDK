# UltimateALPR - Python mobile device testing

This project utilizes the [UltimateALPR-SDK](https://github.com/DoubangoTelecom/ultimateALPR-SDK) by DuobangoTelecom to test ALPR performance on mobile devices.
For more information on the full project, visit the hyperlink above.

## Setup:
Clone repository into desired location.

    git clone https://github.com/Erlein/ultimateALPR-SDK.git UALPR
*Final argument ("UALPR") simply names the directory to clone into. Omit for default.*

Navigate to relevant Binaries folder:
	binaries/\<os>/\<platform>
Example for linux on a desktop computer (x86_64):

    cd UALPR/binaries/linux/x86_64

If you are uncertain what platform you are running (on linux), ```uname -m``` in a terminal can provide the answer.

#### Linux x86 users:
You will need to aquire tensorflow library files.
Duobango host two variations here:
One with GPU support: [Libtensorflow r1.14 cpu+gpu linux x86](https://doubango.org/deep_learning/libtensorflow_r1.14_cpu+gpu_linux_x86-64.tar.gz)
And one for CPU only: [Libtensorflow r1.14 cpu linux x86](https://doubango.org/deep_learning/libtensorflow_r1.14_cpu_linux_x86-64.tar.gz)
These can easily be downloaded using wget and extracted on your linux system, example for GPU+CPU version below:

    wget https://doubango.org/deep_learning/libtensorflow_r1.14_cpu+gpu_linux_x86-64.tar.gz
    tar -xf libtensorflow_r1.14_cpu+gpu_linux_x86-64.tar.gz

To verify dependencies on linux x86_64, use  ```ldd libultimate_alpr-sdk.so``` in **binaries/linux/x86_64**.

#### Windows users:
To utilize GPU on Windows, tensorflow.dll located in **binaries/windows/x86_64** needs to be overridden with one found [here](https://doubango.org/deep_learning/libtensorflow_r1.15_cpu+gpu_windows_x86-64.zip) (hosted by duobango).

### Build the Python extension for your device:
Still in the relevant ```binaries/<os>/<platform> ```, call the following command:

    python ../../../python/setup.py build_ext --inplace -v
Use `python3` instead if you want to ensure python3 being used.

### Insert images to be tested
Put test-images (all will be loaded) into `/imgs` directory back in the root folder of the program.
(Only .jpg images with RGB24 format is supported as of now)

### Run the program
We can now call the program using the included exec.sh script.
From the relevant binaries directory, call `./exec.sh`
If "Permission denied" error is presented,  use `chmod +x exec.sh` to allow the bash script to be executed.
