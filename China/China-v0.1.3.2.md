***Latest Version***

***Software Spec (Test) Version: China-v0.1.3***

**SUMMIT Reader: 10.1.3.6**

**SUMMIT Server: 10.1.3.6**

* [x] Testing passed. 

      **Date: 2020/03/18**,     **Sign: Elina**

* [ ] Customers' devices status checked. 

      **Date: ____________**,   **Sign: ____________**

* [ ] Softwares installed and operations checked. 

      **Date: ____________**,   **Sign: ____________**

*  **Content**
    *  Submodule Version
        *  Grid: **v1.1.1.1**,          Date: **2020/01/22**
        *  Bamboo-Lake3: **CN-v0.1.3.4**,  Date: **2020/03/18**
        *  Daemon: **CNI-v1.15.6**,        Date: **2020/03/10**
        *  Magpie3: **CN-v0.1.3.8**,       Date: **2020/03/06**
        *  FW: **0C5.10**

    *  Release Notes
        *  Grid:
        
            none

        * Bamboo-Lake3:
            1. Experiment Manager support X1B.

        *  Daemon:
            1. Update: abort command now check task running status and surely abort the task. The old implementation is time based check and may not abort the running task if the time duration between abort check points is too long.
            2. Feature: LED used time related function.
            3. Feature: Final error handling and time stability checker.
            4. Feature: Auto scan and related setting.
            5. Feature: PLATE_MOVE_IN(OUT) command added.
            6. Feature: Camera re-open flow.
            7. Update: Remove RFID read during tray scanning.
            8. Update: COVER_SWITCH close not move plate.
            9. Development: Bring all critical unit test back.
            10. Reduce log noise.
            11. Camera long exposure time protect.
            12. LED used time QAQC display use HH:MM::SS.
            13. Version only show 2 digits.
            14. Bugfix: scan and camera preview conflict.
            15. Bugfix: mainboard de-initialize crash.
            16. Bugfix: exception not send to client.
            17. Bugfix: Bugfix: camera exposure time not changed when preview running.
            18. Bugfix: add camera setting input value check.
            19. Bugfix: daemon status dump return without waiting.
            20. Bugfix: daemon down compatible to firmware 0C5.9. The SN value of chip log will show empty if firmware version < 0C5.10
            
        *  Magpie3:
            1. Bugfix: License expired view and initialize failed view should not same.
            2. Bugfix: Able to reopen during scanning.
        
* **Software Publish** 
    * server-setup-10.1.3.6 @ smtdata\john\Summit_builds\server-setup-10.1.3.6
    * reader-setup-10.1.3.6 @ smtdata\john\Summit_builds\reader-setup-10.1.3.6

=============================================================================================

***Previous Version***

**SUMMIT Reader: 10.1.3.0a**

**SUMMIT Server: 10.1.3.0a**
