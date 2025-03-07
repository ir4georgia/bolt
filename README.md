# bolt

## Python script to analyze a .har log captured from Bolt/Beam Player
The purpose of this tool is to verify that the expected tracking beacons actually fire  
It is difficult to do by hand, when the user is opted out of US Privacy.  
*  The links are long, and do not have human readable information

### Basic Steps to use:
  
* Enable SSL in Charles for Bolt domains
    * https://br-default.any-any.prd.api.discomax.com
    * https://br-default.br-amer.prd.api.discomax.com
    * https://gmss.use1.prd.api.discomax.com
* Capture a Charles proxy log on B/R App
* Export to .har format
* Update remoteHarFile location in the script
* Look in Logs directory for the report

Example Report:  

Otto: ############################################################  
Otto: ##############  Klaatu barada nikto  #######################  
Otto: ############################################################  
Otto: BOLT Charles Log Analyzer  
Otto: EAT Tool - https://backoffice.prd.api.discomax.com/adtech/eat/beam/prd/search  
Otto: ############################################################  
Otto: BR-2.0-iPhone Testing Began at 2025-03-06 at 02:01 PM  
Otto: /Users/mpierce/Desktop/MML-Chls/BR-Iphone-Opt-Out.har  
Otto: ############################################################  
Otto: Step 1: Load the Charles File  
Otto:    Successfully Loaded Har File  
Otto:    File was 170.219 MB  
Otto: ############################################################  
Otto: Step 2: Extract Info from the Charles Log  
Otto:    Searched the Log for specified BOLT entries  
Otto: ############################################################  
Otto: Extraction Results:  
Otto: User Info: 5  
Otto: Playback Info: 4  
Otto: BOLT Tracker Events: 64  
Otto: FW Tracker Events: 0  
Otto: ############################################################  
Otto: Step 3: Extract User Info  
Otto: User: Michael Pierce ID: USERID:bolt:360674cf-4fcd-41c7-b8db-01f5ca2c13d0 Type: user  
Otto: User: Michael Pierce ID: USERID:bolt:360674cf-4fcd-41c7-b8db-01f5ca2c13d0 Type: user  
Otto: User: Michael Pierce ID: USERID:bolt:360674cf-4fcd-41c7-b8db-01f5ca2c13d0 Type: user  
Otto: User: Michael Pierce ID: USERID:bolt:360674cf-4fcd-41c7-b8db-01f5ca2c13d0 Type: user  
Otto: User: Michael Pierce ID: USERID:bolt:360674cf-4fcd-41c7-b8db-01f5ca2c13d0 Type: user  
Otto: ############################################################  
Otto: Step 4: Extract Playback Info  
Otto: Playback Session ID 0: CC3CFBC6-E1EB-4D27-BDAD-6AD495777BC8 Privacy: 1YNN isLat: 1  
Otto: Playback Session ID 1: 1D05A9DF-7B6A-480F-A7D2-0E4B97550B2F Privacy: 1YNN isLat: 1  
Otto: Playback Session ID 2: 10ADC3B1-EEF4-4805-B77A-AB554A408B1F Privacy: 1YNN isLat: 1  
Otto: Playback Session ID 3: 7957F092-8EB3-4E04-9D33-30FC01DC7F93 Privacy: 1YNN isLat: 1  
Otto:  
Otto: Response Session ID 0: CC3CFBC6-E1EB-4D27-BDAD-6AD495777BC8  
Otto: Video ID: 58edb763-60cb-535e-9623-509408b92cee  
Otto: Ad Break: 0 Ad ID: 82820053 Ad System: FreeWheel  
Otto: Expected Events  
Otto: Found Impression expected tracker: True  
Otto: Found 1st Quartile expected tracker: True  
Otto: Found 2nd Quartile expected tracker: True  
Otto: Found 3rd Quartile expected tracker: True  
Otto: Found 4th Quartile expected tracker: True  
Otto:
Otto: Response Session ID 1: 1D05A9DF-7B6A-480F-A7D2-0E4B97550B2F  
Otto: Video ID: 446f34de-4a24-534a-a462-a84326e3d4ed  
Otto: Ad Break: 0 Ad ID: 607041838 Ad System: DCM  
Otto: Expected Events  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found 1st Quartile expected tracker: True  
Otto: Found 1st Quartile expected tracker: True  
Otto: Found 1st Quartile expected tracker: True  
Otto: Found 2nd Quartile expected tracker: True  
Otto: Found 2nd Quartile expected tracker: True  
Otto: Found 2nd Quartile expected tracker: True  
Otto: Found 3rd Quartile expected tracker: True  
Otto: Found 3rd Quartile expected tracker: True  
Otto: Found 3rd Quartile expected tracker: True  
Otto: Found 4th Quartile expected tracker: True  
Otto: Found 4th Quartile expected tracker: True  
Otto: Found 4th Quartile expected tracker: True  
Otto:  
Otto: Response Session ID 2: 10ADC3B1-EEF4-4805-B77A-AB554A408B1F  
Otto: Video ID: de6f286b-68df-5e02-bced-21ce840e6c35  
Otto: Ad Break: 0 Ad ID: 607041838 Ad System: DCM  
Otto: Expected Events  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found 1st Quartile expected tracker: True  
Otto: Found 1st Quartile expected tracker: True  
Otto: Found 1st Quartile expected tracker: True  
Otto: Found 2nd Quartile expected tracker: True  
Otto: Found 2nd Quartile expected tracker: True  
Otto: Found 2nd Quartile expected tracker: True  
Otto: Found 3rd Quartile expected tracker: True  
Otto: Found 3rd Quartile expected tracker: True  
Otto: Found 3rd Quartile expected tracker: True  
Otto: Found 4th Quartile expected tracker: True  
Otto: Found 4th Quartile expected tracker: True  
Otto: Found 4th Quartile expected tracker: True  
Otto:  
Otto: Response Session ID 3: 7957F092-8EB3-4E04-9D33-30FC01DC7F93  
Otto: Video ID: 58edb763-60cb-535e-9623-509408b92cee  
Otto: Ad Break: 0 Ad ID: 82820053 Ad System: FreeWheel  
Otto: Expected Events  
Otto: Found Impression expected tracker: True  
Otto: Found 1st Quartile expected tracker: True  
Otto: Found 2nd Quartile expected tracker: True  
Otto: Found 3rd Quartile expected tracker: True  
Otto: Found 4th Quartile expected tracker: True  
Otto:  
Otto: ############################################################  
Otto: Analyzed a 170.219 MB File in 0:00:03.221757 seconds  
Otto: Go Dawgs!  
Otto: ############################################################  