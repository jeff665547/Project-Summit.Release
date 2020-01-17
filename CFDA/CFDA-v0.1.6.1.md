***Latest Version***

***Software Spec (Test) Version: CFDA-v0.1.6***

**SUMMIT Reader: 00.1.6.1**

**SUMMIT Server: 00.1.6.1**

* [x] Testing passed.

      **Date: 2019/11/20**,     **Sign: Michael**

* [x] Customers' devices status checked.

      **Date: 2020/01/15**,   **Sign: Joye Li**
      
      Note. This is CFDA computer

* [x] Softwares installed and operations checked. 

      **Date: 2020/01/15**,   **Sign: Joye Li**

*  **Content**
    *  Submodule Version
        *  Grid: **CFDA-v0.1.6-v1.0.11**,          Date: **2019/10/25**
        *  Daemon: **CFDA-v0.1.6-0.14.19.2**,        Date: **2019/11/19**
        *  Magpie2: **CFDA-v0.1.6-2**,       Date: **2019/11/15**

    *  Release Notes
        *  Grid:
            1.  Bugfix: ZION chip gridding failed (from 1.0.0)
            2.  Bugfix: BANFF chip crash (from 1.0.2)
            3.  Feature: Add white marker append
            4.  Update: Update run batch script
            5.  Bugfix: None auto grid sometimes crash(marker append ROI bug)
			6.  Bugfix: Crypto algorithm
			7.  Bugfix: no backgroud process workflow cell margin twice
			8.  Feature: debug mode add margin view.
			9.  Feature: add raw stitch image output
			10. Feature: new ArUco matching algorithm import
			11. Develop update: Linux use new dynamic link solution
			12. Update: ArUco matching update
			13. Source code: MSVC build support
				1. Currently only support Visual Studio 2017 v15.9.
			14. Update: light mean application output detail probe informations.
			15. Bugfix: CEN file Channel ID not match specification.
			16. Bugfix: debug flag effect the image process behavior
				1. ArUco marker detection failed when debug level <= 1.

        *  Daemon:
            1.  Add chip scan fail state.
			2.  Bugfix: SN input/output incorrect.
			3.  Add filesystem issue detection.
			4.  More hardware issue defense for daemon.
			5.  Bugfix: chip scan failed state not show.
			6.  Bugfix: state message not work after space not enough error occur.
			7.  Feature update: Preview command at least change the icon in task bar.
			8.  Feature: watch dog able to quit from stdin.
			9.  Bugfix: image encryption control works incorrectly.
			10. Change channel default configuration:
				1. green -> 0.25 sec.
				2. red -> 1 sec.
            11. CFDA: remove failed chip stage.
			12. CFDA: extend available date (~2020/06).

        *  Magpie2:
            1.  New Tag Rule Test.
			2.  Fix shows that the disk is full.
			3.  Add account login.

* **Software Publish**
	* CFDA-20191120 @ smtdata\jeff\CFDA\CFDA-20191120

=============================================================================================

***Previous Version***

**SUMMIT Reader: A version after 20190712**

**SUMMIT Server: A version after 20190712**
