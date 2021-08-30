




***Latest Version***

***Software Spec (Test) Version: USA-v0.2.24***

**SUMMIT Reader: 20.2.24.3a**

**SUMMIT Server: 20.2.24.3a**

* [ ] Testing passed.

      **Date: ____________**,   **Sign: ____________**

* [ ] Customers' devices status checked.

      **Date: ____________**,   **Sign: ____________**

* [ ] Softwares installed and operations checked.

      **Date: ____________**,   **Sign: ____________**

*  **Content**  
    *  Submodule Version  
        *  Magpie3: **USA-v0.2.24.1**,          Date: **2021/05/19**  
        *  Bamboo-lake3: **USA-v0.2.24.0**,          Date: **2021/4/14**  
        *  Summit.daemon: **USI-v1.15.65**,          Date: **2021/07/27**  
        *  Summit.grid: **v1.3.14**,          Date: **2021/07/27**  
        *  FW: **__________**

    *  Release Notes  
        *  Magpie3:
  
        *  Bamboo-lake3:
  
        *  Summit.daemon:  
            1. Feature: New autofocus mechanism and algorithm for finding location (ArUco) marker and quick scanning.  
            2. Feature: Jasper chip (J1C, J2C) support.  
            3. Average chip scanning time (seconds):  
            4. | Chip Type    | Precise (v1.15.63) | Qucik (v1.15.63) | Precise (v1.15.65) | Qucik (v1.15.65) | Precise **Speedup** | Qucik **Speedup** |  
            5. |:------------:|:------------------:|:----------------:|:------------------:|:----------------:|:-------------------:|:-----------------:|  
            6. | S1C_TL (1x1) | 17.697 (s)         | 10.354 (s)       | 14.533 (s)         | 7.067 (s)        | **1.22x**           | **1.47x**         |  
            7. | S1C (2x2)    | 54.011 (s)         | 21.090 (s)       | 50.867 (s)         | 11.800 (s)       | **1.06x**           | **1.79x**         |  
            8. | B1C (3x3)    | 189.266 (s)        | 72.246 (s)       | 148.200 (s)        | 35.533 (s)       | **1.28x**           | **2.03x**         |  
            9. | Y2B (7x7)    | 985.411 (s)        | 423.705 (s)      | 779.333 (s)        | 207.333 (s)      | **1.26x**           | **2.04x**         |  
            10. Full tray scanning time (hours):  
            11. | S1C_TL (384) | 2.345 (h)          | 1.564 (h)        | 1.805 (h)          | 1.029 (h)        | **1.30x**           | **1.52x**         |  
            12. | S1C (384)    | 6.219 (h)          | 2.707 (h)        | 5.693 (h)          | 1.537 (h)        | **1.09x**           | **1.76x**         |  
            13. | B1C (384)    | 20.634 (h)         | 6.428 (h)        | 16.130 (h)         | 4.050 (h)        | **1.28x**           | **2.59x**         |  
            14. | Y2B (96)     | 26.425 (h)         | 10.429 (h)       | 17.081 (h)         | 5.807 (h)        | **1.55x**           | **1.80x**         |  
            15. Feature: Extend the use date to 2022/7.  
            16. Feature: DF1000 chip (D1B) support.
  
        *  Summit.grid:  
            1. Feature: Jasper chip (J1C, J2C) support.  
            2. Feature: Generate the log of the gridding program to each chip folder when the corresponding argument (-g / --enable_log) is given in the command line.
  
* **Software Publish** 

    * reader-setup-dev-20.2.24.3a @ smtdata/john/Summit_builds/reader-setup-dev-20.2.24.3a

    * server-setup-dev-20.2.24.3a @ smtdata/john/Summit_builds/server-setup-dev-20.2.24.3a

    or https://centrilliontechtw-my.sharepoint.com/:f:/g/personal/jeffho_centrilliontech_com_tw/EszoMSDmBvRPoDLnl2i_blMBH63d2gHUkYPdhjDA4CD2xg?e=jS8R5f

=============================================================================================

***Previous Version***

**SUMMIT Reader: 20.2.24.2a**

**SUMMIT Server: 20.2.24.2a**