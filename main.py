import os
import requests

bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhNcHdjdFl4YWlRdWg4Y0M0ejN0UCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucmVwaHJhc2UuYWkvIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDc5MzE5NjY0MDQ5NzA4MTMwNjYiLCJhdWQiOlsiaHR0cHM6Ly9kaXkucmVwaHJhc2UuYWkvYXV0aDAiLCJodHRwczovL3JlcGhyYXNlYWktcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc5NzQ3NzQzLCJleHAiOjE2Nzk4MzQxNDMsImF6cCI6IjNLVTVqdkVxV0pCQ1VLblBYMjZvbmFTUHkzakozMEo0Iiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSByZWFkOnJlcGhyYXNlLmFpIGFsbDpkaXkgcmVhZDpyZXBocmFzZS5haSJ9.LwGcknsaVymqpzCiYcxL4rYDQD9fS7q9PHRURpjA4DAv4qki9SgISglx8jlB_r4L-quTiX_zZjbB4iqYgK-YBZWXIiRJN3gP6I4SL8fGEFlk244G5q0sax6pnKHgLNiV1vIZPWJevGLdJ5SmIFcP1G_5GMD4enRZRyCWElTnz2AB2KdEh7w5sAD8uk-rx97504D8kBJ-fog-fLMm-dEl7QEnbP70zZ-FkrJk2UkQgecQRUFEdXWW5mf8f9BOhvU4wxQZWUvqvljIk4mpl3p93N74NngaBD5BVMG0b0GMkguRA0nRviwdqWYM0DujfWT1s1zRBPmVpeFPjUcYA7fYmg"

url = "https://personalized-brand.api.rephrase.ai/v2/campaign/create"

payload = {
    "videoDimension": {"height": 1080, "width": 1920},
    "scenes": [
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "http://sahilsaini.in/wp-content/uploads/2016/01/Picture15.png",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "kind": "Spokesperson",
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>The text describes Sahil Saini's academic and professional profile. He is currently pursuing B.Tech in Chemical Engineering from IIT (BHU), Varanasi and has scored 9.08 CGPA. He has skills in Git/GitHub, Python, C/C++, HTML, CSS, and JavaScript, and has worked with technologies like Django, MERN, and Rest APIs. He has done an internship as a frontend developer and developed the website for Candid Connections using ReactJS, Figma, and AWS EC2. He has also contributed to several open-source projects and created a GitHub action using JavaScript. He has worked in positions of responsibility as a reviewer, informatics executive, and mentor. He has received honors and achievements like being a RunnerUp in Robovation, 2nd RunnerUp in ECell Pitch-er-Perfect, and merging six PRs in Hacktoberfest'21. He is an active member of the Athletics Club, COPS IIT (BHU), Varanasi, and has spoken at Dev Talk on UI/UX design.</speak>",
                            "transcript_type": "ssml_limited",
                        },
                    },
                },
            ]
        },
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://www.iitbhu.ac.in/contents/iitbhu/img/slider/iit_bhu_slider_05.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>In 1982, Michael released, Thriller, which spent months at the top of the Billboard 200 charts... Cause this is thriller, thriller night...  </speak>",
                            "transcript_type": "ssml_limited",
                        },
                        "kind": "Spokesperson",
                    },
                },
            ]
        },
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://blog.siriusxm.com/wp-content/uploads/2022/11/MichaelJacksonChannel-1117.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>Check out Michael's wikipedia to know more about him. Thank you, have a great day.</speak>",
                            "transcript_type": "ssml_limited",
                        },
                        "kind": "Spokesperson",
                    },
                },
            ]
        },
    ],
    "title": "Into to MJ",
    "thumbnailUrl": "https://blog.siriusxm.com/wp-content/uploads/2022/11/MichaelJacksonChannel-1117.jpg",
}
headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
    "content-type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(f"CAMPAIGN_ID= {response.text}")