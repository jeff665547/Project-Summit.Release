



***Latest Version***

***Software Spec (Test) Version: USA-v0.2.22***

**SUMMIT Reader: 20.2.22.5**

**SUMMIT Server: 20.2.22.5**

* [X] Testing passed.

      **Date:  2020/11/20 **,   **Sign: Silvia, Isla**

      **Know issue: E-tools RFID status issue when use Flowcell Scaning**

* [ ] Customers' devices status checked.

      **Date: ____________**,   **Sign: ____________**

* [x] Softwares installed and operations checked.

      **Date: 2020/11/20**,   **Sign: vons**
      send the installation files to USA for an update.

*  **Content**  
    *  Submodule Version  
        *  Magpie3: **USA-v0.2.22.3**,          Date: **2020/11/10**  
        *  Bamboo-lake3: **USA-v0.2.22.2**,          Date: **2020/10/28**  
        *  Summit.daemon: **USI-v1.15.52**,          Date: **2020/11/18**  
        *  Summit.grid: **v1.3.3**,          Date: **2020/11/17**  
        *  FW: **0C.5.13**

    *  Release Notes  
        *  Magpie3:
  
        *  Bamboo-lake3:
  
        *  Summit.daemon:  
            1. Bugfix: syntax error  
            2. Bugfix: make sleep in no_fram_handler.hpp:good_handle() and trait.hpp:close_camera() be true sleep, prevent other coroutine job uses camera during it's off  
            3. Bugfix: grammer update, make open camera fail procedure retry being waiting instead of coroutine waiting  
            4. Bugfix: make open camera fail procedure retry being waiting instead of coroutine waiting
  
        *  Summit.grid:  
            1. Bugfix: More stable for the M/pT marker type at fluorescent channel.  
            2. Bugfix: More stable for quick scan mode image.
  
* **Software Publish** 

    * reader-setup-dev-20.2.22.5 @ smtdata/john/Summit_builds/reader-setup-dev-20.2.22.5

    * server-setup-dev-20.2.22.5 @ smtdata/john/Summit_builds/server-setup-dev-20.2.22.5

    or https://centrilliontechtw-my.sharepoint.com/:f:/g/personal/jeffho_centrilliontech_com_tw/EszoMSDmBvRPoDLnl2i_blMBH63d2gHUkYPdhjDA4CD2xg?e=jS8R5f

=============================================================================================

***Previous Version***

**SUMMIT Reader: 20.2.22.3a**

**SUMMIT Server: 20.2.22.3a**
