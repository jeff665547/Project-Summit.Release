***Latest Version***

***Software Spec (Test) Version: USA-v0.2.9***

**SUMMIT Reader: 20.2.9.3**

**SUMMIT Server: 20.2.9.3**

* [X] Testing passed. 

      **Date: 2020/03/06**,     **Sign: Cynthia & Elina**

* [ ] Customers' devices status checked. 

      **Date: ____________**,   **Sign: ____________**

* [ ] Softwares installed and operations checked. 

      **Date: ____________**,   **Sign: ____________**

*  **Content**
    *  Submodule Version
        *  Grid: **v1.1.1.1**,          Date: **2020/01/22**
        *  Bamboo-Lake3: **USA-v0.2.9.1**,  Date: **2020/02/27**
        *  Daemon: **USI-v1.15.5**,        Date: **2020/03/05**
        *  Magpie3: **USA-v0.2.9.9**,       Date: **2020/03/06**

    *  Release Notes
        *  Grid:
        
            none.

        * Bamboo-Lake3:
            1. Support YZ01(X1B).
            2. Ignore X1B when Image gridding selects RFID.
            3. Fix image gridding download.

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
            17. Bugfix: camera exposure time not changed when preview running.
            18. Bugfix: add camera setting input value check.
            
        *  Magpie3:
            1. Optimize scan module initialization.
            2. Scan module able to view the auto scanning process.
            3. Bring etool able to ran on browser.
            4. Scan module cover, abort interaction optimize.
            5. Scan module optimize initialization.
            6. Scan module error diagnosis in runtime.
            7. Etool loading time optimize.
            8. Bugfix: Scan module switch to Etool during initialization not crash.
            9. Bugfix: scan module initialize failed.
            10. Bugfix: Configuration not saved into filesystem.
            11. Bugfix: Configuration display not synchronized.
            12. Etool UI/UX visualization optimize.
            13. Bugfix: Initial failed by ASAR filesystem.
            14. Bugfix: Etool shutter switch not work.
            15. Bugfix: Scan module cover close no insert plate (only with daemon > 1.15).
            16. Feature: Commander editor more function.
            17. Feature: Optimize initialization.
            18. Bugfix: Prevent image sync with same source and destination.
            19. Feature: Add license expired view.
            20. Bugfix: Calibration rectangle not show in preview.
            21. Bugfix: License expired view and initialize failed view should not same.
            22. Bugfix: Able to reopen during scanning.
        
* **Software Publish** 
    * server-setup-20.2.9.3 @ smtdata\john\Summit_builds\server-setup-20.2.9.3
    * reader-setup-20.2.9.3 @ smtdata\john\Summit_builds\reader-setup-20.2.9.3

=============================================================================================

***Previous Version***

**SUMMIT Reader: 20.2.8.2a**

**SUMMIT Server: 20.2.8.2a**
