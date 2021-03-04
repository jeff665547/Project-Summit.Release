



***Latest Version***

***Software Spec (Test) Version: USA-v0.2.23***

**SUMMIT Reader: 20.2.23.3**

**SUMMIT Server: 20.2.23.3**

* [x] Testing passed.

      **Date: 2021/03/04**,   **Sign: Silvia**

* [ ] Customers' devices status checked.

      **Date: ____________**,   **Sign: ____________**

* [x] Softwares installed and operations checked.

      **Date: 2021/03/04**,   **Sign: vons**
      send the installation files to USA for update.

*  **Content**  
    *  Submodule Version  
        *  Magpie3: **USA-v0.2.23.1**,          Date: **2021/01/22**  
        *  Bamboo-lake3: **USA-v0.2.23.0**,          Date: **2021/1/20**  
        *  Summit.daemon: **USI-v1.15.57**,          Date: **2021/03/02**  
        *  Summit.grid: **v1.3.8**,          Date: **2021/02/23**  
        *  FW: **0C.5.13**

    *  Release Notes  
        *  Magpie3:
  
        *  Bamboo-lake3:
  
        *  Summit.daemon:  
            1. Update: update ChipImgProc to fix the grid2 issue.  
            2. Update: Upgrade to Grid2.  
            3. Bugfix: unit test failed issue of ARUCO.  
            4. CI test change aruco_test_img-1.tiff to aruco_test_img-0.tiff in origin_infer_test.cpp
  
        *  Summit.grid:  
            1. Feature: Generate WARNING file for reference when one of the following conditions is met:  
            2. 1. The gridding program detect some unexpected error.  
            3. 2. The value of "grid_done" in the grid_log.json is false.  
            4. 3. The value of "grid_bad" in the grid_log.json is true.  
            5. 4. The quality of BF or fluorescent marker_append images are lower than the expected threshold.  
            6. Feature: Automatically evaluate the gridding quality from denosied marker_append images. (For BF images gridding process, evaluate the BF marker_append image only.)  
            7. Feature: Output files adjustment: For each channel, viewable_raw folder contains cropped and raw scaled (e.g. 1 Feature corresponds to about 9.6 pixels in YZ01 chip) FOV images, stitched image and its corresponding gridline x and y positions (floating-point format).  
            8. Feature: Output files adjustment: For each channel, original data in the viewable_raw folder will be moved into viewable_rescale folder (viewable_rescale folder only generate in debug >= 5).  
            9. Feature: Add fluorescent images gridding process.
  
* **Software Publish** 

    * reader-setup-dev-20.2.23.3 @ smtdata/john/Summit_builds/reader-setup-dev-20.2.23.3

    * server-setup-dev-20.2.23.3 @ smtdata/john/Summit_builds/server-setup-dev-20.2.23.3

    or https://centrilliontechtw-my.sharepoint.com/:f:/g/personal/jeffho_centrilliontech_com_tw/EszoMSDmBvRPoDLnl2i_blMBH63d2gHUkYPdhjDA4CD2xg?e=jS8R5f

=============================================================================================

***Previous Version***

**SUMMIT Reader: 20.2.23.1**

**SUMMIT Server: 20.2.23.1**