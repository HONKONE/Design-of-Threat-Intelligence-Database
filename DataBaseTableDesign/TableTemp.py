{
    "DataType":"data",#DataType is one of [Domain,IP,Url,DGA,SHA1,SHA256,MD5]
	"Target":[]
    "IOCs":[
		{
        "Update_time":"time",#this is the analysist time from the threat information or the threart information when you got it(if not find time in threat from information)
        "Source":"str",#where are you got this information
        "Threat_soce":int,
        "Categories":["str"],
        "Familes":["str"],
        "Organizations":["str"],#APT Organization or Other name of them
        "Description":"str"
        "Source_url":["url"]#maybe this information is from blob or analysis page 
		}
	],
    "Relation_urls":[
        {
            "url":"str"
        },
    ],
    "Relation_ips":[
        {
            "ip":""
        },
    ]
    "Relation_domain":[
        {
            "domain":""
        }
    ]
    "Relation_sample":[
        {
            "MD5":"xx",
            "SHA1":"xxx",
            "SHA256":"xxxx",
        },
    ]
}