***Latest Version***

***Software Spec (Test) Version: USA-v0.2.5***

**SUMMIT Reader: 10.1.4.1**

**SUMMIT Server: 10.1.4.1**

* [x] Testing passed. 

      **Date: 2020/03/27**,     **Sign: Cynthia**

* [ ] Customers' devices status checked. 

      **Date: ____________**,   **Sign: ____________**

* [x] Softwares installed and operations checked. 

      **Date: 2020/3/31**,   **Sign: vons**
      Only update the computer 181 and 694, computer 249 does not update this time due to the customer's requirement.
     

*  **Content**
    *  Submodule Version
        *  Grid: **v1.1.2**,          Date: **2020/03/19**
        *  Bamboo-Lake3: **CN-v0.1.4.1**,  Date: **2020/03/25**
        *  Daemon: **CNI-v1.15.10**,        Date: **2020/03/26**
        *  Magpie3: **CN-v0.1.4.0**,       Date: **2020/03/18**
        *  FW: **0C5.10**

    *  Release Notes
        *  Grid:
            1. Update: Use raw channel name as CEN file channel name, instead of channel-0/1.
            2. Feature: Add Kenai support.
            3. Feature: Background subtraction use Spline algorithm.

        * Bamboo-Lake3:
            1. Add kenai c11 c22.

        *  Daemon:
            1. Feature: support Kenai chip scanning.
            2. Bugfix: COM port automatic search failed.
            3. Develop: Internal update for QAQC tool.
            4. Bugfix: ArUco marker origin inference failed.
            5. Bugfix: Chip roation estimatation optimize.
            
        *  Magpie3:
            1. Bugfix: Abort after scan reopen not open the cover.
            2. Feature: Remove initialize failed dialog. (The license expired dialog still preserved).
            3. Feature: Add API server IP configuration on intial setting dialog.
            4. Feature: The sync directory(and API server IP config) will show after scan module initialize failed.
            5. Feature: If license expired, the license expired dialog will directly show after initialize end.
        
* **Software Publish** 
    * server-setup-10.1.4.1 @ smtdata\john\Summit_builds\server-setup-10.1.4.1
    * reader-setup-10.1.4.1 @ smtdata\john\Summit_builds\reader-setup-10.1.4.1

=============================================================================================

***Previous Version***

**SUMMIT Reader: 10.1.3.6**

**SUMMIT Server: 10.1.3.6**
