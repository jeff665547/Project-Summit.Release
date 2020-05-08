***Latest Version***

***Software Spec (Test) Version: China-v0.1.5***

**SUMMIT Reader: 10.1.5.5**

**SUMMIT Server: 10.1.5.5**

* [x] Testing passed. 

      **Date: 2020/04/17**,     **Sign: Cynthia & Elina**

* [ ] Customers' devices status checked. 

      **Date: ____________**,   **Sign: ____________**

* [x] Softwares installed and operations checked. 

      **Date: 2020/4/21**,   **Sign: Vons**

*  **Content**
    *  Submodule Version
        *  Grid: **v1.1.4**,          Date: **2020/4/14**
        *  Bamboo-Lake3: **CN-v0.1.5.5**,  Date: **2020/4/17**
        *  Daemon: **CNI-v1.15.13**,        Date: **2020/4/8**
        *  Magpie3: **CN-v0.1.5.1**,       Date: **2020/4/15**
        *  FW: **0C.5.9**

    *  Release Notes
        *  Grid:
            1. Feature: Add debug grid stiched image. All channel stacked into a multi-channel image(png).
                - Use option "-d 5" and the result will generate in "grid" directory.
                - The color mapping is follow the channel filter:
                - 0 -> blue
                - 2 -> green
                - 4 -> red
            2. Feature: More stitched image.

        * Bamboo-Lake3:
            1. Image Viewer adds preview zoom function.
            2. Image Viewer increases the loading speed of large images.
            3. Image Viewer partially reconstructed layout.
            4. jszip module bug fix.
            5. Image Viewer modify grid button style and operation.
            6. Added automatic image segmentation script.
            7. Image Gridding adds "apply viewer" button.
            8. Bug fix.

        *  Daemon:
            1. Bugfix: Clean deprecated trayinfo.
            2. Bugfix: Scan flow blocked after camera reopen.
            3. Feature: Change default image save path.
            4. Feature: Prevent host sleep when Summit running.
            5. Feature: Loose CPU resource monitor.
            6. Update: New license expired detection.
            7. Bugfix: long exposure time image capture failed.
            8. Bugfix: JSSC COM port sometimes close failed.
            9. Feature: Workflow for reader switch to on/off during the daemon running.
            10. Feature: System halting protection: Large time gap suicide workflow.
            
        *  Magpie3:
            1. Bugfix: Scan module unable to show K1B layout.
        
* **Software Publish** 
    * server-setup-10.1.5.5 @ smtdata\john\Summit_builds\server-setup-10.1.5.5
    * reader-setup-10.1.5.5 @ smtdata\john\Summit_builds\reader-setup-10.1.5.5

=============================================================================================

***Previous Version***

**SUMMIT Reader: 10.1.4.1**

**SUMMIT Server: 10.1.4.1**
