# bolt toolset

* queryParamDiff.py
* Bolt-har-analyzer

## queryParamDiff is a Python script to compare query parameters of a Prod and Staging Ad Reqests
The purpose of this tool is to ensure Ad Calls from TOP2 players have the correct query parameters as we switch to  
BOLT back-end infrastructure by changing the YoSpace Ads Promotion  

## Bolt-har-analyzer is Python script to analyze a .har log captured from Bolt/Beam Player
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
Otto: BR-2.0-iPhone Testing Began at 2025-04-21 at 03:39 PM  
Otto: HARFiles/BR-App-4.21.25.har  
Otto: ############################################################  
Otto: Step 1: Load the Charles File  
Otto:    Successfully Loaded Har File  
Otto:    File was 13.14 MB  
Otto: ############################################################  
Otto: Step 2: Extract Info from the Charles Log  
Otto:    Searched the Log for specified BOLT entries  
Otto: ############################################################  
Otto: Extraction Results:  
Otto: User Info: 0  
Otto: Playback Info: 1  
Otto: BOLT Tracker Events: 12  
Otto: FW Tracker Events: 0  
Otto: ############################################################  
Otto: Step 3: Extract User Info  
Otto: ############################################################  
Otto: Step 4: Extract Playback Info  
Otto: Playback Session ID 0: 1C3CB7AC-D66D-4382-AF88-CE0A7EF9F18E Privacy: 1YNN isLat: 1  
Otto:  
Otto: Response Session ID 0: 1C3CB7AC-D66D-4382-AF88-CE0A7EF9F18E  
Otto: Video ID: 795895dc-fbb3-c2e0-66a2-ab1d487c35f1  
Otto: Ad Break: 0 Ad ID: 84734076 Ad System: FreeWheel  
Otto: Placement: 92778489-1_BR CPM O&O Video FW_NEW  
Otto: Expected Events  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found Impression expected tracker: True  
Otto: Found 1st Quartile expected tracker: True  
Otto: Found 2nd Quartile expected tracker: True  
Otto: Found 3rd Quartile expected tracker: True  
Otto: Found 4th Quartile expected tracker: True  
Otto:  
Otto: ############################################################  
Otto: Analyzed a 13.14 MB File in 0:00:00.158888 seconds  
Otto: Go Dawgs!  
Otto: ############################################################  