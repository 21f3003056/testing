# Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]

- **Topic ID**: 164277
- **Tags**: announcement, term1-2025, tds-project-1
- **Saved on**: 2025-06-18 17:55:51
- **Original URL**: https:/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025
- **Total posts**: 614

---

## Post #1

- **Author**: s.anand
- **Posted on**: 2025-01-19T08:17:46.856Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/1

Please post any questions related to [Project 1 - LLM-based Automation Agent](https://tds.s-anand.net/#/project-1).

Deadline: Sunday, February 16, 2025 6:29 PM

**Update on 27 Jan 2025**:

A *sample* evaluation script for Project 1 tasks A1-A10 is available at [tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub](https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1)

You can use this to validate your code for Project 1.

Please note:

1. This is a sample. It **WILL** change.
2. Don’t rely on the dataset being the same. It **WILL** change.
3. LLMs give different results each time they are called. Make sure:
   * Your code gives correct results *reliably* (i.e. try a few times)
   * Change the task in the evaluation script slightly to test variations
4. Your [AI Proxy usage](https://aiproxy.sanand.workers.dev/) resets on 1 Feb. You have a limited budget. Utilize what you can this month.
5. For those who [submit their code](https://docs.google.com/forms/d/e/1FAIpQLSdOaljgV-INdbKrPotV9OMUKV01QVaFEfcnr5dAxBZqM4x37g/viewform?usp=dialog) by Friday 31 Jan, I will run a sample evaluation and share the results.

---

## Post #2

- **Author**: s.anand
- **Posted on**: 2025-01-19T08:20:32.879Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/2



---

## Post #3

- **Author**: roy2003
- **Posted on**: 2025-01-19T13:44:38.945Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/3

sir show us all the way to do project

---

## Post #4

- **Author**: Jivraj
- **Posted on**: 2025-01-19T13:45:31.017Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/4

Hi Shouvik,

We will have live sessions to guide on how to do project.

Kind regards  
Jivraj

---

## Post #5

- **Author**: 23f2000237
- **Posted on**: 2025-01-20T10:44:32.687Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/5

Will those session be on youtube too?

---

## Post #6

- **Author**: carlton
- **Posted on**: 2025-01-20T10:48:22.899Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/6

Hi Sakthivel,

Yes all sessions are being recorded and are available on youtube within a day.  
[Jan 25 TDS Playlist](https://www.youtube.com/playlist?list=PL_h5u1jMeBCl1BquBhgunA4t08XAxsA-C)

Kind regards

---

## Post #7

- **Author**: 22f3001315
- **Posted on**: 2025-01-23T09:57:29.120Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/7

[![Screenshot 2025-01-23 151614](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/0/20410aa56e88be04883b6f3feca5010089afe276_2_690x67.png)

Screenshot 2025-01-23 1516141281×125 18.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/0/20410aa56e88be04883b6f3feca5010089afe276.png "Screenshot 2025-01-23 151614")

  
sir [@Jivraj](/u/jivraj) after editing line 127 in datagen.py i got those required data files. is it allowed ? also i had to run datagen.py MANUALLY(is this process also should be automatic)?

---

## Post #8

- **Author**: Jivraj
- **Posted on**: 2025-01-23T11:30:21.008Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/8

Hi Guddu ,

I didn’t make any changes to file and it worked for me. Can you mention what is need of making changes ?

command that I used :  
`uv run datagen.py 22f3002542@ds.study.iitm.ac.in --root ./data`

here --root option defines the folder where you want to store generated data. by default it would try to create a folder in root directory of operating system.

Kind regards  
Jivraj

---

## Post #10

- **Author**: 23f2005325
- **Posted on**: 2025-01-23T13:05:16.643Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/10

getting this issue :

```
openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_issuer'}}

```

---

## Post #11

- **Author**: Jivraj
- **Posted on**: 2025-01-23T13:22:03.304Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/11

Hi Aishik,

Pls add context to your query, without that we won’t be able to understand, where exactly you are facing problem.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2005325/48/68296_2.png) 23f2005325:

> ```
> openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_issuer'}}
>
> ```

Possible reasons for this issue:

1. Not using anand sir’s proxy url for sending requests.
2. Token not being correct.

---

## Post #12

- **Author**: 23f2005325
- **Posted on**: 2025-01-25T16:20:57.111Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/12

yes I was not setting the base url to the proxy. I have fixed it thank you .

---

## Post #13

- **Author**: 23f2005325
- **Posted on**: 2025-01-25T18:12:39.754Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/13

While implementing task A5, I am confused about what recent actually means in the phrase “recent log file”, mentioned under task A5, in the problem statement. This confusion arises because there are no dates corresponding to the log files. Should I consider log-0 as the most recent one? or the log-<largest\_number> file? Please clarify.

---

## Post #15

- **Author**: 23f2005325
- **Posted on**: 2025-01-26T10:30:43.750Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/15

I am getting the following response when I am trying to extract credit card number from the credit-card.png :

```
{'id': 'chatcmpl-<redacted>', 'object': 'chat.completion', 'created': 1737872397, 'model': 'gpt-4o-mini-2024-07-18', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': "I'm sorry, but I can't assist with that.", 'refusal': None}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 946, 'completion_tokens': 11, 'total_tokens': 957, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'service_tier': 'default', 'system_fingerprint': '<redacted>', 'monthlyCost': 0.07715699999999998, 'cost': 0.0029040000000000003, 'monthlyRequests': 31, 'costError': 'crypto.createHash is not a function'}

```

my code is as below :

```
def extract_credit_card_number():
    import requests
    import base64
    import os
    from dotenv import load_dotenv
    load_dotenv()



    BASE_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ["AIPROXY_TOKEN"]}"
    }

    image_path = "../data/credit_card.png"

    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",  
                "content": "You are a helpful assistant that provides detailed and accurate descriptions of images. Focus on describing the objects, colors, textures, the overall scene, and most importantly, the text and numbers in the image. Be concise but thorough."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are given an image containing a credit card number. Extract the credit card number from the image"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
    }

    
    response = requests.post(BASE_URL, headers=headers, json=payload)

    
    if response.status_code == 200:
        result = response.json()
        print("RESULT:", result)
        cno = result["choices"][0]["message"]["content"]
        print("CREDIT CARD NUMBER:", cno)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

```

please guide [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

## Post #16

- **Author**: 23f1000299
- **Posted on**: 2025-01-26T17:16:01.337Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/16

do we have to do these tasks in the linux? As in some of the GA1, the linux answers only accepted. Please tell me that, do we can do it in the desktop or we have to use linux?  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

## Post #17

- **Author**: Saransh_Saini
- **Posted on**: 2025-01-26T18:10:34.636Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/17

The bash commands are usually run in a linux machine, but you can easily run those commands in VSCode without installing any virtual machines. Download the WSL extension in VSCode and you will get a WSL terminal to work with.

For more information watch this video <https://youtu.be/q74CP4fB7cY?si=M_zw8WzpmMCyVQat> or watch TDS Live Sessions.

Regards,  
TDS TA

---

## Post #18

- **Author**: 23f1002382
- **Posted on**: 2025-01-27T01:27:41.658Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/18

what frameworks can we use? hopefully anything?

or what frameworks can’t we use?  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #19

- **Author**: carlton
- **Posted on**: 2025-01-27T03:04:44.636Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/19

Project 1 deliverables are all that matter. How you accomplish them is not very relevant. The keys to a successful Project 1 are:  
Deliverables,  
and *an example* of the Evaluation has been provided.  
If your project runs in accordance with the Evaluation methodology then it is considered.  

[![Screenshot 2025-01-27 at 8.35.23 am](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/8/488e23f9ea65d35c5ba806fab09f4b5934ed2ed4_2_500x500.png)

Screenshot 2025-01-27 at 8.35.23 am1764×1764 374 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/8/488e23f9ea65d35c5ba806fab09f4b5934ed2ed4.png "Screenshot 2025-01-27 at 8.35.23 am")

Please read the documentation carefully from top to bottom.

So the main question is how do you test if the script will run according to the evaluation? The whole point is for it to run not just on your system. It should be deployable anywhere on any machine. Your solution should work anywhere we test it. Thats why you package it in a docker container. How you achieve that is up to you. But if we cannot run your docker container according to the specification we have provided then it has failed this crucial test.

Kind regards

---

## Post #20

- **Author**: carlton
- **Posted on**: 2025-01-27T03:09:21.493Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/20

[@23f1002382](/u/23f1002382)

You can use any library as long as your Project 1 meets the deliverable requirements and does all the (20+) API tasks.

Kind regards

---

## Post #21

- **Author**: s.anand
- **Posted on**: 2025-01-27T13:32:36.477Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/21

A *sample* evaluation script for Project 1 tasks A1-A10 is available at [tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub](https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1)

You can use this to validate your code for Project 1.

Please note:

1. This is a sample. It **WILL** change.
2. Don’t rely on the dataset being the same. It **WILL** change.
3. LLMs give different results each time they are called. Make sure:
   * Your code gives correct results *reliably* (i.e. try a few times)
   * Change the task in the evaluation script slightly to test variations
4. Your [AI Proxy usage](https://aiproxy.sanand.workers.dev/) resets on 1 Feb. You have a limited budget. Utilize what you can this month.
5. For those who [submit their code](https://docs.google.com/forms/d/e/1FAIpQLSdOaljgV-INdbKrPotV9OMUKV01QVaFEfcnr5dAxBZqM4x37g/viewform?usp=dialog) by Friday, I will run a sample evaluation and share the results.

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) - please socialize this during the live sessions.

---

## Post #22

- **Author**: Divya1
- **Posted on**: 2025-01-27T14:00:22.634Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/22

By clicking the project link ,I am getting the notes…but no project is available in my project 1

---

## Post #23

- **Author**: Divya1
- **Posted on**: 2025-01-27T14:02:29.072Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/23

by clicking the link

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/2/32bd53681054ab17de6350c49f68b405acd538b9_2_690x78.png)

image1198×136 9.49 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/2/32bd53681054ab17de6350c49f68b405acd538b9.png "image")

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/3/937562cc32dc76a582f6845678b048730622d388_2_690x229.png)

image1750×581 70.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/3/937562cc32dc76a582f6845678b048730622d388.png "image")

  
I am getting this opened.

---

## Post #24

- **Author**: Jivraj
- **Posted on**: 2025-01-27T21:30:57.919Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/24

Hi [@Divya1](/u/divya1) ,

There won’t be any project1 page such as GA1s, there is a google form(which can be found in same page) which needs to be filled after you do project1.

---

## Post #25

- **Author**: Jivraj
- **Posted on**: 2025-01-27T21:57:49.221Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/25

Hi [@23f2005325](/u/23f2005325) ,

Extracting details from credit cards is sensitive, try using strong prompts or take code from LLM and execute it in script.

kind regards

---

## Post #26

- **Author**: 23f1002382
- **Posted on**: 2025-01-28T08:28:17.260Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/26

Regarding Wednenday 9-10 pm live session, maybe the instructors could also discuss how to use docker as a virtual environment using maybe ollama(local llm as now there is deepseek opensource, i doubt we would need to use openai for testing, just for production(test submission) would be enough) and also some agent(langchain, autogen, crewai) just a quick how-to on setting up and problems while setting up if possible

More resources on docker. Using docker as a virtual environment. Editing and executing code in Dockerfiles (like when you change code in src a web framework automatically reloads page(hot reload)), something along the lines of this .

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #27

- **Author**: Jivraj
- **Posted on**: 2025-01-28T11:55:55.799Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/27

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1002382/48/68945_2.png) 23f1002382:

> Regarding Wednenday 9-10 pm live session, maybe the instructors could also discuss how to use docker as a virtual environmen

In Tuesday’s(21 January) session we had discussed docker towards ending of session.  
What was discussed in that live session regarding docker:

1. Search for existing containers on repositories such as dockerhub.
2. Pull an existing docker image.
3. Run that image inside a container.
4. Enter to that container and modify something(such as installing python inside a ubuntu container, for customization or create some file)
5. Once done you can commit it.
6. And push customized container’s image to docker hub.

Regarding local models running for project1, it’s a good idea, we will see if it’s possible to discuss in session.

---

## Post #29

- **Author**: Divya1
- **Posted on**: 2025-01-28T18:07:19.143Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/29

In the google forms , I have 2 questions in one form now to submit should it is compulsory that to answer the both the questions?

---

## Post #30

- **Author**: carlton
- **Posted on**: 2025-01-29T02:57:18.959Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/30

Hi [@Divya1](/u/divya1)

[![Screenshot 2025-01-29 at 8.19.05 am](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/35e7ce763c7605e99ee1fad3906e1cd31d094b31_2_690x389.png)

Screenshot 2025-01-29 at 8.19.05 am1738×982 122 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/5/35e7ce763c7605e99ee1fad3906e1cd31d094b31.png "Screenshot 2025-01-29 at 8.19.05 am")

Please do very carefully all things mentioned in the Deliverables as well as look at the Evaluation Section.  

[![Screenshot 2025-01-29 at 8.26.08 am](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/9/898ab28ebe773e40fb3ad9b98c71ce4c5d063c09_2_690x234.png)

Screenshot 2025-01-29 at 8.26.08 am1460×496 45.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/9/898ab28ebe773e40fb3ad9b98c71ce4c5d063c09.png "Screenshot 2025-01-29 at 8.26.08 am")

We had a session on 28th Jan introducing all the important aspects of Project.

If you do not do everything exactly as mentioned **especially the pre - requisites** mentioned in the Evaluation section you will get 0 in the project and *there will be no appeal* for failing to meet the pre - requisites of the evaluation criteria.

In order for us to evaluate the project you have to provide the deliverables mentioned above.

Kind regards

---

## Post #31

- **Author**: 23f1002382
- **Posted on**: 2025-01-29T06:32:45.816Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/31

---

**Subject:** Request to Add Instructors to Private GitHub Repo

**Message:**  
*"Dear [Instructors’ Names],*

*I’ve set up the environment and dependencies for the project and was wondering if it would be appropriate to add you to my private GitHub repository. I’d appreciate any guidance on improving performance, scalability, and design principles. Please let me know if this is feasible or if there’s a more suitable way to seek feedback. Apologies if this request is out of scope.*

*Thank you for your time!*

*Best,*  
[Your Name]"\*

ChatGPT can make mistakes. Check important info.

---

## Post #32

- **Author**: s.anand
- **Posted on**: 2025-01-29T10:41:16.527Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/32

[@23f1002382](/u/23f1002382) - You’re welcome to use the evaluation script in this post for private repos.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png)
[Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/21) [Tools in Data Science](/c/courses/tds-kb/34)

> A sample evaluation script for Project 1 tasks A1-A10 is available at [tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub](https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1)
> You can use this to validate your code for Project 1.
> Please note:
> This is a sample. It WILL change.
> Don’t rely on the dataset being the same. It WILL change.
> LLMs give different results each time they are called. Make sure:
> Your code gives correct results reliably (i.e. try a few times)
> Change the task in t…

For public repos submitted in the form, I’ll run this script over the weekend and share preliminary results.

---

## Post #33

- **Author**: 23f1002382
- **Posted on**: 2025-01-29T11:29:04.323Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/33

T h a n k y o u sir.

---

## Post #34

- **Author**: JoelJeffrey
- **Posted on**: 2025-01-30T06:20:34.650Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/34

For A6, /data/docs/ has subfolders with .md files from which we have to extract the heading level 1’s (#) right? Apparently there are few files with different content but the same name. Can someone confirm the same? If yes how to address these files [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

## Post #35

- **Author**: 23f1002382
- **Posted on**: 2025-01-30T06:26:20.605Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/35

I had set up the environment and dependencies and everything was working fine. When i tried to recreate it from scratch in a new codespace it broke. I fixed almost everything except this error

```
@ANdIeCOOl ➜ /workspaces/TDS-Project-1 (main) $ crewai create crew b2b
Traceback (most recent call last):
  File "/home/codespace/.python/current/bin/crewai", line 5, in <module>
    from crewai.cli.cli import crewai
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/__init__.py", line 3, in <module>
    from crewai.agent import Agent
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agent.py", line 7, in <module>
    from crewai.agents import CacheHandler
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/__init__.py", line 2, in <module>
    from .parser import CrewAgentParser
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/parser.py", line 6, in <module>
    from crewai.utilities import I18N
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/__init__.py", line 13, in <module>
    from .embedding_configurator import EmbeddingConfigurator
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/embedding_configurator.py", line 4, in <module>
    from chromadb import Documents, EmbeddingFunction, Embeddings
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/__init__.py", line 6, in <module>
    from chromadb.auth.token_authn import TokenTransportHeader
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py", line 24, in <module>
    from chromadb.telemetry.opentelemetry import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 13, in <module>
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/trace_exporter/__init__.py", line 25, in <module>
    from opentelemetry.exporter.otlp.proto.grpc.exporter import (  # noqa: F401
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/exporter.py", line 72, in <module>
    from opentelemetry.sdk.metrics.export import MetricsData
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py", line 16, in <module>
    from opentelemetry.sdk.metrics._internal import Meter, MeterProvider
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py", line 56, in <module>
    from opentelemetry.sdk.metrics._internal.measurement_consumer import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py", line 29, in <module>
    from opentelemetry.sdk.metrics._internal.metric_reader_storage import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py", line 26, in <module>
    from opentelemetry.sdk.metrics._internal._view_instrument_match import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py", line 22, in <module>
    from opentelemetry.sdk.metrics._internal.aggregation import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py", line 48, in <module>
    from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.exponent_mapping import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py", line 25, in <module>
    from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.ieee_754 import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py", line 15, in <module>
    from ctypes import c_double, c_uint64
  File "/usr/local/python/3.12.1/lib/python3.12/ctypes/__init__.py", line 8, in <module>
    from _ctypes import Union, Structure, Array
ImportError: /usr/local/python/3.12.1/lib/python3.12/lib-dynload/_ctypes.cpython-312-x86_64-linux-gnu.so: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0

```

i updated the libffi package using sudo but while breaking something else can someone pls help me? [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

history of commands in new codespace

```
    1  crewai --version
    2  pip install crewai crewai-tools
    3  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    4  export PATH=/opt/conda/bin:$PATH
    5  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    6  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    7  crewai create crew <project_name>
    8  crewai create crew b2b
    9  history

```

  
  

UPDATE: IT’s WORKING if you do this in order

```
    1  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    2  export PATH=/opt/conda/bin:$PATH
    3  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    4  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    5  pip install --no-cache-dir --force-reinstall typing_extensions pydantic crewai crewai-tools
    6  conda install -c conda-forge typing_extensions
    7  exec bash
    8  crewai create crew "Project 1 - LLM-based Automation Agent"

```

Something about different environment conda and python can the instructors please help me understand it(resources ), so i can trouble shoot this later with better accuracy come precision

---

## Post #36

- **Author**: 23f1002382
- **Posted on**: 2025-01-30T12:51:19.538Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/36

evaluate.py  
TDS course repo

![](https://github.githubassets.com/favicons/favicon.svg)
[github.com](https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1)

### [tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip ·...](https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1)

Contribute to sanand0/tools-in-data-science-public development by creating an account on GitHub.

line 20

```
from datagen import (
    get_markdown,
    get_dates,
    get_contacts,
    get_logs,
    get_docs,
    get_email,
    get_credit_card,
    get_comments,
    get_tickets,
)

```

but we get datagen.py only in a1 task  
line 69

```
async def a1(email: str, **kwargs):
    await run(
        f"""
Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py`
with `{email}` as the only argument
"""
    )
    return email in await read("/data/format.md")

```

The issue is **importing `datagen` before ensuring it exists**

just checking

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #37

- **Author**: Jivraj
- **Posted on**: 2025-01-30T21:37:48.839Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/37

Hi [@23f1002382](/u/23f1002382),

Yes datagen.py must be present in same directory from where you are executing evaluate.py.

Oh, You trying to use crewai locally for Project1  
kind regards

---

## Post #38

- **Author**: Jivraj
- **Posted on**: 2025-01-30T21:56:52.077Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/38

Hi [@JoelJeffrey](/u/joeljeffrey) ,

Filepath is unique for every file, which needs to be inserted to json file.

---

## Post #39

- **Author**: JoelJeffrey
- **Posted on**: 2025-01-31T06:55:55.139Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/39

Ok. So just to confirm, since there are files with the same name, the json file should map the filepath and not the filename to the title right?  

[![Screenshot from 2025-01-31 12-25-29](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/3/d3ebea3238860bad920a47ff55ac33cb02ad2d63.png)

Screenshot from 2025-01-31 12-25-29790×117 19.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/3/d3ebea3238860bad920a47ff55ac33cb02ad2d63.png "Screenshot from 2025-01-31 12-25-29")

---

## Post #40

- **Author**: 23f1002382
- **Posted on**: 2025-01-31T08:40:50.303Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/40

no crewai, it takes really long i put time out for 300 secs(in run(task:str) in evaluate.py) still sometimes its not enough. I’ll try with autogen next and then langchain

---

## Post #41

- **Author**: 22f3001315
- **Posted on**: 2025-01-31T08:41:45.108Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/41

```
INFO:     127.0.0.1:65085 - "GET /read?path=/data/format.md HTTP/1.1" 200 OK
data/format.md 81ms
INFO:     127.0.0.1:65149 - "POST /run?task=%0AFormat+the+contents+of+%60%2Fdata%2Fformat.md%60+using+%60prettier%403.4.2%60%2C+updating+the+file+in-place%0A HTTP/1.1" 200 OK
INFO:     127.0.0.1:65251 - "GET /read?path=/data/format.md HTTP/1.1" 200 OK
INFO:     127.0.0.1:65263 - "POST /run?task=The+file+%60%2Fdata%2Fdates.txt%60+contains+a+list+of+dates%2C+one+per+line.+Count+the+number+of+Wednesdays+in+the+list%2C+and+write+just+the+number+to+%60%2Fdata%2Fdates-wednesdays.txt%60 HTTP/1.1" 200 OK
INFO:     127.0.0.1:65298 - "GET /read?path=/data/dates-wednesdays.txt HTTP/1.1" 200 OK
INFO:     127.0.0.1:65312 - "POST /run?task=Sort+the+array+of+contacts+in+%60%2Fdata%2Fcontacts.json%60+by+%60last_name%60%2C+then+%60first_name%60%2C+and+write+the+result+to+%60%2Fdata%2Fcontacts-sorted.json%60 HTTP/1.1" 200 OK
INFO:     127.0.0.1:65350 - "GET /read?path=/data/contacts-sorted.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:65361 - "POST /run?task=Write+the+first+line+of+the+10+most+recent+%60.log%60+file+in+%60%2Fdata%2Flogs%2F%60+to+%60%2Fdata%2Flogs-recent.txt%60%2C+most+recent+first HTTP/1.1" 200 OK
INFO:     127.0.0.1:65390 - "GET /read?path=/data/logs-recent.txt HTTP/1.1" 200 OK
INFO:     127.0.0.1:65402 - "POST /run?task=Find+all+Markdown+%28%60.md%60%29+files+in+%60%2Fdata%2Fdocs%2F%60.%0AFor+each+file%2C+extract+the+first+occurrance+of+each+H1+%28i.e.+a+line+starting+with+%60%23+%60%29.%0ACreate+an+index+file+%60%2Fdata%2Fdocs%2Findex.json%60+that+maps+each+filename+%28without+the+%60%2Fdata%2Fdocs%2F%60+prefix%29+to+its+title%0A%28e.g.+%60%7B%22README.md%22%3A+%22Home%22%2C+%22path%2Fto%2Flarge-language-models.md%22%3A+%22Large+Language+Models%22%2C+...%7D%60%29 HTTP/1.1" 200 OK
INFO:     127.0.0.1:65436 - "GET /read?path=/data/docs/index.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:65452 - "POST /run?task=%60%2Fdata%2Fcredit_card.png%60+contains+a+credit+card+number.+Pass+the+image+to+an+LLM%2C+have+it+extract+the+card+number%2C+and+write+it+without+spaces+to+%60%2Fdata%2Fcredit-card.txt%60 HTTP/1.1" 500 Internal Server Error
INFO:     127.0.0.1:65482 - "GET /read?path=/data/credit-card.txt HTTP/1.1" 500 Internal Server Error
INFO:     127.0.0.1:65503 - "POST /run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 HTTP/1.1" 200 OK
INFO:     127.0.0.1:49154 - "GET /read?path=/data/ticket-sales-gold.txt HTTP/1.1" 200 OK

```

result after running evaluate.py:

![:dart:](https://emoji.discourse-cdn.com/google/dart.png?v=12 ":dart:") Score: 0 / 10

why sir [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) what is the problem here??  
please do a live session of complete project process with one or two tasks if possible

---

## Post #42

- **Author**: carlton
- **Posted on**: 2025-01-31T09:04:35.954Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/42

Hi Guddu,

We are planning several project sessions in order to show the workflow of creating a successful project.

Although you are returning a 200 ok, the get request file must match the expectation. In other words after running the first task for example, has the new format.md been formatted correctly and matches the expected output.

In this case you would write out the the `expected` variable in the `evaluate.py` and see if `result` variable matches the `expected`. Then you can figure out what went wrong.

Kind regards

---

## Post #43

- **Author**: 22f3001315
- **Posted on**: 2025-01-31T09:32:51.688Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/43

Ok sir  
But please try to take those sessions sooner  
Because it’s taking too much time for me to do any problem(plus two more courses and one oppe you know) .so I just want to build the project before deadline.

---

## Post #44

- **Author**: 23f1002382
- **Posted on**: 2025-01-31T11:10:36.199Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/44

Please give the date, time and agenda also please.

---

## Post #45

- **Author**: carlton
- **Posted on**: 2025-01-31T11:38:24.014Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/45

Yes sir ,![:saluting_face:](https://emoji.discourse-cdn.com/google/saluting_face.png?v=12 ":saluting_face:")

As soon as we know we will send an announcement.

Kind regards.

---

## Post #46

- **Author**: 23f1002382
- **Posted on**: 2025-02-01T06:48:06.736Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/46

the model keeps wrong answer, it says uvicorn for uv and has no info on how to run uv even after explicitly giving instructions(basically an older model) , basic “ls” command is also wrong, among other things. You can check your logs with respect to my api key.  
Do you think we could access a better model?

Maybe Download Deepseek 70b or even 671b and create an api while y’all run the model locally, in the long it would be cheaper for the course?  
because the model doesn’t know basic commands after telling how to do it.  
So if the model gives us wrong commands 2/3 times then how would we even solve the question.  
I spent a week on this just saying  
[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #47

- **Author**: 23f1002382
- **Posted on**: 2025-02-01T07:03:38.242Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/47

sent pull request maybe accept it then please ![:upside_down_face:](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=12 ":upside_down_face:")

---

## Post #48

- **Author**: 23f1002382
- **Posted on**: 2025-02-01T07:50:52.938Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/48

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/5/75628a6b4c923f0a11501b30fafc0317310f82fd.jpeg "2025-01-31 Week 3 - Session 4 - TDS Jan 25")](https://www.youtube.com/watch?v=sdg4N-H4BR0)

can we have the code for this session please?  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

## Post #51

- **Author**: 23f1002382
- **Posted on**: 2025-02-02T08:46:20.663Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/51

i need some help can you send me your repo?

---

## Post #52

- **Author**: 23f3001745
- **Posted on**: 2025-02-02T19:19:05.604Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/52

Hello, I recently started working on the project. I understood how to do all the phase A tasks on a high level but I’m struggling to start the implementation of the first task in phase A. I’m confused mainly about how the /data directory is supposed to be created, I don’t know how to generate the data and a little confused about the output formats. I would appreciate if I could get in contact with anyone who could guide me in the right direction.

---

## Post #53

- **Author**: 21f3002390
- **Posted on**: 2025-02-03T06:42:50.121Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/53

Hello everyone, [@s.anand](/u/s.anand) [@carlton](/u/carlton)  
I had a few queries regarding the project;

1. I am preloading my docker image with uv and generating the /data files when the container is ran. For task A1, I am automating my server to remove the /data directory that’s already present and run datagen.py again. Is this fine?
2. For /read endpoint, is there a standard for parameters like “path=/data/format.md” or the parameter could be a plain english sentence like “path=show the data in format.md”?
3. Are we concerned about what’s shown on the console if I run a /run command as long as it gets the job done?
4. For tasks A1-10, are the file paths provided in the project doc standard or even they’re flexible? Ex. “Count the number of Wednesdays in file /data/format.md, and write just the number to /data/out.txt”

---

## Post #54

- **Author**: 23f1002382
- **Posted on**: 2025-02-03T08:00:58.755Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/54

+1

---

## Post #55

- **Author**: 24DS1000121_ULAGAOOZ
- **Posted on**: 2025-02-03T08:54:03.151Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/55

Dear Sir,  
Can we have a mentorship program for TDS for those who have no experience in programming like me ?  
thanks & regards.  
ULAGAOOZHIAN

---

## Post #56

- **Author**: 23f2004781
- **Posted on**: 2025-02-02T10:36:40.360Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/56

For Project-1 to complete, it requires:  
"You MUST complete ALL these 3 steps to get a score. Failure to do so will result in getting 0 in the project. If you do not do ALL these 3 steps before the deadline, there will be no appeal available.  
• Fill the form that is on the Project Page  
But I did not get the form; where is it? While I checked inside the project pages also.

---

## Post #57

- **Author**: carlton
- **Posted on**: 2025-02-03T13:02:45.150Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/57

Hi Dewang,

[![Screenshot 2025-02-03 at 6.27.39 pm 1](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/2/9286f3dcf5984d514cf6a40996bd5040f5d9c306_2_642x500.png)

Screenshot 2025-02-03 at 6.27.39 pm 12268×1766 491 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/2/9286f3dcf5984d514cf6a40996bd5040f5d9c306.png "Screenshot 2025-02-03 at 6.27.39 pm 1")

Please *read* the Project page Deliverables carefully as well as the Evaluation Pre - Requisites.

Kind regards

---

## Post #58

- **Author**: 23f1002382
- **Posted on**: 2025-02-04T09:04:40.260Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/58

[github.com/ANdIeCOOl/TDS-Project1-Ollama\_FastAPI-](https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md)

#### [README.md](https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md)

[`main`](https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md)

```
# TDS-Project1-Ollama_FastAPI-
## Info
- Create codespaces on main or evalution script branch
Use history.txt to get sqlite to version 3.45.3 into bash session 
   - 64  export PATH=/opt/conda/bin:$PATH
   - 65  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
   - 66  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"

- cd to latest_ai_development and run cmd [ crewai run] which set up server 
- Then in a separate bash terminal run "python evaluate.py" 
- also make sure to enter openai or sanand api key in crew.py

# Simple history of commands
1. Terminal 1 
    - 1  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    - 2  export PATH=/opt/conda/bin:$PATH
    - 3  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    - 4  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    - 5  cd latest_ai_development/
    - 7  pip install crewai crewai-tools

```

This file has been truncated. [show original](https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md)

My take on autonomous agents. Limited by model capabilities to some extent. Will use function calling hence forth but here is a quick look at using crewai for agent tasks.

---

## Post #59

- **Author**: 22f3001315
- **Posted on**: 2025-02-04T09:55:02.489Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/59

Sir [@carlton](/u/carlton) [@Jivraj](/u/jivraj) just saying,  
If possible Please do 40-50% of project in upcoming live sessions so that we all have atleast something to submit.

---

## Post #60

- **Author**: Arjun7
- **Posted on**: 2025-02-05T16:32:16.103Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/60

I am using ubuntu. How do I use python 3.13. It says my python version is 3.12 even after installing python 3.13  
Someone please help

---

## Post #61

- **Author**: 22f3000819
- **Posted on**: 2025-02-05T18:38:02.561Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/61

[@s.anand](/u/s.anand) sir, I see that the project 1 timeline was changed from February 7 - 17, 2025 to January 17 - February 15 which undoubtedly is a good increase in duration. However, I have my GATE DA exam on Feb 15 and the exam center is unexpectedly far. So, I request you to consider pushing the deadline to at least Feb 16. If not, I’ll still do my best.

---

## Post #63

- **Author**: 21f3002390
- **Posted on**: 2025-02-06T07:04:26.179Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/63

Hello! [@carlton](/u/carlton) [@s.anand](/u/s.anand)

Is the proxy server down right now?  
I am getting this error when I am accessing the endpoint:

{‘id’: ‘chatcmpl-Axq55TzulOVjHYuXYIhkRQzCC3PNl’, ‘object’: ‘chat.completion’, ‘created’: 1738824915, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: …, ‘costError’: ‘crypto.createHash is not a function’}

Or, do I have to install crypto module?

---

## Post #64

- **Author**: s.anand
- **Posted on**: 2025-02-06T07:29:30.529Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/64

[@21f3002390](/u/21f3002390) - AI Proxy is working and you *did* get the result. You can ignore any `costError`. It won’t happen in the future anyway.

**What’s happening?** I was trying to generate a unique hash for each request, as a precursor to caching requests. But I made a mistake in the code. Specifically, `crypto.createHash` is not supported in CloudFlare. [I fixed that](https://github.com/sanand0/aiproxy/commit/5943b6d355deffff88ac07d17aa0c6969cacc3d5) by removing this. I’ll introduce caching later if required.

---

## Post #65

- **Author**: 23f2005138
- **Posted on**: 2025-02-06T09:28:32.920Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/65

For the question #A8 on recognizing the credit card number in the image, Open AI doesn’t seem to be recognizing the number correctly and as a result the evaluation is failing. What should be the solution?  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eab0a8c362c564a00917bb033bce6ad5ba40d103.png)

image913×498 13.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eab0a8c362c564a00917bb033bce6ad5ba40d103.png "image")

---

## Post #66

- **Author**: 23f2004097
- **Posted on**: 2025-02-06T12:31:43.426Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/66

When will live sessions for demo project start? If started please provide link for that as I am unable to get what the project is about and what are the initial steps to start project.

---

## Post #67

- **Author**: 23f2005325
- **Posted on**: 2025-02-06T20:18:10.571Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/67

Getting the following error :

```
127.0.0.1 - - [07/Feb/2025 01:44:54] "GET /run?task=generate%20data%20for%20ujanaishik109@gmail.com HTTP/1.1" 200 -
  File "/tmp/datagenyhqKlO.py", line 1
    404: Not Found
    ^^^
SyntaxError: illegal target for annotation


```

when executing the following code :

Main.py
-------

```
@routes.route("/run", methods=["GET", "POST"])
def run():
    task = request.args.get("task")
    try:
        res = get_func_name(task)
        func_name = res["func_name"]
        args = res.get("arguments", [])
        print("ARGUMENTS : ", args)
        if args:
            generated_func = globals()[func_name](*args)
            print("GENERATED FUNC :",generated_func)
            res = f"{func_name} executed successfully"
        else:
            generated_func = globals()[func_name]()
            print(generated_func)
            res = f"{func_name} executed successfully"
    except Exception as e:
        res = None
        print("error : ", e)
    return jsonify(res)


```

Tasks.py
--------

```
def generate_data_files(user_email: str):
    subprocess.Popen(
        [
            "uv",
            "run",
            "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py",
            f"{user_email}",
            "--root",
            "../data",
        ]
    )
    print("data generated successfully")

```

Please Guide [@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #68

- **Author**: JoelJeffrey
- **Posted on**: 2025-02-07T07:29:18.667Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/68

A query regarding the task description in the query given to LLM for phase A.

For task A3, we have been asked to count wednesdays and the python file corresponding to A3 does count for wednesday alone. However the example says the LLM might be asked to count Sundays or other days. Should we be modifying task A3 code? Or was that just an example and only Wednesdays would need to be counted?

---

## Post #69

- **Author**: 23f1002382
- **Posted on**: 2025-02-07T10:11:59.243Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/69

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) Please respond .

---

## Post #70

- **Author**: 22f3001777
- **Posted on**: 2025-02-07T13:37:29.745Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/70

When will the project session be held? If I have missed it, can I get the recording?

[@carlton](/u/carlton)

---

## Post #71

- **Author**: carlton
- **Posted on**: 2025-02-07T14:15:14.659Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/71

Tuesday is when we are currently planning a project session.

Kind regards

---

## Post #72

- **Author**: carlton
- **Posted on**: 2025-02-07T14:21:00.051Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/72

Tasks in Phase A are defined but that does not mean it has to do one precise thing. If that was the case then there is no use for an LLM.

Your application should be able to take parse the input and be able to run commands that do similar things in parameterised fashion. It could be Wednesdays or Sundays or it might be in Arabic days or anything. So coding to precisely do something very specific is not the goal.

The program has to be intelligent to do a certain type or class of tasks.

We had a session introducing project. Week 3 session 1. But we will have a more hands on session on Tuesday.

Kind regards

---

## Post #73

- **Author**: 23f2003751
- **Posted on**: 2025-02-07T15:47:26.981Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/73

the last date of project submission is gonne get extended?

---

## Post #74

- **Author**: carlton
- **Posted on**: 2025-02-07T16:03:54.000Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/74

Project 1 was released over a month ago. So there will be no extension for Project 1

---

## Post #75

- **Author**: 21f3002277
- **Posted on**: 2025-02-07T16:06:52.107Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/75

how to handle this error  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/b/cb2aa2c67034917f4e124243281661285cbe26a6.png)

image1425×490 11.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/b/cb2aa2c67034917f4e124243281661285cbe26a6.png "image")

  
[@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

## Post #76

- **Author**: 22f3001315
- **Posted on**: 2025-02-07T19:50:53.195Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/76

```
    expected = sum(1 for date in dates if parse(date).weekday() == 2)
    if result.strip() != str(expected):
        return mismatch("/data/dates-wednesdays.txt", expected, result)
    return True```



```

![:red_circle:](https://emoji.discourse-cdn.com/google/red_circle.png?v=12 ":red_circle:") /data/dates-wednesdays.txt  
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") EXPECTED:  
129  
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") RESULT:  
“129”

If it is expecting str then why throw error sir ? [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
or just tell me how to pass count as an int here

```
with open(output_file, "w") as f:
        f.write(str(count)) 

```

---

## Post #77

- **Author**: 22f2001640
- **Posted on**: 2025-02-08T08:33:27.497Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/77

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
**I am getting below error message from LLM end points **<https://api.openai.com/v1/chat/completions> or <https://aiproxy.sanand.workers.dev/openai/v1/embeddings>** , while running my project .**

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/7/775bdd56ec848f8c87546375952710aacc722ba1.png)  
Kindly help me to resolve this issue. ![:cry:](https://emoji.discourse-cdn.com/google/cry.png?v=12 ":cry:")

---

## Post #78

- **Author**: 23f2005138
- **Posted on**: 2025-02-08T10:13:42.037Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/78

[@carlton](/u/carlton) Will there be evaluation script for tasks in group B also?

Some questions about ‘B’ group tasks:

Q1: For the following tasks (B5, B7, B9, and B10) tasks, how will input files be provided? Will it be URL or will `datagen.py` also generate files for these?

Q2: For the above tasks as well as for B6 ( Extract data from (i.e. scrape) a website), how should output be returned?

Q3: In task B8, for transcribing audio file, which Python package is recommended or do we need to use OpenAI API?

B5. Run a SQL query on a SQLite or DuckDB database  
B7. Compress or resize an image  
B8. Transcribe audio from an MP3 file  
B9. Convert Markdown to HTML  
B10. Write an API endpoint that filters a CSV file and returns JSON data

---

## Post #79

- **Author**: 22f3001315
- **Posted on**: 2025-02-08T10:14:39.105Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/79

its expecting to match every single detail in that even " and ’ .  
in that case changing evaluate.py will result in zero or less marks.  
llm will only handle -calling function based on query and parameter . What is it going to do about the logic of functions.

If i still focus on passing evaluate.py will it be any good sir [@carlton](/u/carlton) [@s.anand](/u/s.anand)

```
🔴 /data/contacts-sorted.json
⚠️ EXPECTED:
[{'first_name': 'Kevin', 'last_name': 'Aguirre', 'email': 'ricardocarlson@example.net'}, {'first_name': 'Andrew', 'last_name': 'Anderson', 'email': 'kimberly08@example.com'}, {'first_name': 'Robert', 'last_name': 'Arnold', 'email': 'hunterpamela@example.com'}, {'first_name': 'Isaac', 'last_name': 'Barker', 'email': 'jessicabriggs@example.net'}, {'first_name': 

```

My output was in good looking structured form but I had to make it look like this just to pass the evaluation.

```
⚠️ RESULT:
[{"first_name": "Kevin", "last_name": "Aguirre", "email": "ricardocarlson@example.net"}, {"first_name": "Andrew", "last_name": "Anderson", "email": "kimberly08@example.com"}, {"first_name": "Robert", "last_name": "Arnold", "email": "hunterpamela@example.com"}, {"first_name": "Isaac", "last_name": "Barker", "email": "jessicabriggs@example.net"}, {"first_name": "Anthony", "last_name": "Barrett", "email": "kevinknox@example.org"}, {"first_name": "Monique", "last_name": "Bass", "email": "lindsaymcgrath@example.net"}, {"first_name": "Michael", "last_name": "Berry", "email": "an

```

---

## Post #81

- **Author**: 23f2003751
- **Posted on**: 2025-02-09T06:06:02.825Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/81

Sorry, sir, not trying to be rude, but there isn’t a single full-fledged project session. It’s a bit difficult to dive into the project without guidance on how to do it. It would be nice to have a full project session where we can start a project from the beginning and follow it to completion.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---

## Post #82

- **Author**: Yogesh1
- **Posted on**: 2025-02-09T06:33:13.210Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/82

Yes. I am very worried about this project. I have been trying to do this. But have gotten nowhere until now.

---

## Post #83

- **Author**: 22f2001590
- **Posted on**: 2025-02-09T08:10:55.954Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/83

[@carlton](/u/carlton) sir I request you demonstrate atleast few tasks, I spent last 2 days trying to implement but din’t reach anywhere, its really demotivating sir.

---

## Post #84

- **Author**: akashkunwar
- **Posted on**: 2025-02-09T09:38:41.944Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/84

Can you please demonstrate it by just doing One task or provide sample example code of 1 similar task in the way you explained here. It will be very helpful right now it is very confusing.

---

## Post #85

- **Author**: carlton
- **Posted on**: 2025-02-09T10:30:37.275Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/85

We will be doing project session on ~~Tuesday 9 Feb~~ [correction] Tuesday 11th of Feb (thanks [@23f1002382](/u/23f1002382) [@23f2000237](/u/23f2000237)) . Project 1 uses the things you learnt in week 1-3. But mostly week 2 & 3.

We dont do it in the beginning, (but introduced it 2 weeks ago in a live session), to give students chance to practise the new learnings from week 2 & 3.

The plan has always been to demonstrate a few tasks and have you try doing the rest.

Kind regards

---

## Post #86

- **Author**: 22f2001640
- **Posted on**: 2025-02-09T10:41:46.503Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/86

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
**I am getting below error message from LLM end points **<https://api.openai.com/v1/chat/completions> or <https://aiproxy.sanand.workers.dev/openai/v1/embeddings>** , while running my project .**

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/7/775bdd56ec848f8c87546375952710aacc722ba1.png)  
Kindly help me to resolve this issue. I am unable to proceed with my project.

---

## Post #88

- **Author**: 23f2000237
- **Posted on**: 2025-02-09T11:07:42.376Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/88

Today’s 9th Feb and it’s a Sunday.

---

## Post #89

- **Author**: 23f2000983
- **Posted on**: 2025-02-09T15:27:58.255Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/89

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png) s.anand:

> **Update: 27 Feb 2025**:

Sir, does this mean 27th is submission deadline?

---

## Post #90

- **Author**: carlton
- **Posted on**: 2025-02-10T02:01:43.833Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/90

Hi Aindree,

No its a typo (and will be corrected soon). In the context of what was written it clearly means it was *updated* on 27th January. The update being that the evaluation.py file was provided so that you could test your code against it.

Thanks for bringing it to our attention.

Kind regards

---

## Post #91

- **Author**: JoelJeffrey
- **Posted on**: 2025-02-10T05:47:01.257Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/91

Hi

This would be only for a selected few questions right because say for the credit card question, where the LLM is involved, to get the card number itself, we have to give a fine-tuned and strong query.

---

## Post #92

- **Author**: 23f2000237
- **Posted on**: 2025-02-10T09:14:25.875Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/92

Try using the eval() function, that seemed to work for me

---

## Post #93

- **Author**: 23f2005138
- **Posted on**: 2025-02-10T10:38:11.034Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/93

[@carlton](/u/carlton) [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj) Sir, could you please share some guidance on the above?

---

## Post #94

- **Author**: 23ds1000022
- **Posted on**: 2025-02-10T11:26:25.879Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/94

[@jivraj](/u/jivraj),[@carlton](/u/carlton)  
I have done the a1 to a10 task and tried querying through localhost and its working fine basically all these ten steps but dont know whether its enough or not. also steps in phase B i am confused that should we create separate endpoints for these tasks or should it be with same /run endpoint and query. then will the input be random by any user. what about the output . where should it be given. phase b needs more explanation.

---

## Post #95

- **Author**: 23f2001305
- **Posted on**: 2025-02-10T11:35:58.014Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/95

At what time will the session be happening tomorrow sir can you please give the details?

---

## Post #96

- **Author**: apanjwani
- **Posted on**: 2025-02-10T14:27:20.468Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/96

Hi [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Facing some issues in running my project. Taking an example of the Phase A - A3 task.

I am able to read my files through the GET/read/data/dates.txt query.  
I am also able to use the count\_wednesdays function through the POST/run task/count\_wednesdays.

But when I am entering a query such as “count\_wednesdays in data/dates.txt” I am unable to get a response.  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3409badd267a53d868ee0474c770481d75a98510.png)

image618×246 6.28 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3409badd267a53d868ee0474c770481d75a98510.png "image")

  
Please advice. Thank you.

---

## Post #97

- **Author**: 23f1000299
- **Posted on**: 2025-02-10T17:09:42.837Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/97

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/4/a47a14f732c91f801761f2728bdf74f5611c81f0_2_690x63.png)

image1215×112 19 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a47a14f732c91f801761f2728bdf74f5611c81f0.png "image")

On task A8, credit-card.png is given, but it is in credit\_card.  
it makes the errors. I checked that 2 to 3 tasks depend on these, and we create the ouput file with ‘-’ this only. please clarify that output and input files name ‘-’ or ‘\_’ [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #98

- **Author**: 23f1000299
- **Posted on**: 2025-02-10T17:13:41.736Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/98

On tomorrow live sessions, kindly explain how to use docker, evaluations, github, what generally we have to do submit, please get some tuturials for us to submit those answers. Thankyou Sir [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

## Post #99

- **Author**: 23f1002382
- **Posted on**: 2025-02-10T18:51:11.574Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/99

(post deleted by author)

---

## Post #100

- **Author**: 23f1002382
- **Posted on**: 2025-02-10T21:15:48.888Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/100

(post deleted by author)

---

## Post #101

- **Author**: 23f1002382
- **Posted on**: 2025-02-10T21:25:21.100Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/101

(post deleted by author)

---

## Post #102

- **Author**: 23f1002382
- **Posted on**: 2025-02-10T21:59:07.953Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/102

![:dart:](https://emoji.discourse-cdn.com/google/dart.png?v=12 ":dart:") Score: 9 / 10  
Almost done with A tasks. Please use this for local llm to verify output  
Also Ollama doesn’t require Schemas  
  
CHECK OUT THE REPO AND ANY INPUTS ARE WELCOME  
[Link to ReadMe and also repo](https://github.com/ANdIeCOOl/TDS-Project-1/blob/checking-with-evaluate.py/README.md)

---

## Post #103

- **Author**: carlton
- **Posted on**: 2025-02-11T03:51:52.920Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/103

Hi Andrew,

You have done a great job with the Phase A tasks. Very methodical, well structured, logical and even incorporates (unnecessarily) two different ways of evaluating its performance via local llm or the project proxy.

I just want to forewarn you (and others who are tempted to just blindly copy and paste) that evaluate.py is not meant to give you an exact expectation of what prompts will be sent to your application.

**In other words getting 10/10 in `evaluate.py` does NOT guarantee 10/10 or even 5/10 or 1/10 in the real evaluation.**

So do not write your code so rigidly that it will only work in the very strict interpretation of `evaluate.py`. It has always been meant to give you a feel for what to aim for. Your code should be flexible enough to deal with the general *idea* of the task.

That said, `evaluate.py` is a good way to know what to expect. Some of Phase A tasks although given a detailed specification in the project description, will still be given challenging prompts (i.e. hard difficulty, and requires some clever self correcting mechanism). Some of the tasks will be given straight forward prompt (i.e. easy for your application). Some of the tasks will be given with some level of parameterisation that deviates from the strict interpretation (i.e. medium difficulty).

Hope that helps with how you deal with Phase B tasks (and making your Phase A more robust to a stronger evaluation.)

**A word of caution:** *(i.e. this is just some advice, not a set in stone recommendation)* Your requirements.txt is massive. If your code does not execute a task (*possibly your first task*) within 20 seconds (on our server) then it will fail that task. You might want to consider a dynamic, flexible way of installing only required libraries when necessary and keeping the image footprint small and efficient, as we will necessarily have limits on how big we allow images to grow since we have to run and evaluate hundreds of images automatically.

Kind regards

---

## Post #105

- **Author**: 22f2001640
- **Posted on**: 2025-02-11T07:01:21.237Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/105

Respected [@s.anand](/u/s.anand) [@carlton](/u/carlton) and [@Jivraj](/u/jivraj) ,

Is anyone actively monitoring the Discourse page? I have been raising this issue for the past few days, but there has been no response. Does this mean the TAs are not addressing students’ concerns?

I am encountering the following error while running my project with these LLM endpoints:

* **<https://api.openai.com/v1/chat/completions>**
* **<https://aiproxy.sanand.workers.dev/openai/v1/embeddings>**  
  ![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/7/775bdd56ec848f8c87546375952710aacc722ba1.png)  
  This issue is blocking my progress, and I urgently need assistance to resolve it. Kindly provide guidance or suggest a solution at the earliest.

Looking forward to your response.

Thanks,  
Telvin Varghese

---

## Post #106

- **Author**: Kratikajain
- **Posted on**: 2025-02-11T07:17:01.378Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/106

Hi,  
I am not able to understand how to do the Project 1. The date is also very near.

The problem I am facing is, When I did the Modules the page was different, but now in the Project 1 I am not getting any section to submit the project.

Please let me know where are the questions and how tot submit that.  
The deadline is near.

---

## Post #107

- **Author**: 23f1002382
- **Posted on**: 2025-02-11T07:18:03.044Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/107

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

> o do not write your code so rigidly that it will only work in the very strict interpretation of `evaluate.py`. It has always been meant to give you a feel for what to aim for. Your code should be flexible enough to deal with the general *idea* of the task.

This where I need help, i tried doing with agentic framework but i failed with the model in llm proxy, which was highly suspect because, that model should have known what the uv framework but it seemed to me to be outdated. Hence executing code Interpreter tools failed as the model gave outdated code. I have raised this issue before

Hence i moved to function calling, using local llms as cost-effective solution and it was quite robust.

I just need to understand how the function should be general, maybe 2-3 tasks you could provide the general description along with all the ways one would query the agent llm(ie our project). This general function is what i need help with. Please kindly do the needful.

---

## Post #108

- **Author**: 21f2000709
- **Posted on**: 2025-02-11T07:54:33.324Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/108

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

> keeping the image footprint small and efficient, as we will necessarily have limits on how big we allow images to grow since we have to run and evaluate hundreds of images automatically.

Any tentative size cutoff for the docker image?

---

## Post #109

- **Author**: carlton
- **Posted on**: 2025-02-11T10:14:00.116Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/109

Hi Telvin

You have run out of tokens. Thats what the message is saying. You ran out 3 days ago. It was clearly mentioned that the limit is $1. You have exceeded $2.

[![Screenshot 2025-02-11 at 3.36.50 pm](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b74cf0c060e28cd3459173bce28d123a8d5da05_2_690x423.png)

Screenshot 2025-02-11 at 3.36.50 pm2078×1276 305 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/b/1b74cf0c060e28cd3459173bce28d123a8d5da05.png "Screenshot 2025-02-11 at 3.36.50 pm")

In our current internal build of project 1, we have yet to exceed $0.50

As to whether it can be renewed is something we have still not yet decided, because the question you have raised equally would apply to everyone. Raising it for you means raising it for everyone. $1 for everyone equals raising it by $1600+ *(i.e Rs 1.39 Lakhs)* for us!

The budget question then involves more than one person. It also involves the BS Team Operations and not just the TDS team and therefore instead of responding with a response that is not useful, we typically try to solve the problem first and then respond.

In short we are working on it. But as we have mentioned repeatedly in our sessions, use APIs efficiently, thats part of the skill. As soon as we have a resolution we will inform everyone via an announcement and an email.

Kind regards

---

## Post #110

- **Author**: 22f2001640
- **Posted on**: 2025-02-11T10:34:24.293Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/110

Thanks for your response, [@Carlton](/u/carlton). It seems I won’t be able to proceed with the project until this issue is resolved. Also, I haven’t used LLM so much until February 7th to cost $2.

---

## Post #111

- **Author**: carlton
- **Posted on**: 2025-02-11T10:43:05.396Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/111

Every request you send, gives you a response back with exactly how much that request cost. So you can track your usage.

---

## Post #112

- **Author**: 22f2001640
- **Posted on**: 2025-02-11T11:08:19.962Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/112

I’m aware of that. I’ve mostly noticed a cost of $0.0003 per request, so I haven’t been tracking my total monthly expenses. Moving forward, I’ll keep a record of the cost for each request. Also, do strong prompts impact the overall cost?

---

## Post #113

- **Author**: 21f2000709
- **Posted on**: 2025-02-11T11:32:35.401Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/113

[@carlton](/u/carlton) Is the project session happening today? I don’t have the link. Can you please send it if it’s happening?

---

## Post #114

- **Author**: apanjwani
- **Posted on**: 2025-02-11T11:34:29.425Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/114

Hi, where is the link for todays Project 1 demo session? [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #115

- **Author**: 23f2000573
- **Posted on**: 2025-02-11T11:37:00.655Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/115

<https://meet.google.com/odh-ycbm-ahj?authuser=0>

---

## Post #116

- **Author**: 22f3002786
- **Posted on**: 2025-02-11T11:46:25.605Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/116

request
=======

```
http://localhost:8000/run?task=Extract the sender's email from /data/email.txt and write to /data/email-sender.txt](http://localhost:8000/run?task=Extract the sender's email from /data/email.txt and write to /data/email-sender.txt)

```

output
======

```
{    "detail": "Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid\_request\_error', 'param': None, 'code': 'invalid\_issuer'}}"}

```

[@carlton](/u/carlton) sir I am getting this issue while running my script. Please help!

---

## Post #117

- **Author**: 23f2000983
- **Posted on**: 2025-02-11T12:19:31.097Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/117

I’m getting an error in task a2, def do\_a2():  
“”“Format markdown using prettier”“”  
format\_md\_path = DATA\_ROOT / “format.md”  
subprocess.Popen([“prettier”, str(format\_md\_path), “–write”, “–parser”, “markdown”])  
print(“data formatted successfully”)

any idea how to fix this? Also in A8, a 5 and a 3 is getting interchanged. Can someone help why that is hapening, I changed the prompt to include caution about not switching 3 and 5 as well, that didn’t help either

---

## Post #118

- **Author**: 22f2000113
- **Posted on**: 2025-02-11T12:35:58.890Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/118

what is the session time?

---

## Post #119

- **Author**: 23f1002104
- **Posted on**: 2025-02-11T12:45:30.356Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/119

[![Screenshot 2025-02-11 181453](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/7/b7b024074300d61b0df1d7ebf727f9cfb8fcceae.png)

Screenshot 2025-02-11 1814531459×207 15.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/7/b7b024074300d61b0df1d7ebf727f9cfb8fcceae.png "Screenshot 2025-02-11 181453")

  
Could you kindly help me with this

---

## Post #120

- **Author**: 23f1001524
- **Posted on**: 2025-02-11T15:23:49.900Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/120

in checking for the task of json my code is outputting json with double quotes (valid json) and evaluate.py has exact same json but with single quotes , what should I do?

---

## Post #121

- **Author**: 23f1002382
- **Posted on**: 2025-02-11T15:26:23.894Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/121

check out my repo and download the datagen and evaluate file for testing

---

## Post #122

- **Author**: 23f1002382
- **Posted on**: 2025-02-11T15:27:01.472Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/122

it should work, use fastapi text response when /read api

---

## Post #123

- **Author**: 22f2000113
- **Posted on**: 2025-02-11T16:22:42.078Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/123

Has anyone used a local LLM for testing? If so, could you please share the request URL and the request body format? I attempted to use a local LLM, but I was unable to succeed

---

## Post #124

- **Author**: 23f1002382
- **Posted on**: 2025-02-11T17:07:07.884Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/124

use ollama it is openai api compatible, supports function calling without json schema for tool usage. Check it out

---

## Post #125

- **Author**: 23f1002382
- **Posted on**: 2025-02-11T18:04:05.195Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/125

NEED HELP. CAN SOMEONE CONTACT OLLAMA AND ASK THEM TO CHECK THEIR CODE ITS HAS SOME SILLY MISTAKES IN CODE EXAMPLES. I DONT KNOW HOW TO DO IT.

[LINK TO PAGE WITH CODE EXAMPLE](https://ollama.com/blog/embedding-models)

[![Screenshot 2025-02-11 232608](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/7/27adf05313946c445fec614cd1fd17ba6c1f4cde.png)

Screenshot 2025-02-11 232608919×714 22.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/7/27adf05313946c445fec614cd1fd17ba6c1f4cde.png "Screenshot 2025-02-11 232608")

  
  
  
  
correct code in step 2 collection query step

```
response = ollama.embed(
  model="nomic-embed-text:latest",
  input=task
)
results = collection.query(
  query_embeddings=response["embeddings"], #here embeddings and also not list of list as response embeddings already gives correct format
  n_results=1
)
data = results['documents'][0][0]

```

[@s.anand](/u/s.anand) [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

## Post #126

- **Author**: 23f2005325
- **Posted on**: 2025-02-11T19:51:59.902Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/126

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

While implementing the Phase B tasks, can I take the data (csv file, git repo, audio, sqlite/duckdb database, website, image and markdown file) of my choice and perform any operation on them as long as they meet the critetia mentioned in the Phase B task list? Please guide.

---

## Post #127

- **Author**: 23f2005325
- **Posted on**: 2025-02-11T20:29:08.345Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/127

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

In the Task B5, where we have to run an SQL query on a sqlite or duckdb database, should I create a database on my own and then take the query to be ran on it as an argument? Or should I take the query as an argument and run it on the ticker\_sales.db in ./data folder? Please guide

---

## Post #128

- **Author**: 23f2001978
- **Posted on**: 2025-02-11T21:56:07.834Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/128

same issue on my side as well

---

## Post #129

- **Author**: 23f2001978
- **Posted on**: 2025-02-11T22:23:51.126Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/129

on using the AIPROXY\_TOKEN from here <https://aiproxy.sanand.workers.dev/>

getting this error :

Error: Your authentication token is not from a valid issuer.

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) please help!

---

## Post #130

- **Author**: Yogesh1
- **Posted on**: 2025-02-12T00:20:25.124Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/130

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) Can the link to the live session (for project) be provided?

---

## Post #131

- **Author**: 23f2004752
- **Posted on**: 2025-02-12T00:57:04.758Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/131

As in the previous session for task a1 we use llm just to get the url and email , so after retriving the both arguments can i use them in a function and got the work given in work done in function.  
Also, am i correct that we use llm only to retrive url or location ??

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #132

- **Author**: 23f2004752
- **Posted on**: 2025-02-12T01:27:51.130Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/132

Anyone whom have done have done any one task of phase a and one task of phase b, please help…

---

## Post #133

- **Author**: 23f2004752
- **Posted on**: 2025-02-12T01:47:54.869Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/133

Can you do one task from each phase in today’s session. Please [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #134

- **Author**: 22f2000113
- **Posted on**: 2025-02-12T02:13:05.286Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/134

thanks for the reply I will check

---

## Post #135

- **Author**: thinkmachine
- **Posted on**: 2025-02-12T03:29:46.481Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/135

TDS project ![:x:](https://emoji.discourse-cdn.com/google/x.png?v=12 ":x:") Tedious project ![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:")

---

## Post #136

- **Author**: AnvithaV
- **Posted on**: 2025-02-12T05:12:14.328Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/136

can anyone share the link of yesterdays live session if there in youtube

---

## Post #137

- **Author**: 23f2004042
- **Posted on**: 2025-02-12T05:16:06.451Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/137

Its updated in the TDS live sessions playlist

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b990ffaadbfcbad12d865c514f3d6b48e5bc7cf2.jpeg "2025-02-06 Week 5 - Session 1 - TDS Jan 25")](https://www.youtube.com/watch?v=jXj6bqy4R4c)

---

## Post #138

- **Author**: Adithya
- **Posted on**: 2025-02-12T06:27:17.724Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/138

*For task A2*:

* **A2**. Format the contents of `/data/format.md` using `prettier@3.4.2`, updating the file in-place

I am getting the following error:  
`🔴 A2 failed: Command '['npx', 'prettier@3.4.2', '--stdin-filepath', '/data/format.md']' returned non-zero exit status 1.`

However, running a **POST request** to <https://localhost:8000/run?task=Format+/data/format.md+with+prettier+3.4.2> gives successful output.

`{"success":true,"message":"Formatted and verified successfully!"}%`

Here is my code snippet:

```
def format_file(filepath):
    while True:  # Loop until formatting and verification pass
        try:
            result = subprocess.run(
                ["npx", "prettier@3.4.2", "--write", filepath],
                check=False,  # Don't raise exception automatically
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                return {"success": False, "message": f"Prettier write failed: {result.stderr}"}

            if verify_prettier_formatting(filepath):
                return {"success": True, "message": "Formatted and verified successfully!"}
            else:
                logging.info("Verification failed. Retrying formatting...") #Log the retry
                # If verification fails, the loop continues and prettier --write is executed again.

        except Exception as e:
            return {"success": False, "message": str(e)}

def verify_prettier_formatting(filepath):
    try:
        subprocess.run(["npx", "prettier@3.4.2", "--check", filepath], check=True, capture_output=True, text=True) #Capture output
        return True  # File is formatted correctly
    except subprocess.CalledProcessError as e:
        logging.error(f"Prettier check failed: {e.stderr}") # Log the error from prettier check
        return False  # File is not formatted correctly

```

What am I missing here?

---

## Post #139

- **Author**: 22f3001307
- **Posted on**: 2025-02-12T07:05:33.610Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/139

I am getting the same error. Did you find any solution?

---

## Post #140

- **Author**: 21f2000709
- **Posted on**: 2025-02-12T07:08:29.395Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/140

Has anyone succeeded in the extraction of credit cards details task? The LLM seems to consider it as illegal task and if I use pytessaract the docker image size will become really large. What to do in this case?

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #141

- **Author**: 22f3001307
- **Posted on**: 2025-02-12T07:12:02.257Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/141

Hi [@carlton](/u/carlton) [@Jivraj](/u/jivraj),

I followed what you taught in Feb 11 session and tried implementing task A1. My understanding is once i run the subprocess, datagen.py file should be run and /data folder should be created in the project folder. But it is not happening to me. I am getting the following error

```
Traceback (most recent call last):
  File "/var/folders/rj/z_3b8hl51558519w90k5hp600000gn/T/datagen4COEF3.py", line 284, in <module>
    os.makedirs(config["root"], exist_ok=True)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen os>", line 227, in makedirs
OSError: [Errno 30] Read-only file system: '/data'

```

If i can’t automate this process, i don’t see the point writing code for other tasks. Can anyone help me solving this error?

---

## Post #142

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T07:22:31.307Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/142

shell = true in evaluate.py, remove it meaning comment it out, task a2 thats causing the error

---

## Post #143

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T07:25:19.252Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/143

the admin banned me from using laughing emoji [@jkmadathil](/u/jkmadathil)

---

## Post #144

- **Author**: JoelJeffrey
- **Posted on**: 2025-02-12T08:44:41.379Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/144

For task A6,

> HTTP Request: GET <http://localhost:8000/read?path=/data/docs/index.json> “HTTP/1.1 200 OK”

```
⚠️ EXPECTED:
{'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/culture.md': 'Prevent north only miss cold.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/family.md': 'Debate at office traditional stop great.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/bar.md': 'Among ago cover good.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/story.md': 'Anything song key first.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'drop/former.md': 'Brother college detail.', 'drop/add.md': 'Fish work to individual.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/else.md': 'Fly candidate may so college.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/ready.md': 'Central about ready information.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/question.md': 'Family evening its degree.', 'civil/argue.md': 'Line culture seven six.', 'civil/gas.md': 'Talk why around necessary.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/central.md': 'Believe region their our whatever.', 'standard/easy.md': 'Myself must detail win.', 'standard/sound.md': 'Night national film next.', 'standard/five.md': 'Lay would green generation season.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/late.md': 'Scientist people may story.', 'standard/level.md': 'Work around ask to.', 'standard/analysis.md': 'While natural from staff option artist can.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/sometimes.md': 'Big order defense field represent.', 'few/weight.md': 'Man mission American.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/my.md': 'Open line address contain whole impact into front.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/southern.md': 'Meet prove admit.', 'few/theory.md': 'Security effort protect future task long close.', 'few/information.md': 'Really morning yeah.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/save.md': 'Thought hear home set employee early purpose.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/book.md': 'Mr oil difficult dog.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/cold.md': 'Election buy member alone school audience.', 'community/else.md': 'Actually service thank state.', 'community/left.md': 'Picture let tell never.', 'community/soldier.md': 'It lawyer cover job.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'Congress/remember.md': 'Purpose good policy line trade.', 'ten/rock.md': 'Method wall when book agency.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/nature.md': 'Eight own hot first success.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/serve.md': 'Want exist bank book.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/white.md': 'Whatever significant capital air about.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/own.md': 'Say small finish sing raise.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/discuss.md': 'Hit result find miss culture heart clear task.'}

```

```
⚠️ RESULT:
{'suddenly/mouth.md': 'Outside food subject positive human.', 'suddenly/add.md': 'Window word during born do finally.', 'suddenly/free.md': 'Them ball significant different which traditional.', 'suddenly/management.md': 'Man fire long hour modern.', 'suddenly/leave.md': 'Season people Democrat hand among too.', 'suddenly/low.md': 'Front actually decision security fast song believe leg.', 'suddenly/why.md': 'Account listen such day method sing.', 'suddenly/miss.md': 'Rather although team thank.', 'suddenly/base.md': 'Total low room structure staff.', 'suddenly/strategy.md': 'Never understand less operation onto still trade environment.', 'ground/girl.md': 'Civil speech back sell.', 'ground/game.md': 'Fill whose card or daughter old meet.', 'ground/term.md': 'Pick return put set.', 'ground/every.md': 'Free service trouble effort somebody blood modern.', 'ground/along.md': 'Important plant increase door much.', 'ground/call.md': 'Article agent three scientist.', 'ground/do.md': 'Memory food strategy meeting.', 'ground/end.md': 'Large player discussion similar prove part.', 'ground/full.md': 'Actually start commercial.', 'ground/ever.md': 'Human example gun now my just Republican.', 'way/not.md': 'Decision together land chair.', 'way/morning.md': 'Information later service raise after trial base.', 'way/responsibility.md': 'Our child why environment care goal.', 'way/increase.md': 'Return say response political.', 'way/relationship.md': 'General view thing poor machine market peace.', 'way/soldier.md': 'Produce table should will school produce player wall.', 'way/act.md': 'Smile guess simple read style its international.', 'way/sound.md': 'Conference first finally recognize as.', 'way/reach.md': 'Exactly size discuss management miss article.', 'way/hotel.md': 'From become actually.', 'hit/run.md': 'Stock several region put thought decade evening.', 'hit/free.md': 'Crime usually produce.', 'hit/foot.md': 'Ball specific trip state.', 'hit/ball.md': 'Condition color focus traditional.', 'hit/song.md': 'Section environmental final light word in yes operation.', 'hit/since.md': 'Shoulder wrong matter seek cultural vote themselves.', 'hit/safe.md': 'Hear try spend item can along light.', 'hit/much.md': 'Guess great dream through concern feel.', 'hit/prove.md': 'Her base cup forward.', 'hit/stop.md': 'Nation this avoid herself deal place memory.', 'few/sometimes.md': 'Big order defense field represent.', 'few/southern.md': 'Meet prove admit.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/weight.md': 'Man mission American.', 'few/information.md': 'Really morning yeah.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/theory.md': 'Security effort protect future task long close.', 'few/my.md': 'Open line address contain whole impact into front.', 'resource/rest.md': 'Ok tough talk.', 'resource/move.md': 'Law write democratic drug itself house accept through.', 'resource/particularly.md': 'Affect woman nice.', 'resource/entire.md': 'Focus to once sea friend group.', 'resource/painting.md': 'Customer environment none trade.', 'resource/structure.md': 'Stuff return protect our bit reality.', 'resource/until.md': 'Growth industry region receive.', 'resource/significant.md': 'Long million fall throughout government tend.', 'resource/hospital.md': 'Quality certain fight want much body between.', 'resource/marriage.md': 'Foot specific mission.', 'for/hope.md': 'Whatever report wife fly close lot student.', 'for/poor.md': 'Explain claim police eye paper much when.', 'for/assume.md': 'Control yeah effect local economy worry.', 'for/couple.md': 'Floor both take indeed audience.', 'for/money.md': 'Join live next care material.', 'for/never.md': 'Me natural full.', 'for/situation.md': 'Show book instead hope lawyer.', 'for/north.md': 'Card level kind send loss growth.', 'for/hit.md': 'Minute wish above pass just later watch.', 'for/perhaps.md': 'Every professor sport unit rock bed.', 'project/individual.md': 'Tough safe machine small outside mention could must.', 'project/change.md': 'Century drug value.', 'project/home.md': 'Big decade edge feeling surface matter force student.', 'project/want.md': 'Region catch nation civil one Mr specific.', 'project/something.md': 'Major control three.', 'project/reality.md': 'Mouth including fine.', 'project/my.md': 'Fire point or success marriage write example.', 'project/issue.md': 'Former true career similar use visit machine.', 'project/surface.md': 'Cold reduce task life American act stage.', 'project/drug.md': 'Reason still field animal.', 'effort/morning.md': 'Policy quickly get capital smile.', 'effort/he.md': 'Thought view product interview explain.', 'effort/house.md': 'High hear thought according.', 'effort/church.md': 'Culture ask change focus.', 'effort/effect.md': 'Before suddenly who student could boy serve.', 'effort/price.md': 'Shoulder financial public reason home explain safe.', 'effort/company.md': 'Exactly treatment concern fly factor care drive.', 'effort/international.md': 'Rich take hear open.', 'effort/federal.md': 'Difference rate character by his blood this.', 'effort/computer.md': 'Lay financial article exactly.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/culture.md': 'Prevent north only miss cold.', 'by/family.md': 'Debate at office traditional stop great.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'bill/appear.md': 'Whole senior next stop yard national section.', 'bill/room.md': 'Able improve anything teacher media writer employee.', 'bill/citizen.md': 'Safe anyone major reach mother ground over leave.', 'bill/for.md': 'A several low detail.', 'bill/role.md': 'More light anything study hand power.', 'bill/set.md': 'Necessary century drive attack capital.', 'bill/generation.md': 'Stay could quality shake.', 'bill/drive.md': 'Situation we his.', 'bill/computer.md': 'Culture ahead change perhaps however audience.', 'bill/gas.md': 'Reveal attack and church.', 'color/sell.md': 'Mention although while boy turn.', 'color/throughout.md': 'She actually gun start.', 'color/management.md': 'Short serve beat increase than visit.', 'color/smile.md': 'His season employee husband.', 'color/wear.md': 'Share green measure sometimes.', 'color/official.md': 'Suddenly seat tend thus office action move.', 'color/admit.md': 'Each important clear.', 'color/treat.md': 'Tv outside attorney rich say same environment.', 'color/turn.md': 'Try drop old along.', 'color/sit.md': 'Including turn seem none computer.', 'build/together.md': 'Finally point only police artist.', 'build/rest.md': 'Author run let.', 'build/wall.md': 'Administration a week form side feeling.', 'build/none.md': 'Commercial stop page else.', 'build/explain.md': 'Join tend idea stand not option woman.', 'build/decision.md': 'Poor fund interesting bring.', 'build/beyond.md': 'Artist billion begin record anything none management practice.', 'build/dream.md': 'Decision suddenly prevent speak old power herself.', 'build/each.md': 'Able out key.', 'build/street.md': 'Knowledge specific technology before leave.', 'wrong/market.md': 'Realize key point whatever Democrat or say.', 'wrong/free.md': 'Deal even from mouth source.', 'wrong/sure.md': 'Similar him believe actually.', 'wrong/apply.md': 'Everybody office list service stock significant.', 'wrong/share.md': 'Painting every apply.', 'wrong/standard.md': 'Already place fund really.', 'wrong/might.md': 'Possible during claim view.', 'wrong/nation.md': 'About prove cold question race.', 'wrong/be.md': 'Land debate natural American.', 'wrong/suggest.md': 'Could environmental rather can us night.', 'Congress/remember.md': 'Purpose good policy line trade.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'industry/wrong.md': 'Floor race land those hard actually avoid property.', 'industry/book.md': 'Together state billion race beautiful how.', 'industry/car.md': 'Heart central eye thought painting government appear.', 'industry/cause.md': 'Time religious describe oil heart.', 'industry/feeling.md': 'Include memory strategy other statement imagine teach.', 'industry/small.md': 'Little third your season kind.', 'industry/heavy.md': 'Quality international window probably adult attention.', 'industry/election.md': 'Democrat often turn.', 'industry/possible.md': 'Structure high discover half dog half forward.', 'industry/fish.md': 'Much without in fight miss.', 'live/white.md': 'Whatever significant capital air about.', 'live/discuss.md': 'Hit result find miss culture heart clear task.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/own.md': 'Say small finish sing raise.', 'lot/seat.md': 'Method institution third political.', 'lot/wall.md': 'Each feel program size different kid.', 'lot/worry.md': 'Support moment maintain majority American rule rock.', 'lot/improve.md': 'Reason better difficult take.', 'lot/heart.md': 'Make let way.', 'lot/modern.md': 'Example first recently let.', 'lot/make.md': 'First eat data executive.', 'lot/check.md': 'Wall artist recent side approach.', 'lot/hotel.md': 'Technology town film nothing writer head from.', 'lot/perhaps.md': 'Main manage authority serious short.', 'drop/add.md': 'Fish work to individual.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/else.md': 'Fly candidate may so college.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/former.md': 'Brother college detail.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'central/several.md': 'Appear talk administration sort.', 'central/them.md': 'Unit huge call.', 'central/often.md': 'For nice after analysis series.', 'central/before.md': 'Account vote off police since.', 'central/commercial.md': 'Address country last teacher game compare.', 'central/these.md': 'Feeling rate first national.', 'central/tough.md': 'Party single media process statement forget.', 'central/crime.md': 'Hotel we five blue lawyer argue.', 'central/less.md': 'Guess environmental cover three late.', 'central/nice.md': 'Those religious audience case those.', 'civil/argue.md': 'Line culture seven six.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/ready.md': 'Central about ready information.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/question.md': 'Family evening its degree.', 'civil/gas.md': 'Talk why around necessary.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/central.md': 'Believe region their our whatever.', 'friend/oil.md': 'Little someone story put hundred able.', 'friend/discover.md': 'Someone city idea.', 'friend/month.md': 'Race walk people its Democrat sound.', 'friend/alone.md': 'Suffer concern choose participant work.', 'friend/myself.md': 'Truth simply memory alone plant large.', 'friend/note.md': 'Word end size enough.', 'friend/large.md': 'Tough glass per.', 'friend/wife.md': 'Sea investment many difference keep like improve.', 'friend/allow.md': 'Become personal own behavior sport.', 'friend/hand.md': 'Nation yourself final ground thus follow.', 'standard/late.md': 'Scientist people may story.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/level.md': 'Work around ask to.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/sound.md': 'Night national film next.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/easy.md': 'Myself must detail win.', 'standard/five.md': 'Lay would green generation season.', 'standard/analysis.md': 'While natural from staff option artist can.', 'community/book.md': 'Mr oil difficult dog.', 'community/else.md': 'Actually service thank state.', 'community/soldier.md': 'It lawyer cover job.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/cold.md': 'Election buy member alone school audience.', 'community/left.md': 'Picture let tell never.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/save.md': 'Thought hear home set employee early purpose.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/story.md': 'Anything song key first.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/bar.md': 'Among ago cover good.', 'education/evening.md': 'Give tonight sell over whole word care.', 'education/body.md': 'Note start bad part positive during.', 'education/total.md': 'Contain hit individual college month.', 'education/nature.md': 'Skin look fine policy special part.', 'education/really.md': 'Difference beyond cost but.', 'education/reason.md': 'Wrong increase investment deep near simply spring.', 'education/blood.md': 'North smile know.', 'education/imagine.md': 'Summer keep conference.', 'education/fish.md': 'Answer impact sense professor gun fast me.', 'education/article.md': 'Usually could bad attack customer couple represent.', 'lead/rest.md': 'Address half hit.', 'lead/speech.md': 'Maintain prepare indicate production surface.', 'lead/become.md': 'Building plant air something direction fall provide.', 'lead/stage.md': 'View main when Republican father plant.', 'lead/under.md': 'Test next education series.', 'lead/adult.md': 'Rule others especially institution total what law.', 'lead/which.md': 'Far task service radio reach morning accept.', 'lead/phone.md': 'Unit good including show stand.', 'lead/would.md': 'President still follow race analysis opportunity.', 'lead/trade.md': 'Success whatever environmental avoid father how although may.', 'why/show.md': 'Decade station development character movement.', 'why/data.md': 'Itself feeling fund mean.', 'why/more.md': 'Address music fish team national tough.', 'why/debate.md': 'Meeting wind medical can city face cost.', 'why/something.md': 'Everybody bed economic own least peace executive.', 'why/most.md': 'Agreement station room name.', 'why/spring.md': 'Fine according mission against.', 'why/phone.md': 'By near next teacher be degree although.', 'why/full.md': 'Yard like phone catch on attention your.', 'why/stuff.md': 'Cup everybody open book he decade.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/serve.md': 'Want exist bank book.', 'ten/nature.md': 'Eight own hot first success.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/rock.md': 'Method wall when book agency.', 'rule/hear.md': 'History event character everybody paper machine little billion.', 'rule/thing.md': 'Trial produce despite water range television.', 'rule/feel.md': 'Soon give never future difference.', 'rule/system.md': 'Bill article station despite.', 'rule/produce.md': 'Yes method sense.', 'rule/eye.md': 'Finally this team yet throughout.', 'rule/nation.md': 'Radio entire ago behavior prevent response ten according.', 'rule/thousand.md': 'Anything help military with run.', 'rule/goal.md': 'Inside firm without.', 'rule/perhaps.md': 'Back election leave.'}

```

If I am not wrong, both the expected and actual result contain the same entries. It is just that the ordering is different. The expected result also doesnt follow any particular format (so does the actual result).

Kindly advise on this [@carlton](/u/carlton)

**EDIT** : Resolved on a later evaluation

---

## Post #145

- **Author**: 21f2000709
- **Posted on**: 2025-02-12T08:55:40.171Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/145

For the task - \* **B10**. Write an API endpoint that filters a CSV file and returns JSON data

Do we have to handle prompts for converting CSV to JSON or for writing an endpoint for doing so?

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #146

- **Author**: 22f3001315
- **Posted on**: 2025-02-12T09:04:36.688Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/146

yeah i am also facing the same doubt

---

## Post #147

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T09:04:54.804Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/147

+1…  
[@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---

## Post #148

- **Author**: 23f2003413
- **Posted on**: 2025-02-12T09:36:12.326Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/148

could someone please share their repo for reference. it would be very much helpful

---

## Post #149

- **Author**: TRIGON
- **Posted on**: 2025-02-12T09:38:35.778Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/149

Dear Instructors ([@carlton](/u/carlton), [@iamprasna](/u/iamprasna)):

Confirming, just to be needfully pedantic:

It will **solely** be the responsibility of the Project Evaluator (human or machine) to parse the correct `AIPROXY_TOKEN` generated against my IITM email ID (presumably, per some database which holds all such generated `AIPROXY_TOKEN`s of the students who have generated one); and the correct `$IMAGE_NAME` (to-be-submitted by myself in the Project Submission Google Form) in `podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000`, correct?

Asking this seemingly obvious question, as (apparently) the actual `AIPROXY_TOKEN` is not to be included anywhere in the code, or the repository, or the dockerfile.

---

## Post #150

- **Author**: Adithya
- **Posted on**: 2025-02-12T09:51:42.226Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/150

I am also facing the same issue, just that the ordering is different.  
Sorting by keys also didn’t help.  
Please help on this [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #151

- **Author**: Haricharan
- **Posted on**: 2025-02-12T10:36:08.869Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/151

sir will the tasks of Phase A and Phase B change? like currently do we need to make llm write the code for all tasks dynamically or can we write a pre defined python code to execute tasks after the llm parses the task and runs python code

---

## Post #152

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T10:42:34.656Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/152

Check length of result and length of expected, one is 98 and other is 298

```
expected = {'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/culture.md': 'Prevent north only miss cold.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/family.md': 'Debate at office traditional stop great.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/bar.md': 'Among ago cover good.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/story.md': 'Anything song key first.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'drop/former.md': 'Brother college detail.', 'drop/add.md': 'Fish work to individual.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/else.md': 'Fly candidate may so college.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/ready.md': 'Central about ready information.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/question.md': 'Family evening its degree.', 'civil/argue.md': 'Line culture seven six.', 'civil/gas.md': 'Talk why around necessary.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/central.md': 'Believe region their our whatever.', 'standard/easy.md': 'Myself must detail win.', 'standard/sound.md': 'Night national film next.', 'standard/five.md': 'Lay would green generation season.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/late.md': 'Scientist people may story.', 'standard/level.md': 'Work around ask to.', 'standard/analysis.md': 'While natural from staff option artist can.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/sometimes.md': 'Big order defense field represent.', 'few/weight.md': 'Man mission American.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/my.md': 'Open line address contain whole impact into front.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/southern.md': 'Meet prove admit.', 'few/theory.md': 'Security effort protect future task long close.', 'few/information.md': 'Really morning yeah.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/save.md': 'Thought hear home set employee early purpose.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/book.md': 'Mr oil difficult dog.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/cold.md': 'Election buy member alone school audience.', 'community/else.md': 'Actually service thank state.', 'community/left.md': 'Picture let tell never.', 'community/soldier.md': 'It lawyer cover job.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'Congress/remember.md': 'Purpose good policy line trade.', 'ten/rock.md': 'Method wall when book agency.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/nature.md': 'Eight own hot first success.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/serve.md': 'Want exist bank book.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/white.md': 'Whatever significant capital air about.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/own.md': 'Say small finish sing raise.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/discuss.md': 'Hit result find miss culture heart clear task.'}
result  = {'suddenly/mouth.md': 'Outside food subject positive human.', 'suddenly/add.md': 'Window word during born do finally.', 'suddenly/free.md': 'Them ball significant different which traditional.', 'suddenly/management.md': 'Man fire long hour modern.', 'suddenly/leave.md': 'Season people Democrat hand among too.', 'suddenly/low.md': 'Front actually decision security fast song believe leg.', 'suddenly/why.md': 'Account listen such day method sing.', 'suddenly/miss.md': 'Rather although team thank.', 'suddenly/base.md': 'Total low room structure staff.', 'suddenly/strategy.md': 'Never understand less operation onto still trade environment.', 'ground/girl.md': 'Civil speech back sell.', 'ground/game.md': 'Fill whose card or daughter old meet.', 'ground/term.md': 'Pick return put set.', 'ground/every.md': 'Free service trouble effort somebody blood modern.', 'ground/along.md': 'Important plant increase door much.', 'ground/call.md': 'Article agent three scientist.', 'ground/do.md': 'Memory food strategy meeting.', 'ground/end.md': 'Large player discussion similar prove part.', 'ground/full.md': 'Actually start commercial.', 'ground/ever.md': 'Human example gun now my just Republican.', 'way/not.md': 'Decision together land chair.', 'way/morning.md': 'Information later service raise after trial base.', 'way/responsibility.md': 'Our child why environment care goal.', 'way/increase.md': 'Return say response political.', 'way/relationship.md': 'General view thing poor machine market peace.', 'way/soldier.md': 'Produce table should will school produce player wall.', 'way/act.md': 'Smile guess simple read style its international.', 'way/sound.md': 'Conference first finally recognize as.', 'way/reach.md': 'Exactly size discuss management miss article.', 'way/hotel.md': 'From become actually.', 'hit/run.md': 'Stock several region put thought decade evening.', 'hit/free.md': 'Crime usually produce.', 'hit/foot.md': 'Ball specific trip state.', 'hit/ball.md': 'Condition color focus traditional.', 'hit/song.md': 'Section environmental final light word in yes operation.', 'hit/since.md': 'Shoulder wrong matter seek cultural vote themselves.', 'hit/safe.md': 'Hear try spend item can along light.', 'hit/much.md': 'Guess great dream through concern feel.', 'hit/prove.md': 'Her base cup forward.', 'hit/stop.md': 'Nation this avoid herself deal place memory.', 'few/sometimes.md': 'Big order defense field represent.', 'few/southern.md': 'Meet prove admit.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/weight.md': 'Man mission American.', 'few/information.md': 'Really morning yeah.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/theory.md': 'Security effort protect future task long close.', 'few/my.md': 'Open line address contain whole impact into front.', 'resource/rest.md': 'Ok tough talk.', 'resource/move.md': 'Law write democratic drug itself house accept through.', 'resource/particularly.md': 'Affect woman nice.', 'resource/entire.md': 'Focus to once sea friend group.', 'resource/painting.md': 'Customer environment none trade.', 'resource/structure.md': 'Stuff return protect our bit reality.', 'resource/until.md': 'Growth industry region receive.', 'resource/significant.md': 'Long million fall throughout government tend.', 'resource/hospital.md': 'Quality certain fight want much body between.', 'resource/marriage.md': 'Foot specific mission.', 'for/hope.md': 'Whatever report wife fly close lot student.', 'for/poor.md': 'Explain claim police eye paper much when.', 'for/assume.md': 'Control yeah effect local economy worry.', 'for/couple.md': 'Floor both take indeed audience.', 'for/money.md': 'Join live next care material.', 'for/never.md': 'Me natural full.', 'for/situation.md': 'Show book instead hope lawyer.', 'for/north.md': 'Card level kind send loss growth.', 'for/hit.md': 'Minute wish above pass just later watch.', 'for/perhaps.md': 'Every professor sport unit rock bed.', 'project/individual.md': 'Tough safe machine small outside mention could must.', 'project/change.md': 'Century drug value.', 'project/home.md': 'Big decade edge feeling surface matter force student.', 'project/want.md': 'Region catch nation civil one Mr specific.', 'project/something.md': 'Major control three.', 'project/reality.md': 'Mouth including fine.', 'project/my.md': 'Fire point or success marriage write example.', 'project/issue.md': 'Former true career similar use visit machine.', 'project/surface.md': 'Cold reduce task life American act stage.', 'project/drug.md': 'Reason still field animal.', 'effort/morning.md': 'Policy quickly get capital smile.', 'effort/he.md': 'Thought view product interview explain.', 'effort/house.md': 'High hear thought according.', 'effort/church.md': 'Culture ask change focus.', 'effort/effect.md': 'Before suddenly who student could boy serve.', 'effort/price.md': 'Shoulder financial public reason home explain safe.', 'effort/company.md': 'Exactly treatment concern fly factor care drive.', 'effort/international.md': 'Rich take hear open.', 'effort/federal.md': 'Difference rate character by his blood this.', 'effort/computer.md': 'Lay financial article exactly.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/culture.md': 'Prevent north only miss cold.', 'by/family.md': 'Debate at office traditional stop great.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'bill/appear.md': 'Whole senior next stop yard national section.', 'bill/room.md': 'Able improve anything teacher media writer employee.', 'bill/citizen.md': 'Safe anyone major reach mother ground over leave.', 'bill/for.md': 'A several low detail.', 'bill/role.md': 'More light anything study hand power.', 'bill/set.md': 'Necessary century drive attack capital.', 'bill/generation.md': 'Stay could quality shake.', 'bill/drive.md': 'Situation we his.', 'bill/computer.md': 'Culture ahead change perhaps however audience.', 'bill/gas.md': 'Reveal attack and church.', 'color/sell.md': 'Mention although while boy turn.', 'color/throughout.md': 'She actually gun start.', 'color/management.md': 'Short serve beat increase than visit.', 'color/smile.md': 'His season employee husband.', 'color/wear.md': 'Share green measure sometimes.', 'color/official.md': 'Suddenly seat tend thus office action move.', 'color/admit.md': 'Each important clear.', 'color/treat.md': 'Tv outside attorney rich say same environment.', 'color/turn.md': 'Try drop old along.', 'color/sit.md': 'Including turn seem none computer.', 'build/together.md': 'Finally point only police artist.', 'build/rest.md': 'Author run let.', 'build/wall.md': 'Administration a week form side feeling.', 'build/none.md': 'Commercial stop page else.', 'build/explain.md': 'Join tend idea stand not option woman.', 'build/decision.md': 'Poor fund interesting bring.', 'build/beyond.md': 'Artist billion begin record anything none management practice.', 'build/dream.md': 'Decision suddenly prevent speak old power herself.', 'build/each.md': 'Able out key.', 'build/street.md': 'Knowledge specific technology before leave.', 'wrong/market.md': 'Realize key point whatever Democrat or say.', 'wrong/free.md': 'Deal even from mouth source.', 'wrong/sure.md': 'Similar him believe actually.', 'wrong/apply.md': 'Everybody office list service stock significant.', 'wrong/share.md': 'Painting every apply.', 'wrong/standard.md': 'Already place fund really.', 'wrong/might.md': 'Possible during claim view.', 'wrong/nation.md': 'About prove cold question race.', 'wrong/be.md': 'Land debate natural American.', 'wrong/suggest.md': 'Could environmental rather can us night.', 'Congress/remember.md': 'Purpose good policy line trade.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'industry/wrong.md': 'Floor race land those hard actually avoid property.', 'industry/book.md': 'Together state billion race beautiful how.', 'industry/car.md': 'Heart central eye thought painting government appear.', 'industry/cause.md': 'Time religious describe oil heart.', 'industry/feeling.md': 'Include memory strategy other statement imagine teach.', 'industry/small.md': 'Little third your season kind.', 'industry/heavy.md': 'Quality international window probably adult attention.', 'industry/election.md': 'Democrat often turn.', 'industry/possible.md': 'Structure high discover half dog half forward.', 'industry/fish.md': 'Much without in fight miss.', 'live/white.md': 'Whatever significant capital air about.', 'live/discuss.md': 'Hit result find miss culture heart clear task.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/own.md': 'Say small finish sing raise.', 'lot/seat.md': 'Method institution third political.', 'lot/wall.md': 'Each feel program size different kid.', 'lot/worry.md': 'Support moment maintain majority American rule rock.', 'lot/improve.md': 'Reason better difficult take.', 'lot/heart.md': 'Make let way.', 'lot/modern.md': 'Example first recently let.', 'lot/make.md': 'First eat data executive.', 'lot/check.md': 'Wall artist recent side approach.', 'lot/hotel.md': 'Technology town film nothing writer head from.', 'lot/perhaps.md': 'Main manage authority serious short.', 'drop/add.md': 'Fish work to individual.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/else.md': 'Fly candidate may so college.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/former.md': 'Brother college detail.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'central/several.md': 'Appear talk administration sort.', 'central/them.md': 'Unit huge call.', 'central/often.md': 'For nice after analysis series.', 'central/before.md': 'Account vote off police since.', 'central/commercial.md': 'Address country last teacher game compare.', 'central/these.md': 'Feeling rate first national.', 'central/tough.md': 'Party single media process statement forget.', 'central/crime.md': 'Hotel we five blue lawyer argue.', 'central/less.md': 'Guess environmental cover three late.', 'central/nice.md': 'Those religious audience case those.', 'civil/argue.md': 'Line culture seven six.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/ready.md': 'Central about ready information.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/question.md': 'Family evening its degree.', 'civil/gas.md': 'Talk why around necessary.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/central.md': 'Believe region their our whatever.', 'friend/oil.md': 'Little someone story put hundred able.', 'friend/discover.md': 'Someone city idea.', 'friend/month.md': 'Race walk people its Democrat sound.', 'friend/alone.md': 'Suffer concern choose participant work.', 'friend/myself.md': 'Truth simply memory alone plant large.', 'friend/note.md': 'Word end size enough.', 'friend/large.md': 'Tough glass per.', 'friend/wife.md': 'Sea investment many difference keep like improve.', 'friend/allow.md': 'Become personal own behavior sport.', 'friend/hand.md': 'Nation yourself final ground thus follow.', 'standard/late.md': 'Scientist people may story.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/level.md': 'Work around ask to.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/sound.md': 'Night national film next.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/easy.md': 'Myself must detail win.', 'standard/five.md': 'Lay would green generation season.', 'standard/analysis.md': 'While natural from staff option artist can.', 'community/book.md': 'Mr oil difficult dog.', 'community/else.md': 'Actually service thank state.', 'community/soldier.md': 'It lawyer cover job.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/cold.md': 'Election buy member alone school audience.', 'community/left.md': 'Picture let tell never.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/save.md': 'Thought hear home set employee early purpose.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/story.md': 'Anything song key first.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/bar.md': 'Among ago cover good.', 'education/evening.md': 'Give tonight sell over whole word care.', 'education/body.md': 'Note start bad part positive during.', 'education/total.md': 'Contain hit individual college month.', 'education/nature.md': 'Skin look fine policy special part.', 'education/really.md': 'Difference beyond cost but.', 'education/reason.md': 'Wrong increase investment deep near simply spring.', 'education/blood.md': 'North smile know.', 'education/imagine.md': 'Summer keep conference.', 'education/fish.md': 'Answer impact sense professor gun fast me.', 'education/article.md': 'Usually could bad attack customer couple represent.', 'lead/rest.md': 'Address half hit.', 'lead/speech.md': 'Maintain prepare indicate production surface.', 'lead/become.md': 'Building plant air something direction fall provide.', 'lead/stage.md': 'View main when Republican father plant.', 'lead/under.md': 'Test next education series.', 'lead/adult.md': 'Rule others especially institution total what law.', 'lead/which.md': 'Far task service radio reach morning accept.', 'lead/phone.md': 'Unit good including show stand.', 'lead/would.md': 'President still follow race analysis opportunity.', 'lead/trade.md': 'Success whatever environmental avoid father how although may.', 'why/show.md': 'Decade station development character movement.', 'why/data.md': 'Itself feeling fund mean.', 'why/more.md': 'Address music fish team national tough.', 'why/debate.md': 'Meeting wind medical can city face cost.', 'why/something.md': 'Everybody bed economic own least peace executive.', 'why/most.md': 'Agreement station room name.', 'why/spring.md': 'Fine according mission against.', 'why/phone.md': 'By near next teacher be degree although.', 'why/full.md': 'Yard like phone catch on attention your.', 'why/stuff.md': 'Cup everybody open book he decade.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/serve.md': 'Want exist bank book.', 'ten/nature.md': 'Eight own hot first success.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/rock.md': 'Method wall when book agency.', 'rule/hear.md': 'History event character everybody paper machine little billion.', 'rule/thing.md': 'Trial produce despite water range television.', 'rule/feel.md': 'Soon give never future difference.', 'rule/system.md': 'Bill article station despite.', 'rule/produce.md': 'Yes method sense.', 'rule/eye.md': 'Finally this team yet throughout.', 'rule/nation.md': 'Radio entire ago behavior prevent response ten according.', 'rule/thousand.md': 'Anything help military with run.', 'rule/goal.md': 'Inside firm without.', 'rule/perhaps.md': 'Back election leave.'}
print(len(set(result)), len(set(expected)))
count = 0
print("length of result", len(result))
print("length of expected", len(expected))
for y in result:
    if y not in expected:
        count += 1
        print(f"{y}:{result[y]} IS EXTRA FILE")
        print(count)

```

---

## Post #153

- **Author**: 21f2000709
- **Posted on**: 2025-02-12T11:18:23.620Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/153

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png) s.anand:

> A *sample* evaluation script for Project 1 tasks A1-A10 is available at [tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub](https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1)

Sir there is an error in the evaluation script for task A1, url - <https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py> doesn’t exist,  
instead this should - <https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py>

---

## Post #155

- **Author**: carlton
- **Posted on**: 2025-02-12T12:54:37.329Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/155

[@23f2001978](/u/23f2001978)

That error is usually if you are using the wrong endpoint (ie. using open ai libraries instead of sending requests to aiproxy).

Without seeing the request its hard to tell you what the cause of the error is.

Kind regards

---

## Post #156

- **Author**: carlton
- **Posted on**: 2025-02-12T13:20:19.960Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/156

[@21f2000709](/u/21f2000709) [@23f1002382](/u/23f1002382)

B10 → Create a service that creates a specified endpoint that receives a CSV and returns a JSON data . Where the JSON is expected, whether in the response body of the endpoint , or in a file will be specified by the task master ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

Kind regards

---

## Post #157

- **Author**: 22f3002771
- **Posted on**: 2025-02-12T14:02:08.980Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/157

hi [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
for A2 i am getting this particular error and i don’t know what i am doing wrong in this  

[![Screenshot from 2025-02-12 19-31-47](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/6/463f25f29e9ac0e51e43914eb00cef2e89341c90_2_690x259.png)

Screenshot from 2025-02-12 19-31-471501×564 44.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/6/463f25f29e9ac0e51e43914eb00cef2e89341c90.png "Screenshot from 2025-02-12 19-31-47")

---

## Post #159

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T14:07:21.156Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/159

issue with evaluate.py , post the code snippet in task a2, where it calculates the result and checks with expected.

---

## Post #160

- **Author**: 22f3002771
- **Posted on**: 2025-02-12T14:16:26.408Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/160

you mean screenshot of evaluate.py file?  

[![Screenshot from 2025-02-12 20-21-56](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/8/18e7419bec3e953904b029c887a657f57b376377_2_690x259.png)

Screenshot from 2025-02-12 20-21-561501×564 61.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/8/18e7419bec3e953904b029c887a657f57b376377.png "Screenshot from 2025-02-12 20-21-56")

---

## Post #161

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T14:55:36.830Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/161

running in docker?  
////////////////////////////

---

## Post #162

- **Author**: 22f3002771
- **Posted on**: 2025-02-12T15:01:11.724Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/162

Yes, I commented out check=True to see the error

---

## Post #163

- **Author**: 23f2003413
- **Posted on**: 2025-02-12T15:56:31.053Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/163

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
could you please help me out on how to start with TDS Project-1, as I am stuck at the moment and don’t know where to start from. This project is very much unfamiliar for me and I need some guidance on how to start with it. It would be really great if you could provide some help through resources/materials/videos and help me complete the project. Thanks in advance!

---

## Post #165

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T16:46:18.918Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/165

then im not sure exactly wait lemme check

---

## Post #166

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T16:49:41.628Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/166

issue with evaluate py, specifically , how it formats the file, maybe shell=True should be uncommented if commented out. then im not sure. Im not in composing docker files yet

---

## Post #167

- **Author**: AnvithaV
- **Posted on**: 2025-02-12T17:08:28.279Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/167

Could anyone please help me with the project… I am trying to do it but I’m always getting errors even while starting.

---

## Post #168

- **Author**: 21f2000709
- **Posted on**: 2025-02-12T17:16:22.873Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/168

My final docker image size is coming 1.25 gb, I am using the ubuntu base image as I thought it would be appropriate given the tasks. Is it ok with that size?

PS - Also I would be running out of token if I need to test again with some other base image now.  
[@carlton](/u/carlton)

---

## Post #169

- **Author**: 21f2000709
- **Posted on**: 2025-02-12T17:21:35.526Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/169

Go through the week 1-3 assignments once, you would be good to go with Phase A tasks.

[@23f2003413](/u/23f2003413) [@AnvithaV](/u/anvithav)

---

## Post #170

- **Author**: carlton
- **Posted on**: 2025-02-12T17:29:12.353Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/170

You do not need the whole of ubuntu!

Just python and uv

More like 128mb image.

Please watch Tues week 5 session 1

Kind regards

---

## Post #171

- **Author**: 22f3001777
- **Posted on**: 2025-02-12T17:38:21.482Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/171

Will there be more live sessions on project ?

[@carlton](/u/carlton)

---

## Post #172

- **Author**: 21f2000709
- **Posted on**: 2025-02-12T17:53:19.068Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/172

I could pull it down to 610 mb, using python:3.9-slim now, but there are some essential libraries that is needed which is taking up the space…will it be ok? I mean installing on the go with uv might lead to timeout during evaluation…

---

## Post #173

- **Author**: ShahbaazSingh
- **Posted on**: 2025-02-12T18:30:50.906Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/173

How did you corrected it ?

---

## Post #174

- **Author**: 21f2000709
- **Posted on**: 2025-02-12T19:09:36.761Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/174

I tried cutting it down further but it is affecting the functionality, this is the best I can do, i.e., 610 mb

---

## Post #175

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T19:33:11.401Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/175

could you help later, when i need to construct docker image, via gmeet? PLEASE

---

## Post #176

- **Author**: 22f3001315
- **Posted on**: 2025-02-12T20:00:07.871Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/176

ANY SUGGESTIONS (just one digit away) ::

```
import easyocr
from pathlib import Path
import re

def extract_credit_card_number(input_image: str, output_file: str):
    
    input_path = Path(f".{input_image}")
    output_path = Path(f".{output_file}")

    if not input_path.exists():
        raise ValueError(f"Image file {input_path} does not exist.")

    # Step 1: Use OCR to extract text from the image
    reader = easyocr.Reader(['en'])
    try:
        result = reader.readtext(str(input_path))
    except Exception as e:
        raise ValueError(f"OCR processing failed: {str(e)}")

    # Combine all extracted text into a single string
    extracted_text = " ".join([text for (_, text, _) in result])

    # Step 2: Use the LLM to refine the extracted text and extract the credit card number
    prompt = f"""
    The following text was extracted from an image. It may contain a credit card number. 
    Extract the credit card number and return only the number without spaces or dashes. 
    If no credit card number is found, return "None".

    Extracted text: {extracted_text}
    """
    try:
        response = chat_completion(prompt)
        card_number = response.get("choices", [])[0].get("message", {}).get("content", "").strip()

        # Validate the card number (basic check for 16 digits)
        if card_number.lower() == "none" or not card_number.isdigit() or len(card_number) != 16:
            raise ValueError("No valid credit card number found in the image.")

        # Write the card number to the output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(card_number)

        return f"A8 Completed: Credit card number extracted and written to {output_file}"
    except Exception as e:
        raise ValueError(f"Failed to process text with LLM: {str(e)}")

```

```
 /data/credit-card.txt
⚠️ EXPECTED:
4026399336539356
⚠️ RESULT:
4026399338539356

```

---

## Post #177

- **Author**: 23f1002382
- **Posted on**: 2025-02-12T20:31:46.779Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/177

<Response [200]>  
{‘id’: ‘chatcmpl-B0De8V66WZAucAweJe6e32BWSLnpT’, ‘object’: ‘chat.completion’, ‘created’: 1739392156, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: “I’m sorry, but I can’t assist with that.”, ‘refusal’: None}, ‘logprobs’: None, ‘finish\_reason’: ‘stop’}], ‘usage’: {‘prompt\_tokens’: 874, ‘completion\_tokens’: 11, ‘total\_tokens’: 885, ‘prompt\_tokens\_details’: {‘cached\_tokens’: 0, ‘audio\_tokens’: 0}, ‘completion\_tokens\_details’: {‘reasoning\_tokens’: 0, ‘audio\_tokens’: 0, ‘accepted\_prediction\_tokens’: 0, ‘rejected\_prediction\_tokens’: 0}}, ‘service\_tier’: ‘default’, ‘system\_fingerprint’: ‘fp\_bd83329f63’, ‘monthlyCost’: 0.048128640000000014, ‘cost’: 0.0026880000000000003, ‘monthlyRequests’: 51}

```
def query_gpt_image(image_path: str, task: str):
    print("🔍 Image Path:", image_path)
    image_format = image_path.split(".")[-1]
    with open(image_path, "rb") as file:
        image_data = base64.b64encode(file.read()).decode("utf-8")
    response = requests.post(
        "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {"APIKEY"}",
                "Content-Type": "application/json"},
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": task},
                    {
                    "type": "image_url",
                    "image_url": { "url": f"data:image/{image_format};base64,{image_data}" }
                    }
                ]
                }
            ]
            }
                     )
    response.raise_for_status()
    print(response)
    print(response.json())
    result = response.json() 
response = query_gpt_image("data/credit_card.png","Extract the credit card number from image")

```

Why is this not working?  
EDIT: Requires prompt engineering as “credit card” is sensitive information ![:roll_eyes:](https://emoji.discourse-cdn.com/google/roll_eyes.png?v=12 ":roll_eyes:")![:roll_eyes:](https://emoji.discourse-cdn.com/google/roll_eyes.png?v=12 ":roll_eyes:")

<Response [200]>  
{‘id’: ‘chatcmpl-B0Dlie1ZIS68PZBCT0XJKhLKbyPAC’, ‘object’: ‘chat.completion’, ‘created’: 1739392626, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: ‘The numbers extracted from the image are:\n\n- 3009 1429 5211 59\n- 09/29\n- 113’, ‘refusal’: None}, ‘logprobs’: None, ‘finish\_reason’: ‘stop’}], ‘usage’: {‘prompt\_tokens’: 871, ‘completion\_tokens’: 31, ‘total\_tokens’: 902, ‘prompt\_tokens\_details’: {‘cached\_tokens’: 0, ‘audio\_tokens’: 0}, ‘completion\_tokens\_details’: {‘reasoning\_tokens’: 0, ‘audio\_tokens’: 0, ‘accepted\_prediction\_tokens’: 0, ‘rejected\_prediction\_tokens’: 0}}, ‘service\_tier’: ‘default’, ‘system\_fingerprint’: ‘fp\_bd83329f63’, ‘monthlyCost’: 0.05092764000000002, ‘cost’: 0.002799, ‘monthlyRequests’: 52}

```
response = query_gpt_image("data/credit_card.png","Extract number from image")

```

---

## Post #179

- **Author**: Rishabh2
- **Posted on**: 2025-02-13T02:36:19.536Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/179

Sir in main.py file I’m defining task with different variables . But in evaluate.py tasks are defined by different variables to test and when I’m testing it using python evaluate.py it returns unsuccessful . I’m testing all my tasks of main.py with Postman it returns successful.  
My query is that how the tasks get evaluated and do i need to change my variables in main.py ? And what are the other things i have to change.  
Also plss update evaluate.py fie with phase B tasks

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

---

## Post #180

- **Author**: carlton
- **Posted on**: 2025-02-13T03:29:31.245Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/180

[@22f3001777](/u/22f3001777)

Yes there will be one more session today (13th Feb) at usual time 8pm to 10pm

Kind regards

---

## Post #181

- **Author**: trebhuvansb
- **Posted on**: 2025-02-13T04:09:50.378Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/181

Hi instructors and TAs,  
For the different tasks in Phase B, I don’t have a clear idea of what type of a response you expect.

eg.

* Run a SQL query on a SQLite or DuckDB database & Extract data from (i.e. scrape) a website & Transcribe audio from an MP3 file - Do you want the query’s response on an output file like A10? or as a response?

I understand that these are broad problems you except us to solve, but it would be helpful to know what type of response you would require.

Thanks,  
Trebhuvan

---

## Post #182

- **Author**: 22f3001307
- **Posted on**: 2025-02-13T04:45:34.403Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/182

Hi,  
Pls tell us how to use evaluate.py script to check our codes

---

## Post #183

- **Author**: carlton
- **Posted on**: 2025-02-13T04:49:57.160Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/183

Output specifications will be detailed in the “task” sent to the endpoint.

Phase B is meant to be vague because if you can solve it, without an elaborate and gratuitous use of gpt function calling, then you can actually solve *all tasks using the same function* !

Kind regards

---

## Post #184

- **Author**: 21f2000709
- **Posted on**: 2025-02-13T04:54:35.243Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/184

Okay sure!! Ping me when you require to generate…

---

## Post #185

- **Author**: 22f3002248
- **Posted on**: 2025-02-13T05:05:17.862Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/185

Hello sir,  
Is yesterday’s session not uploaded to YouTube yet ?  
I couldn’t find it in calendar either… It will be very helpful if you (or anyone else) could provide yesterday session’s recording’s link…

---

## Post #186

- **Author**: 21f2000709
- **Posted on**: 2025-02-13T05:14:41.733Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/186

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png) 21f2000709:

> I tried cutting it down further but it is affecting the functionality, this is the best I can do, i.e., 610 mb

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

will it be ok? Actually I developed it in a way that require some of the essential dependencies and at this point of time it would be dangerous to alter the way of handling it as I am running short of AIProxy Token credits.

Earlier when I asked this:

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png) 21f2000709:

> Any tentative size cutoff for the docker image?

I could have altered my way of handling dependencies but at that point of time there was no clear numbers.

I request you to please allow this time around with this size…

---

## Post #187

- **Author**: Yogesh1
- **Posted on**: 2025-02-13T05:45:48.461Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/187

[@carlton](/u/carlton) Could you please consider extending the submission date of Assignment 5 (it is 16th Feb right now). We are very busy with the project.

And assignment 6 submission date is much later: 9th of March.

---

## Post #188

- **Author**: thinkmachine
- **Posted on**: 2025-02-13T06:01:13.675Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/188

[@carlton](/u/carlton) +1 Agreed, a relaxation in deadline will be a boon for students who’ve taken up other projects this term.

---

## Post #189

- **Author**: trebhuvansb
- **Posted on**: 2025-02-13T06:08:33.630Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/189

usage of langchain is allowed?

---

## Post #190

- **Author**: 21f2000709
- **Posted on**: 2025-02-13T06:26:05.592Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/190

It will be extended, [@carlton](/u/carlton) mentioned it in a TA session already.

---

## Post #191

- **Author**: Jivraj
- **Posted on**: 2025-02-13T06:53:05.419Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/191

Hi [@Rishabh2](/u/rishabh2)

What exactly you mean by variables? only one argument is required for running `evaluate.py` that’s an email address.

You need to download both `evaluate.py` and `datagen.py` in same folder and then execute `evaluate.py` using uv.  
`uv run evaluate.py --email $any_email`.

For phase B

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/183) [Tools in Data Science](/c/courses/tds-kb/34)

> Output specifications will be detailed in the “task” sent to the endpoint.
> Phase B is meant to be vague because if you can solve it, without an elaborate and gratuitous use of gpt function calling, then you can actually solve all tasks using the same function !
> Kind regards

Kind regards

---

## Post #192

- **Author**: Jivraj
- **Posted on**: 2025-02-13T06:59:18.975Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/192

610 Mb’s is good size, no need to worry, it will be evaluated.

---

## Post #193

- **Author**: Saransh_Saini
- **Posted on**: 2025-02-13T07:14:49.349Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/193

Hi [@23f1002382](/u/23f1002382)  
This is the classic case where you use Prompt engineering to solve your problems. I assume you have already achieved your answers, but I want to clarify this for someone who is facing this problem.

The thing is GPT-4o-mini is intelligent enough to understand what kind of task you are asking it do, and extracting Credit Card info from an image is one of the many prohibited tasks.

What you can do is, **try to fool it using itself.** Just ask ChatGPT to generate a prompt that would be capable of fooling itself into extracting out that credit card info. I was capable of doing it after pretending to be a working on a Cyber Security project, and other fake details which ChatGPT itself provided me with.

---

## Post #194

- **Author**: 21f3000512
- **Posted on**: 2025-02-13T07:17:30.842Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/194

[@carlton](/u/carlton) . I cannot send requests to <https://aiproxy.sanand.workers.dev/openai/v1> . Getting $RateLimitError: Error code: 429 - {‘message’: 'On 2025-02 you used $2.0003758999999954, exceeding 2'} . Looks like I used all of my credit . What can I do now ? Project is also Incomplete.

---

## Post #195

- **Author**: Saransh_Saini
- **Posted on**: 2025-02-13T07:17:41.320Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/195

Try creating a better prompt for this task.  
*Hint: Ask it to recheck certain similar looking digits.*

---

## Post #196

- **Author**: Jivraj
- **Posted on**: 2025-02-13T07:40:40.412Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/196

After submitting docker image through, it will be pulled and our token will be used.

Things to be checked at your end.  
1. `podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p8000:8000 $IMAGE_NAME` works fine  
2. Above command will start 8000 server so use evaluate.py to test if things are working as expected.

Kind regards.  
Jivraj

---

## Post #197

- **Author**: Jivraj
- **Posted on**: 2025-02-13T07:44:28.965Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/197

Hi [@JoelJeffrey](/u/joeljeffrey)

What you did wrong and how did you correct it?

---

## Post #198

- **Author**: JoelJeffrey
- **Posted on**: 2025-02-13T07:47:38.549Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/198

I think there was something wrong with the way the code was getting inputs (keys). I just rewrote that part and it worked

---

## Post #199

- **Author**: Jivraj
- **Posted on**: 2025-02-13T07:50:10.661Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/199

Hi [@22f3001307](/u/22f3001307)

Provide required write permissions to `/data` folder. We will also discuss this issue regarding permissions in initial part of today’s session.

Kind regards

---

## Post #201

- **Author**: 22f3002248
- **Posted on**: 2025-02-13T07:55:57.725Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/201

Hello sir,  
Is yesterday’s session not uploaded to YouTube yet ?  
I couldn’t find it in calendar either…

---

## Post #202

- **Author**: 21f2000709
- **Posted on**: 2025-02-13T08:00:18.511Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/202

Command to run the image in the docs, seemed to have some error,

![Screenshot 2025-02-13 at 1.31.01 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/e/0e724c8ad15be3f5051e9abaf562830a2a1217ec.png)

The command:  
`podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000`

gives the error:  
`crun: executable file `-e` not found in $PATH: No such file or directory: OCI runtime attempted to invoke a command that was not found`

However the correct command seems to be:  
`podman run -e AIPROXY_TOKEN="$AIPROXY_TOKEN" -p 8000:8000 $IMAGE_NAME`

This works totally fine.

![Screenshot 2025-02-13 at 1.33.21 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/f/cf9060b0880a8d94e57a14ce300b4dcc714ed117.png)

[@Jivraj](/u/jivraj)

---

## Post #203

- **Author**: 23f1002382
- **Posted on**: 2025-02-13T08:10:36.247Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/203

nvm i can laugh nw xD

---

## Post #204

- **Author**: 21f2000709
- **Posted on**: 2025-02-13T08:25:27.022Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/204

One final question [@Jivraj](/u/jivraj) [@carlton](/u/carlton) , will our projects be evaluated with our `AIPROXY_TOKEN` or a different one.

Because my project is done but for evaluation if my `AIPROXY_TOKEN` is used, it might be out of credits.

---

## Post #205

- **Author**: Yogesh1
- **Posted on**: 2025-02-13T08:36:10.341Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/205

Thanks. Do you know the new date?

---

## Post #206

- **Author**: 21f2000709
- **Posted on**: 2025-02-13T08:57:25.731Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/206

That wasn’t said, but it was not this weekend for sure.

---

## Post #207

- **Author**: 23f2001975
- **Posted on**: 2025-02-13T09:14:14.569Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/207

my automation is happening and prompt distribution too but it just isnt able to pass any test after 1st in evaluation.py did someone else face same problem if yes then how to solve it please help

---

## Post #208

- **Author**: 22f3001315
- **Posted on**: 2025-02-13T09:24:19.052Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/208

actually that easyocr is directly sending the clear text(no confusion) to llm and llm is just extracting the exact numbers from it .

---

## Post #212

- **Author**: 23f2001975
- **Posted on**: 2025-02-13T10:04:26.644Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/212

[quote=“23f2001975, post:211, topic:164277, full:true”]  
[@s.anand](/u/s.anand) [@carlton](/u/carlton)  
While running the evaluation.py i am facing several issues because my output isnt strictly adhering sometimes to it will the checking be on such a basis only

for example in A3  
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") EXPECTED:  
129  
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") RESULT:  
“129”  
this is the error i get while it is the function in eval.py checking problem as it gets response as text and doesnt strip (“”)

Please guide what should i do

---

## Post #213

- **Author**: Jivraj
- **Posted on**: 2025-02-13T10:18:32.032Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/213

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png) 21f2000709:

> podman run -e AIPROXY\_TOKEN=“$AIPROXY\_TOKEN” -p 8000:8000 $IMAGE\_NAME

Yes this is correct command, we will update in project page.

---

## Post #215

- **Author**: Jivraj
- **Posted on**: 2025-02-13T10:22:50.807Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/215

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png)
[Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/196) [Tools in Data Science](/c/courses/tds-kb/34)

> After submitting docker image through, it will be pulled and our token will be used.
> Things to be checked at your end.
> 1. podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p8000:8000 $IMAGE\_NAME works fine
> 2. Above command will start 8000 server so use evaluate.py to test if things are working as expected.
> Kind regards.
> Jivraj

---

## Post #216

- **Author**: vikramjncasr
- **Posted on**: 2025-02-13T10:25:17.421Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/216

[@Jivraj](/u/jivraj) sir I get this error  
but my app.py is able to get the server running on localhost and not on 0.0.0.  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/d/ed519f25f712a007f48e1e2f3cf5cf7f946271cb.png)

image1014×190 18.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/d/ed519f25f712a007f48e1e2f3cf5cf7f946271cb.png "image")

  
could you please help ?

---

## Post #217

- **Author**: 22f3001307
- **Posted on**: 2025-02-13T10:27:23.392Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/217

When i am trying evaluate the code, I am getting the following error

```
Traceback (most recent call last):
  File "/var/folders/rj/z_3b8hl51558519w90k5hp600000gn/T/evaluateyea70I.py", line 20, in <module>
    from datagen import (
    ...<9 lines>...
    )
ModuleNotFoundError: No module named 'datagen'

```

can someone tell me what i should do?  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

## Post #218

- **Author**: Jivraj
- **Posted on**: 2025-02-13T10:28:13.927Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/218

[@22f3001307](/u/22f3001307)  
Install datagen.py in the same folder from where you are executing evaluate.py.

[@vikramjncasr](/u/vikramjncasr) Check how you are executing, use uv or else install required modules globally  
Kind regards

---

## Post #219

- **Author**: 22f3001307
- **Posted on**: 2025-02-13T10:33:05.878Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/219

Sir,  
the folder already exists in that folder  
besides, I am using `OPENAI_API_KEY=$AIPROXY_TOKEN uv run https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/evaluate.py` from Anand sir’s page to run the code in my system

---

## Post #220

- **Author**: vikramjncasr
- **Posted on**: 2025-02-13T10:39:36.193Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/220

Sir would the belowformat be ok when you evaluate ?  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/8/58c6872accc838dcec5fda23f4290f5e284dde1e.png)

image985×211 24.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/8/58c6872accc838dcec5fda23f4290f5e284dde1e.png "image")

---

## Post #221

- **Author**: vikramjncasr
- **Posted on**: 2025-02-13T10:40:54.014Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/221

But when I use podman i keep getting errror.

---

## Post #222

- **Author**: 24f2006061
- **Posted on**: 2025-02-13T10:58:35.935Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/222

Hello,

Can anyone please reset my AIProxy limit. I am getting this error, {“detail”:“Agent error: 429 Client Error: Too Many Requests for url: <https://aiproxy.sanand.workers.dev/openai/v1/chat/completions>”}  
Thank you.

---

## Post #223

- **Author**: 22f3002771
- **Posted on**: 2025-02-13T11:09:48.608Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/223

i am getting unauthorized error in A9 again and again, i have pasted my code if someone can help please look into this.

```
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "numpy",
#   "httpx",
#   "fastapi",
# ]
# ///


import httpx
import numpy as np
import datetime
import os

from fastapi import HTTPException


now = datetime.datetime.now()

OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"


# async def get_similarity_from_embeddings(emb1: list[float], emb2: list[float]) -> float:
def get_similarity_from_embeddings(emb1: list[float], emb2: list[float]) -> float:
    # """Calculate cosine similarity between two texts."""
    # emb1 = await embed(text1)
    # emb2 = await embed(text2)
    return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))


# async def embed_list(text_list: list[str]) -> list[float]:
async def embed_list(text_list: list[str]) -> list[float]:
    OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
    OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"
    """Get embedding vector for text using OpenAI's API."""
    try:
        async with httpx.AsyncClient() as client:
            # with httpx.AsyncClient() as client:
            response = await client.post(
                # response = httpx.post(
                OPENAI_API_URL,
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                
                json={"model": "text-embedding-3-small", "input": text_list},
            )
        # print(f'{response.json()["data"][0]["embedding"]}')
        emb_list = [emb["embedding"] for emb in response.json()["data"]]
        print(f"Number of embeddings returned = {len(emb_list)}")
        return emb_list

    except KeyError as e:
        print(f"INSIDE EMBED_LIST IN A9. KeyError occurred while querying GPT: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        print(f"INSIDE EMBED_LIST IN A9. General Error while querying gpt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


def most_similar(embeddings):
    # Extract the phrases and their corresponding embeddings
    phrases = list(embeddings.keys())
    emb_values = list(embeddings.values())

    # Initialize variables to track the maximum similarity
    max_similarity = -1  # Start with the smallest possible similarity value
    most_similar_pair = None

    # Compute cosine similarity between each pair of embeddings
    for i in range(len(emb_values)):
        for j in range(i + 1, len(emb_values)):  # Avoid repeating pairs
            similarity = get_similarity_from_embeddings(emb_values[i], emb_values[j])
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_pair = (phrases[i], phrases[j])

    return most_similar_pair


# async def get_similar_comments(input_file_path: str, output_file_path: str):
async def get_similar_comments(input_file_path: str, output_file_path: str):
    print(f"Reading the input file: {input_file_path}")
    with open(input_file_path, "r") as file:
        comments = file.readlines()

    print(f"Embedding the comments")
    # embeddings = await embed_list(comments)
    embeddings = await embed_list(comments)
    embed_dict = dict(zip(comments, embeddings))
    most_similar_pair = most_similar(embed_dict)
    print(f"Most similar comments: {most_similar_pair}")

    with open(output_file_path, "w") as file:
        for comment in most_similar_pair:
            file.write(f"{comment.strip()}\n")
        # file.write(f"Most similar comments: {most_similar_pair}")


if __name__ == "__main__":
    # import asyncio

    input_file_path = "/data/comments.txt"
    output_file_path = "/data/similar_comments.txt"
    # asyncio.run(get_similar_comments(input_file_path, output_file_path))
    get_similar_comments(input_file_path, output_file_path)

```

---

## Post #224

- **Author**: 23f2004752
- **Posted on**: 2025-02-13T11:30:20.720Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/224

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir can you take my doubt in today’s session please , i have successfully run docker server but endpoints are not working…  

[![Screenshot 2025-02-13 165912](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f3f203d53c41f1d3c7c214f4904ca32579085bea_2_690x368.png)

Screenshot 2025-02-13 1659121917×1024 124 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/3/f3f203d53c41f1d3c7c214f4904ca32579085bea.png "Screenshot 2025-02-13 165912")

  
If anyone have knowledge about this , please help

---

## Post #225

- **Author**: Adithya
- **Posted on**: 2025-02-13T11:32:12.216Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/225

How did u resolve the issue? [@JoelJeffrey](/u/joeljeffrey)

---

## Post #226

- **Author**: Adithya
- **Posted on**: 2025-02-13T11:38:28.558Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/226

I am also facing the same issue.  
Evaluation Output:

```
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"

🔴 A9 failed: 'data'

❌ A9 FAILED

```

I sense ‘Authentication Problem’ happens only with the evaluation script, as the curl requests seems to work fine.

```
INFO:httpx:HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
INFO:     127.0.0.1:60849 - "POST /run?task=%60%2Fdata%2Fcomments.txt%20contains%20a%20list%20of%20comments,%20one%20per%20line.%20Using%20embeddings,%20find%20the%20most%20similar%20pair%20of%20comments%20and%20write%20them%20to%20%2Fdata%2Fcomments-similar.txt,%20one%20per%20line HTTP/1.1" 200 OK

```

Any views? [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #227

- **Author**: vidushi
- **Posted on**: 2025-02-13T12:36:04.971Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/227

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) Sir i keep getting this error  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/c/acf1856ac9b092f16e614440286674227fb05f45.png)

image671×109 8.64 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/c/acf1856ac9b092f16e614440286674227fb05f45.png "image")

  
even though i have downloaded the packages globally and tried installing them by making a venv but nothing seems to work please help

---

## Post #228

- **Author**: Udipth
- **Posted on**: 2025-02-13T12:56:58.706Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/228

what is the base url?

---

## Post #229

- **Author**: 23f1002382
- **Posted on**: 2025-02-13T13:16:47.743Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/229

use your api key guys

---

## Post #230

- **Author**: 22f3002771
- **Posted on**: 2025-02-13T13:17:52.970Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/230

we are using that only bro, only for A9 it says unauthorized

---

## Post #231

- **Author**: 23f1002382
- **Posted on**: 2025-02-13T13:18:10.933Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/231

network mapping or something, even im working that out

---

## Post #232

- **Author**: AnvithaV
- **Posted on**: 2025-02-13T13:18:26.065Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/232

Even i am facing the same problem. I am unable to resolve it ,i tried many ways.  
could anyone please help

---

## Post #233

- **Author**: 23f1002382
- **Posted on**: 2025-02-13T13:20:38.830Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/233

2 ways, try command line package installing, or inside venv, try which python,etc and make paths reconcile, or inside venv, uv pip install , if that doesn’t work, inside venv pip install

---

## Post #234

- **Author**: 23f2004752
- **Posted on**: 2025-02-13T13:37:48.723Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/234

thanks , already it work out

---

## Post #236

- **Author**: vikramjncasr
- **Posted on**: 2025-02-13T15:44:57.509Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/236

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir please help

When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?  
needs sudo permission all the time…  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/2/529a3326ad0a3a4a60a7c95b080336814e487f6c_2_690x62.png)

image1368×124 19.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/2/529a3326ad0a3a4a60a7c95b080336814e487f6c.png "image")

---

## Post #237

- **Author**: huzaifa
- **Posted on**: 2025-02-13T15:58:57.713Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/237

Hello Sir [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
What are implications on missing the project 1.  
Due to some personal reasons I wasn’t able to start any work on my project 1. It seems difficult for me to complete it.  
Could you please tell what will be the implications of missing it. Will I in anyway be able to cover up and pass in the subject doing future assignments and projects?

Thank you

PS: This isn’t any request to extend dates. I accept my fault and respect the dates provided by the team.

---

## Post #238

- **Author**: 23f2001286
- **Posted on**: 2025-02-13T16:55:25.125Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/238

Sir I haven’t initaiated the podman earlier.  
Now when i try to use podman using the wsl via the code “sudo apt install -y podman” it is asking for the password…  
The problem is:

1. I haven’t set any password for podman earlier.
2. Though it is asking for password but it is not taking any input.(ie I am unable type anything there).  
   what should I am supposed to do…  

   [![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/3/d36db27ac5478d6c2d5fee2e15c56e2068836c20_2_690x153.png)

   image1612×359 21.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/3/d36db27ac5478d6c2d5fee2e15c56e2068836c20.png "image")

---

## Post #239

- **Author**: Vihaanv07
- **Posted on**: 2025-02-13T17:52:50.211Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/239

[@s.anand](/u/s.anand) [@Jivraj](/u/jivraj) I think the evaluation.py test case is broken for A8 because I can manually see more folders and markdown files than the expected case output of A8 evaluation. And also is there any evaluation file for Part B

---

## Post #240

- **Author**: 23f2004094
- **Posted on**: 2025-02-13T18:04:07.546Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/240

password are not visible in wsl when typed, just type and enter if it matches, the process will continue

---

## Post #241

- **Author**: 22f1000376
- **Posted on**: 2025-02-13T18:22:04.034Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/241

Sir If possible please extend the Project deadline.

---

## Post #242

- **Author**: 23f3004024
- **Posted on**: 2025-02-13T19:01:28.625Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/242

same error the execution is correct but format.md file is not modified with correct markdown format

---

## Post #243

- **Author**: 23f2003413
- **Posted on**: 2025-02-13T19:53:34.059Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/243

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
can u please upload the video that was recorded on 12th Feb, as I am able to view only the video that was last recorded on 11th Feb (3 hrs 57 mins video). As I am doing the project completely from the recorded videos, please post those videos in youtube at the earliest.

---

## Post #244

- **Author**: Jivraj
- **Posted on**: 2025-02-13T20:43:28.497Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/244

Hi [@23f2003413](/u/23f2003413)  
Because of some technical issues we could not record 12 Feb session. That was doubt clearing session regrading project1.

Kind regards

---

## Post #245

- **Author**: 23f2004752
- **Posted on**: 2025-02-14T00:36:17.755Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/245

Can we submit project number of times before deadline…

---

## Post #246

- **Author**: 23f2001286
- **Posted on**: 2025-02-14T02:49:04.476Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/246

thanks for you feedbacak I have figured it out! Thanks it means a lot…

---

## Post #247

- **Author**: 23f2001286
- **Posted on**: 2025-02-14T03:05:23.382Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/247

A silly Doubt though but still a doubt!  
Could we create an image first of our project in initial stage(ie the my “app.py” is not completely ready) but I have build an docker image including the app.py and other dependencies.  
Should I give the same url now and then carry on updating the app.py  
Or, Should first complete and then upload in the form!

plz reply!!

---

## Post #248

- **Author**: 23f2001305
- **Posted on**: 2025-02-14T05:30:00.714Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/248

Can you send the link for the video on 11th Feb?

---

## Post #249

- **Author**: 24f2003130
- **Posted on**: 2025-02-14T05:49:41.750Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/249

How did you resolve the file cannot be found error?

---

## Post #250

- **Author**: 23f1002279
- **Posted on**: 2025-02-14T06:55:15.716Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/250

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/c/5c040c4323f2d2dfbeb3c76334f44adc7a59343f.png)

image872×550 16.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/c/5c040c4323f2d2dfbeb3c76334f44adc7a59343f.png "image")

  
pls help with this error

---

## Post #251

- **Author**: sharma_abhay
- **Posted on**: 2025-02-14T07:01:23.751Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/251

Sir, could you please mention the title of youtube videos in which the project session are covered?

---

## Post #252

- **Author**: 23f2005419
- **Posted on**: 2025-02-14T07:18:15.478Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/252

Hi,

When yesterday’s recorded video will be uploaded in youtube?

---

## Post #253

- **Author**: 23f2003413
- **Posted on**: 2025-02-14T07:34:01.905Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/253

Thanks for the prompt reply [@Jivraj](/u/jivraj) . I have done the project setup till whatever was covered on the 11th Feb session. I am not able to proceed further as I have no clue on how to work on this. Can you please help me out as it would mean a lot.

---

## Post #254

- **Author**: 23f1002279
- **Posted on**: 2025-02-14T07:39:06.932Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/254

[@carlton](/u/carlton) [@23f1002382](/u/23f1002382)

---

## Post #255

- **Author**: 23f2003413
- **Posted on**: 2025-02-14T07:40:07.303Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/255

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b990ffaadbfcbad12d865c514f3d6b48e5bc7cf2.jpeg "2025-02-11 Week 5 - Session 1 - TDS Jan 25")](https://www.youtube.com/watch?v=jXj6bqy4R4c)

---

## Post #256

- **Author**: carlton
- **Posted on**: 2025-02-14T07:40:32.531Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/256

Are you subscribed to the TDS channel? If you were it would notify you immediately when it was uploaded. (10am this morning).

Please subscribe to the channel. It was also on the main page for TDS.  
<https://tds.s-anand.net/#/README>

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/5/85553e6b4edcc2dda60afe0f9f82c7f3dbf31e04.png)
[YouTube](https://www.youtube.com/@se-lr5ff)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/5/05fae46322d62fdfa90a7c47a2011056f549cd9b_2_500x500.jpeg)

### [Tools in Data Science](https://www.youtube.com/@se-lr5ff)

Share your videos with friends, family, and the world

Kind regards

---

## Post #257

- **Author**: 23f2005419
- **Posted on**: 2025-02-14T07:42:08.309Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/257

Thanks sir, Now I subscribed to the channel.

---

## Post #258

- **Author**: 23f2003413
- **Posted on**: 2025-02-14T07:45:02.221Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/258

Hi [@carlton](/u/carlton) sir! Is this video (Week-5 Session-3) the continuation video from the previous session (Week-5 Session-1), since the Session-2 video has not been recorded and uploaded. I am totally relying on these videos to complete the project sir. Please help me out!

---

## Post #259

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T08:04:25.977Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/259

offical answer is you dont, you let run it in docker and it would apparently work , im not there yet, bus as of of now , create your docker image and start testing there

---

## Post #260

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T08:08:24.668Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/260

The deadline is at 11:59 pm right Saturday? Feb 15th? Google Standard Time?

---

## Post #261

- **Author**: Jivraj
- **Posted on**: 2025-02-14T08:17:41.120Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/261

Yes feb 15 11:59 PM indian standard time.

---

## Post #262

- **Author**: Jivraj
- **Posted on**: 2025-02-14T08:21:27.720Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/262

Hi [@23f2003413](/u/23f2003413)

Session 3 was continuation of session1.  
Session 2 was DCS(doubts clearing session)

Kind regards

---

## Post #263

- **Author**: 23f2003413
- **Posted on**: 2025-02-14T08:25:42.250Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/263

Got it. Thank you sir!

---

## Post #264

- **Author**: 23f2005419
- **Posted on**: 2025-02-14T08:33:06.508Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/264

Hi [@Jivraj](/u/jivraj), [@carlton](/u/carlton), [@Saransh\_Saini](/u/saransh_saini) sir,

I’m getting the following error while post mapping, I couldn’t able to fix it.  
I’m getting status code as 400 from the llm api response. How to fix it sir?

```
   "json": {
        "message": "Invalid JSON body: SyntaxError: Unexpected token 'm', \"model=gpt-\"... is not valid JSON"
    }

```

---

## Post #265

- **Author**: Jivraj
- **Posted on**: 2025-02-14T08:35:17.405Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/265

There is some problem with the json that you are using.

Try to debug it with GPT.

---

## Post #266

- **Author**: Jivraj
- **Posted on**: 2025-02-14T08:36:01.337Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/266

week5 session 1 and session3

---

## Post #267

- **Author**: 23f2001286
- **Posted on**: 2025-02-14T08:38:10.454Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/267

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/f/bf2517eb87feb20f7270ef8730daf3f1c5599473.png)

image929×427 11.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/f/bf2517eb87feb20f7270ef8730daf3f1c5599473.png "image")

  
Is someone else are also getting this kind of error messages…  
I have a low end system, then shifted to high one then again this popped up…  
Does anyone know how to come over this…

---

## Post #268

- **Author**: 21f2000588
- **Posted on**: 2025-02-14T09:23:07.838Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/268

Hello [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) sir, I have implemented the code for B3 & B6 but unfortunately as per the instructions given in project for B3 & B6 —

* **B6**. Extract data from (i.e. scrape) a website
* **B3**. Fetch data from an API and save it

They are almost similar and it’s getting confusing in both cases, it’s given output based on B3 and not reading the input for B6, so could you please help me out with this?

Is anyone else facing this or a similar issue?

---

## Post #269

- **Author**: Jivraj
- **Posted on**: 2025-02-14T09:27:49.421Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/269

Two solutions

1. give proper permissions.
2. use docker containers this is what we will test on.

I would prefer 2nd approach

---

## Post #271

- **Author**: Jivraj
- **Posted on**: 2025-02-14T09:31:58.136Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/271

For B tasks use LLM to write code on the fly and execute it, use better prompts. In evaluation script detailed task will be provided with what data needs to be scraped, endpoints, parameters, etc.

---

## Post #272

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T09:45:19.679Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/272

{‘error’: {‘message’: “Invalid ‘tools[6].function.description’: string too long. Expected a string with maximum length 1024, but got a string with length 4384 instead.”, ‘type’: ‘invalid\_request\_error’, ‘param’: ‘tools[6].function.description’, ‘code’: ‘string\_above\_max\_length’}, ‘monthlyCost’: 0.08569882000000002, ‘cost’: 0, ‘monthlyRequests’: 82}

i cant send long prompts then what is the point?

---

## Post #273

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T09:45:59.531Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/273

local llm also we cant use you because you have some limit on file size, we send long prompt also it doesn’t work xD . What do we do?  
[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj) @anybodywhowouldatleastreplyONCE

---

## Post #274

- **Author**: Saransh_Saini
- **Posted on**: 2025-02-14T10:04:32.618Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/274

Hi,  
If you read these questions carefully then they are not similar, one is asking you to extract data from a webpage, meaning you have to do something related to the HTML code. And the other is simply sending a request to a given endpoint.

---

## Post #275

- **Author**: 22f2001640
- **Posted on**: 2025-02-14T11:13:31.475Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/275

Hi [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) ,  
In task A6  
**Find all Markdown (`.md` ) files in `/data/docs/` . For each file, extract the first occurrance of each H1 (i.e. a line starting with `#`  ). Create an index file `/data/docs/index.json` that maps each filename (without the `/data/docs/` prefix) to its title (e.g. `{"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...}` ).**

Here expected output JSON “key” is file name or file path without prefix /data/docs/ as prompt is bit confusing . when “path/to/large-language-models.md” is given in example is actually referring to file path or filename itself is “path/to/large-language-models.md”.

---

## Post #276

- **Author**: Saransh_Saini
- **Posted on**: 2025-02-14T11:44:32.114Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/276

This can easily be checked by runing the evaluate.py file.  
Anyways, a file present in data/docs/folder\_a/folder\_b/md\_file should be folder\_a/folder\_b/md\_file as key.

---

## Post #277

- **Author**: 22f3002248
- **Posted on**: 2025-02-14T11:48:06.753Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/277

hey [@23f2001975](/u/23f2001975) did you find the solution to this problem ?  
i am facing the exact same issue

---

## Post #278

- **Author**: 22f3001777
- **Posted on**: 2025-02-14T12:44:44.847Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/278

[@carlton](/u/carlton)  
Sir, my token limit has crossed the $1 limit. Will I receive new limit or a fresh token ? I still need to complete my project.  
Thank you

---

## Post #279

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T12:50:06.658Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/279

![:red_circle:](https://emoji.discourse-cdn.com/google/red_circle.png?v=12 ":red_circle:") /data/credit-card.txt  
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") EXPECTED:  
30091429521159  
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") RESULT:  
3009142952159

{‘role’: ‘assistant’, ‘content’: ‘3009142952159’, ‘refusal’: None} if LLM is giving wrong output. I hope y’all look into edge cases. Some people tried really hard. to prompt it xD ![:upside_down_face:](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=12 ":upside_down_face:") ![:upside_down_face:](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=12 ":upside_down_face:") ![:upside_down_face:](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=12 ":upside_down_face:").  
  
You can check the logs

  
(venv) @ANDIECOOLER2 ➜ /workspaces/TDS-Project-1/app (checking-with-open-ai) $ uv run evaluate.py
🟡 Running task: Install `uv` (if required) and run the script `https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama\_FastAPI-/refs/heads/main/datagen.py`
with `23f1002382@ds.study.iitm.ac.in` as the only argument

HTTP Request: POST [http://localhost:8000/run?task=
Install+`uv`+(if+required)+and+run+the+script+`https%3A%2F%2Fraw.githubusercontent.com%2FANdIeCOOl%2FTDS-Project1-Ollama\_FastAPI-%2Frefs%2Fheads%2Fmain%2Fdatagen.py`
with+`23f1002382%40ds.study.iitm.ac.in`+as+the+only+argument](http://localhost:8000/run?task=%0AInstall+%60uv%60+%28if+required%29+and+run+the+script+%60https%3A%2F%2Fraw.githubusercontent.com%2FANdIeCOOl%2FTDS-Project1-Ollama_FastAPI-%2Frefs%2Fheads%2Fmain%2Fdatagen.py%60%0Awith+%6023f1002382%40ds.study.iitm.ac.in%60+as+the+only+argument%0A) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/format.md> “HTTP/1.1 200 OK”

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:") A1 PASSED

10.8.2  
![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: Format the contents of `/data/format.md` using `prettier@3.4.2`, updating the file in-place

HTTP Request: POST [http://localhost:8000/run?task=
Format+the+contents+of+`%2Fdata%2Fformat.md`+using+`prettier%403.4.2`%2C+updating+the+file+in-place](http://localhost:8000/run?task=%0AFormat+the+contents+of+%60%2Fdata%2Fformat.md%60+using+%60prettier%403.4.2%60%2C+updating+the+file+in-place%0A) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/format.md> “HTTP/1.1 200 OK”

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:") A2 PASSED

![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: The file `/data/dates.txt` contains a list of dates, one per line. Count the number of Wednesdays in the list, and write just the number to `/data/dates-wednesdays.txt`

HTTP Request: POST [http://localhost:8000/run?task=The+file+`%2Fdata%2Fdates.txt`+contains+a+list+of+dates%2C+one+per+line.+Count+the+number+of+Wednesdays+in+the+list%2C+and+write+just+the+number+to+`%2Fdata%2Fdates-wednesdays.txt`](http://localhost:8000/run?task=The+file+%60%2Fdata%2Fdates.txt%60+contains+a+list+of+dates%2C+one+per+line.+Count+the+number+of+Wednesdays+in+the+list%2C+and+write+just+the+number+to+%60%2Fdata%2Fdates-wednesdays.txt%60) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/dates-wednesdays.txt> “HTTP/1.1 200 OK”

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:") A3 PASSED

![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: Sort the array of contacts in `/data/contacts.json` by `last_name`, then `first_name`, and write the result to `/data/contacts-sorted.json`

HTTP Request: POST [http://localhost:8000/run?task=Sort+the+array+of+contacts+in+`%2Fdata%2Fcontacts.json`+by+`last\_name`%2C+then+`first\_name`%2C+and+write+the+result+to+`%2Fdata%2Fcontacts-sorted.json`](http://localhost:8000/run?task=Sort+the+array+of+contacts+in+%60%2Fdata%2Fcontacts.json%60+by+%60last_name%60%2C+then+%60first_name%60%2C+and+write+the+result+to+%60%2Fdata%2Fcontacts-sorted.json%60) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/contacts-sorted.json> “HTTP/1.1 200 OK”

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:") A4 PASSED

![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: Write the first line of the 10 most recent `.log` file in `/data/logs/` to `/data/logs-recent.txt`, most recent first

HTTP Request: POST [http://localhost:8000/run?task=Write+the+first+line+of+the+10+most+recent+`.log`+file+in+`%2Fdata%2Flogs%2F`+to+`%2Fdata%2Flogs-recent.txt`%2C+most+recent+first](http://localhost:8000/run?task=Write+the+first+line+of+the+10+most+recent+%60.log%60+file+in+%60%2Fdata%2Flogs%2F%60+to+%60%2Fdata%2Flogs-recent.txt%60%2C+most+recent+first) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/logs-recent.txt> “HTTP/1.1 200 OK”

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:") A5 PASSED

![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: Find all Markdown (`.md`) files in `/data/docs/`.  
For each file, extract the first occurrance of each H1 (i.e. a line starting with `#` ).  
Create an index file `/data/docs/index.json` that maps each filename (without the `/data/docs/` prefix) to its title  
(e.g. `{"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...}`)

HTTP Request: POST [http://localhost:8000/run?task=Find+all+Markdown+(`.md`)+files+in+`%2Fdata%2Fdocs%2F`.
For+each+file%2C+extract+the+first+occurrance+of+each+H1+(i.e.+a+line+starting+with+`%23+`).
Create+an+index+file+`%2Fdata%2Fdocs%2Findex.json`+that+maps+each+filename+(without+the+`%2Fdata%2Fdocs%2F`+prefix)+to+its+title
(e.g.+`{“README.md”%3A+“Home”%2C+“path%2Fto%2Flarge-language-models.md”%3A+“Large+Language+Models”%2C+...}`)](http://localhost:8000/run?task=Find+all+Markdown+%28%60.md%60%29+files+in+%60%2Fdata%2Fdocs%2F%60.%0AFor+each+file%2C+extract+the+first+occurrance+of+each+H1+%28i.e.+a+line+starting+with+%60%23+%60%29.%0ACreate+an+index+file+%60%2Fdata%2Fdocs%2Findex.json%60+that+maps+each+filename+%28without+the+%60%2Fdata%2Fdocs%2F%60+prefix%29+to+its+title%0A%28e.g.+%60%7B%22README.md%22%3A+%22Home%22%2C+%22path%2Fto%2Flarge-language-models.md%22%3A+%22Large+Language+Models%22%2C+...%7D%60%29) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/docs/index.json> “HTTP/1.1 200 OK”

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:") A6 PASSED

![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: `/data/email.txt` contains an email message. Pass the content to an LLM with instructions to extract the sender’s email address, and write just the email address to `/data/email-sender.txt`

HTTP Request: POST [http://localhost:8000/run?task=`%2Fdata%2Femail.txt`+contains+an+email+message.+Pass+the+content+to+an+LLM+with+instructions+to+extract+the+sender’s+email+address%2C+and+write+just+the+email+address+to+`%2Fdata%2Femail-sender.txt`](http://localhost:8000/run?task=%60%2Fdata%2Femail.txt%60+contains+an+email+message.+Pass+the+content+to+an+LLM+with+instructions+to+extract+the+sender%27s+email+address%2C+and+write+just+the+email+address+to+%60%2Fdata%2Femail-sender.txt%60) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/email-sender.txt> “HTTP/1.1 200 OK”

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:") A7 PASSED

![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: `/data/credit_card.png` contains a credit card number. Pass the image to an LLM, have it extract the card number, and write it without spaces to `/data/credit-card.txt`

HTTP Request: POST [http://localhost:8000/run?task=`%2Fdata%2Fcredit\_card.png`+contains+a+credit+card+number.+Pass+the+image+to+an+LLM%2C+have+it+extract+the+card+number%2C+and+write+it+without+spaces+to+`%2Fdata%2Fcredit-card.txt`](http://localhost:8000/run?task=%60%2Fdata%2Fcredit_card.png%60+contains+a+credit+card+number.+Pass+the+image+to+an+LLM%2C+have+it+extract+the+card+number%2C+and+write+it+without+spaces+to+%60%2Fdata%2Fcredit-card.txt%60) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/credit-card.txt> “HTTP/1.1 200 OK”

![:red_circle:](https://emoji.discourse-cdn.com/google/red_circle.png?v=12 ":red_circle:") /data/credit-card.txt  
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") EXPECTED:  
30091429521159  
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") RESULT:  
3009142952159

![:x:](https://emoji.discourse-cdn.com/google/x.png?v=12 ":x:") A8 FAILED

HTTP Request: POST <https://aiproxy.sanand.workers.dev/openai/v1/embeddings> “HTTP/1.1 200 OK”

![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: `/data/comments.txt` contains a list of comments, one per line. Using embeddings, find the most similar pair of comments and write them to `/data/comments-similar.txt`, one per line

HTTP Request: POST [http://localhost:8000/run?task=`%2Fdata%2Fcomments.txt`+contains+a+list+of+comments%2C+one+per+line.+Using+embeddings%2C+find+the+most+similar+pair+of+comments+and+write+them+to+`%2Fdata%2Fcomments-similar.txt`%2C+one+per+line](http://localhost:8000/run?task=%60%2Fdata%2Fcomments.txt%60+contains+a+list+of+comments%2C+one+per+line.+Using+embeddings%2C+find+the+most+similar+pair+of+comments+and+write+them+to+%60%2Fdata%2Fcomments-similar.txt%60%2C+one+per+line) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/comments-similar.txt> “HTTP/1.1 200 OK”

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:") A9 PASSED

![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: The SQLite database file `/data/ticket-sales.db` has a `tickets` with columns `type`, `units`, and `price`. Each row is a customer bid for a concert ticket. What is the total sales of all the items in the “Gold” ticket type? Write the number in `/data/ticket-sales-gold.txt`

HTTP Request: POST [http://localhost:8000/run?task=The+SQLite+database+file+`%2Fdata%2Fticket-sales.db`+has+a+`tickets`+with+columns+`type`%2C+`units`%2C+and+`price`.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+“Gold”+ticket+type%3F+Write+the+number+in+`%2Fdata%2Fticket-sales-gold.txt`](http://localhost:8000/run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60) “HTTP/1.1 200 OK”

![:green_circle:](https://emoji.discourse-cdn.com/google/green_circle.png?v=12 ":green_circle:") HTTP 200 {  
“status”: “success”,  
“message”: “Task executed successfully”  
}

HTTP Request: GET <http://localhost:8000/read?path=/data/ticket-sales-gold.txt> “HTTP/1.1 200 OK”

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:") A10 PASSED

![:dart:](https://emoji.discourse-cdn.com/google/dart.png?v=12 ":dart:") Score: 9 / 10 proof  
EDIT CREDIT CARD NUMBERS are 16 digits, so even there is discrepancy

---

## Post #280

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T12:51:37.874Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/280

usage’: {‘prompt\_tokens’: 1384,  
‘completion\_tokens’: 67,  
‘total\_tokens’: 1451,  
‘prompt\_tokens\_details’: {‘cached\_tokens’: 0, ‘audio\_tokens’: 0},  
‘completion\_tokens\_details’: {‘reasoning\_tokens’: 0, ‘audio\_tokens’: 0, ‘accepted\_prediction\_tokens’: 0, ‘rejected\_prediction\_tokens’: 0}},  
‘service\_tier’: ‘default’, ‘system\_fingerprint’: ‘fp\_13eed4fce1’,  
‘monthlyCost’: 0.5243745800000005,  
‘cost’: 0.004554000000000001

GPT-4o mini  
Fine-tuning price  
Input:--------------------------> CALCUATION: (1384/10^6)\*$0.30 = 0.0004152  
$0.30 / 1M tokens  
Cached input:  
$0.15 / 1M tokens  
Output:-------------------------> CALCUATION: (67/10^6)$1.20 = 0.0000804  
$1.20 / 1M tokens  
Training:  
$3.00 / 1M tokens  
TOTAL = 0.0004152 + 0.0000804 = 0.0004956  
‘cost’: 0.004554000000000001 MAKE IT MAKE SENSE?  
‘total\_tokens’: 1451, so only input and completion tokens used?  
  
  
  
  
  
  
  
  
INFO: Uvicorn running on <http://0.0.0.0:8000> (Press CTRL+C to quit)  
INFO:root:10  
INFO:root:Inside run\_task with task:  
Install `uv` (if required) and run the script `https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/refs/heads/main/datagen.py`  
with `23f1002382@ds.study.iitm.ac.in` as the only argument

INFO:root:PRINTING RESPONSE:::PRINTING RESPONSE:::PRINTING RESPONSE:::  
{‘id’: ‘chatcmpl-B0pChhrBiCN8x8ueL2u57rwQiucl7’, ‘object’: ‘chat.completion’, ‘created’: 1739536527, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: None, ‘tool\_calls’: [{‘id’: ‘call\_ULCgfFzpEcnGNditwVwGwRIS’, ‘type’: ‘function’, ‘function’: {‘name’: ‘install\_and\_run\_script’, ‘arguments’: ‘{“package”:“uv”,“args”:[“23f1002382@ds.study.iitm.ac.in”],“script\_url”:“<https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/refs/heads/main/datagen.py>”}’}}], ‘refusal’: None}, ‘logprobs’: None, ‘finish\_reason’: ‘tool\_calls’}], ‘usage’: {‘prompt\_tokens’: 1384, ‘completion\_tokens’: 67, ‘total\_tokens’: 1451, ‘prompt\_tokens\_details’: {‘cached\_tokens’: 0, ‘audio\_tokens’: 0}, ‘completion\_tokens\_details’: {‘reasoning\_tokens’: 0, ‘audio\_tokens’: 0, ‘accepted\_prediction\_tokens’: 0, ‘rejected\_prediction\_tokens’: 0}}, ‘service\_tier’: ‘default’, ‘system\_fingerprint’: ‘fp\_13eed4fce1’, ‘monthlyCost’: 0.5243745800000005, ‘cost’: 0.004554000000000001, ‘monthlyRequests’: 217}

[@s.anand](/u/s.anand) How is the usage calculated? Just asking not implying  
UPDATE: ITS EVEN MORE CHEAPER, I gave benefir of doubt better its much cheaper? ???  

[![Screenshot 2025-02-14 183844](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/a/7a085e66044ea9d25d6ad8e95640d6b635c9cd40_2_690x357.png)

Screenshot 2025-02-14 1838441695×879 52 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/a/7a085e66044ea9d25d6ad8e95640d6b635c9cd40.png "Screenshot 2025-02-14 183844")

---

## Post #281

- **Author**: carlton
- **Posted on**: 2025-02-14T13:02:49.800Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/281

You can continue to $2. Then you would need to ask for a new token.

---

## Post #282

- **Author**: 24ds3000061
- **Posted on**: 2025-02-14T13:07:11.530Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/282

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) please upload recording of TDS Week 5 - Session 2. Only recordings of session 1 & 3 have been uploaded.

---

## Post #283

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T13:28:09.267Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/283

[github.com](https://github.com/ANdIeCOOl/TDS-Project-1)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/b/3bfc6f97a124e61d5c97c25e6dd6c901e0262fde_2_690x344.png)

### [GitHub - ANdIeCOOl/TDS-Project-1](https://github.com/ANdIeCOOl/TDS-Project-1)

Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.

DONE WITH A TASK , you have to create DOCKER IMAGE THOUGH < HAVE ENV file with keys , check the key value pair names, an cheers guy , we all get 9 marks hopefully

---

## Post #284

- **Author**: 23f2002592
- **Posted on**: 2025-02-14T13:29:19.598Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/284

For as task description like this

* Write the # of Thursdays in `/data/extracts.txt` into `/data/extracts-count.txt`

I have given the prompt in such detail to the LLM but it is still not able to understand the task because of the “#” symbol. The task is getting truncated even before it reaches to the LLM.  
Can anyone help me on this because I have tried so many things to fix this but nothing seems to help.

---

## Post #285

- **Author**: 23f2005419
- **Posted on**: 2025-02-14T13:39:06.561Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/285

Hi [@Jivraj](/u/jivraj), [@carlton](/u/carlton) sir,

I have created a docker file and run the application but it’s throwing error for  
A2 task  
No such file or directory: ‘npx’  
Do i need give the node install in docker file?

---

## Post #286

- **Author**: carlton
- **Posted on**: 2025-02-14T13:41:01.000Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/286

Hash is just another way of writing “number”

---

## Post #287

- **Author**: 23f2001286
- **Posted on**: 2025-02-14T13:51:49.280Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/287

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
sir i have tried to solve the A1. when I want to check the solution we are asked for the datagen module as the evaluate.py have  
’

```
''from datagen import (
    get_markdown,
    get_dates,
    get_contacts,
    get_logs,
    get_docs,
    get_email,
    get_credit_card,
    get_comments,
    get_tickets,
)
'''

```

so do we need to download the datagen.py in the local system first…

Or it should be the part of the automation only…

---

## Post #288

- **Author**: sharma_abhay
- **Posted on**: 2025-02-14T13:53:07.372Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/288

I am getting internal server error for task A1, I have been trying for a long time. It may be possible that i have issues with my ai\_proxy token thus tell how to properly set the taken.

---

## Post #289

- **Author**: 23f2002592
- **Posted on**: 2025-02-14T14:05:45.308Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/289

Yes I know that but LLM does not know that # indicates number. And no prompt is fixing this issue because the task has to be passed as query parameter and by the time LLM reads the task, it is already half gone due to #.

---

## Post #290

- **Author**: 23f2001305
- **Posted on**: 2025-02-14T14:13:13.898Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/290

Where to find AIProxy token from?

---

## Post #291

- **Author**: daksh76
- **Posted on**: 2025-02-14T14:16:15.399Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/291

what if we are out of token sir how do we complete our project then?

---

## Post #292

- **Author**: daksh76
- **Posted on**: 2025-02-14T14:17:20.568Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/292

could u share your code once i think you should explicitly try to install npx in your code

---

## Post #293

- **Author**: daksh76
- **Posted on**: 2025-02-14T14:19:01.883Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/293

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1002382/48/68945_2.png) 23f1002382:

> ANDIECOOLER2

could you help me out with q2?

---

## Post #294

- **Author**: 23f2001305
- **Posted on**: 2025-02-14T14:19:08.253Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/294

Can you tell me where to get the AIPROXY Token from and also are u able to execute docker image push command it keeps showing as an error to me

---

## Post #295

- **Author**: 23f2005419
- **Posted on**: 2025-02-14T14:19:40.681Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/295

```
def format_with_prettier(file_path:str, prettier_version:str):
    if file_path and os.path.exists(file_path):
        print('Path exisit - will perform prettier')
        subprocess.run(["npx", f"prettier@{prettier_version}", "--write", file_path])
    else:
        raise FileNotFoundError()

```

This is my code

---

## Post #296

- **Author**: daksh76
- **Posted on**: 2025-02-14T14:21:56.574Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/296

this isnt also working are you sure its right?

---

## Post #297

- **Author**: daksh76
- **Posted on**: 2025-02-14T14:22:42.231Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/297

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/dbd85efd1bbce9710794cb0434a90d37a8c20a25.png)

image1027×917 28.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/dbd85efd1bbce9710794cb0434a90d37a8c20a25.png "image")

---

## Post #298

- **Author**: 23f2005419
- **Posted on**: 2025-02-14T14:24:13.838Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/298

okay but in my docker image when i tried to run that in local, its asking for npx and it doesnt work

---

## Post #299

- **Author**: daksh76
- **Posted on**: 2025-02-14T14:25:02.922Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/299

[@carlton](/u/carlton) could you please give a hint as to why this isnt working

---

## Post #300

- **Author**: daksh76
- **Posted on**: 2025-02-14T14:25:35.496Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/300

im running locally first and then will use docker when i get a 10/10 score

---

## Post #301

- **Author**: 23f2005419
- **Posted on**: 2025-02-14T14:27:05.634Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/301

Okay, actually when i tried with local, i’m facing path error

```
./data/format.md
[WinError 2] The system cannot find the file specified

```

So that’s why i moved to docker but there also i’m getting error for A2.

---

## Post #302

- **Author**: daksh76
- **Posted on**: 2025-02-14T14:28:35.283Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/302

you should manually check if the file really exists or not because i think the code and the folder where datagen.py is downloading files(data folder) are different

---

## Post #303

- **Author**: 23f2005419
- **Posted on**: 2025-02-14T14:30:50.228Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/303

yes yes i moved the folder to current working directory

---

## Post #304

- **Author**: carlton
- **Posted on**: 2025-02-14T14:42:57.529Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/304

If you are using the function calling approach, you could just parse the ‘#’ and change it to ‘number’ and then send the prompt to the llm for that particular task.

Or another approach is tell the llm,

If you ever see the phrase ‘count the # of’ in a task, please interpret it as ‘count the number of’. For example  
Count the # of Fridays means  
Count the number of Fridays

---

## Post #305

- **Author**: 21f3002277
- **Posted on**: 2025-02-14T14:51:01.614Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/305

[![Screenshot 2025-02-14 201854](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3dacf2bf3fd48309342a483aeb249f46faf1dc55_2_690x364.png)

Screenshot 2025-02-14 2018541919×1015 81.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/d/3dacf2bf3fd48309342a483aeb249f46faf1dc55.png "Screenshot 2025-02-14 201854")

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) this is showing while docker image is running

---

## Post #306

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T15:06:44.218Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/306

in project page, ctrl+F and search ai proxy, one link s.anandProxy or something, there it will validate you email and get you your token.

---

## Post #307

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T15:08:15.660Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/307

can you share your code for dynamic code generation, i dont have the base to start with , can you send me the code?  
whatever this image is , llm\_code,oy and etc

---

## Post #308

- **Author**: 23f2005702
- **Posted on**: 2025-02-14T15:20:58.709Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/308

What file should we have while pushing it to git and making image  
should datagen file and data be there or not?

---

## Post #309

- **Author**: carlton
- **Posted on**: 2025-02-14T15:24:08.470Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/309

Please read the deliverables and evalute section.

datagen.py and evaluate.py were for only for your testing purposes so that you have an idea of the workflow and how the evaluation works. They are NOT part of your project submission.

Only DO what the project page tells you in the deliverables and evalute sections.

Kind regards

---

## Post #310

- **Author**: Sourabhraj
- **Posted on**: 2025-02-14T16:01:26.721Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/310

sir i am getting this error by running the docker image  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7d16a8ef3054bbd7db0999d3efcf5aaadae798d5.png)

image656×116 3.28 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7d16a8ef3054bbd7db0999d3efcf5aaadae798d5.png "image")

i tried troubleshooting this for hours but no luck could you please tell me what i did wrong here

---

## Post #311

- **Author**: 23ds1000005
- **Posted on**: 2025-02-14T16:05:32.054Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/311

i can help you up, if you need my help you can email me

---

## Post #312

- **Author**: ShahbaazSingh
- **Posted on**: 2025-02-14T16:34:56.570Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/312

[@s.anand](/u/s.anand) Sir please tell me this I am not using podman i am using docker for building and hosting is it fine sir ?

---

## Post #313

- **Author**: 21f2000709
- **Posted on**: 2025-02-14T16:56:52.460Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/313

Hey [@carlton](/u/carlton) [@Jivraj](/u/jivraj) , I actually submitted the project already in the morning,  
I included all the deliverables and things mentioned in the evaluation section.

But since I was actively testing with the - `datagen.py` and `evaluate.py`, I forgot to remove them before submission.

However these files do not play a role in my project execution in any way, they just sit idle. Will there be any issue?

---

## Post #314

- **Author**: 22f3002723
- **Posted on**: 2025-02-14T16:57:01.976Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/314

when trying to use function call way of open api

```
tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_email_sender",
            "description": "Extract sender email from a specific file in directory",
            "parameters": {},
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "count_day_of_week",
            "description": "To count the occurances of a specific day of a week in a file with various dates",
            "parameters": {
                "type": "object",
                "properties": {
                    "day_of_week": {
                        "type": "string",
                        "description": "day of week"
                    }
                },
                "required": ["day_of_week"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]

```

```
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": user_input},
                
        ],      
	"tools": tools,
    "tool_choice": "auto",
    "max_tokens": 500,
    "temperature": 0.7
    }

```

facing the below issue  
ror’: {‘message’: “Invalid type for ‘tools[0]’: expected an object, but got an array instead.”

---

## Post #315

- **Author**: AnvithaV
- **Posted on**: 2025-02-14T17:04:07.947Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/315

when i run POST request t is showing output “HTTP/1.1 200 OK” but when i give GET request it is showing HTTP/1.1" 404 Not Found. Can you please say how can it be solved

---

## Post #316

- **Author**: 21f2000709
- **Posted on**: 2025-02-14T17:06:05.703Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/316

These files are inside a separate folder - `evaluation` in my project root directory. Since I already submitted please do consider.

Thanks & Regards  
Pradeep

---

## Post #317

- **Author**: 21f2000709
- **Posted on**: 2025-02-14T17:09:07.670Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/317

This indicates your task execution returns “HTTP/1.1 200 OK” but the execution doesn’t creates the required file in the given location that the evaluation script is requesting.

---

## Post #318

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T17:09:40.757Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/318

If have doubts in building DOCKER stuff can you help me debug

PLEASE SENPAI

![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:fish_cake:](https://emoji.discourse-cdn.com/google/fish_cake.png?v=12 ":fish_cake:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")![:dolls:](https://emoji.discourse-cdn.com/google/dolls.png?v=12 ":dolls:")

---

## Post #319

- **Author**: 21f2000709
- **Posted on**: 2025-02-14T17:10:23.045Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/319

sure!! how can I help?

---

## Post #320

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T17:10:55.142Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/320

+1  
SENPAI is right ![:innocent:](https://emoji.discourse-cdn.com/google/innocent.png?v=12 ":innocent:")

---

## Post #321

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T17:12:09.065Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/321

not yet maybe in an hour, im building, but after that running in docker is different ball game, thats why , i need quick debugs in a meeting, other people also can join, maybe tomorrow, i have an exam tomorrow, so preferably , collectively before project submission . IF YOU HAVE TIME

---

## Post #322

- **Author**: 21f2000709
- **Posted on**: 2025-02-14T17:14:03.094Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/322

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1002382/48/68945_2.png) 23f1002382:

Sure tell me I would try, if I am online then otherwise tomorrow if it’s late

---

## Post #323

- **Author**: 23f2004752
- **Posted on**: 2025-02-14T17:30:23.474Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/323

I am getting this error while pulling docker image

ansh@Lenovo:~/llm\_project$ podman pull [docker.io/ansh205/llm\_project:final](http://docker.io/ansh205/llm_project:final)  
Trying to pull [docker.io/ansh205/llm\_project:final](http://docker.io/ansh205/llm_project:final)…  
Error: parsing image configuration: Get “<https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/07/079f65bc553514a8f38a08fd959e932ca984894a64eed71fca406f3353b71d3b/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250214%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250214T172706Z&X-Amz-Expires=1200&X-Amz-SignedHeaders=host&X-Amz-Signature=073575bf08338fcdda378b997ebe749b15a6b676ed7b80fbf4c3f8080a791152>”: dial tcp: lookup [docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com](http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com) on 10.255.255.254:53: server misbehavingPreformatted text

---

## Post #324

- **Author**: 23f2004752
- **Posted on**: 2025-02-14T17:50:37.272Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/324

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) [@Saransh\_Saini](/u/saransh_saini)  
sir please provide me other api key. My current request cost is full.

Full LLM Response: {‘message’: ‘On 2025-02 you used $2.000143640000001, exceeding $2’}

---

## Post #325

- **Author**: 22f3002723
- **Posted on**: 2025-02-14T17:54:51.017Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/325

```
 curl -X POST http://localhost:8001/run?task=Extract%20sender%20email
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    36  100    36    0     0      9      0  0:00:04  0:00:03  0:00:01     9{"results":"wrighttara@example.net"}

```

is this expectation of having %20 for blanks in query string fine ?

---

## Post #326

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T18:00:47.841Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/326

docker run -e OPEN\_AI\_PROXY\_TOKEN=your\_token\_value   
-e OPEN\_AI\_PROXY\_URL=your\_proxy\_url   
-e OPEN\_AI\_EMBEDDING\_URL=your\_embedding\_url   
-p 8000:8000

how do we get out urls inside, hardcode?

---

## Post #327

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T18:44:42.380Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/327

Can you help with docker size image?  
is it 2 GB?

---

## Post #328

- **Author**: 23f2001975
- **Posted on**: 2025-02-14T19:25:07.571Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/328

I want to reset my aiproxys i have used them all if i could even buy some would work i need it to test my app or could iitm help in resetting it please tell

---

## Post #329

- **Author**: daksh76
- **Posted on**: 2025-02-14T19:33:27.385Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/329

could u help me in q9 thats the one left

---

## Post #330

- **Author**: daksh76
- **Posted on**: 2025-02-14T19:34:15.132Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/330

[@carlton](/u/carlton) my aiproxy is also exhausted please help me out

---

## Post #331

- **Author**: Namannn28
- **Posted on**: 2025-02-14T19:35:02.251Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/331

sir my api tokens limit reached to one dollar , hiw to reset it

---

## Post #332

- **Author**: 23f2001975
- **Posted on**: 2025-02-14T19:39:31.640Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/332

bro can you help me with q2

---

## Post #334

- **Author**: 21f3000512
- **Posted on**: 2025-02-14T20:00:49.013Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/334

How to handle task a8 ? I tried pytesseract but gave wrong results.EasyOCR is giving the exact answer so tried in docker but some Model download is interrupting the flow of evaluate.py resulting in error .  
I appreciate any help/procedure or code to handle taska8.  
Thanks in advance.

---

## Post #335

- **Author**: 23f2001975
- **Posted on**: 2025-02-14T20:10:42.788Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/335

Did you get any solution to this

---

## Post #336

- **Author**: TheVishal
- **Posted on**: 2025-02-14T20:14:40.100Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/336

u can use groq api groq api is compatible with openai

---

## Post #337

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T20:19:32.979Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/337

whats up?  
/////////////////////

---

## Post #339

- **Author**: TheVishal
- **Posted on**: 2025-02-14T20:22:37.469Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/339

bro can please check my repo i am only able to do 7 tasks.

repo url: [GitHub - 23f2005593/tds-project-1: TDS Project 1](https://github.com/23f2005593/tds-project-1)

---

## Post #340

- **Author**: 23f1002382
- **Posted on**: 2025-02-14T20:34:21.048Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/340

got the docker working?

---

## Post #341

- **Author**: 22f3001011
- **Posted on**: 2025-02-14T21:26:37.667Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/341

[@carlton](/u/carlton) [@Jeeveash.k](/u/jeeveash.k)  
sir i submitted the wrong docker image file while submitted the form. Can you please let me change it, or make it such that we can reupload it  
thank you.

---

## Post #343

- **Author**: s.anand
- **Posted on**: 2025-02-14T21:43:12.220Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/343

22f3001011 I’ve enabled “Allow response editing” on the form. I *think* that means you can edit your response… but since you had submitted it before it was enabled, I’m not sure what the procedure is. Worst case, please submit again.

---

## Post #344

- **Author**: 22f3000079
- **Posted on**: 2025-02-14T21:53:15.084Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/344

**Please make this change in evaluation.py**

In evaluation script url of datagen.py is different than actual one please change it

evaluation.py line 72

Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py`

**change this to**

Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py`

---

## Post #345

- **Author**: 23f2001975
- **Posted on**: 2025-02-14T22:56:20.796Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/345

very true there is too much confusion Id like to ask if you know that evaluate.py is mean to run only for [user@example.com](mailto:user@example.com) or our own mail too because there was written **You MUST use your Student Id** (eg. 22f3xxxxxx@ds.study.iitm.ac.in) **to do the Project, otherwise your score will not be considered for evaluation.**

---

## Post #346

- **Author**: 23f2005419
- **Posted on**: 2025-02-14T23:29:27.439Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/346

Hi any one have any idea on the below,

```
SyntaxError: illegal target for annotation

```

I’m getting this error only when i run the evaluate.py but in with postman it works as expected.

Anyone please help on this

---

## Post #348

- **Author**: 21f3002277
- **Posted on**: 2025-02-15T01:57:19.909Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/348

[![Screenshot 2025-02-15 071910](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae2a4772672aef536d8e69b87e59e4f94853ebc8_2_690x367.png)

Screenshot 2025-02-15 0719101919×1021 71.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/e/ae2a4772672aef536d8e69b87e59e4f94853ebc8.png "Screenshot 2025-02-15 071910")

sir why the datagen.py in not created in the tree and the data folder please help me [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

## Post #349

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T02:08:18.515Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/349

created in toot, cd /data in docker will take you there.

---

## Post #350

- **Author**: 21f3002277
- **Posted on**: 2025-02-15T02:42:37.695Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/350

[![Screenshot 2025-02-15 075843](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/2/d2cb339eab8983304f220c258a57f4db8cd76213_2_690x365.png)

Screenshot 2025-02-15 0758431919×1017 70.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/2/d2cb339eab8983304f220c258a57f4db8cd76213.png "Screenshot 2025-02-15 075843")

is changes is required in Dockerfile

---

## Post #351

- **Author**: 23f2002205
- **Posted on**: 2025-02-15T03:36:59.904Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/351

i too got the same error you can change the the tools part in your payload to

```
"tools": [{"type": "function", "function": schema} for schema in function_schema]

```

---

## Post #352

- **Author**: 23f2002205
- **Posted on**: 2025-02-15T03:42:16.807Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/352

i think you have to run the following command

```
uv run datagen.py <your_email> --root ./data

```

try to include --root ./data in your code

---

## Post #353

- **Author**: 23f2002205
- **Posted on**: 2025-02-15T03:47:05.826Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/353

sorry i forgot the change the name of function\_schema to tools please you do that

---

## Post #354

- **Author**: 22f3002248
- **Posted on**: 2025-02-15T04:05:04.243Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/354

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Hello,  
just a silly question, if my code runs well in docker environment with `/data` in root directory, will it be fine ?  
or should i keep the relative `./data` directory like in the lecture ?  
Thanks

---

## Post #355

- **Author**: carlton
- **Posted on**: 2025-02-15T04:22:25.373Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/355

The reason in the lecture they were using ./data was because they were debugging in their local machine not in the docker.

For the docker image (the official submission) you must use /data.  
It is a clear requirement mentioned in the project page.

Thats why it works fine when you use it in the docker image.

Kind regards

---

## Post #356

- **Author**: Atimanas
- **Posted on**: 2025-02-15T04:52:07.911Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/356

[![Screenshot 2025-02-15 101818](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/69011e1ad4ea3c00a9294163be28e49ebc671faa.png)

Screenshot 2025-02-15 101818858×521 24.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/69011e1ad4ea3c00a9294163be28e49ebc671faa.png "Screenshot 2025-02-15 101818")

  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
hello sir i need help here. I have pushed my image into a docker repo and trying to submit it on ht google form. but it is not accepting it and asking to remove the tag .  
What do i do ?

---

## Post #357

- **Author**: 22f3001011
- **Posted on**: 2025-02-15T05:05:47.472Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/357

Alright sir. Thank you very much for your help.

---

## Post #358

- **Author**: 22f3002034
- **Posted on**: 2025-02-15T06:03:11.059Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/358

Are multiple submissions allowed for project?

---

## Post #359

- **Author**: 23f2004912
- **Posted on**: 2025-02-15T06:20:07.084Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/359

[![A8](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/8/68423b54f8da150ecf68a17a19215d51def3ae83_2_281x500.jpeg)

A8720×1280 85.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/68423b54f8da150ecf68a17a19215d51def3ae83.jpeg "A8")

  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

please check this one…

---

## Post #360

- **Author**: 23f2005419
- **Posted on**: 2025-02-15T06:23:42.508Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/360

Hi [@carlton](/u/carlton) [@Jivraj](/u/jivraj) sir,

For A2 do i need to install node in the docker? I’m getting error with npx.  
please suggest some way sir?

---

## Post #361

- **Author**: 23f2004752
- **Posted on**: 2025-02-15T06:23:48.438Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/361

if i have two repo on docker , is there any problem in that

---

## Post #362

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T07:15:04.110Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/362

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b63973070de46f577b8184dd1cdeae4449e60a64.png)

image684×316 12.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b63973070de46f577b8184dd1cdeae4449e60a64.png "image")

  
why do i get this error? can someone please help me out [@Jivraj](/u/jivraj) [@carlton](/u/carlton)…Anyone pls help

---

## Post #363

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T07:20:31.804Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/363

can u please share the base proxy url

---

## Post #364

- **Author**: Samra
- **Posted on**: 2025-02-15T07:47:01.264Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/364

I’m also getting the same error. I have used a proxy URL and token. Before, it was working, but now it’s not.

---

## Post #365

- **Author**: 23f2005702
- **Posted on**: 2025-02-15T07:59:47.243Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/365

sir or anyone can you please provide what should be the content inside the docker file … i am getting confuse like /data or python-slim etc  
… i am done with locally testing and only this thing left.

---

## Post #366

- **Author**: 23f2002592
- **Posted on**: 2025-02-15T08:02:21.376Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/366

yes please explain somebody. What should be inside the dockerfile

---

## Post #367

- **Author**: 23f2005419
- **Posted on**: 2025-02-15T08:08:08.614Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/367

Hi ,

Anyone completed Task B, I don’t know how to combine task A (function calling) and task B (self creating python code)

can anyone suggest how to do that? It will be really helpful

---

## Post #368

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T08:20:53.033Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/368

“<http://aiproxy.sanand.workers.dev/openai/v1>” use this as proxy URL. its working for me now!

---

## Post #369

- **Author**: sarvan108
- **Posted on**: 2025-02-15T08:24:19.337Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/369

How to resolve this?  
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds\_pro$ uv run app.py  
Traceback (most recent call last):  
File “/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds\_pro/app.py”, line 10, in   
from fastapi import FastAPI  
ModuleNotFoundError: No module named ‘fastapi’  
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds\_pro$ pip show fastapi  
WARNING: Package(s) not found: fastapi  
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds\_pro$ pip install fastapi  
error: externally-managed-environment

× This environment is externally managed  
╰─> To install Python packages system-wide, try apt install  
python3-xyz, where xyz is the package you are trying to  
install.

```
If you wish to install a non-Debian-packaged Python package,
create a virtual environment using python3 -m venv path/to/venv.
Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
sure you have python3-full installed.

If you wish to install a non-Debian packaged Python application,
it may be easiest to use pipx install xyz, which will manage a
virtual environment for you. Make sure you have pipx installed.

See /usr/share/doc/python3.12/README.venv for more information.

```

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.  
hint: See PEP 668 for the detailed specification.

---

## Post #370

- **Author**: 23f2001286
- **Posted on**: 2025-02-15T08:35:27.325Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/370

sir,  
It is a humble requests from my side, to plz extend the deadline.  
Because student like who come from non technical background, are unable to come up with this project…  
though we have somehow comeup with the GAs taking the helps of groups, seniors and sessions.  
Moreover I am Dual Degree student. It is very hectic for me.  
Sir you won’t believe but I am continuously trying since last week. Specially after the release of the sessions… Whole day and night have gone like nothing, infront of the computer…  
Plz sir understand the situation and extend the deadline…

---

## Post #371

- **Author**: Samra
- **Posted on**: 2025-02-15T08:39:19.292Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/371

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003413/48/66883_2.png) 23f2003413:

> <http://aiproxy.sanand.workers.dev/openai/v1>

For me it says invalid path

---

## Post #372

- **Author**: 21f3002277
- **Posted on**: 2025-02-15T08:39:42.373Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/372

![Screenshot 2025-02-15 140726](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/4/545dc513707cfdd63db2d8d88d8c355d88316c55.png)

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #373

- **Author**: 22f3002319
- **Posted on**: 2025-02-15T08:43:54.893Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/373

same issue happening with me even though working for last whole week only got 4 correct . please extend some time so we can complete the project as weekends are the time when we get a day off from our primary college and can work with full attention on this project.

---

## Post #374

- **Author**: Jaideep
- **Posted on**: 2025-02-15T08:59:45.643Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/374

it usually happens in some GNU/Linux OS. since you are using some distribution based on Debian namely Ubuntu or whatever try doing sudo apt install python-packagename (replace package name with fastapi for fastapi)  
then it works. It usually happens due to manual intervention with pip3 the user might break some system dependencies which require some python3 package. No need to worry about it.  
Another Fix: try using a virtual environment which is highly suggested since there is no chance for you to interfere with the system packages.  
create a venv using python3 -m venv name\_of\_venv  
add this line to your .bashrc in ~ folder as source /path/to/your/venv/location  
and run source .bashrc. This time no error occurs as you do everything in your virtual environment you can install anything python3 package using pip3 install package name.  
It even happened for me

[![Screenshot_20250215_143357](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac_2_690x181.png)

Screenshot\_20250215\_1433573841×1009 237 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac.png "Screenshot_20250215_143357")

---

## Post #375

- **Author**: carlton
- **Posted on**: 2025-02-15T09:03:19.240Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/375

Most of your questions and doubts will be solved in todays sessions. First 20 mins will be a clear overview of the logic and workflow and how evaluation actually works.  
Rest of the session will be bug fixing and doubts.

Kind regards

---

## Post #376

- **Author**: Jayeshbansal
- **Posted on**: 2025-02-15T09:10:10.123Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/376

![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") EXPECTED:  
Everybody significant bank herself them process build body. Price live size. Assume begin better language east like machine.  
New customer green strategy.  
Feeling stock experience certainly history talk buy. Quality perform appear human general religious feeling. Kid indicate fear word win carry.  
During professional sport growth citizen glass great student. Exactly receive cause. Couple off current between role natural.  
Wind develop world next. Impact appear capital cold stock we. Quality get run case huge that.  
Use century general above more region. Radio him quality stage. Truth least military dinner growth.  
Study maybe source. For expect imagine.  
Analysis remain voice dog sit part. Safe them store spring life girl.  
House bring challenge. Tell but rock able great.  
Mouth president worker common Mr billion.

![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") RESULT:  
“Everybody significant bank herself them process build body. Price live size. Assume begin better language east like machine.\nNew customer green strategy.\nFeeling stock experience certainly history talk buy. Quality perform appear human general religious feeling. Kid indicate fear word win carry.\nDuring professional sport growth citizen glass great student. Exactly receive cause. Couple off current between role natural.\nWind develop world next. Impact appear capital cold stock we. Quality get run case huge that.\nUse century general above more region. Radio him quality stage. Truth least military dinner growth.\nStudy maybe source. For expect imagine.\nAnalysis remain voice dog sit part. Safe them store spring life girl.\nHouse bring challenge. Tell but rock able great.\nMouth president worker common Mr billion.”  
it is the error i am facing but when i am opening manually, i am not getting any error, what should I do?  
this same issue is with 3-4 questions

---

## Post #377

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T10:02:56.723Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/377

when will the session be conducted and how can we join it sir?

---

## Post #378

- **Author**: sarvan108
- **Posted on**: 2025-02-15T10:03:30.828Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/378

Hi Thanks.  
Yes. it works when venv is created. But I see that it was working find in Week 5-Session 1 video without creating virtual environment.

---

## Post #379

- **Author**: 21f1003816
- **Posted on**: 2025-02-15T10:12:37.060Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/379

I will not submit project.

---

## Post #380

- **Author**: Jivraj
- **Posted on**: 2025-02-15T10:27:38.324Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/380

Get authentication token from this [AI Proxy](https://aiproxy.sanand.workers.dev/) and usage and follow documentation for sending requests.  
[sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)

---

## Post #381

- **Author**: Jivraj
- **Posted on**: 2025-02-15T10:28:22.183Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/381

No Problems, just fill form with correct image name in google forms.

---

## Post #382

- **Author**: Jivraj
- **Posted on**: 2025-02-15T10:28:56.422Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/382

yes npx will require node to be installed.

---

## Post #383

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T10:31:05.324Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/383

[@Jivraj](/u/jivraj) when would today’s live session be conducted and how can we attend it sir

---

## Post #384

- **Author**: Rrishit
- **Posted on**: 2025-02-15T10:45:33.373Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/384

evaluate.py is not working sir.

---

## Post #385

- **Author**: 24f2000074
- **Posted on**: 2025-02-15T10:53:42.320Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/385

What if you run out of credits during or just before final evaluation?

---

## Post #386

- **Author**: Jivraj
- **Posted on**: 2025-02-15T11:07:54.170Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/386

This is only for testing on local machine.

In docker image keep /data.

---

## Post #387

- **Author**: Jivraj
- **Posted on**: 2025-02-15T11:09:03.532Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/387

One session is going live right now (from 3 to 5 pm).  
It will be visible from calendra.

---

## Post #388

- **Author**: Vedant22
- **Posted on**: 2025-02-15T11:15:05.016Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/388

sir,  
It is a humble requests from my side, to plz extend the deadline.  
Because student like who come from non technical background, are unable to come up with this project…  
though we have somehow comeup with the GAs taking the helps of groups, seniors and sessions.  
Moreover I am Dual Degree student. It is very hectic for me.  
Sir you won’t believe but I am continuously trying since last week. Specially after the release of the sessions… Whole day and night have gone like nothing, infront of the computer…  
Plz sir understand the situation and extend the deadline…

---

## Post #389

- **Author**: sharma_abhay
- **Posted on**: 2025-02-15T11:15:42.013Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/389

Sir, I have put my AIPROXY\_TOKEN in .env file should I need to push the .env file also in the github

---

## Post #391

- **Author**: Namannn28
- **Posted on**: 2025-02-15T11:21:06.394Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/391

yes sir do we have to put env file also [@carlton](/u/carlton) sir [@Jivraj](/u/jivraj) sir

---

## Post #392

- **Author**: 23f2001286
- **Posted on**: 2025-02-15T11:31:22.936Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/392

In the evaluation.py there is an import require named from datagen import some stuff.  
which means inorder to run the evaluation.py we need to manually bring the datagen.py in the working directory…

Because in order to run the evaluation.py we need the datagen. plz help…

---

## Post #393

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T11:32:33.850Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/393

can someone send the meet link for the live session happening now

---

## Post #394

- **Author**: Kabir1203
- **Posted on**: 2025-02-15T11:38:34.015Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/394

Everytime I run datagen.py for the A1 task, the data file gets downloaded in the C drive instead of the current project folder. I even tried to set the current project folder as the root directory but it still downloads the files in C drive and I cant seem to find a workaround this. Can someone please help with this issue. Thanks!

---

## Post #395

- **Author**: Kabir1203
- **Posted on**: 2025-02-15T11:42:30.317Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/395

Can you please make the changes in the datagen.py file

config = {“root”: “/data”}

This is where I have been facing the issue.

The only solution I can think of is moving the /data folder from the root to the project directory. which I am not sure is a good way to solve this issue.

---

## Post #396

- **Author**: gouthamnischay
- **Posted on**: 2025-02-15T12:03:17.621Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/396

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/ef51e62fc93908c084aebcfe587121a226bb1397.jpeg "TDS Jan 2025 Live Stream")](https://www.youtube.com/watch?v=NkUmOagUORE)

---

## Post #397

- **Author**: 23f2001978
- **Posted on**: 2025-02-15T12:04:54.730Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/397

[@carlton](/u/carlton)

please tell do we have to put this url in a variable for A1 task ?

<https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py>

---

## Post #398

- **Author**: Nelson
- **Posted on**: 2025-02-15T12:06:18.314Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/398

Task A9 fails.

> HTTP Request: POST <https://aiproxy.sanand.workers.dev/openai/v1/embeddings> “HTTP/1.1 401 Unauthorized”  
> ![:red_circle:](https://emoji.discourse-cdn.com/google/red_circle.png?v=12 ":red_circle:") A9 failed: ‘data’  
> ![:x:](https://emoji.discourse-cdn.com/google/x.png?v=12 ":x:") A9 FAILED

If I run

```
curl -X POST http://aiproxy.sanand.workers.dev/openai/v1/embeddings -H "Content-Type: application/json" -H "Authorization: Bearer $AIPROXY_TOKEN" -d '{"model": "text-embedding-3-small", "input": ["king", "queen"]}'

```

I get

```
{
  "message": "Missing Authorization: Bearer header. See https://github.com/sanand0/aiproxy"
}

```

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---

## Post #399

- **Author**: 23f1002279
- **Posted on**: 2025-02-15T12:08:35.195Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/399

[@carlton](/u/carlton) sir [@Jivraj](/u/jivraj) sir do i have to put env file in docker

---

## Post #400

- **Author**: 22f3002248
- **Posted on**: 2025-02-15T12:23:41.857Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/400

you have to give the `AIPROXY_TOKEN` to the evaluate.py by either  
bash - `export AIPROXY_TOKEN="your token"`  
or  
powershell - `$env:AIPROXY_TOKEN="your token"`  
the evaluate.py file takes the token to send request to embedding end point for processing.  
so you have to set `AIPROXY_TOKEN` in both terminals  
i.e. app.py and evaluate.py teminals

---

## Post #401

- **Author**: Kabir1203
- **Posted on**: 2025-02-15T12:29:10.140Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/401

when I run the evaluation file, i get the following error - ![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py` with `user@example.com` as the only argument ![:red_circle:](https://emoji.discourse-cdn.com/google/red_circle.png?v=12 ":red_circle:") A1 failed: All connection attempts failed ![:x:](https://emoji.discourse-cdn.com/google/x.png?v=12 ":x:") A1 FAILED

I am getting the following error when running the evaluation scripts, can someone help me understand what this error is?

---

## Post #402

- **Author**: koustubhr
- **Posted on**: 2025-02-15T12:34:03.097Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/402

Humble request to extend the deadline please. Finding it extremely difficult and having time atleast till Sunday will be really helpful for working professionals like me

---

## Post #403

- **Author**: Nelson
- **Posted on**: 2025-02-15T12:58:45.926Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/403

All my tasks are running except A9. I have created a .env file and added my token. Despite that I ran commands in both the terminals. A9 still fails.

---

## Post #404

- **Author**: Kabir1203
- **Posted on**: 2025-02-15T12:59:11.585Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/404

I second this, have been trying to debug the project for the past 1 week, spending over 4 hours daily and yet facing issues everytime I reopen. An extension of even 24 hours would be extremely appreciated. Please consider this. Thanks.

---

## Post #405

- **Author**: 23f2001978
- **Posted on**: 2025-02-15T13:09:56.100Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/405

same issue on my side as well

---

## Post #406

- **Author**: 23f2001978
- **Posted on**: 2025-02-15T13:10:27.279Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/406

how u did A2  
could u please share ?

---

## Post #408

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T13:21:11.144Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/408

[@s.anand](/u/s.anand) [@jivraj](/u/jivraj) [@carlton](/u/carlton)  
AIPROXY\_TOKEN=$AIPROXY\_TOKEN  
what abt m url stuff?

---

## Post #409

- **Author**: NarendraAbhiyantrik
- **Posted on**: 2025-02-15T13:24:31.715Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/409

Sir, I request you to Please extend the deadline, Because it is time consuming and regular Students and Working professionals have only saturday and sunday to complete this project.

Thanks

---

## Post #410

- **Author**: 22f3002248
- **Posted on**: 2025-02-15T13:32:08.963Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/410

also, in evaluate.py file, the embedding url is wrong and the AIPROXY\_TOKEN is changed to OPENAI\_API\_TOKEN or something. i could send you edited evaluate.py… check your messages on discourse

---

## Post #411

- **Author**: Nelson
- **Posted on**: 2025-02-15T13:40:33.913Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/411

On bash it gives below output. On PowerShell it says missing authorization. A9 is failed.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/040960e1d380f811ec53df35434564307fbd8388.png)

image907×661 26.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/040960e1d380f811ec53df35434564307fbd8388.png "image")

In PowerShell  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd8b1f78ee2e9e130956f545a8e96d89d6785b2e.png)

image967×292 16.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd8b1f78ee2e9e130956f545a8e96d89d6785b2e.png "image")

---

## Post #412

- **Author**: Kabir1203
- **Posted on**: 2025-02-15T13:45:17.659Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/412

My data is getting generated -  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ffe4cd24a993c763714ff420d85a202940240cfa.png)

image459×454 12.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ffe4cd24a993c763714ff420d85a202940240cfa.png "image")

  
despite this I am getting an error when evaluating the file with no explanation of the error. Can someone please help with this.  
![:yellow_circle:](https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12 ":yellow_circle:") Running task: Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py`  
with `user@example.com` as the only argument

![:red_circle:](https://emoji.discourse-cdn.com/google/red_circle.png?v=12 ":red_circle:") A1 failed:

![:x:](https://emoji.discourse-cdn.com/google/x.png?v=12 ":x:") A1 FAILED

---

## Post #413

- **Author**: Kabir1203
- **Posted on**: 2025-02-15T13:47:58.449Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/413

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ffcb4192d3b1be3bc881e54720f2baa8d1b8a51e.png)

image820×404 12.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ffcb4192d3b1be3bc881e54720f2baa8d1b8a51e.png "image")

  
Even the markdown file shows the correct email. What are the possible issues that I could be facing with this one.

---

## Post #414

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T13:57:58.100Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/414

![](https://github.githubassets.com/favicons/favicon.svg)
[github.com](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main)

### [GitHub - ANdIeCOOl/TDS-Project-1](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main)

[main](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main)

Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.

ATLEAST 6 minimum score use at own risk(MIT LICENCE xD)  
  
  
BUILD TIME TAKES 2 mins  
WITH DOCKER FILE

```
@ANdIeCOOl ➜ /workspaces/TDS-Project-1/tds-project-1 (main) $ docker build -t tds-project-1 .
[+] Building 123.9s (13/13) FINISHED                                                                       docker:default
 => [internal] load build definition from Dockerfile                                                                 0.0s
 => => transferring dockerfile: 1.18kB                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                  2.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                        0.0s
 => [internal] load .dockerignore                                                                                    0.0s
 => => transferring context: 2B                                                                                      0.0s
 => [internal] load build context                                                                                    0.1s
 => => transferring context: 34.30kB                                                                                 0.0s
 => [1/7] FROM docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8  8.7s
 => => resolve docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8  0.0s
 => => sha256:2c2c44fb54acb184dbedee948d7ba6460b1075a60a014d66857ce46543d4d840 5.29kB / 5.29kB                       0.0s
 => => sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260 28.21MB / 28.21MB                     0.7s
 => => sha256:73c4bbda278d9a2b5133d6dabfac3eec43a92b8c8c15da914f298b4c966bea53 3.51MB / 3.51MB                       0.9s
 => => sha256:acc53c3e87ac87c98e44b79e0d2a6293146650f5cba576f424dab77f8c0a4335 16.20MB / 16.20MB                     1.6s
 => => sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8b52eda 9.13kB / 9.13kB                       0.0s
 => => sha256:a66bd09b8d35bb52cd106a94c23a94ba22e6fde6bd13d6c5912ec4f5888a7f14 1.75kB / 1.75kB                       0.0s
 => => extracting sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260                            2.2s
 => => sha256:ad3b14759e4f8c9a73d51c897a8b96f022ec96ffc237502ad3f1f12b0b0e361f 249B / 249B                           1.9s
 => => extracting sha256:73c4bbda278d9a2b5133d6dabfac3eec43a92b8c8c15da914f298b4c966bea53                            0.2s
 => => extracting sha256:acc53c3e87ac87c98e44b79e0d2a6293146650f5cba576f424dab77f8c0a4335                            1.4s
 => => extracting sha256:ad3b14759e4f8c9a73d51c897a8b96f022ec96ffc237502ad3f1f12b0b0e361f                            0.0s
 => [2/7] WORKDIR /app                                                                                               0.2s
 => [3/7] RUN pip install --upgrade pip setuptools wheel                                                             8.7s
 => [4/7] RUN apt-get update && apt-get install -y --no-install-recommends     gcc     g++     make     libffi-dev  84.5s
 => [5/7] RUN npm install -g prettier                                                                                1.5s
 => [6/7] COPY app /app                                                                                              0.1s
 => [7/7] RUN pip install uv                                                                                         4.5s
 => exporting to image                                                                                              13.4s
 => => exporting layers                                                                                             13.4s
 => => writing image sha256:39add91710bc7970d44dae04b3f4a0c4f227d1471fac4df7b01cec86ce7af3cf                         0.0s
 => => naming to docker.io/library/tds-project-1                                                                     0.0s

```

@ANdIeCOOl ➜ /workspaces/TDS-Project-1/tds-project-1 (main) $ docker images  
REPOSITORY TAG IMAGE ID CREATED SIZE  
tds-project-1 latest 39add91710bc 31 seconds ago 923MB

if this cause any issues please notify [@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #415

- **Author**: 23f3000709
- **Posted on**: 2025-02-15T14:00:16.470Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/415

in phase B tasks are we supposed to create files to store the output or return it in the response ???

Please answer ASAP sir.

---

## Post #416

- **Author**: lakshaygarg654
- **Posted on**: 2025-02-15T14:02:17.277Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/416

[@s.anand](/u/s.anand)  
Respected Sir,  
I sincerely request you to kindly consider granting a one-day extension for Project 1. Many key clarifications were provided in today’s session, and we need just one additional day to effectively implement them. This extension would be immensely helpful in ensuring a more refined submission.  
I truly appreciate your time and consideration.  
Thank you.

---

## Post #418

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T14:07:14.907Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/418

@all can everyone please test my image and let me know PLEASE. THIS IS THE MOST YOU ALL CAN DO FOR ME. I WILL BE BERY GRATEFUL

![](https://github.githubassets.com/favicons/favicon.svg)
[github.com](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main)

### [GitHub - ANdIeCOOl/TDS-Project-1](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main)

[main](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main)

Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.

---

## Post #419

- **Author**: 23f3000709
- **Posted on**: 2025-02-15T14:08:05.189Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/419

hey I have a few doubts, if something was said about this please say so.

1. in Phase be tasks do we have to store the output in files or just return it in the response
2. When I call my some of my endpoints using post man or CURL they work but if I run the evaluate.py it throws an error, this I think is a bug in the eval.py file.

any idea about these ?

---

## Post #420

- **Author**: 22f3002723
- **Posted on**: 2025-02-15T14:22:28.484Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/420

facing the issue on submission  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/9/89bdffb424290fa15cf3f07c367b81fac5898b12_2_690x381.png)

image942×521 28.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/9/89bdffb424290fa15cf3f07c367b81fac5898b12.png "image")

---

## Post #421

- **Author**: 22f3002723
- **Posted on**: 2025-02-15T14:25:14.239Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/421

please ignore the above… there was a upper case issue in image name… now fine

---

## Post #422

- **Author**: Sagan
- **Posted on**: 2025-02-15T14:35:04.549Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/422

Is it import to use python 3.13?  
It is not stable yet

---

## Post #423

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T14:38:13.967Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/423

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d64ee81798b48ccad186d5051823d3f565424bc2.png)

image1831×146 7.91 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d64ee81798b48ccad186d5051823d3f565424bc2.png "image")

  
can someone help me fix this error [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

## Post #424

- **Author**: abhigyandsa
- **Posted on**: 2025-02-15T14:40:37.732Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/424

for the datagen script is it ok to hardcode the scripts url and my email id? I understand the script itself may change but can I count on the link remaining the same? Also is it necessary to pass the email as argument?

---

## Post #425

- **Author**: TheVishal
- **Posted on**: 2025-02-15T14:41:38.706Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/425

from dotenv import load\_dotenv  
load\_dotenv()

---

## Post #426

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T14:45:08.620Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/426

yahh i have it in my code…still facing the issue

---

## Post #427

- **Author**: abhigyandsa
- **Posted on**: 2025-02-15T14:55:45.137Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/427

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [filler to extend length]

---

## Post #429

- **Author**: 24ds3000061
- **Posted on**: 2025-02-15T15:05:52.096Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/429

whats the image’s name on Docker?

---

## Post #430

- **Author**: 23f2004936
- **Posted on**: 2025-02-15T15:05:54.911Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/430

just completed my sem exams started worrking on the project from 2 days please give extension of deadline for the project sir

---

## Post #431

- **Author**: 23f2003751
- **Posted on**: 2025-02-15T15:32:09.297Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/431

dont we have to add the data folder or folder like datagen in the repo?

---

## Post #432

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T15:33:23.890Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/432

thats confidential, im not an idiot xD, that will get me definitely in trouble

---

## Post #433

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T15:33:55.303Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/433

no, not really . Just your app

---

## Post #434

- **Author**: 23f2003751
- **Posted on**: 2025-02-15T15:42:54.272Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/434

in your project,in the app folder you have the data folder which is empty so should I keep that or remove it

---

## Post #435

- **Author**: 23f2003751
- **Posted on**: 2025-02-15T15:45:15.797Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/435

and also will u be making any chnages in the repo

---

## Post #436

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T15:47:05.777Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/436

File “/app/app.py”, line 35, in   
client = OpenAI(  
^^^^^^^  
File “/usr/local/lib/python3.12/site-packages/openai/\_client.py”, line 110, in **init**  
raise OpenAIError(  
openai.OpenAIError: The api\_key client option must be set either by passing api\_key to the client or by setting the OPENAI\_API\_KEY environment variable some pls help me fix this error!!

---

## Post #437

- **Author**: Jivraj
- **Posted on**: 2025-02-15T16:01:54.136Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/437

Blunder in your `main.py`.  
You are using API\_KEY = os.getenv(“AI\_PROXY\_TOKEN”) but it should be AIPROXY\_TOKEN.

Btw what you using for phase B?

---

## Post #438

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T16:03:05.233Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/438

yes i will change that

---

## Post #439

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T16:03:54.280Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/439

nothing i think, i’ll import those generic functions and use tool usage only probably if can’t crack dynamic code generation

---

## Post #440

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T16:04:55.343Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/440

i don’t have that

![](https://github.githubassets.com/favicons/favicon.svg)
[github.com](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app)

### [TDS-Project-1/tds-project-1/app at main · ANdIeCOOl/TDS-Project-1](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app)

Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.

---

## Post #441

- **Author**: Jivraj
- **Posted on**: 2025-02-15T16:05:12.024Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/441

What we expect in project.

1. server running inside docker container at 8000.
2. And all files will be accessed from data folder in root directory.

Apart from these two you can have anything extra.

---

## Post #442

- **Author**: 21f2000710
- **Posted on**: 2025-02-15T16:05:55.854Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/442

[![Screenshot 2025-02-15 212826](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/68c6be0490c5eb006c1edaa43f50996e440f8a03.png)

Screenshot 2025-02-15 2128261903×492 32.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/68c6be0490c5eb006c1edaa43f50996e440f8a03.png "Screenshot 2025-02-15 212826")

  
how to fix this error ?

---

## Post #443

- **Author**: Jivraj
- **Posted on**: 2025-02-15T16:05:58.397Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/443

What problem you facing with that dynamic code generation part?

---

## Post #444

- **Author**: 23f2001413
- **Posted on**: 2025-02-15T16:06:26.583Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/444

I have exhausted my api limit of $2. I need to test my project. Can you please provide some more credits? [@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

## Post #445

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T16:07:35.874Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/445

no problem but im losing steam slowly, i need to buckle up and PUSH [@Jivraj](/u/jivraj)

---

## Post #446

- **Author**: 23f2004644
- **Posted on**: 2025-02-15T16:08:57.535Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/446

**Subject:** Request for Project Deadline Extension

Dear Sir,

This project is highly complex, and we need additional time to ensure its successful completion. We kindly request an extension of the deadline to allow for thorough testing and proper implementation. An extension would greatly help us deliver the best results.

Thank you for your understanding [@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

## Post #447

- **Author**: Jivraj
- **Posted on**: 2025-02-15T16:13:14.808Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/447

This might be problem with network settings(unstable internet, firewall, VPN interference)

try to debug it with help of chatgpt.

You can also use codespaces for trying another network.

[Streamlining setup with GitHub Codespaces](https://www.youtube.com/watch?v=fqQOu2JVI1o)

---

## Post #448

- **Author**: Jivraj
- **Posted on**: 2025-02-15T16:13:42.738Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/448

Push push [@23f1002382](/u/23f1002382)

---

## Post #449

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T16:18:02.598Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/449

[@Jivraj](/u/jivraj) is it fine if i have my AIPROXY\_TOKEN in my code instead of getting it as environment variable?

---

## Post #450

- **Author**: 23f2001413
- **Posted on**: 2025-02-15T16:20:06.323Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/450

if you do that then during evaluation, it would use your credit limit. if it gets exhausted, you may face problems. [@23f2003413](/u/23f2003413)

---

## Post #451

- **Author**: 23f2003751
- **Posted on**: 2025-02-15T16:21:10.108Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/451

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/e/ce7f8f838b86960153991fdea76f15b4a50f80f7.png)

image266×559 12.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/e/ce7f8f838b86960153991fdea76f15b4a50f80f7.png "image")

  
this is what i am doing first using the podman given in the portal and then running the evaluate.py file

---

## Post #452

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T16:21:31.012Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/452

ahhh okay, but i am getting an error while trying to fetch the token as an environment variable. any suggestions to fix this issue?

---

## Post #453

- **Author**: 23f2001413
- **Posted on**: 2025-02-15T16:22:17.623Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/453

you can use python-dotenv. check that out.

---

## Post #454

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T16:23:07.849Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/454

tried that still not getting T\_T anyways thanks mate!

---

## Post #455

- **Author**: Jivraj
- **Posted on**: 2025-02-15T16:25:07.138Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/455

No don’t do that, just follow the procedure.  
Two problems with keeping token in file.

1. It will become public after you push to github.
2. While running evaluation script after submission your token might run out of credits.

---

## Post #456

- **Author**: 24ds3000061
- **Posted on**: 2025-02-15T16:27:24.797Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/456

ohh yes, didn’t think it through xD

---

## Post #457

- **Author**: 22f3000880
- **Posted on**: 2025-02-15T16:29:14.206Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/457

I am facing the same error. and I have checked for solutions and found none. Did you resolve it? If yes can you please guide me through it?

---

## Post #458

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T16:34:00.432Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/458

{  
“detail”: “Error code: 401 - {‘error’: {‘message’: ‘Your authentication token is not from a valid issuer.’, ‘type’: ‘invalid\_request\_error’, ‘param’: None, ‘code’: ‘invalid\_issuer’}}”  
} getting this error sir

---

## Post #459

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T16:40:47.374Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/459

![](https://github.githubassets.com/favicons/favicon.svg)
[github.com](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app)

### [TDS-Project-1/tds-project-1/app at main · ANdIeCOOl/TDS-Project-1](https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app)

Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.

i keep updating, check this

---

## Post #460

- **Author**: AyushTiwari
- **Posted on**: 2025-02-15T16:47:32.801Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/460

Please extend deadline by 1 day. i just got discharged from hospital today, was suffering from liver problem since some days and got high heart beat due to a medicine unrelated to liver and made me got admitted@Jivraj

---

## Post #461

- **Author**: 23f1002382
- **Posted on**: 2025-02-15T16:49:06.628Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/461

11:59 + 5 hours atthe most, [@s.anand](/u/s.anand) ? ![:face_holding_back_tears:](https://emoji.discourse-cdn.com/google/face_holding_back_tears.png?v=12 ":face_holding_back_tears:") ![:face_holding_back_tears:](https://emoji.discourse-cdn.com/google/face_holding_back_tears.png?v=12 ":face_holding_back_tears:") ![:face_holding_back_tears:](https://emoji.discourse-cdn.com/google/face_holding_back_tears.png?v=12 ":face_holding_back_tears:")

---

## Post #462

- **Author**: jkmadathil
- **Posted on**: 2025-02-15T20:11:45.990Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/462

11 posts were split to a new topic: [Project 1 - Casual banter](/t/project-1-casual-banter/167344)

---

## Post #467

- **Author**: 23f1002279
- **Posted on**: 2025-02-15T16:59:47.955Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/467

[@Jivraj](/u/jivraj) sir [@carlton](/u/carlton) sir do have to add datagen in the docker container?  
As when I’m running it locally, it gives 9/10, but when I pull it from Hub and run eval, it says:detail": “[Errno 2] No such file or directory: ‘/data/datagen.py’”

---

## Post #469

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T17:03:12.600Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/469

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a4995efdbe57c4d2d865982896333f8faf0c8c.png)

image706×193 6.15 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a4995efdbe57c4d2d865982896333f8faf0c8c.png "image")

  
someone please help me fix this error

---

## Post #475

- **Author**: rohitgarg
- **Posted on**: 2025-02-15T17:10:19.057Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/475

[@carlton](/u/carlton) can you pl merge this

[github.com/sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public/pull/7)

#### [Update evaluate.py with correct link of datagen.py for task `A1`](https://github.com/sanand0/tools-in-data-science-public/pull/7)

`tds-2025-01` ← `rohitxiitm:patch-1`

opened 10:56AM - 15 Feb 25 UTC

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/c/8c0f24d20066c96d044a995469181fefafc28aff.jpeg)
rohitxiitm](https://github.com/rohitxiitm)

[+1
-1](https://github.com/sanand0/tools-in-data-science-public/pull/7/files)

ppl are facing issues in evaluate.py for task A2

---

## Post #476

- **Author**: rohitgarg
- **Posted on**: 2025-02-15T17:15:51.605Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/476

folks, need a confirmation. i don’t know but i heard it from someone or somewhere.  
we cannot send json in response, if it is success ? need to send text

is that really the case ?

---

## Post #477

- **Author**: s.anand
- **Posted on**: 2025-02-15T17:21:01.750Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/477

[@rohitgarg](/u/rohitgarg) - thanks for this. Merged your PR pointing to the correct link for `evaluate.py`

---

## Post #478

- **Author**: 23F3004407_RATANPRIY
- **Posted on**: 2025-02-15T18:07:41.953Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/478

Sir from which session to which session is about tds project?

---

## Post #479

- **Author**: 23f2003413
- **Posted on**: 2025-02-15T18:22:39.454Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/479

week-5 session-1 & week-5 session-3

---

## Post #481

- **Author**: 23f3004114
- **Posted on**: 2025-02-15T18:38:04.029Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/481

Here is a Bruno collection (open source alternate for postman) for API testing A1 to A6  
[bruno collection](https://drive.google.com/file/d/11TsXO3_uOnKtHxN7hTgmzdX5Cszc2IUc/view?usp=sharing)

---

## Post #484

- **Author**: abhigyandsa
- **Posted on**: 2025-02-15T18:44:11.463Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/484

On my system evaulate.py is throwing an error on A2 trying to execute npx on format.md before the llm is even invoked. However running the command directly on the command line works.

evaluate.py:  
![:red_circle:](https://emoji.discourse-cdn.com/google/red_circle.png?v=12 ":red_circle:") A2 failed: Command ‘[‘npx’, ‘prettier@3.4.2’, ‘–stdin-filepath’, ‘data/format.md’]’ returned non-zero exit status 2.

![:x:](https://emoji.discourse-cdn.com/google/x.png?v=12 ":x:") A2 FAILED

bash:  
npx prettier@3.4.2 --stdin-filepath data/format.md

bash works as expected. Can someone help?

---

## Post #485

- **Author**: 22f3001777
- **Posted on**: 2025-02-15T18:56:27.273Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/485

[@carlton](/u/carlton)  
Is there a maximum size limit for the Docker Image?

Thanking you

---

## Post #486

- **Author**: RoyalAagman
- **Posted on**: 2025-02-15T19:34:01.014Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/486

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

Hi ,

I am trying to build using both docker and podman but it failed on both. I have watched many videos trying to resolve this adn also chatgpt in order to resolve the issue but it seems to persist. I even uninstalled and reinstalled both podman and doceker multiple times but no help.

When i run command docker build -t \_\_\_\_\_\_\_\_\_\_\_ .

the error that comes is :

Dockerfile:2
------------

1 | # Use a lightweight Python image 
2 | >>> FROM python:3.12-slim 
3 | 
4 | # Set the working directory in the container
--------------------------------------------------------------------------------------------------------------------------

ERROR: failed to solve: python:3.12-slim: failed to resolve source metadata for [Docker Hub Container Image Library | App Containerization](http://docker.io/library/python:3.12-slim:) failed to copy: httpReadSeeker: failed open: failed to do request: Get “<https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/6f/6f3c6367c5a38963f84310cbb24dfcfbddab1dad40cff18afb8fe89098891f08/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250215%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250215T192245Z&X-Amz-Expires=1200&X-Amz-SignedHeaders=host&X-Amz-Signature=ed37cf0c346e2ed440f29638ec43ce66640bdc7d285e7be7bf25c308c46fd6b1>”: dialing [docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443](http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443) container via direct connection because static system has no HTTPS proxy: connecting to [docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443](http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443): dial tcp: lookup [docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com](http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com): no such host

Even tried getting python:3.12-slim separatly and trying again but that also didn’t work.  
I think there is some problem in getting python:3.12-slim as the build always stops at this.

on asking ChatGPT it shows that some DNS or network issue is there. I even tried all the remedy that was provided on creating custom network etc. but this was also of no use

Kindly help me finding solution to this and pls mention any other assistance I may require to get this running

Thank You.  
Regards,  
Aagman

---

## Post #487

- **Author**: 22f3000639
- **Posted on**: 2025-02-15T19:53:57.298Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/487

i am getting this error, I have tried many times but still the error persists:  
“message”: “Bearer YOUR\_AIPROXY\_TOKEN is invalid: JWSInvalid: Invalid Compact JWS”

---

## Post #488

- **Author**: 22f3000639
- **Posted on**: 2025-02-15T19:56:55.979Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/488

someone please help!!!

---

## Post #490

- **Author**: rohitgarg
- **Posted on**: 2025-02-15T19:59:52.597Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/490

[@carlton](/u/carlton) needed a confirmation on this task

`A8 * `/data/credit-card.png` contains a credit card number. Pass the image to an LLM, have it extract the card number, and write it without spaces to `/data/credit-card.txt` - in this task i assume prompt can ask for credit card number or other details like cvv and name.

My question is, whether my system should allow prompt that CVV or or such info ? or should give it ?

---

## Post #491

- **Author**: 23f2001413
- **Posted on**: 2025-02-15T20:29:22.437Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/491

1. Previously I asked for some more credits to test my project. I got an email stating I have been provided with a new token but I think I got that same token again, not a new one. I still cant send request to the AIPROXY. Please help.
2. Do I need to submit the docker image name with the tag or without the tag? I submitted it before without the tag. Now i see that I have tagged the image with as v1 but I cant submit the form due to pattern matching problems. Should i submit again after tagging it with :latest ?

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #492

- **Author**: 23f1002279
- **Posted on**: 2025-02-15T21:20:23.334Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/492

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir in the phase B will the input and output path will be given ?

---

## Post #493

- **Author**: 22f3000819
- **Posted on**: 2025-02-15T21:44:56.585Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/493

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
When I run my docker image using

`podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME`

Task A2 fails as the podman container is unable to find npx.

Running the same image using

`docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME`

works fine and Task A2 passes. I can’t understand why this is happening.

I also ran the image in both docker and podman in interactive mode as show in the below snippet from terminal.  
When run using docker, `which node` gives `/usr/bin/node` as output but when run using podman, nothing.

```
shiva@shiva:~/Desktop/tdsp1$ sudo podman run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo docker run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
/usr/bin/node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo podman run --user=root --rm -it docker.io/myusername/myreponame /bin/sh
# which node
# which node
# exit

```

---

## Post #494

- **Author**: 23f1003186
- **Posted on**: 2025-02-15T22:00:56.106Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/494

Here’s how to prompt folks. Just do what [@carlton](/u/carlton) mentioned in today’s live session (the 5 hour marathon) and you should be good for Project-1!

[x.com](https://x.com/aakashg0/status/1890492955842007087?s=46&t=U3mfkIFH433B6kVe5ZktSw)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/7/67f2a2d0db391947304ab4e006d7ea42c3b8850d.jpeg)

#### [Aakash Gupta](https://x.com/aakashg0/status/1890492955842007087?s=46&t=U3mfkIFH433B6kVe5ZktSw)

[@aakashg0](https://x.com/aakashg0/status/1890492955842007087?s=46&t=U3mfkIFH433B6kVe5ZktSw)

Most people are still prompting wrong.
I've found this framework, which was even shared by OpenAI President Greg Brockman.
Here’s how it works: [pic.x.com/2MMcEqBeIJ](https://x.com/aakashg0/status/1890492955842007087/photo/1)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/e/ce7a62f2fa1f33758771e9ef57dd90fe2d98b09d_2_502x500.jpeg)

[8:06 PM - 14 Feb 2025](https://x.com/aakashg0/status/1890492955842007087?s=46&t=U3mfkIFH433B6kVe5ZktSw)


5.5K


360

---

## Post #495

- **Author**: Yogesh1
- **Posted on**: 2025-02-15T23:08:34.656Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/495

Same issue. Got the same token. Can’t use it since 2 dollar limit has been crossed. Please help. [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #496

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T03:01:42.744Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/496

Yes I also need the answer of this.

---

## Post #497

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T03:03:43.445Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/497

Is there any way of figuring what is the usage of my token and if yes then how…  
Plz some peers help…

---

## Post #498

- **Author**: carlton
- **Posted on**: 2025-02-16T03:06:01.016Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/498

It will be corrected soon by [@jkmadathil](/u/jkmadathil)  
He is in charge of our budget for TDS and the tokens are being issued by him.

Please tag him for any token related issues.

---

## Post #499

- **Author**: jkmadathil
- **Posted on**: 2025-02-16T03:34:46.233Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/499

New token assigned to the students. Emails are also sent.

---

## Post #500

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T04:34:50.606Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/500

sir I am noticing a pattern, that when I am running the datagen first. And then using the evaluate.py, then I am getting the A2 right.  
But running the evaluation.py for the 2nd time cause the A2 to fail…  
Probabbly Because the file in the data folder gets upated should I worry for that…

---

## Post #501

- **Author**: Jayeshbansal
- **Posted on**: 2025-02-16T05:21:27.713Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/501

in the phase B, we have no idea about how many arguments are there, so should we make every function mapping with 2 arguments ( 1 containing the input location and other containing output location) or should we take the parameters in some other way

---

## Post #502

- **Author**: carlton
- **Posted on**: 2025-02-16T06:21:36.637Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/502

There has been an outage in some parts of the country related to cloudflare servers. What helped some students (and us) is using a completely different network eg. instead of using your home wifi, use mobile internet, since they go through a different DNS and this sometimes works.

Kind regards

---

## Post #503

- **Author**: carlton
- **Posted on**: 2025-02-16T06:22:27.485Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/503

We have not specified a size limit for the docker image, so in theory there is not a limit to the docker image size.

Kind regards

---

## Post #504

- **Author**: kushabarodekar
- **Posted on**: 2025-02-16T06:26:11.317Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/504

Hello [@carlton](/u/carlton) Sir,  
While running evaluate.py , I have observed that the expected and actual output is having difference like “\n” then also it marks task as fail.

eg:  
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") EXPECTED:  
Cover west give likely individual though question inside. System many human plant card among provide. Large former seek mouth there long.  
Attention officer successful. Us population the true show.  
Real cold if play side wind affect. Street cause investment receive have miss page station.  
Cold rest term her conference. Animal sure campaign new.  
Meeting back page exactly itself book forward. Decision western series under from shoulder. Pay during feeling newspaper human. Professional old recent beyond girl three human.  
Difficult yourself build increase back put others.  
Although artist operation thing skin lead. Billion deep measure down adult suggest. Anything action start artist when first.  
Whole way know down. Music machine trip father rather.  
Must medical bad law issue.  
Someone explain seven maintain wrong day factor property.

![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=12 ":warning:") RESULT:  
“Cover west give likely individual though question inside. System many human plant card among provide. Large former seek mouth there long.\nAttention officer successful. Us population the true show.\nReal cold if play side wind affect. Street cause investment receive have miss page station.\nCold rest term her conference. Animal sure campaign new.\nMeeting back page exactly itself book forward. Decision western series under from shoulder. Pay during feeling newspaper human. Professional old recent beyond girl three human.\nDifficult yourself build increase back put others.\nAlthough artist operation thing skin lead. Billion deep measure down adult suggest. Anything action start artist when first.\nWhole way know down. Music machine trip father rather.\nMust medical bad law issue.\nSomeone explain seven maintain wrong day factor property.\n”

![:x:](https://emoji.discourse-cdn.com/google/x.png?v=12 ":x:") A5 FAILED

Will this be considered as failure in actual evaluation as well or will this be taken care in actual evaluation?

---

## Post #505

- **Author**: Kabir1203
- **Posted on**: 2025-02-16T06:34:16.658Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/505

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/5/7567f3068b587402b54f6d01f3e133f6c21a114a_2_690x121.png)

image1412×248 16.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/5/7567f3068b587402b54f6d01f3e133f6c21a114a.png "image")

Im able to execute the query succesfully.  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/622e4a15020aefe140e92f8aa38035c5518ae41a_2_690x354.png)

image1109×570 40.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/2/622e4a15020aefe140e92f8aa38035c5518ae41a.png "image")

But the data gets downloaded to C drive instead of the project folder  
The datagen.py file is in the project folder itself.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/5/65498f6319cf654240d6dbf5f62a9313ebd5fd41.png)

image821×149 9.61 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/5/65498f6319cf654240d6dbf5f62a9313ebd5fd41.png "image")

am I making any error when setting the directories?

Please help, have been facing this issue since the beginning of this project, initially tried to move the files from C drive to project folder but that does not seem like a viable solution.

---

## Post #506

- **Author**: Kabir1203
- **Posted on**: 2025-02-16T06:51:41.708Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/506

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/1/213611a3e30fbaa75a62a4a99c19b20458a92609.png)

image1123×760 42.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/1/213611a3e30fbaa75a62a4a99c19b20458a92609.png "image")

  
I am also running datagen.py in the project directory, yet data folder is created in C drive.

---

## Post #507

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T06:54:08.636Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/507

[@jkmadathil](/u/jkmadathil)  
sir plz renew my token…  
Showing,  
{‘message’: ‘On 2025-02 you used $2.0041067399999912, exceeding $2’}

Sorry sir!..

---

## Post #508

- **Author**: 21f3002277
- **Posted on**: 2025-02-16T06:57:30.673Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/508

use PlainTextResponse for /read

---

## Post #509

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T06:59:34.007Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/509

Plz do someone reply.

---

## Post #510

- **Author**: Kabir1203
- **Posted on**: 2025-02-16T07:04:53.309Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/510

[@carlton](/u/carlton) [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj)

Please review the code and help me fix the error in order to proceed further. Thanks.

---

## Post #511

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T07:19:46.325Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/511

[github.com/ANdIeCOOl/TDS\_CLUTCH\_PROJECT\_1](https://github.com/ANdIeCOOl/TDS_CLUTCH_PROJECT_1/blob/main/README.md)

#### [README.md](https://github.com/ANdIeCOOl/TDS_CLUTCH_PROJECT_1/blob/main/README.md)

[`main`](https://github.com/ANdIeCOOl/TDS_CLUTCH_PROJECT_1/blob/main/README.md)

```
# TDS_CLUTCH_AT_6AY

```

using code generation, getting 6/10 or \* if lucky, similar comments needs a tool function call for sure, maybe someone can implement and create pull request, if you all can get 10/10 fine tuning with tool functions

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) Please help if it meets deliverables

---

## Post #512

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T08:28:50.991Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/512

Sir I need a help, In hte B portion where no any destination and source files are given…  
There we need to ask the user to povide the source and destination files or does we should store it in any default file locations…

As the statement is very vauge saying the “agent should handle this”…  
Thanks Sir!!

---

## Post #513

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T09:09:06.299Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/513

[@jkmadathil](/u/jkmadathil) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Sir earlier my code was running fine, but after the assigment of the new token,  
it is now showing 400 bad request, which simply implies there is something wrong with the token…  
plz do something sir…  
![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/3/9334f2224cfb61ea025ddfe149bbfd3df02db6f2.png)

I have do have cross verified the new token been correctly been assigned to the system variable…

---

## Post #514

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T09:19:36.290Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/514

More Particularily the failure occurs in the response portion…

```
def get_completions(prompt: str):
    print("Inside get_completions")#Debug
    with httpx.Client(timeout=20) as client:
        response = client.post(
            f"{openai_api_chat}",
            headers=headers,
            json=
                {
                    "model": "gpt-4o-mini",
                    "messages": [
                                    {"role": "system", "content": "You are a function classifier that extracts structured parameters from queries."},
                                    {"role": "user", "content": prompt}
                                ],
                    "tools": [
                                {
                                    "type": "function",
                                    "function": function
                                } for function in function_definitions_llm
                            ],
                    "tool_choice": "auto"
                },
        )

    print("DId suceessful llm calll")#Debug

```

```
INFO:     127.0.0.1:52108 - "POST /run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 HTTP/1.1" 400 Bad Request

```

---

## Post #515

- **Author**: 23f2003413
- **Posted on**: 2025-02-16T09:19:54.114Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/515

is there any limit on the size of the docker image [@Jivraj](/u/jivraj) [@carlton](/u/carlton) ? because mine is about 5.6Gb

---

## Post #516

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T09:20:56.839Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/516

bhai nhi hai…  
koi size limit

---

## Post #517

- **Author**: 23f3002091
- **Posted on**: 2025-02-16T10:12:11.868Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/517

uv run <https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/evaluate.py>  
Installed 13 packages in 543ms  
Traceback (most recent call last):  
File “/tmp/evaluateF6zgG9.py”, line 20, in   
from datagen import (  
…<9 lines>…  
)  
ModuleNotFoundError: No module named ‘datagen’

I am getting this error when I try to run evaluate.py

when I run the evaluate.py by having datagen.py in same folder , it is running perfectly. But my doubt is only after task a1 runs the datagen.py will be downloaded into the /data folder right ?

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)  
Kindly help me with this issue

---

## Post #518

- **Author**: Aditya_Sahu
- **Posted on**: 2025-02-16T10:15:40.611Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/518

Use following as first parameter of `subprocess.run()` to create `data/` directory inside your project instead of C: drive

```
["uv", "run", script_url, user_email, "--root", "./data"]

```

Also, you don’t need to download to script, you can directly run it from the url.

---

## Post #519

- **Author**: Aditya_Sahu
- **Posted on**: 2025-02-16T10:33:45.101Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/519

The reason for error is `evaluate.py` is trying to import `datagen.py` which doesn’t exist in your system. I’ll suggest download both the files, keep them in same folder and run `evaluate.py` from your computer

---

## Post #520

- **Author**: 23f3002091
- **Posted on**: 2025-02-16T10:35:51.852Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/520

Yes actually Thats my doubt , when I run both in same folder it is working , but only after task a1 runs datagen.py will be downloaded in /data folder right ?,

or did I misunderstood something??

---

## Post #521

- **Author**: TheVishal
- **Posted on**: 2025-02-16T10:38:05.164Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/521

### Generation-Based Automation Agent (No Hard Coding)

**Repository Link:** [GitHub - 23f2005593/tds](https://github.com/23f2005593/tds)

Currently, it can complete 7 out of 10 tasks. In reality, it can complete 9 out of 10 tasks, but the expected results are not flexible in evaluate.py file.

If we can extract credit card numbers, it will be able to complete 10 out of 10 tasks.

Please contribute to this repository. **We will win together.**

---

## Post #522

- **Author**: 21F1005510
- **Posted on**: 2025-02-16T10:42:00.545Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/522

{  
“message”: “On 2025-02 you used $2.0041388599999848, exceeding $2”  
}

What to do?

---

## Post #523

- **Author**: 21F1005510
- **Posted on**: 2025-02-16T10:43:32.880Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/523

facing same error, have you fouind any solution?

---

## Post #524

- **Author**: 21f3000745
- **Posted on**: 2025-02-16T11:07:43.937Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/524

sir for this task- A6 Find all Markdown (`.md` ) files in `/data/docs/` . For each file, extract the first occurrance of each H1 (i.e. a line starting with `#`  ). Create an index file `/data/docs/index.json` that maps each filename (without the `/data/docs/` prefix) to its title (e.g. `{"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...}` ) …I am getting correct result for all files but for the very first file budget.md it shows wrong.  
my result- { “budget.md”: “Success easy same main modern doctor.”,  
“build.md”: “Shoulder follow own never above.”,  
and in the data files there is different heading in budget.md.- # Series dog who make specific agree between.  
my question is this if it works for all the files then why not for this file budget.md [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

## Post #526

- **Author**: 21f3000745
- **Posted on**: 2025-02-16T11:14:46.456Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/526

do you able to do this task \* **A5**. Write the first line of the 10 most recent `.log` file in `/data/logs/` to `/data/logs-recent.txt`, most recent first …  
i am also doing using prompt no hard-coded.

---

## Post #527

- **Author**: 21f3000745
- **Posted on**: 2025-02-16T11:15:48.711Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/527

yes doing this only but finding correct for most of the files.

---

## Post #528

- **Author**: TheVishal
- **Posted on**: 2025-02-16T11:17:05.625Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/528

yes i am able to do task a5.

---

## Post #530

- **Author**: 21f3000745
- **Posted on**: 2025-02-16T11:19:16.557Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/530

so you directly using prompt for doing this task.

---

## Post #531

- **Author**: TheVishal
- **Posted on**: 2025-02-16T11:20:42.518Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/531

yes i am only using prompt based method

---

## Post #532

- **Author**: 21f3000745
- **Posted on**: 2025-02-16T11:22:43.078Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/532

If filename has number in its name then extract the number from the filename and convert it to an integer before sorting .Ensure numbers inside filenames are compared as integers, not as strings, to maintain proper order. Sort filenames in said in task. Avoid any lexicographical sorting issues. i am using this extra info for doing this but still it does not give accurate result. can you help me in this

---

## Post #533

- **Author**: TheVishal
- **Posted on**: 2025-02-16T11:23:51.476Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/533

i already shared my repo u can check there.

---

## Post #534

- **Author**: 23f2003751
- **Posted on**: 2025-02-16T12:17:41.613Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/534

you have pushed data,datagen and evaluate files…do we have to submit them as well??  
(also send the docker file)

---

## Post #535

- **Author**: Saransh_Saini
- **Posted on**: 2025-02-16T12:24:19.136Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/535

Check the file once, there is a possibility that it’s either fetching a comment or the second heading. Refactor your prompt to search only for the First Heading, specify it explixitly.

---

## Post #536

- **Author**: 21f3000745
- **Posted on**: 2025-02-16T12:34:43.548Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/536

okay let me check once.  
one more thing sir {“first\_name”: “Crystal”, “last\_name”: “Wilson”, “email”: “[delgadorebecca@example.com](mailto:delgadorebecca@example.com)”} then what will be the sorted-contact for this as in email there is no first and lastname present. [@Saransh\_Saini](/u/saransh_saini)

---

## Post #537

- **Author**: 23f1000371
- **Posted on**: 2025-02-16T12:58:43.228Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/537

Hey, I submitted the project links in the google form yesterday but, today in the portal it shows that I have not submitted the project.

---

## Post #538

- **Author**: 23f2005325
- **Posted on**: 2025-02-16T13:11:13.013Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/538

I am getting this error while running evaluate.py on task A9

```
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"

🔴 A9 failed: 'data'

```

There were no authentication issues till yesterday.

please guide [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

## Post #540

- **Author**: Saransh_Saini
- **Posted on**: 2025-02-16T13:20:12.206Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/540

This is happening because evaluate.py is unable to fetch your API Key from the environment variables. Create a new variable and set it’s value to your API Key then try.

---

## Post #541

- **Author**: Flibon
- **Posted on**: 2025-02-16T13:22:14.284Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/541

Hi everyone,

I’m running into an issue with the AI Proxy embeddings endpoint while executing the A9 task. Every time I send a POST request to:

bash

Copy

```
https://aiproxy.sanand.workers.dev/openai/v1/embeddings

```

I receive a **401 Unauthorized** response. This, in turn, causes my code to fail with a `KeyError: 'data'` because the expected JSON response doesn’t include the `"data"` key.

### What I’ve Tried

1. **Token Verification:**

* I’m using the `AIPROXY_TOKEN` obtained by logging in at [aiproxy.sanand.workers.dev](https://aiproxy.sanand.workers.dev/) with my IITM email.
* The token is passed in the header as follows:

python

Copy

```
"Authorization": f"Bearer {AIPROXY_TOKEN}"

```

* I added debug prints to confirm that the token is being used correctly (printing the first few characters).

2. **API Request Details:**

* The request includes the correct `Content-Type: application/json` header.
* The payload is set as:

json

Copy

```
{"model": "text-embedding-3-small", "input": ["Test"]}

```

* Despite this, the response status is consistently 401 Unauthorized.

3. **Debug Output:**  
   Here’s a snippet of the debug output:

bash

Copy

```
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"
🔴 A9 failed: 'data'

```

This confirms that the issue is with the authentication rather than our processing logic.

### What I Suspect

* The token may be invalid, expired, or misconfigured.
* There could be changes in the token permissions or endpoint requirements that I’m not aware of.
* Alternatively, there might be an issue on the server side with token validation.

### Request for Help

Has anyone else encountered this issue recently? Could someone verify if there are any changes to the authentication requirements for the embeddings endpoint? Any insights or updated instructions on how to ensure the token is valid and has the proper permissions would be greatly appreciated.

Thanks in advance for your assistance!

---

## Post #542

- **Author**: 23f2001286
- **Posted on**: 2025-02-16T13:26:14.110Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/542

B5. Run a SQL query on a SQLite or DuckDB database  
Should I ask for the SQL data base. Or the agent should be smart enough to find the required database…  
Moreover in the data folder there is only one database is it should be robust to handle multiple databases…

---

## Post #543

- **Author**: 23f2004644
- **Posted on**: 2025-02-16T13:31:32.080Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/543

same issue i also face pls sir help us fix this issue and provide us more token

HTTP Request: POST <https://aiproxy.sanand.workers.dev/openai/v1/embeddings> “HTTP/1.1 429 Too Many Requests”

![:red_circle:](https://emoji.discourse-cdn.com/google/red_circle.png?v=12 ":red_circle:") A9 failed: ‘data’

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

---

## Post #544

- **Author**: bhashwar_sengupta
- **Posted on**: 2025-02-16T13:55:52.482Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/544

I had a question on evaluation by the course team. To test that my application would run everywhere, I first deleted all images from my local machine using `podman rmi -a` and then ran `podman run --rm -p 8000:8000 -e AIPROXY_TOKEN=$AIPROXY_TOKEN $IMAGE_NAME` with the appropriate variables set. This is as per the instructions provided [here](https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1). But this gave me the following error:

```
Error: short-name "freshbash/dataworks-agent" did not resolve to an alias and no unqualified-search registries are defined in "/etc/containers/registries.conf

```

The above is the format in which we have to provide the image name in the Google form. So, I was confused whether this would succeed during actual evaluation.

The only way its working right now is when I specify the image name to be `docker.io/freshbash/dataworks-agent`

I’m not yet very good with how containers work so some insights would be very helpful. Thanks!

---

## Post #545

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:06:32.676Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/545

Nice bro, if its getting 8 you are sorted, probably get more later. But Prompting seems a little less info  
BUT

|  | Structured Outputs | JSON Mode |
| --- | --- | --- |
| Outputs valid JSON | Yes | Yes |
| Adheres to schema | Yes (see supported schemas) | No |
| Compatible models | gpt-4o-mini, gpt-4o-2024-08-06, and later | gpt-3.5-turbo, gpt-4-\* and gpt-4o-\* models |
| Enabling | response\_format: { type: json\_schema, json\_schema: {strict: true, schema: …} } | response\_format: { type: json\_object } |

```
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"}
        )

```

[github.com/23f2005593/tds](https://github.com/23f2005593/tds/blob/main/app.py#L142)

#### [app.py](https://github.com/23f2005593/tds/blob/main/app.py#L142)

[`main`](https://github.com/23f2005593/tds/blob/main/app.py#L142)

```


132. prompt = (
133. f"The Python code generated for the task '{task}' produced the following error when executed:\n"
134. f"{error_message}\n\n"
135. f"Here is the original code:\n{original_code_data['code']}\n\n"
136. "Please provide a corrected version of the code that fixes the error. Return only a JSON object with:\n"
137. "- code: the corrected Python code as a string\n"
138. "- function_name: name of the main function\n"
139. "- required_libraries: list of required pip packages\n\n"
140. "Make sure the code is simple, direct, and error-free this time. And try not to mess it up like before."
141. )
142. try:
143. response = client.chat.completions.create(
144. model="gpt-4o-mini",
145. messages=[{"role": "user", "content": prompt}],
146. temperature=0,
147. response_format={"type": "json_object"}
148. )
149. except Exception as exc:
150. logger.error("Error connecting to OpenAI API for auto-fix: %s", exc)
151. raise HTTPException(status_code=500, detail="Connection error during auto-fix. Maybe it's time to admit defeat?")


```

you are taking a chance on that format

---

## Post #546

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:18:18.312Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/546

[![Screenshot 2025-02-16 091341](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/2/32b55ca09f5894f9baa7082d8a44fdb1d14268f0_2_690x211.png)

Screenshot 2025-02-16 0913411315×404 24.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/2/32b55ca09f5894f9baa7082d8a44fdb1d14268f0.png "Screenshot 2025-02-16 091341")

  

[![Screenshot 2025-02-16 091101](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980_2_690x149.png)

Screenshot 2025-02-16 0911011351×292 13.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980.png "Screenshot 2025-02-16 091101")

Hardest i ever worked in my life. Thank you [@s.anand](/u/s.anand)

---

## Post #547

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:26:15.111Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/547

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/thevishal/48/110717_2.png) TheVishal:

> If we can extract credit card numbers, it will be able to complete 10 out of 10 tasks.

have tried function calling? with open code generation ?

---

## Post #548

- **Author**: TheVishal
- **Posted on**: 2025-02-16T14:32:03.478Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/548

not yet… but i have another problem when i am running this by using docker it is giving error “datagen module not found”

---

## Post #549

- **Author**: TheVishal
- **Posted on**: 2025-02-16T14:32:46.201Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/549

bro please help by contribute please

---

## Post #550

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:35:15.324Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/550

come off on one meet

---

## Post #551

- **Author**: 23f2003413
- **Posted on**: 2025-02-16T14:35:21.050Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/551

what should we push in the github repo [@Jivraj](/u/jivraj) [@carlton](/u/carlton) ??  
is it enough if we just push the Dockerfile, app.py, datagen.py and the LICENSE. Someone pls help!

---

## Post #552

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:35:55.720Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/552

bro i used all my codespaces credits xD  
i am nitpicking and editing from website and running not exceed limit XD

---

## Post #553

- **Author**: 23f2003413
- **Posted on**: 2025-02-16T14:36:37.073Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/553

someone pls help T\_T

---

## Post #554

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:37:29.809Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/554

submit image and github repo link, evalhaters will handle the rest im assuming

---

## Post #555

- **Author**: 23f2003413
- **Posted on**: 2025-02-16T14:38:25.332Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/555

yeaa i got that but what should we add in the github repo…like should we add the generated data folder?  
or is it enough if we just add the code and the Dockerfile to the repo

---

## Post #556

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:38:49.907Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/556

doesn’t matter they use only image

---

## Post #557

- **Author**: TheVishal
- **Posted on**: 2025-02-16T14:38:54.080Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/557

use local editor naa bro

---

## Post #558

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:39:34.694Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/558

and run my code xD i have one crazy setup XD give me some time, at 9:30 we’ll hop on eachother

---

## Post #559

- **Author**: 23f2003751
- **Posted on**: 2025-02-16T14:39:56.899Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/559

which repo u submitting yesterday one or todays.  
i am unable to run the yesterday one

---

## Post #560

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:40:08.771Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/560

this one new one only xD

---

## Post #561

- **Author**: 23f2003413
- **Posted on**: 2025-02-16T14:40:42.997Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/561

and what do they mean by image-name in the gform…is it the repo name in dockerhub?

---

## Post #562

- **Author**: 23f2003751
- **Posted on**: 2025-02-16T14:40:45.742Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/562

what evil have u done xd

---

## Post #563

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T14:41:05.660Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/563

why? ///////////// O—O

---

## Post #564

- **Author**: 23f2003751
- **Posted on**: 2025-02-16T14:41:09.153Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/564

dockerhub image name

---

## Post #565

- **Author**: 23f2003751
- **Posted on**: 2025-02-16T14:42:06.039Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/565

ur words are saying something else ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

---

## Post #566

- **Author**: 23f2003413
- **Posted on**: 2025-02-16T14:42:21.966Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/566

image name as in i dont get it lol.

---

## Post #567

- **Author**: shubhamatkal
- **Posted on**: 2025-02-16T14:43:47.628Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/567

```
(general) [shubham@laptop data]$ curl https://api.openai.com/v1/models -H "Authorization: Bearer $AIPROXY_TOKEN"
{
  "error": {
    "message": "Your authentication token is not from a valid issuer.",
    "type": "invalid_request_error",
    "param": null,
    "code": "invalid_issuer"
  }

```

pls help

---

## Post #568

- **Author**: 23f2003751
- **Posted on**: 2025-02-16T14:43:56.779Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/568

push ur image to docker hub that it will be available for them to use  
(use chatgpt on how to push to docker hub 2 3 steps to flw)

---

## Post #569

- **Author**: 23f2003413
- **Posted on**: 2025-02-16T14:45:42.604Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/569

yeah i hv pushed the image to dockerhub but i exactly dont get what image name is

like is it the name of my repo

---

## Post #570

- **Author**: 23f2003751
- **Posted on**: 2025-02-16T14:46:17.824Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/570

ur docker-username/image-name

---

## Post #571

- **Author**: 23f2003413
- **Posted on**: 2025-02-16T14:46:36.853Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/571

check if u have exported the AIPROXY\_TOKEN properly in your environment

---

## Post #572

- **Author**: 23f2003751
- **Posted on**: 2025-02-16T14:47:29.759Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/572

anyone check my repo

[github.com](https://github.com/Tusharisme/TDS_Project_1)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/f/0f711604313d08011bd1d17317c9e8190f364b1d_2_690x344.png)

### [GitHub - Tusharisme/TDS\_Project\_1](https://github.com/Tusharisme/TDS_Project_1)

Contribute to Tusharisme/TDS\_Project\_1 development by creating an account on GitHub.

---

## Post #573

- **Author**: shubhamatkal
- **Posted on**: 2025-02-16T14:48:49.549Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/573

yes i have the same key which is provided on ai proxy website for my login  
and yes i have that key properly exported

---

## Post #574

- **Author**: 23f2003413
- **Posted on**: 2025-02-16T14:55:12.204Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/574

check if u have used the correct ai proxy url then

---

## Post #575

- **Author**: Yogesh1
- **Posted on**: 2025-02-16T14:58:49.547Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/575

An email I just received says my license doesn’t have “MIT” in it. Although it does have it. I don’t know what I am missing. Someone help (if you didn’t get this mail). [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Post #576

- **Author**: 22f3001307
- **Posted on**: 2025-02-16T14:59:55.018Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/576

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

Hi,  
I received a mail saying that my submission has no Dockerfile. But git repo has a dockerfile.

even if i am to submit again, i have submit the same repo.  
what should i do?

---

## Post #577

- **Author**: 21f2001550
- **Posted on**: 2025-02-16T15:00:00.884Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/577

Hey I just got a mail saying that my github repo has no Dockerfile present. and im confused .

It doesnt mention anywhere that the dockerfile must be present in the root directory as a requirement/prerequisite of the project.

In my case its present inside the app directory. Could the team help clarify on this issue.

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

## Post #578

- **Author**: 23f2004636
- **Posted on**: 2025-02-16T15:01:32.983Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/578

What is expected repo structure ?  
I have a folder in my repo and dockerfile and license are present in that folder but I still received a mail regarding missing License and Dockerfile.

---

## Post #579

- **Author**: shubhamatkal
- **Posted on**: 2025-02-16T15:08:50.764Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/579

do we need to have data folder in repo no right?

---

## Post #580

- **Author**: 22f3001307
- **Posted on**: 2025-02-16T15:11:29.583Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/580

No, it is not needed

---

## Post #581

- **Author**: 22f3001011
- **Posted on**: 2025-02-16T15:14:47.324Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/581

We see that your submission [GitHub - 22f3001011/project-1](https://github.com/22f3001011/project-1/tree/main) has a result of FAIL due to the below reasons:  
No “MIT” in LICENSE

Hello sir, i got this mail despite having added the mit license as stated in the project problem statement. I cant figure out what the issue is, and help me out here.  
[@carlton](/u/carlton) [@Jeeveash.k](/u/jeeveash.k)

![](https://github.githubassets.com/favicons/favicon.svg)
[github.com](https://github.com/22f3001011/project-1/tree/main)

### [GitHub - 22f3001011/project-1](https://github.com/22f3001011/project-1/tree/main)

[main](https://github.com/22f3001011/project-1/tree/main)

Contribute to 22f3001011/project-1 development by creating an account on GitHub.

Thank you  
Regards  
Shashank J Shetth  
22f3001011

---

## Post #582

- **Author**: Yogesh1
- **Posted on**: 2025-02-16T15:22:38.923Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/582

Yeah. Same issue. Someone who didn’t get this error, please share the MIT license.

---

## Post #584

- **Author**: 23f2002592
- **Posted on**: 2025-02-16T15:31:46.769Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/584

<https://github.com/saniyanz/tds-p1new>

check my repo. what`s wrong. I`ve also got the mail but I`ve included the MIT License and the Dockerfile

---

## Post #585

- **Author**: 23f1001231
- **Posted on**: 2025-02-16T15:32:47.336Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/585

Rename `LICENSE.txt` to `LICENSE`

---

## Post #586

- **Author**: nayonika
- **Posted on**: 2025-02-16T15:41:04.020Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/586

I got a mail saying my Dockerfile is missing. However I have a dockerfile already in my github repository. Is it an issue with the spelling of dockerfile since I have submitted it in all small case as ‘dockerfile’. It was showing the score when I checked with the evaluate.py that was provided by iitm.

Shall I just change the name of the file from ‘dockerfile’ to ‘Dockerfile’ in github repository of mine or is there anything else that is needed to detect the Dockerfile?

---

## Post #587

- **Author**: 21f2001550
- **Posted on**: 2025-02-16T15:42:09.636Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/587

Hey team, I just moved my Dockerfile to the root level on my Github repo. Hope this solves the issue.

Small doubt: Do i need to submit the google form again?

---

## Post #589

- **Author**: 23f1002909
- **Posted on**: 2025-02-16T15:53:49.088Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/589

I ran out of tokens. Please help me. Please its urgent.

---

## Post #590

- **Author**: ShahbaazSingh
- **Posted on**: 2025-02-16T15:57:49.722Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/590

[@carlton](/u/carlton) sir [@s.anand](/u/s.anand) sir please provide me more tokens, I am out of tokens i don’t knwo what happened i hade 151 requests use and 0.09 usd and suddenly i check it was 300 requests and 2 usd i don’t knwo what happened can you provide me more tokens.

---

## Post #591

- **Author**: lakshaygarg654
- **Posted on**: 2025-02-16T16:00:21.667Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/591

Dear [@s.anand](/u/s.anand) , [@carlton](/u/carlton) , [@Jivraj](/u/jivraj) , and [@Saransh\_Saini](/u/saransh_saini)

Thank you all for this wonderful project. Coming from a non-coding background, I have learned a lot new things throughout this project building process.

[@carlton](/u/carlton) Sir, yesterday’s session provided valuable insights into Method 1 (prompt engineering) for dynamically handling tasks. I was able to develop an application using this approach; however, due to submission time constraints, I could not verify all tasks (my bad). While I tested some tasks and found the results to be highly accurate, I was unable to validate everything thoroughly.  
Therefore, I submitted the function-calling approach (Method 2) instead.

I sincerely appreciate everyone’s guidance and support.

---

## Post #592

- **Author**: ShahbaazSingh
- **Posted on**: 2025-02-16T16:09:36.850Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/592

Did you ran out of tokens suddenly like me ?  
How many requests have you sent in total ?

---

## Post #593

- **Author**: 23f2003751
- **Posted on**: 2025-02-16T16:17:51.919Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/593

can u share ur repo  
i really need it

---

## Post #594

- **Author**: Saransh_Saini
- **Posted on**: 2025-02-16T16:24:56.917Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/594

Thanks [@lakshaygarg654](/u/lakshaygarg654) for this feedback. Glad to know you learned from our efforts, it means a lot. This proves that even a person from non-tech background with determination can achieve it.

---

## Post #595

- **Author**: 23f2004644
- **Posted on**: 2025-02-16T16:26:27.020Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/595

sir pls provide more token [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) sir pls , give any reply we have only 2 hr left

---

## Post #596

- **Author**: Saransh_Saini
- **Posted on**: 2025-02-16T16:29:52.723Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/596

Change the name of your dockerfile to “Dockerfile”

---

## Post #597

- **Author**: ShahbaazSingh
- **Posted on**: 2025-02-16T16:29:54.811Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/597

yes sir please provide more tokens to me also [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

---

## Post #598

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T16:38:00.300Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/598

i hope i get 1 mark xD

im getting tasks only maybe 3 / 10

---

## Post #599

- **Author**: Algsoch
- **Posted on**: 2025-02-16T16:55:41.066Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/599

i have done many attempt but it is not working please show my environment saying fastapi is not installed but i have installed and it is showing on checking but no running file it is saying no module i have installed in both virtual and system  
please help

---

## Post #600

- **Author**: Algsoch
- **Posted on**: 2025-02-16T17:01:20.102Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/600

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/0/d084b074bcf4af69fe3e57753664fd39b016c2ef_2_690x365.png)

image1919×1016 117 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/0/d084b074bcf4af69fe3e57753664fd39b016c2ef.png "image")

  
this problem occuring sir since two days

---

## Post #601

- **Author**: Kabir1203
- **Posted on**: 2025-02-16T17:02:17.300Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/601

How long does it take to make a docker image, I’ve been doing it for the past 25 minutes and it’s still not completed.

---

## Post #602

- **Author**: lakshaygarg654
- **Posted on**: 2025-02-16T17:09:40.646Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/602

1. Your LLM app should be designed like it can give desire result based on task desc at run endpoint, and that result should be accessible at read endpoint.
2. Evaluation file just for reference to check how things works and it works for phase A tasks only. Also ensure datagen.py file and evaluation.py file are latest. There is one issue in evaluation.py file for task A1, link of datagen.py file not correct, rectify that link. Even it corrected in GitHub repo file but when I download that raw file in local system it takes back previous link.

---

## Post #603

- **Author**: 23f1002382
- **Posted on**: 2025-02-16T17:18:09.197Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/603

I WONDER HOW MANY API REQUESTS THE SERVER IS PROCESSING . It’s too slow

---

## Post #604

- **Author**: 23ds1000005
- **Posted on**: 2025-02-16T17:43:00.472Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/604

too much in the last few hours it feel

---

## Post #605

- **Author**: 22f1000120
- **Posted on**: 2025-02-16T18:31:13.198Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/605

I guess what is done is done. I should have maintained my version history properly. I am getting 4 correct but with minor formatting issues so only 1 correct I guess.

---

## Post #606

- **Author**: 22f1000120
- **Posted on**: 2025-02-16T18:35:21.452Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/606

It was tough… I will probably not score much but I enjoyed it a lot. Thank you for pushing us so hard. At least I am not scared of docker now and function calling feels easier than before.

---

## Post #607

- **Author**: s.anand
- **Posted on**: 2025-02-16T18:42:12.153Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/607

Well done, everyone! This is not an easy project. This is the kind of work our clients are asking us for.

I will keep you posted on the evaluation on this thread, it progresses.

* 2025-02-16T18:31:00Z Google Form closed
* 2025-02-16T18:35:00Z Validating submissions. Will post results shortly

---

## Post #608

- **Author**: 22f1000150
- **Posted on**: 2025-02-16T18:45:11.723Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/608

Sir i have missed the submission deadline by 5 minutes, can you give permission for the google form to accept the response for half an hour more.

---

## Post #609

- **Author**: TheVishal
- **Posted on**: 2025-02-16T18:46:21.892Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/609

Sir, due to time panic, I mistakenly named the Docker image incorrectly.

---

## Post #610

- **Author**: 22f1000150
- **Posted on**: 2025-02-16T18:47:14.170Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/610

Sir can you please allow submission for 5 more minutes?

---

## Post #611

- **Author**: Jivraj
- **Posted on**: 2025-02-19T11:00:09.298Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/611

A post was merged into an existing topic: [Project 1 - Casual banter](/t/project-1-casual-banter/167344/13)

---

## Post #612

- **Author**: Rrishit
- **Posted on**: 2025-02-16T18:51:43.271Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/612

[@s.anand](/u/s.anand) [@carlton](/u/carlton)  
Dear Sir,

I am writing to you in a state of distress and humility. An unfortunate mistake on my part has led to the upload of an incorrect Docker image link. When I checked the authenticity of the link, it showed an error, even though the GitHub repository link is functioning perfectly.

I have poured my heart and soul into this project, dedicating countless hours and sleepless nights to ensure its success. The project has successfully passed both Test A and Test B, and I was thrilled to see my hard work paying off. However, this single error has left me devastated.

I am pleading with you, with all my heart, to allow me to correct this mistake by updating the Docker image link. Alternatively, I humbly request that my application be reviewed directly through GitHub. Please consider this an exception, as I have worked tirelessly over the past two weeks to create an application that is 890 lines long.

I beg for your understanding and leniency in this matter. This project means the world to me, and I am genuinely sobbing over this setback.

Thank you for considering my heartfelt request.

Sincerely,

Rishit Jain  
(24F2004595)

---

## Post #613

- **Author**: psisaddicted
- **Posted on**: 2025-02-16T18:55:21.332Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/613

Although couldn’t complete handling every task, but really enjoyed working on this project and learned a lot throughout the process. I appreciate the opportunity to work on such an engaging project. For Project 2, I’ll make sure to allocate sufficient time and approach it with even greater commitment.

---

## Post #614

- **Author**: TheVishal
- **Posted on**: 2025-02-16T18:57:19.930Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/614

Sorry [@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

### Sir, due to time panic, I mistakenly named the Docker image incorrectly.

---

## Post #615

- **Author**: 22f1000120
- **Posted on**: 2025-02-16T19:15:02.324Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/615

Just push the latest image to docker asap. Hopefully the team considers it.

---

## Post #616

- **Author**: 22f1000120
- **Posted on**: 2025-02-16T19:16:30.050Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/616

True. Same here. Just giving 2 days for this project was definitely a big mistake on my part… but I couldn’t really give more time due to work commitments.

---

## Post #617

- **Author**: TheVishal
- **Posted on**: 2025-02-16T19:28:13.949Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/617

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

Sir, due to time panic, I mistakenly named the Docker image incorrectly.

I am not 100% sure but i guess i used “ii” instead of “i” in “thevixhal/tdsvishal”… is there any way to check this ?

---

## Post #618

- **Author**: Sagan
- **Posted on**: 2025-02-16T19:34:57.475Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/618

Can the submissions open just for some time? In minutes?  
Many students did silly mistakes due toh nervousness, we can just correct it.

---

## Post #619

- **Author**: GIRISH_VISHVESHVAR_B
- **Posted on**: 2025-02-17T02:56:32.384Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/619

I don’t think the project is too difficult to implement—it’s essentially a simple HTTP API for an AI agent that reads a task, converts it into parameters, and passes those parameters to specific functions to complete the task. However, the instructions in the project question aren’t very clear. Before the session, I am unable to fully understand the question. It took me almost an entire day just to understand what we need to do.  
Sir Could you provide test cases or a sample answer for Phase B?

---

## Post #620

- **Author**: lakshaygarg654
- **Posted on**: 2025-02-17T04:47:02.331Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/620

[@s.anand](/u/s.anand)  
[@carlton](/u/carlton) sorry to disturb you, project1 deadline is over.  
I made a mistake in my project. In my call llm function i set some payload instead of default for open ai api call like max token, temp. , n, stop etc.  
Due to this, some tasks may fail especially credit card image task will fail 100%, if possible can i just remove that payload from git hub repository . or you can check this call llm function present in my task\_handler.py file of my repository.  
I found this issue after deadline. If possible consider this request. I never engaged in a project or course like for this one. I love this project genuinely.

my github repo : [GitHub - 21f3001076/TDS\_Project\_1: This is IITM Data Science TDS Course Project 1 Repository](https://github.com/21f3001076/TDS_Project_1)  
Thankyou  
Lakshay  
student id: 21f3001076@ds.study.iitm.ac.in

---

## Post #621

- **Author**: 23f1001611
- **Posted on**: 2025-02-17T05:41:26.456Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/621

Dear [@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj) ,  
Thank you so much for this wonderful project! We have learned so many things from this experience, especially the power of prompts. The team has put in tremendous effort, extending a few sessions and patiently clearing all our doubts. We truly appreciate the dedication and support

Regards,  
Arjun

---

## Post #622

- **Author**: swatikap
- **Posted on**: 2025-02-17T05:48:47.338Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/622

I would like to sincerely thank the course faculty [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) for their support on the project throughout the week. They were so patient in listening to our issues and helping us resolve them, even if the issues were repeated.

I was not able to complete some or maybe many of the tasks but overall, it was a very good learning for me, and I thoroughly enjoyed it.

Thanks very much again for your guidance and support.

Regards,  
Swati

---

## Post #623

- **Author**: Saransh_Saini
- **Posted on**: 2025-02-17T09:28:09.859Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/623

Thanks for your compliments Swati. It’s always nice to know our efforts paid off.  
*Happy Learning ![:+1:](https://emoji.discourse-cdn.com/google/+1.png?v=12 ":+1:")*

---

## Post #624

- **Author**: Udipth
- **Posted on**: 2025-02-17T10:07:52.089Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/624

I have received a mail that my project has ""No “MIT” in LICENSE;No Dockerfile " which I saw today. My project has MIT licence and Dockerfile was also there… but to reconfirm I pulled my dockerfile from dockerhub to github only . NOw am not sure will that be considered now in my project submission or not. Requesting to kindly consider current state of my project in submission for my project.

---

## Post #625

- **Author**: 23f1002382
- **Posted on**: 2025-02-17T11:09:20.695Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/625

WOMP WOMP should i call a wambulance?

---

## Post #626

- **Author**: 23f1002382
- **Posted on**: 2025-02-17T11:10:37.785Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/626

(post deleted by author)

---

## Post #627

- **Author**: 23f1002382
- **Posted on**: 2025-02-17T11:12:30.279Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/627

@all those who didn’t submit, its ok EVEN I did NOT submit. Even though i get zero, i am happy with the learning i did. Once again thank you sir [@carlton](/u/carlton) [@s.anand](/u/s.anand) . This a been awesome experience , i haven’t been this alive in forever. Cheers.

---

## Post #628

- **Author**: 23f2000237
- **Posted on**: 2025-02-17T11:43:24.604Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/628

I noticed something quite funny. The project never specified the required tech stack, so one could have done this entirely with JavaScript as well, assuming the necessary libraries are installed.

---

## Post #629

- **Author**: 23f1002382
- **Posted on**: 2025-02-17T11:52:41.002Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/629

[@TheVishal](/u/thevishal)  
EDIT: Create a new docker image with the mistaken image name , so when they pull image from repo, that image with the wrong name also gets pulled.  
what to do

* push a new image with the mistaken name, so in your repo there will be two images  
    
  how will this help?
* since you are unsure, which image link you posted, you can be sure that even you had a mistake in link, a new image will exist with the wrong name after you push another image

@all  
use this to update your image even after submission, as now they only validate the images, they do not pull it so you can edit your project and add more functionality if they release the code solutiion

CHEERS  
Andrew OUT.

---

## Post #630

- **Author**: Sagan
- **Posted on**: 2025-02-17T12:22:39.676Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/630

I didn’t submit the google form, I have made the github repo and docker image for TDS project 1. I, mistakenly, thought that I had submitted the google form but actually it was saved as a draft and closed my laptop. As soon as I realized my mistake, I hit the submit button but this was shown then,  
“The form TDS Jan 2025 - Project 1 Submission is no longer accepting responses.”

I apologize for this. I have been working on this project for weeks.  
This was my first TDS project. I would highly appreciated, if you could help me.  
Thankyou

GitHub repo:[GitHub - Sagankaur/TDS\_project1: LLM-based automation agent](https://github.com/Sagankaur/TDS_project1)  
Docker : sagandeep/tds\_project1

---

## Post #631

- **Author**: 21f3002277
- **Posted on**: 2025-02-17T12:47:55.488Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/631

Sir, can we get the evaluation script now

[@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

## Post #632

- **Author**: 24f2003130
- **Posted on**: 2025-02-17T13:55:13.525Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/632

If I am not wrong you were getting 9/10 in task A when many of us were stuck and you didn’t submit… unbelievable ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")

---

## Post #633

- **Author**: 24f2003130
- **Posted on**: 2025-02-17T14:03:52.442Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/633

Thank you, sir, for giving us this amazing opportunity! Honestly, I learned more in the last week than I did throughout the three modules.

The project was a rollercoaster ride—especially with all the errors that kept popping up—but overall, the experience was incredibly enriching. The amount of knowledge I gained was truly valuable.

A huge thanks to [@Carlton](/u/carlton), [@Saransh\_Saini](/u/saransh_saini), and [@Jivraj](/u/jivraj) sir for their guidance and support. Without the last week’s lectures, the project couldn’t have been completed.

---

## Post #634

- **Author**: 23f1002382
- **Posted on**: 2025-02-17T14:33:09.731Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/634

i couldn’t my code space ran out of compute and then it was just lagging before i found out what happened , i just submitted old code repo and the image the we created in week 2 or week1 when had to create docker image for graded assignments  
EDIT:  

[![Screenshot 2025-02-16 091101](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980_2_690x149.png)

Screenshot 2025-02-16 0911011351×292 13.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980.png "Screenshot 2025-02-16 091101")

  

[![Screenshot 2025-02-17 200414](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/a/da23d8a478ff6a79db4af56fef947fd376297d82_2_690x103.png)

Screenshot 2025-02-17 2004141338×200 18.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/a/da23d8a478ff6a79db4af56fef947fd376297d82.png "Screenshot 2025-02-17 200414")

  

[![Screenshot 2025-02-17 200525](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/f/bfa4ea8edf0da66b0bb609f953c06ce7f6bd8e3f_2_690x168.png)

Screenshot 2025-02-17 2005251312×321 18.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/f/bfa4ea8edf0da66b0bb609f953c06ce7f6bd8e3f.png "Screenshot 2025-02-17 200525")

---

## Post #635

- **Author**: 24f2003130
- **Posted on**: 2025-02-17T15:44:43.711Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/635

Wait we had limits in codespace…I didn’t thought much of it but now that I see… …even mine is not so far from the limit…thanks for reminding…gotta be careful in next project

---

## Post #636

- **Author**: 21f2000709
- **Posted on**: 2025-02-18T07:30:10.106Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/636

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) Is there something like peer-review in the project, I found this in the grading document.

![Screenshot 2025-02-18 at 12.58.15 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/2/52e6c1b35b7e4c898f1c0cc4abb3cbbcc66760c0.png)

[![Screenshot 2025-02-18 at 1.00.50 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/8/08a834722986d3dccd4bf9fb24640bd842d76d08.png)

Screenshot 2025-02-18 at 1.00.50 PM126×226 2.02 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/8/08a834722986d3dccd4bf9fb24640bd842d76d08.png "Screenshot 2025-02-18 at 1.00.50 PM")

---

## Post #637

- **Author**: 21f2000709
- **Posted on**: 2025-02-18T07:44:45.153Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/637

This project is one of the best experiences I had in the entire degree program. I could say this without any hesitation that what I learnt in the past 10 days >> last 3 months.

I really appreciate the idea of open internet type of evaluations, wherein, you implement things without any constraints, learning for the sake of implementing.

Doing this project, I also found many new ideas wherein function calling can be used to solve new problems. I also learned many new things from enthusiastic peers like [@23f1002382](/u/23f1002382) and also got the chance to help a few.

I thank the entire TDS team - [@s.anand](/u/s.anand) sir, [@carlton](/u/carlton) , [@Jivraj](/u/jivraj) for their support throughout this amazing experience.

Regards,  
Pradeep Mondal

---

## Post #638

- **Author**: Sakshi6479
- **Posted on**: 2025-02-14T13:29:17.644Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/638

sir using prompt method also i am having the error please provide a step wise solution so then i can make functions accordingly.

```
#/// Scirpt
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi",
#     "uvicorn",
#     "requests",
# ]
#///

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import requests
import os
import json
from subprocess import run

app = FastAPI()

response_format = {
    "type": "json",
    "json_schema": {
        "name": "taks_runner",
        "schema": {
            "type": "object",
            "required": ["python_dependencies","python_code"],
            "properties": {
                "python_code": {
                    "type": "string",
                    "description": "Python code to perform the task"
                },
                "python_dependencies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "module": {
                                "type": "string",
                                "description": "Name of the python module"
                            }
                        },
                        "required": ["module"],
                        "additionalProperties": False
                    }
            }
        }
    }
}
}

primary_prompt = """
                You are an automated agent, so generate python code that does the specified task.
                Assume that uv and python are pre-installed.
                Assume that code you generate will be executed inside a docker container.
                Inorder to perform any task if some python package is required to install, provide name of those modules. 
"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AIPROXY_TOKEN}"
}

@app.get("/")
def home():
    return {"welcome to the task runner"}
@app.post("/run")
def task_runnner(task: str):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    data = {
        "model": "gpt-4o-mini", 
         "messages": [
             {
              "role": "user", 
              "content": task
              },
              {
                "role": "system",
                "content": f"""{primary_prompt}"""
            }
         ],
         "response_format": response_format
    }

    response = requests.post(url=url, headers=headers, json=data)
    r = response.json()

    return r

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

[![Screenshot 2025-02-14 185820](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a60823d7458d88b699955503f1e0665b9f4e4a4c_2_655x500.png)

Screenshot 2025-02-14 1858201945×1484 229 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a60823d7458d88b699955503f1e0665b9f4e4a4c.png "Screenshot 2025-02-14 185820")

[@carlton](/u/carlton) , [@Saransh\_Saini](/u/saransh_saini) , [@Jivraj](/u/jivraj)

---

## Post #639

- **Author**: carlton
- **Posted on**: 2025-02-14T15:18:46.195Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/639

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/sakshi6479/48/110446_2.png) Sakshi6479:

> ```
> {
>     "type": "json",
>     "json_schema": {
>         "name": "taks_runner",
>         "schema": {
>             "type": "object",
>             "required": ["python_dependencies","python_code"],
>             "properties": {
>                 "python_code": {
>                     "type": "string",
>                     "description": "Python code to perform the task"
>                 },
>                 "python_dependencies": {
>                     "type": "array",
>                     "items": {
>                         "type": "object",
>                         "properties": {
>                             "module": {
>                                 "type": "string",
>                                 "description": "Name of the python module"
>                             }
>                         },
>                         "required": ["module"],
>                         "additionalProperties": False
>                     }
>             }
>         }
>     }
> }
> }
>
> ```

It clearly says in your error message:

Invalid value: ‘json’

if you look at the “type” key in your response\_format variable at the top,

the value cannot be “json”

The error is telling you what the supported values are

‘json\_object’, ‘json\_schema’, and ‘text’

Since you are defining a schema the correct value should be ‘json\_schema’

So therefore you should change

```
"type": "json"

```

to

```
"type": "json_schema"

```

If you have trouble constructing Json schemas,  
either feed it to gpt and have it correct it (along with your error) or please go over Module 3, in particular

<https://tds.s-anand.net/#/llm-text-extraction>

There is a clear example you can use as a template. We use the same one as a template when we do it in the sessions. That way you will make less errors.

Kind regards

---

## Post #641

- **Author**: Jivraj
- **Posted on**: 2025-02-18T15:50:42.691Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/641

Thanks [@21f2000709](/u/21f2000709) for kind words

Tagging Saransh for his efforts to project [@Saransh\_Saini](/u/saransh_saini).

[@23f1002382](/u/23f1002382) most active student on this post thanks to you too.

Kind regards

---

## Post #642

- **Author**: 21f2000709
- **Posted on**: 2025-02-18T16:10:39.846Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/642

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png) 21f2000709:

> [@carlton](/u/carlton) [@Jivraj](/u/jivraj) Is there something like peer-review in the project, I found this in the grading document.

Anyone having any idea on this?

---

## Post #643

- **Author**: carlton
- **Posted on**: 2025-02-24T09:01:12.099Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/643

No human peer reviews. The peer will be an LLM that has been given the rubrics and fine tuned.

Kind regards

---

## Post #644

- **Author**: 21f2000709
- **Posted on**: 2025-02-24T09:47:29.302Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/644

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

> The peer will be an LLM that has been given the rubrics and fine tuned.

May the peer give me good marks ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

---

## Post #645

- **Author**: Yogesh1
- **Posted on**: 2025-02-25T08:02:56.360Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/645

[@carlton](/u/carlton) Would the scores of project 1 be released tomorrow?

---

## Post #646

- **Author**: carlton
- **Posted on**: 2025-02-26T02:41:56.425Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/646

[@Yogesh1](/u/yogesh1)

~~We do not have an ETA on Project 1 scores yet. Might have more clarity soon.~~

Project 1 scores will be available roughly second week of March.

Kind regards

---

## Post #647

- **Author**: carlton
- **Posted on**: 2025-02-26T02:51:34.212Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/647

[@lakshaygarg654](/u/lakshaygarg654)

I know this is a late reply, but its not possible for us to consider changes to your project after the deadline for academic integrity purposes.

If we were to allow it, we would have to allow everyone to make changes to their project as well for it to be fair.

Kind regards

---

## Post #648

- **Author**: carlton
- **Posted on**: 2025-02-26T02:53:21.351Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/648

We will soon provide a complete solution for Project 1 because of its valuable learning.

---

## Post #649

- **Author**: lakshaygarg654
- **Posted on**: 2025-02-26T06:30:31.260Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/649

Alright, [@Carlton](/u/carlton). No problem at all, and thank you for your response.

I just wanted to bring a small limitation in my project’s LLM function to your attention, which I discovered after submission. It may impact one or two tasks. However, no concerns—this has been a great learning experience.

And if possible, just add one line in your Evaluation LLM prompt: *“Give loose marking for effort!”*—because, you know, creativity deserves some extra credit! ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/google/slightly_smiling_face.png?v=12 ":slightly_smiling_face:")

---

## Post #650

- **Author**: garimaa
- **Posted on**: 2025-03-12T14:34:53.467Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/650

I am not able to see my project marks please look into the problem

---

## Post #651

- **Author**: carlton
- **Posted on**: 2025-03-14T11:00:33.184Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/651

Its not been evaluated yet.

We are still processing them.

Kind regards

---

## Post #652

- **Author**: 23f3004114
- **Posted on**: 2025-03-16T15:13:37.996Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/652

So will the solution be based on New MCP style or will they use the same function calling?

---

## Post #653

- **Author**: carlton
- **Posted on**: 2025-03-17T12:40:26.308Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/653

Definitely MCP style. Its the most elegant solution and it works beautifully. As soon as evals are done we will showcase it.

---

## Post #654

- **Author**: Yogesh1
- **Posted on**: 2025-03-22T13:24:45.799Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/654

[@carlton](/u/carlton) Any ETA on project 1 scores?

---

## Post #655

- **Author**: 21f3001993
- **Posted on**: 2025-03-23T07:02:28.304Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/655

I would like to request some bonus like 0.5 bonus mark for each day of delay from the original expected date of receiving score for Project 1 (will be life-saving for us and will be an incentive for team to release scores quickly; or request to TAs if you had better ideas for helping us score more in Project 1)! ![:smiley:](https://emoji.discourse-cdn.com/google/smiley.png?v=14 ":smiley:")

---

## Post #656

- **Author**: 21f2000709
- **Posted on**: 2025-03-26T08:05:58.369Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/656

Any Updates? Can we expect it to be out before P2 deadline?

---

## Post #657

- **Author**: thinkmachine
- **Posted on**: 2025-03-31T21:05:36.632Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/657

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png)

image412×167 4.49 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png "image")

  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png)

image439×204 7.25 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png "image")

***This docker image has outlived many students’ hopes, dreams and ambitions of passing this course.***

**Why is it still not being detected properly on the docker hub?**  
What in the April Fools is this ![:unamused_face:](https://emoji.discourse-cdn.com/google/unamused_face.png?v=14 ":unamused_face:")

> It hasn’t even been morning yet!

PS ( [@carlton](/u/carlton) [@Jivraj](/u/jivraj) ): My P1 submission had passed all the basic sanity checks on 15th February. No breaking modifications to the Github repo nor the DockerHub image have been made since then. There’s something bugged in your scripts. Kindly check.

---

## Post #658

- **Author**: 23f1000879
- **Posted on**: 2025-04-01T01:53:24.825Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/658

same issue here

i have my git repo public but its saying i don’t have public git repo, also i have dockerfile in my root folder but its also said fail, same for mit license  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/3/83f8c6d4eb6481e3b9089ce75d1665cf312904be_2_690x373.png)

image1889×1022 122 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/3/83f8c6d4eb6481e3b9089ce75d1665cf312904be.png "image")

---

## Post #659

- **Author**: HARISH.S
- **Posted on**: 2025-04-01T05:56:46.782Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/659

yes sir same problem  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/9/39b684382d117b9388443c38b9f83bad7be3e0ab.png)

image885×346 15.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/9/39b684382d117b9388443c38b9f83bad7be3e0ab.png "image")

  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f_2_690x372.png)

image1330×718 54.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f.png "image")

please check and say sir.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_690x387.png)

image1918×1078 187 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411.png "image")

sir it seems like there was a problem when i pushed this files to the repo but i defenitely did correctly. PLease allow me to add docker file alone with your permission. As you can see i haven’t opened the dockerfile since the last date of project 1. Kindly allow this sir. and i have MiT license in my repo but still showing fail . kindly check that also sir.  
[@carlton](/u/carlton) [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj)

---

## Post #660

- **Author**: HARISH.S
- **Posted on**: 2025-04-01T06:04:51.580Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/660

yes sir same problem  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/9/39b684382d117b9388443c38b9f83bad7be3e0ab.png)

image885×346 15.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/9/39b684382d117b9388443c38b9f83bad7be3e0ab.png "image")

  

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f_2_690x372.png)

image1330×718 54.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f.png "image")

please check and say sir.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_690x387.png)

image1918×1078 187 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411.png "image")

sir it seems like there was a problem when i pushed this files to the repo but i defenitely did correctly. PLease allow me to add docker file alone with your permission. As you can see i haven’t opened the dockerfile since the last date of project 1. Kindly allow this sir. and i have MiT license in my repo but still showing fail . kindly check that also sir.  
[@carlton](/u/carlton) [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj)

---

## Post #661

- **Author**: 23f1001524
- **Posted on**: 2025-04-01T16:52:05.625Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/661

same issue with me , my repo has both the dockerfile , license and is public. Please look into this . [@carlton](/u/carlton) sir . [GitHub - veershah1231/tds\_proj\_1: Tds project](https://github.com/veershah1231/tds_proj_1) and i have made them 2 months ago and is not a new commit.  

[![1000105386](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg)

10001053861072×1787 256 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3.jpeg "1000105386")

---

## Post #662

- **Author**: 23f1002382
- **Posted on**: 2025-04-06T06:44:58.937Z
- **URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/662

I came pretty close, but too close(double entendre) to the deadline. Classic ICARUS stuff

0/20 ![:neutral_face:](https://emoji.discourse-cdn.com/google/neutral_face.png?v=14 ":neutral_face:")![:ok_hand:t2:](https://emoji.discourse-cdn.com/google/ok_hand/2.png?v=14 ":ok_hand:t2:")

---

