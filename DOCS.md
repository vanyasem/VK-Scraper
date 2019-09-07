Methods cheatsheet
==================

Currently supported VK API version: 5.101.

### Saved pictures

Method: `photos.get`

Params: `owner_id`

Download URL: `item['sizes'][sizes.index(SIZE_LETTER)]['url']`

Response:

```json
{
  "response":{
    "count":1,
    "items":[
      {
        "id":362880139,
        "album_id":-15,
        "owner_id":194957739,
        "sizes":[
          {
            "type":"m",
            "url":"https://sun9-25.u...OM7c3LGmipT8XQrb0sw",
            "width":130,
            "height":85
          },
          {
            "type":"o",
            "url":"https://sun9-25.u...6AjyXX2oty5Vc2SGMIg",
            "width":130,
            "height":87
          },
          {
            "type":"p",
            "url":"https://sun9-15.u...-GNcvDVgn95ErPAj1KU",
            "width":200,
            "height":133
          },
          {
            "type":"q",
            "url":"https://sun9-43.u...noXBg-rUpXSETjA7wlQ",
            "width":320,
            "height":213
          },
          {
            "type":"r",
            "url":"https://sun9-37.u...OxS8SR1fdr_BKSMIf54",
            "width":510,
            "height":340
          },
          {
            "type":"s",
            "url":"https://sun9-31.u...C6v06M_e5l6TpyT1rDA",
            "width":75,
            "height":49
          },
          {
            "type":"x",
            "url":"https://sun9-48.u...ofK6gPEBSjJ8i0Oe7_A",
            "width":604,
            "height":396
          }
        ],
        "text":"",
        "date":1429901293
      }
    ]
  }
}
```

### Photos

Method: `photos.getAll`

Params: `owner_id`

Download URL: `item['sizes'][sizes.index(SIZE_LETTER)]['url']`

Response:

```json
{
  "response":{
    "count":36,
    "items":[
      {
        "id":333810328,
        "album_id":-7,
        "owner_id":194957739,
        "sizes":[
            {
              "type":"m",
              "url":"https://pp.userap...oaA/OzV6ubO4WJE.jpg",
              "width":130,
              "height":97
            },
            {
              "type":"o",
              "url":"https://pp.userap...iqA/Pqb-b4uHVrY.jpg",
              "width":130,
              "height":98
            },
            {
              "type":"p",
              "url":"https://pp.userap...I7w/Gny90DHGdtE.jpg",
              "width":200,
              "height":150
            },
            {
              "type":"q",
              "url":"https://pp.userap...u8Q/gO3OD-5YbmY.jpg",
              "width":320,
              "height":240
            },
            {
              "type":"r",
              "url":"https://pp.userap...6nA/qyqz4z8NKgQ.jpg",
              "width":510,
              "height":383
            },
            {
              "type":"s",
              "url":"https://pp.userap...uew/nHXtpBMr0y0.jpg",
              "width":75,
              "height":56
            },
            {
              "type":"x",
              "url":"https://pp.userap...bNQ/2l8y7kVgDl8.jpg",
              "width":604,
              "height":453
            },
            {
              "type":"y",
              "url":"https://pp.userap...34Q/2cN-yyaYvy4.jpg",
              "width":807,
              "height":605
            },
            {
              "type":"z",
              "url":"https://pp.userap...y_A/Ibi1xizHQYM.jpg",
              "width":960,
              "height":720
            }
        ],
        "text":"",
        "date":1405877119,
        "post_id":394
      }
    ]
  }
}
```

### Stories

Method: `stories.get`

Params: `owner_id`

Download URL photo: `item[0]['photo']['sizes'][sizes.index(SIZE_LETTER)]['url']`

Download URL video: `item[0]['video']['files']['mp4_' + RESOLUTION]`

Response:

```json
{
  "response":{
    "count":1,
    "items":[
      [
        {
          "id":456241552,
          "owner_id":-28905875,
          "date":1567839733,
          "expires_at":1567926133,
          "can_see":1,
          "type":"photo",
          "photo":{
            "id":458238223,
            "album_id":-81,
            "owner_id":-28905875,
            "user_id":100,
            "sizes":[
              {
                "type":"temp",
                "url":"https://sun1-26.u...eE-bILV67hI9OgSpKes",
                "width":28,
                "height":50
              },
              {
                "type":"s",
                "url":"https://sun1-22.u...tHhpaPopbreIdLp2nAY",
                "width":42,
                "height":75
              },
              {
                "type":"m",
                "url":"https://sun1-23.u...QJ28NqkeKBKxkqwSF4o",
                "width":73,
                "height":130
              },
              {
                "type":"j",
                "url":"https://sun1-27.u...DXmTKBaP6hliK5eTQdI",
                "width":144,
                "height":256
              },
              {
                "type":"x",
                "url":"https://sun1-85.u...rliI9kNrSkE6zIH4ViU",
                "width":340,
                "height":604
              },
              {
                "type":"y",
                "url":"https://sun1-83.u...myhgxTvaleOgDDHOK1w",
                "width":454,
                "height":807
              },
              {
                "type":"z",
                "url":"https://sun1-89.u...u5jSHWBglOT5DskiKXM",
                "width":607,
                "height":1080
              },
              {
                "type":"w",
                "url":"https://sun1-88.u...iYckclJI18wPAGzYNdM",
                "width":1080,
                "height":1920
              }
            ],
            "text":"",
            "date":1567839727
          },
          "can_share":1,
          "can_comment":1,
          "can_reply":1,
          "can_hide":1,
          "can_ask":0,
          "can_ask_anonymous":0,
          "seen":1,
          "replies":{
            "count":3
          },
          "access_key":"a9udf34634ba32dab8"
        },
        {
          "id":456241546,
          "owner_id":-28905875,
          "date":1567789511,
          "expires_at":1567875911,
          "can_see":1,
          "type":"video",
          "video":{
            "id":456268542,
            "owner_id":-28905875,
            "title":"vk stories",
            "duration":14,
            "description":"",
            "date":1567789508,
            "comments":0,
            "width":608,
            "height":1080,
            "image":[
              {
                "height":96,
                "url":"https://sun1-28.u...798/oo32TPcRk44.jpg",
                "width":130,
                "with_padding":1
              },
              {
                "height":120,
                "url":"https://sun1-26.u...797/mb604ESc_Sc.jpg",
                "width":160,
                "with_padding":1
              },
              {
                "height":240,
                "url":"https://sun1-85.u...796/p9esmy1JN0Y.jpg",
                "width":320,
                "with_padding":1
              },
              {
                "height":450,
                "url":"https://sun1-16.u...795/gy_1EKSGrD8.jpg",
                "width":800,
                "with_padding":1
              }
            ],
            "first_frame":[
              {
                "url":"https://sun1-85.u...796/p9esmy1JN0Y.jpg",
                "width":320,
                "height":568
              },
              {
                "url":"https://sun1-26.u...797/mb604ESc_Sc.jpg",
                "width":160,
                "height":284
              },
              {
                "url":"https://sun1-28.u...798/oo32TPcRk44.jpg",
                "width":130,
                "height":231
              },
              {
                "url":"https://sun1-16.u...795/gy_1EKSGrD8.jpg",
                "width":800,
                "height":1421
              }
            ],
            "access_key":"cd1e32a0a3e1c80ec2",
            "user_id":144184186,
            "files":{
              "mp4_720":"https://sun1-16.u...IUAhCzoceocgcck-w3g"
            },
            "player":"https://vk.com/vi...d35_GE4TIOJVG43TGOI",
            "can_add":0,
            "is_private":1,
            "type":"video"
          },
          "can_share":1,
          "can_comment":1,
          "can_reply":1,
          "can_hide":1,
          "can_ask":0,
          "can_ask_anonymous":0,
          "seen":1,
          "replies":{
            "count":15
          },
          "access_key":"6e7620d7a5agd16e7f"
        }
      ]
    ]
  }
}
```

### Videos

Method: `video.get`

Params: `owner_id`

Download URL native: Parse `item['player']` to find a download link (first link represents the best quality available) OR pass it to `youtube-dl`

Download URL external: Pass `item['player']` to `youtube-dl`

Response:
```json
{
  "response":{
    "count":46,
    "items":[
      {
        "id":456239032,
        "owner_id":-177887828,
        "title":"VID_20190519_210034.mp4",
        "duration":22,
        "description":"",
        "date":1558300633,
        "comments":0,
        "views":54,
        "width":720,
        "height":1280,
        "image":[
          {
            "height":96,
            "url":"https://sun9-59.userap...k6BGkdy8.jpg",
            "width":130,
            "with_padding":1
          },
          {
            "height":120,
            "url":"https://sun9-9.usera...gidedcEGw.jpg",
            "width":160,
            "with_padding":1
          },
          {
            "height":240,
            "url":"https://sun9-58.userap...vmNLTA4s.jpg",
            "width":320,
            "with_padding":1
          },
          {
            "height":450,
            "url":"https://sun9-56.userap...shRE1Gio.jpg",
            "width":800,
            "with_padding":1
          },
          {
            "height":720,
            "url":"https://sun9-7.userap...sqSMrFe-U.jpg",
            "width":405
          },
          {
            "height":569,
            "url":"https://sun9-19.userap...JtxSYegI.jpg",
            "width":320
          },
          {
            "height":1280,
            "url":"https://sun9-3.userap...qlTbLonDw.jpg",
            "width":720
          },
          {
            "height":1820,
            "url":"https://sun9-43.userap...lNWMfG42I.jpg",
            "width":1024
          },
          {
            "height":4096,
            "url":"https://sun9-19.userap...06O0zK9oc.jpg",
            "width":2304
          }
        ],
        "is_favorite":0,
        "first_frame":[
          {
            "url":"https://sun9-28.userap...gBoAKjlbo.jpg",
            "width":320,
            "height":569
          },
          {
            "url":"https://sun9-2.userap...wpXJKrlbQ.jpg",
            "width":160,
            "height":284
          },
          {
            "url":"https://sun9-3.userap...WQwhrmboo.jpg",
            "width":4096,
            "height":7282
          },
          {
            "url":"https://sun9-16.userap...Gns1QtGXw.jpg",
            "width":130,
            "height":231
          },
          {
            "url":"https://sun9-2.userap...PcBncyEvw.jpg",
            "width":320,
            "height":569
          },
          {
            "url":"https://sun9-19.userap...gg3KHx5M4.jpg",
            "width":720,
            "height":1280
          },
          {
            "url":"https://sun9-10.userap...FfaYqyCH0.jpg",
            "width":1024,
            "height":1820
          },
          {
            "url":"https://sun9-21.userap...EeEnYzb4s.jpg",
            "width":1280,
            "height":2276
          },
          {
            "url":"https://sun9-56.userap...VL6szfhA0.jpg",
            "width":800,
            "height":1422
          }
        ],
        "adding_date":1558371024,
        "user_id":200986040,
        "player":"https://vk.com/video_ext.php?oid=-177887828&id=456239032&hash=e897b1712e9377de&__ref=vk.api&api_hash=1997843195haq8a144e966d863ad_GE4TIOSDV43TGOI",
        "can_add":1,
        "can_comment":1,
        "can_repost":1,
        "can_like":1,
        "can_add_to_faves":1,
        "type":"video"
      },
      {
        "id": 456241895,
        "owner_id": -51189706,
        "title": "Новый учитель",
        "duration": 8,
        "description": "by Grumpy Serg",
        "date": 1494939113,
        "comments": 2,
        "views": 5672,
        "local_views": 5672,
        "image": [{
          "height": 96,
          "url": "https://sun9-2.userap...98a1c7a4.jpg",
          "width": 130,
          "with_padding": 1
        }, {
          "height": 120,
          "url": "https://sun9-52.userap...cd837611.jpg",
          "width": 160,
          "with_padding": 1
        }, {
          "height": 240,
          "url": "https://sun9-42.userap...f52e5b0a.jpg",
          "width": 320,
          "with_padding": 1
        }, {
          "height": 480,
          "url": "https://sun9-45.userap...107400b9.jpg",
          "width": 640,
          "with_padding": 1
        }],
        "is_favorite": 0,
        "adding_date": 1510852713,
        "player": "https://coub.com/embed/trqtr?__ref=vk.api",
        "platform": "Coub",
        "can_add": 1,
        "can_comment": 1,
        "can_repost": 1,
        "can_like": 1,
        "can_add_to_faves": 1,
        "type": "video"
      }
    ]
  }
}
```
