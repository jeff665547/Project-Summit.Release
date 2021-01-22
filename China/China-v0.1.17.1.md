




***Latest Version***

***Software Spec (Test) Version: China-v0.1.17***

**SUMMIT Reader: 10.1.17.1**

**SUMMIT Server: 10.1.17.1**

* [x] Testing passed.

      **Date:  2021/01/22 **,   **Sign:    Silvia   **

* [ ] Customers' devices status checked.

      **Date: ____________**,   **Sign: ____________**

* [ ] Softwares installed and operations checked.

      **Date: ____________**,   **Sign: ____________**

*  **Content**  
    *  Submodule Version  
        *  Magpie3: **CN-v0.1.17.1**,          Date: **2021/01/22**  
        *  Bamboo-lake3: **CN-v0.1.17.0**,          Date: **2021/1/20**  
        *  Summit.daemon: **CNI-v1.15.56**,          Date: **20201/01/20**  
        *  Summit.grid: **v1.3.7**,          Date: **2021/01/20**  
        *  FW: **0C.5.13**

    *  Release Notes  
        *  Magpie3:  
            1. Change the default value of the configuration file.
  
        *  Bamboo-lake3:
  
        *  Summit.daemon:  
            1. Update: Upgrade to Grid2.  
            2. Bugfix: unit test failed issue of ARUCO.  
            3. CI test change aruco_test_img-1.tiff to aruco_test_img-0.tiff in origin_infer_test.cpp
  
        *  Summit.grid:  
            1. Feature: Using bilinear interpolation during getting the ROI from the boundary of the score matrix.  
            2. Feature: Modified structure of warped_mat and other class related to it for the debug mode.  
            3. Feature: Add param about margin to store related parameters for the debug mode.  
            4. Feature: Change the procedure to accelerate processing speed in estimate_bias.hpp.  
            5. Perf: Increase CPU_BASELINE from SSE3 to AVX2 in cmake configuration of opencv  
            6. Perf: Using OpenBLAS to speed up mathamatic calculations  
            7. Misc: Only output debug image if logger level > 5, and output more debug message to help tracing  
            8. Misc: Immediately exit program when error thrown, but only if using highest logger level  
            9. Bugfix: Bugfix for one-pixel shifting issue ("precise", "quick", and "regular" scan mode) in ChipImgProc.  
            10. Feature: Adapt codes of BF image process to for the fluorescent image process.  
            11. Feature: Set "unknown" and "abandoned" scan mode to run default estimate_bias and use reference marker position respectively.  
            12. Log: Output warning message to logger instead of stdout.
  
* **Software Publish** 

    * reader-setup-dev-10.1.17.1 @ smtdata/john/Summit_builds/reader-setup-dev-10.1.17.1

    * server-setup-dev-10.1.17.1 @ smtdata/john/Summit_builds/server-setup-dev-10.1.17.1

    or https://centrilliontechtw-my.sharepoint.com/:f:/g/personal/jeffho_centrilliontech_com_tw/EmWiay6p15tNkAAk1TSHlWYBMioJmnnSNNv1XYo5_mzQsQ?e=XMyfWr

=============================================================================================

***Previous Version***

**SUMMIT Reader: 10.1.16.5**

**SUMMIT Server: 10.1.16.5**
