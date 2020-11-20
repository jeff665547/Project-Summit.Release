




***Latest Version***

***Software Spec (Test) Version: China-v0.1.16***

**SUMMIT Reader: 10.1.16.2**

**SUMMIT Server: 10.1.16.2**

* [ ] Testing passed.

      **Date:  2020/11/20 **,   **Sign: Silvia, Isla**

      **Know issue: E-tools RFID status issue when use Flowcell Scaning**

* [ ] Customers' devices status checked.

      **Date: ____________**,   **Sign: ____________**

* [ ] Softwares installed and operations checked.

      **Date: ____________**,   **Sign: ____________**

*  **Content**  
    *  Submodule Version  
        *  Magpie3: **CN-v0.1.16.3**,          Date: **2020/11/10**  
        *  Bamboo-lake3: **CN-v0.1.16.2**,          Date: **2020/10/28**  
        *  Summit.daemon: **CNI-v1.15.52**,          Date: **2020/11/18**  
        *  Summit.grid: **v1.3.3**,          Date: **2020/11/17**  
        *  FW: **0C.5.13**

    *  Release Notes  
        *  Magpie3:  
            1. Bugfix: Restart robocopy regularly.  
            2. Bugfix: Scanning quick mode supports L1B  
            3. Bugfix: Scanning quick mode supports RFID chip type to determine the order  
            4. Sync logs to remote.  
            5. Etool add quick scan mode.  
            6. Bugfix: Error case should show "camera plug off" but "daemon unable to get ready"
  
        *  Bamboo-lake3:  
            1. Support S1C  
            2. Can be set to send error messages based on the log results from the daemon
  
        *  Summit.daemon:  
            1. Bugfix: syntax error  
            2. Bugfix: make sleep in no_fram_handler.hpp:good_handle() and trait.hpp:close_camera() be true sleep, prevent other coroutine job uses camera during it's off  
            3. Bugfix: grammer update, make open camera fail procedure retry being waiting instead of coroutine waiting  
            4. Bugfix: make open camera fail procedure retry being waiting instead of coroutine waiting  
            5. Bugfix: Adjust firmware command retry and wait time.  
            6. Bugfix: Which result in red alarm frequently.  
            7. Bugfix: More precise initial scanning position support (trayinfo.json) for the S1C chip.  
            8. Bugfix: Make capture reset of no_frame_handler staggered with device request of grab().  
            9. Feature: Sequoia chip (S1C) support.  
            10. Bugfix: Fix the aruco_db.json (value for the index "0").  
            11. Update: Modify reboot.bat to ensure that the process is deleted.  
            12. Bugfix: Clear previous chip scanning information for the new ArUco (ArUco2) detector.  
            13. Update: Lassen wafer Lassen chip (L3B, L4C) support.  
            14. Update: Restart screen prompt.  
            15. Update: camera no frame flow update.  
            16. Update: reduce log message.  
            17. Bugfix: camera network configuration use default.  
            18. Bugfix: get configure state less  
            19. Bugfix: fix the last task not work problem  
            20. Bugfix: Open shutter after reset mainboard  
            21. Bugfix: prevent camera unplug trigger unfixed error  
            22. Update: remove more log noise.  
            23. Feature: multiple level camera no frame reopen  
            24. Feature: Camera reboot workflow more retry  
            25. Bugfix: Fix Lassen AM1E, AM5B swapped issue  
            26. Feature: More log for Vimba API call  
            27. Feature: Lassen wafer Lassen chip (L3B, L4C) support.  
            28. Update: Fix Lassen AM1E, AM5B swapped issue.  
            29. Merge 1.15.35  
            30. Merge 1.15.33  
            31. Merge 1.15.32  
            32. Update: merge 1.15  
            33. Update: Default log option update.  
            34. Feature: More log for task resume.  
            35. Feature: Remove error log noise.  
            36. Bugfix: Camera reboot bug with not full access.  
            37. Feature: add scan fov sequence parameter  
            38. Feature: add L1B@A support  
            39. Bugfix: Camera reboot recover configuration  
            40. Bugfix: Mono8 pixel format not work  
            41. Feature: Lassen default scan flow use classic style.  
            42. Feature: use semi-autofocus by default.  
            43. Feature: support YZ01 4 corners.  
            44. Feature: configurable semi-autofocus workflow  
            45. Feature: single chip scan now use regular RFID as directory  
            46. Bugfix: shutter closed by firmware because temperary connection break  
            47. Bugfix: single chip scan unexpect stop.  
            48. Update: User new Vimba API.
  
        *  Summit.grid:  
            1. Bugfix: More stable for the M/pT marker type at fluorescent channel.  
            2. Bugfix: More stable for quick scan mode image.  
            3. Feature: Support aruco2 and new chip for brighter background  
            4. Feature: Support for Sequoia chip (S1C).  
            5. Bugfix: Lassen marker type swap issue.  
            6. Feature: Support for new Lassen wafer Lassen chip (L3B, L4C) at fluorescent channel.  
            7. Feature: New gridding algorithm (Grid2).  
            8. Bugfix: YZ01 4 cornor configuration not complete.  
            9. Bugfix: Prevent several debug grid generation failed.  
            10. Feature: support YZ01 splited chip.  
            11. Bugfix: heatmap output path error.  
            12. Bugfix: fix yz01-41, Kenai process failed (configuration file problem)  
            13. Bugfix: exit code not work  
            14. Feature: built-in batch process with inplace mode  
            15. Feature: add option --force_inplace(-f)  
            16. Merge 1.1.22 update.
  
* **Software Publish** 

    * reader-setup-dev-10.1.16.2 @ smtdata/john/Summit_builds/reader-setup-dev-10.1.16.2

    * server-setup-dev-10.1.16.2 @ smtdata/john/Summit_builds/server-setup-dev-10.1.16.2

    or https://centrilliontechtw-my.sharepoint.com/:f:/g/personal/jeffho_centrilliontech_com_tw/EmWiay6p15tNkAAk1TSHlWYBMioJmnnSNNv1XYo5_mzQsQ?e=XMyfWr

=============================================================================================

***Previous Version***

**SUMMIT Reader: 10.1.11.0**

**SUMMIT Server: 10.1.11.0**
