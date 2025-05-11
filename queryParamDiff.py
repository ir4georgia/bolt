###################################################################
# Otto: QueryParamDiff
# Compares Query string parameters in an ad call
# M Pierce
# Created May 9, 2025
###################################################################

from urllib.parse import urlparse, parse_qs
import os
import datetime
import html

commentBreaker = "Otto: ############################################################"

log4email = []
dirname = os.path.dirname(__file__)
logPath = "Logs"
logName = "ottoAdRequestDiff.txt"

def msglog(message):
    print(message)
    global log4email
    log4email.append(message)
    logFileName = os.path.join(dirname, logPath, logName)
    f = open(logFileName, "w")
    for log in log4email:
        f.write(log+'\n')
    f.close()

def compare_query_params(prod_ad_request, stage_ad_request):
    msglog(commentBreaker)
    msglog("Otto: Prod vs Stage Ad Call Diff")
    msglog("Otto: This script compares query parameter between two ad calls, Prod and Bolt")
    msglog("Otto: Testing Began at {0}".format(datetime.datetime.now().strftime("%Y-%m-%d at %I:%M %p")))
    msglog(commentBreaker)
    msglog("Otto: Prod Ad Call: {0}".format(prod_ad_request))
    msglog("Otto: BOLT Ad Call: {0}".format(stage_ad_request))
    msglog(commentBreaker)
    
    # convert html-entities to unicode character
    prod_ad_request = html.unescape(prod_ad_request)
    stage_ad_request = html.unescape(stage_ad_request)

    # Parse the query parameters
    params1 = parse_qs(urlparse(prod_ad_request).query)
    params2 = parse_qs(urlparse(stage_ad_request).query)

    keys1 = set(params1.keys())
    keys2 = set(params2.keys())

    common_keys = keys1 & keys2
    unique_to_prod_ad_request = keys1 - keys2
    unique_to_stage_ad_request = keys2 - keys1
    # Sort the sets
    common_keys = sorted(common_keys)
    unique_to_prod_ad_request = sorted(unique_to_prod_ad_request)
    unique_to_stage_ad_request = sorted (unique_to_stage_ad_request)

    msglog("Otto: Analysis")
    msglog(commentBreaker)
    msglog("Otto: Common parameters:")
    msglog(commentBreaker)
    for key in common_keys:
        values1 = params1[key]
        values2 = params2[key]
        if values1 == values2:
            msglog(f"  {key}: SAME ({values1})")
        else:
            msglog(f"  {key}: DIFFERENT (PROD: {values1}, BOLT: {values2})")
    
    msglog(commentBreaker)
    msglog("Otto: Parameters only in PROD AD REQUEST:")
    msglog(commentBreaker)
    for key in unique_to_prod_ad_request:
        msglog(f"  {key}: {params1[key]}")
    msglog(commentBreaker)

    msglog("Otto: Parameters only in BOLT AD REQUEST:")
    msglog(commentBreaker)
    for key in unique_to_stage_ad_request:
        msglog(f"  {key}: {params2[key]}")
    msglog(commentBreaker)


# prod_ad_request = "https://bea4.v.fwmrm.net/ad/g/1?flag=+slcb+aeti+sltp+fbad+vicb+emcr+amcb&nw=48804&asnw=48804&csid=cnn.com_travel_videopage&caid=meea901d75457146dd5885b832d74b4442bef1acfd&vdur=163.7638&prof=48804%3Acnn_web_vod&resp=vmap1+vast4&vprn=1637139997&pvrn=1637139997&mode=on-demand&afid=145854967&vcid=c5882747-e74f-46a7-8020-4f96300d4849&metr=1023&vip=168.161.12.129;_fw_h_user_agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_15_7%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F136.0.0.0+Safari%2F537.36&_fw_ae=&_fw_ar=0&_fw_vcid2=68190686c179a20a3f80590017455181&_fw_cookie_consent=1&_fw_gdpr=0&_fw_us_privacy=1---&playername=top-2.18.0-7&abl=0&zwmc=4365110703619446808&wmuk=c5882747-e74f-46a7-8020-4f96300d4849&vcid=c5882747-e74f-46a7-8020-4f96300d4849&appView=web&wm_vw=stlr&pg=video_leaf&spec=my_happy_place&vpa=0&vpmute=0&audio=unmuted&inFocus=true&protocol=ssl&refdom=cnn&playerType=standard&mode=vod&228=cep_tags&231=cep_tags&15LP=cep_brsf&15LQ=cep_brsf&15FS=cep_iabt&15CC=cep_iabt&15FD=cep_iabt&15F8=cep_iabt&15FN=cep_iabt&15H2=cep_iabt&16BB=cep_sent&2PCG=cep_tags&2JP1=cep_tags&2PCF=cep_tags&58H0=cep_tags&BJF=cep_tags&BLX=cep_tags&BJ1=cep_tags&KKV=cep_tags&BLL=cep_tags&BLH=cep_tags&F8T=cep_tags&13H7=cep_tags&B8FZ=cep_tags&81W=cep_tags&85G=cep_tags&82H=cep_tags&2JP6=cep_tags&2PCB=cep_tags&70M=cep_tags&7B6=cep_tags&89S=cep_tags&8FK=cep_tags&fr=false&adt=veryLow&alc=veryLow&dlm=veryLow&drg=veryLow&hat=veryLow&off=veryLow&vio=veryLow&id=240f7007-2cf0-11f0-b085-0262f8470cdd&ias-kw=IAS_1506613_PG&ias-kw=IAS_1506123_PG&ias-kw=IAS_3006644_PG&ias-kw=IAS_1510285_PG&ias-kw=IAS_1500691_PG&ias-kw=IAS_11535_KW&ias-kw=IAS_1507080_PG&ias-kw=IAS_49_KW&ias-kw=IAS_1467_KW&ias-kw=IAS_1500094_PG&ias-kw=IAS_3010239_PG&110000=pconid&121100=pconid&129900=pconid&129932=pconid&132200=pconid&132209=pconid&210000=pconid&240000=pconid&240001=pconid&240002=pconid&240003=pconid&240004=pconid&240005=pconid&240006=pconid&240007=pconid&240008=pconid&240009=pconid&240011=pconid&240012=pconid&240013=pconid&240014=pconid&240015=pconid&240016=pconid&240017=pconid&240018=pconid&240019=pconid&300003=pconid&diro9j=pconid&3m6014=pconid&n67xo1=pconid&4ea65v=pconid&v4eg8v=pconid&dflk2u=pconid&sr3lz5=pconid&j5234h=pconid&n2mpux=pconid&uljdw0=pconid&xzox48=pconid&19ydr6=pconid&x67pfl=pconid&6oq81h=pconid&pczk0c=pconid&5jm4ip=pconid&pnv48t=pconid&t1xced=pconid&n0603d=pconid&6ks868=pconid&lzfao2=pconid&o1zrte=pconid&7lkp8o=pconid&dem1021=pconid&pa_eye101=pconid&pa_eye97=pconid&pa_eye161=pconid&pa_eye159=pconid&pa_eye83=pconid&pa_eye110=pconid&pa_eye157=pconid&pa_eye111=pconid&_fw_3P_uid=UID2:AgAAEf6v6HwK996bAekNxEd4R4NPHQ1LQhFQdVjteut3bQ4g5VwbywHjy43j6E9uqvDRxnxfoZOKUK8NmJhDp%20fUxG3mbvafcTawYrwcaeH4xlXchVYLC9fKw5YM/hJaTFTjVGkhUttNS4rGyBfEvupIYY2oA0uLbzDmzFvljtqKgN4ShQ==&paln=AQzzBGQEVJzRx_spYnBVM6mxEubnFrnxSuUGUj9c0lmbgWbKB6wZN_UL-Z9OwtVDo9B9ZkRda6nrwABYj6H6UX0qZHmLEGFBvIKq2qSGAwlC7Gty-tpQNmnqErwRzqQShVMfDgvz6fozyf5EMSRx_GoeqKshEk57s2TE8guk4NoGjR9-wHOhdVQot_OQfAG1qtyyVijbJu4WqwKdMj7ewUm_KdjV-AS3BXnWCJ-LzgHCSllrd0KqJZs_2iM4xl-YQt-fNSbueH4XSjnijRPvtl-dDiIdYHnF-q7gqb-R_YstdMjzbMlwMIlHn9ekccRkrOxKdZEvgkBqPak4I_lFsffk46ZLrikrg6uMMaDstszbK0Ie2CBoReLVZUj6wJ5AlAiKUhKtay83CaMmJSHYzF5Igf-v8cMfsLPn32NcezEg3gFCFjxy2Kh8clsjTxYXjnAfyV-dlT1WLmdMgqtWdeKApAyK4sDjD3LOtNsqXfJAth6AUo14q3XZ_AAYZI64WoG4L2g3oknf9O_sddWCqcLDYcrRvRIAc_xJ_NsDlFcTrIkx8OP2ATmDOvSKVuxqevqnuURX7IID-8rp_vKBzbVl1KzdvAIxwe6JpPwwtCHwLnJbkcQnu9HJBH6mkV_-24RVcD3sHeGEKtLTB0jTufN6b7JWwhWq2JsT8EBuoYlKs5h8m2WF1NSvgplzPb1gkRb5DE0afWI_IA2HOueDvnKAKQDX7ysEJY6J907XeCaKyca9C5DxdVmzN9W7yO8tA7AjDLtJNMMXlEJ9_YsGicOeJraDD22QcS33txFClt7gVml_ow6BUPGOwHQmjPgsMVgiUYyH3BQBCN9ekynVbILfplaClV-hMRoAVFz_o1uynRvjGyLy4VClBo8zE8zFNANlaPhyNwR5UqXMDrDzehNWESCIHv7MSYY3UNlAe3smkSs7MjlcBKVu_6gaFm4-8VIafpS58DSOsDh0aV7Lby_BR01Ge9ry3IszipjoC_7ZD4ApOWowTVLq4Qm_HkzLZTSV_7r7r1tg7N4bRe0nRLPJhOtJ9bDYCpeWrc4Lw9lnnY_rH20VkY46AOP9Gj_cea-LNHhAUF3LPMlDiVYlSadSLa0oGEhgmUkGV6mJTDqwqvk1RFQdLl7uf_7K2ll_8XoT1I-nXPq_hG_iLvArwXn7rVAYyNx-UEt6jPQ2q_M2ObyjCQdzEf8Fa_TJqsnlmxCYJEVnm60KUqGLvvZz_CckVn9wSYphmMBhA73Q0kuRGZ01DAb4uPXbk5PcVPFGycTb4POAAEoUR4ZE6GYdg9OKYD26P86O5aMwJYUHeAbuYef0bXkYgI5iBVGgx-SZD9Y1GyXaSGzgGgdchlVxhxpEeXuXlgNiX2ysb6hUAJXesX2kV_TeLlF6gNfXVbyopF7QuSd0gJGsJPCxGccqtKgrbsfmahwyi9FDrJ8UTfiHpkycS2w4vjFg6m6UunzFH0hMNGkyW8roN2U.;ptgt=a&tpcl=preroll"
# stage_ad_request = "https://bea4.v.fwmrm.net/ad/g/1?flag=+slcb+aeti+sltp+fbad+emcr+amcb&nw=42448&asnw=42448&csid=cnn.com_travel_videopage&caid=meea901d75457146dd5885b832d74b4442bef1acfd&vdur=163&prof=48804%3Acnn_web_vod&resp=vmap1+vast4&vprn=8441073128&pvrn=2224351370&mode=on-demand&afid=436525661&vcid=c5882747-e74f-46a7-8020-4f96300d4849&metr=1023&vip=168.161.12.129;_fw_h_user_agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_15_7%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F136.0.0.0+Safari%2F537.36&_fw_h_referer=&_fw_gdpr=0&_fw_gdpr_consent=&_fw_is_lat=0&_fw_atts=&_fw_ae=&_fw_cookie_consent=1&_fw_us_privacy=1---&playername=top-2.18.0-7&device=Desktop&_fw_did=&_fw_vcid2=68190686c179a20a3f80590017455181+&vcid=c5882747-e74f-46a7-8020-4f96300d4849&wmuk=c5882747-e74f-46a7-8020-4f96300d4849&_fw_3P_uid=&_fw_app_bundle=&transactionId=17468118026645088993452659&paln=AQzzBGQEnkoGH2yCKwIrn02B4KQ9VoJUkN5WDPWA5paNGZmcgOl26xoa_uUEWF-FGAYUoeTBtgQ2-op8sMduM8bYGPTAbwj1hlGGdaQ1-nmLe8VUfQ8EToDSnuq3ZbBc9HQ-avDtWEFvleJVLjIJNrJwZ1gyfagF5fuWBRL20gLIaX-HYHSkfLXFvX2EGHmefHLF4NGZfeLpkZ_UOkbZoY-oNlnSO3kdlMyW8uslIeA-Jq6leoZG3Al2Zf2amS4cLZf_A0TvRDMQs0C6W48u-Ryr4Rz1sztLiRr_Ho3qZQQoeEaTW6nkJKuK38bv-Yfno1H3Ok7LrK0zNkumcXVGn7ChZtYvdlms1PCPpWSPkppsytY_I_Dk3Uvssxiflh3vmN3YeiSyv44FNbBLlf791JH0R4ZVSdWphZ88za2bsVWoyf5ujsr4dR69LMF3zHZA2D9s4_OWwSKAJkO28Q8Ii3cymvcer9BfkZJAlOVoXYZFzEcyOKiu3VL82paZ-PPjC-ekHIuvBqrwzoDYNE7031SwCwCqY9YudBd87wnhUElSMQDiKSswQF5Ze30-uMfIE1C7rATDhC-veYK7O9g1LnjRe_EXnz1kLN8o868kuQMzv1-O52RvfnsqY4NL1GZEYRa27OqB9GFnW-aq22uUyDWXwrayRhVL-1Tw-t8W0ZJ7pPbXrLnbtka8qtmyVECCN9KjJVdvJvaJGnfmyy_zv4wbqHrkw6kEkW6sv3ZfQuhXCnAQNfqMhqGBJL1qWFfiDTwbCD48bfN5XPcSsa51jHx_BKdZPLbaRfWd4mLFM9rjHLwOtrqyJ2maswv38-o9SgZgfKioyv7SmwgE5HFUDsTfpWAcV6hlLdarPQDR6Ge4TR64LZ7MgwoSYXNG6WQUWSIljm6EPT_VN7KH1NdGCoIqt--Nzni1eUYD4XXMVOuXXYGfx7n2r6K6wTMbiyczFqzd6oHl2sCqnbUJyfqhmB0KZAJwPR0VoWp4ui2eD8Gqb_xkCSDksSQ4lzI3b_dXAZeD7sOpWSVE0eahw6CmiBXMD9WwWYRZfLPvXWrPfLhHKR5WNrzdKptF6DfgAKGm5yb5lTJwSe4WnHfcn9pX8WyDAd_Kfm7PGsJb47A5rj5_Sy27wCDPCHBbbuPc1aisSa6tVCZyJtgsw0G-oh___Cjt1OyCGiFbWWH2WMUj_CRhKxX7XsLkHFzBSG6aZStjool-jfGevZEieucdTRJZTizGputWdi3SPGQFP0IhPP9VpRzVQsmNQNiFsZC5XQgVn0g3Coi5RL0LNpGq3tMF1twh4lsPLyKTMMm6TYR1vXeazBCWUJm22lyh-mN1tGWHyKN_jbOumr70L2qgglKJntjO4CVtFBjhybf3k09tLVn9B6f0W5HUnwmdF1H8fzgTTWJ-V-KeYlXUSyaNxGF7J0bGTZCCkWi7RUGlrNKoSkNX5CQrhIBozDUl4a5BYg..&_fw_coppa=&_fw_nielsen_app_id=&appname=&category=&sourceId=&affiliateUrl=&pg=video_leaf&spec=my_happy_place&vpa=1&vpmute=1&wta=0&playerHeight=540&playerWidth=960&refDom=other&cdpfl=%26228%3Dcep_tags%26231%3Dcep_tags%2615LP%3Dcep_brsf%2615LQ%3Dcep_brsf%2615FS%3Dcep_iabt%2615CC%3Dcep_iabt%2615FD%3Dcep_iabt%2615F8%3Dcep_iabt%2615FN%3Dcep_iabt%2615H2%3Dcep_iabt%2616BB%3Dcep_sent%262PCG%3Dcep_tags%262JP1%3Dcep_tags%262PCF%3Dcep_tags%2658H0%3Dcep_tags%26BJF%3Dcep_tags%26BLX%3Dcep_tags%26BJ1%3Dcep_tags%26KKV%3Dcep_tags%26BLL%3Dcep_tags%26BLH%3Dcep_tags%26F8T%3Dcep_tags%2613H7%3Dcep_tags%26B8FZ%3Dcep_tags%2681W%3Dcep_tags%2685G%3Dcep_tags%2682H%3Dcep_tags%262JP6%3Dcep_tags%262PCB%3Dcep_tags%2670M%3Dcep_tags%267B6%3Dcep_tags%2689S%3Dcep_tags%268FK%3Dcep_tags26%26110000%3Dpconid%26121100%3Dpconid%26129900%3Dpconid%26129932%3Dpconid%26132200%3Dpconid%26132209%3Dpconid%26210000%3Dpconid%26240000%3Dpconid%26240001%3Dpconid%26240002%3Dpconid%26240003%3Dpconid%26240004%3Dpconid%26240005%3Dpconid%26240006%3Dpconid%26240007%3Dpconid%26240008%3Dpconid%26240009%3Dpconid%26240011%3Dpconid%26240012%3Dpconid%26240013%3Dpconid%26240014%3Dpconid%26240015%3Dpconid%26240016%3Dpconid%26240017%3Dpconid%26240018%3Dpconid%26240019%3Dpconid%26300003%3Dpconid%26diro9j%3Dpconid%263m6014%3Dpconid%26n67xo1%3Dpconid%264ea65v%3Dpconid%26v4eg8v%3Dpconid%26dflk2u%3Dpconid%26sr3lz5%3Dpconid%26j5234h%3Dpconid%26n2mpux%3Dpconid%26uljdw0%3Dpconid%26xzox48%3Dpconid%2619ydr6%3Dpconid%26x67pfl%3Dpconid%266oq81h%3Dpconid%26pczk0c%3Dpconid%265jm4ip%3Dpconid%26pnv48t%3Dpconid%26t1xced%3Dpconid%26n0603d%3Dpconid%266ks868%3Dpconid%26lzfao2%3Dpconid%26o1zrte%3Dpconid%267lkp8o%3Dpconid%26dem1021%3Dpconid%26pa_eye101%3Dpconid%26pa_eye97%3Dpconid%26pa_eye161%3Dpconid%26pa_eye159%3Dpconid%26pa_eye83%3Dpconid%26pa_eye110%3Dpconid%26pa_eye157%3Dpconid%26pa_eye111%3Dpconid&_fw_dpr=2;ptgt=a&tpcl=preroll"

prod_ad_request = "https://bea4.v.fwmrm.net/ad/g/1?flag=+slcb+aeti+sltp+fbad+emcr+amcb&nw=48804&asnw=48804&csid=tbs.com_desktop_live_east&caid=155824-021&vrdu=999999&vdty=variable&prof=48804%3Atbs_web_live&resp=vmap1+vast4&vprn=2137640094&pvrn=2137640094&mode=live&afid=180483280&metr=1023&vip=168.161.12.129;_fw_h_user_agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_15_7%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F136.0.0.0+Safari%2F537.36&_fw_ae=725bd42fc9c9394e790b9a73610da431&_fw_ar=1&_fw_vcid2=ume93d8_7500745000259002765&zwmc=4365110703619446808&ifyr=MAA6J9H0-A-930O&goiz=6ad14d80eff3445aa55b9204058cefdd&vcid=155bff7c-19bc-4ca6-80c7-539d8002f546&wmuk=155bff7c-19bc-4ca6-80c7-539d8002f546&cdpfl=lrfff&abip=na&_fw_cookie_consent=1&_fw_us_privacy=1&#45;&#45;-&playername=top-2.13.0&guid=6817dfbe0491380a3f80590017455181&transactionId=17468201523092232057512024;ptgt=a&slau=midroll&cpsq=1&maxd=320&mind=320&tpos=200"
stage_ad_request = "https://bea4.v.fwmrm.net/ad/g/1?flag=+slcb+aeti+sltp+fbad+emcr+amcb&nw=42448&asnw=42448&csid=tbs.com_desktop_live_east&caid=155824-021&vdur=2000&prof=48804%3Atrutv_web_live&resp=vmap1+vast4&vprn=8459456519&pvrn=1866412328&mode=live&afid=256242188&vcid=155bff7c-19bc-4ca6-80c7-539d8002f546&metr=1023&vip=168.161.12.129;_fw_h_user_agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_15_7%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F136.0.0.0+Safari%2F537.36&_fw_h_referer=https%3A%2F%2Fwww.tbs.com%2F&_fw_gdpr=0&_fw_gdpr_consent=&_fw_is_lat=0&_fw_atts=&_fw_ae=d41d8cd98f00b204e9800998ecf8427e&_fw_cookie_consent=1&_fw_us_privacy=1---&playername=top-2.2.0&device=Desktop&_fw_did=&_fw_vcid2=&vcid=155bff7c-19bc-4ca6-80c7-539d8002f546&wmuk=155bff7c-19bc-4ca6-80c7-539d8002f546&cdpfl=&_fw_3p_uid=&_fw_app_bundle=&transactionId=17468195916675081565014244&paln=&_fw_coppa=&_fw_nielsen_app_id=&vpa=&vpmute=&wta=&playerHeight=0&playerWidth=0&_fw_dpr=2;ptgt=a&slau=midroll&cpsq=1&maxd=320s&mind=320s&tpos=200"


compare_query_params(prod_ad_request, stage_ad_request)

msglog("Otto: End of Comparison")
msglog(commentBreaker)