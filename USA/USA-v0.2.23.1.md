



***Latest Version***

***Software Spec (Test) Version: USA-v0.2.23***

**SUMMIT Reader: 20.2.23.1**

**SUMMIT Server: 20.2.23.1**

* [x] Testing passed.

      **Date:  2021/01/22 **,   **Sign:    Silvia   **

* [ ] Customers' devices status checked.

      **Date: ____________**,   **Sign: ____________**

* [x] Softwares installed and operations checked.

      **Date: 2020/01/22**,   **Sign: vons**
    send the installation files to the USA for update

*  **Content**  
    *  Submodule Version  
        *  Magpie3: **USA-v0.2.23.1**,          Date: **2021/01/22**  
        *  Bamboo-lake3: **USA-v0.2.23.0**,          Date: **2021/1/20**  
        *  Summit.daemon: **USI-v1.15.56**,          Date: **20201/01/20**  
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
  
* **Software Publish** 

    * reader-setup-dev-20.2.23.1 @ smtdata/john/Summit_builds/reader-setup-dev-20.2.23.1

    * server-setup-dev-20.2.23.1 @ smtdata/john/Summit_builds/server-setup-dev-20.2.23.1

    or https://centrilliontechtw-my.sharepoint.com/:f:/g/personal/jeffho_centrilliontech_com_tw/EszoMSDmBvRPoDLnl2i_blMBH63d2gHUkYPdhjDA4CD2xg?e=jS8R5f

=============================================================================================

***Previous Version***

**SUMMIT Reader: 20.2.22.7b**

**SUMMIT Server: 20.2.22.7b**
