{
    "DataType":"data",#DataType is one of [Domain,IP,Url,DGA,SHA1,SHA256,MD5]
    "IOCs":[
		{
                    "Update_time":1521812563,#this is the analysist time from the threat information or the threart information when you got it(if not find time in threat from information)
                    "Source":"nicai",#where are you got this information
                    "Threat_soce":90,
                    "Categories":["str"],
                    "Familes":["str"],
                    "Organizations":["str"],#APT Organization or Other name of them
                    "Description":"str"
                    "Source_url":["url"]#maybe this information is from blob or analysis page 
		},
	],
    "urls":[
        {
            "scan_time":12452342,
            "source":"twitter",
            "url":"http://login.libero.it.imapssl.eu/aggiornamento-email.php"
        },
    ],
    "ips":[
        {
            
            "ip":"132.4.5.6",
            "update_time":23523423,
            "source":"otx"
            
        },
    ],
    "domains":[
        {
            "source":"MalwareConfig",
            "domain":"login.libero.it.imapssl.eu",
            "update_time":1521830582£¬
            "threat_score":90
        },
    ],
    "samples":[
        {
            "source":"Vt",
            "sha256":"xxxxxxxxxxxxxxxxxxxxxx",
            "update_time":1521823378,
        },
    ],
}
