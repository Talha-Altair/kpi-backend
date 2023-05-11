from flask import Blueprint, jsonify, request
from connections import db

dashboard = Blueprint("dashboard", __name__)

dashboard_col = db["dashboard"]

dashboard_data_full = {
    "username": "balaji",
    "image" : "https://raw.githubusercontent.com/Talha-Altair/intellect2k21/prod/static/static_pics/designer%20srirangarajan.jpg",
    "basic": {
        "name": "Dr. Balaji Ramanujam",
        "designation": "Professor",
        "email": "balaji.cse@crescent.education",
        "doj": "21-09-2017",
        "exp": "12 Years",
        "served_in_crescent": "6 Years",
        "research": [
            "Data Mining",
            "Machine Learning",
            "Big Data Analytics",
            "Cloud Computing",
            "Database management System",
            "Advanced Databases",
            "Software Engineering",
            "Object Oriented Software Engineering"
        ]
    },
    "courses": [ 
        "Compiler Design",
        "Green Design",
        "Operating System",
        "Cloud Computing"
    ],
    "prof_memberships": [
        "Member of IEEE",
        "Member of ACM",
        "Member of CSI",
        "Member of IAENG",
        "Member of ISTE",
        "Member of IETE"
    ],
    "funded_projects": [
        "A Novel Approach for Improving Opportunities and Challenges in Opinion Mining, Funded by AICTE, 2019-2022",
        "A Dynamic MooM Dataset Processing under TelMED protocol design for QoS improvisation of telemedicine environment, Funded by IEEE, 2019-2022",
        "Architecture to Minimize Energy Consumption in Cloud Datacenter, International Conference on Intelligent Computing and Applications, Springer Funded by NCERT, 2019-2022",
        "A Acquiring Quality of Service and Quality of Experience Parameter of PaaS Cloud Renderfarm Services, Funded by Govt TN, 2019-2022"
    ],
    "workshops_organized": [
        "One day workshop on “Basics of CorelDraw and Photoshop” on 12th June 2018 at Jeppiaar SRR",
        "Two days workshop on “Opportunities and Challenges in Opinion Mining” on 2nd April 2018.",
        "workshop on “Impact of Predictive analysis on Big data” on 4th April 2018.",
        "One day workshop on “ Web application development using PHP & MySql” on 6th April 2018.",
        "seminar on “Dine-In Instead Of Dine-Out (FOOD- The Elixir of Life)”, on April 30, 2018, at Jeppiaar SRR Engineering College."
    ],
    "teaching_methods": [
        "Slow Paced Lectures",
        "Focus onCase Study",
        "Frequent Group Discussion",
        "Real time Problem Solving"
    ],
    "fdp" : [
        "One day Workshop on Basics of CorelDraw and Photoshop on 12th June 2018 at Jeppiaar SRR",
        "IEI sponsored One day workshop “Opportunities and Challenges in Opinion Mining” on 2nd April 2018.",
        "IEI sponsored One day workshop “Impact of Predictive analysis on Big data” on 4th April 2018.",
        "IEI sponsored One day workshop “ Web application development using PHP & MySql” on 6th April 2018.",
        "One day seminar on “Dine-In Instead Of Dine-Out (FOOD- The Elixir of Life)”, on April 30, 2018, at Jeppiaar SRR Engineering College."
    ],
    "mou_signed": [
        "MoU with Unwind Labs for the project titled “Development of Auto BOTS for Integrated CR”",
        "MoU signed with IBM for the project titled “IBM Career Education Program”",
        "MoU signed with ICTACT for the project titled “ICTACT Bridge”",
        "MoU signed with Capgemini for the project titled “Capgemini Career Education Program”",
    ],
    "newsletter_released": [
        "Crescent Line Magazine 2019",
        "Science and Technology Newsletter",
        "Atoms Today",
        "zarwaliya Magazine",
        "Crescent Line Magazine 2023",
    ],
    "affliate_faculty": [
        "Dr. Moorthy S (SSN College of Engineering) for Computer Networks",
        "Dr. S. Suresh (SSN College of Engineering) for Data Mining",
        "Dr. S. Suresh (Anna University CEG) for Data Science",
        "Dr. S. Suresh (IIT Madras) for Graphic Design",
        "Dr. S. Suresh (Kuppam College of Engineering) for React Native Development",
    ],
    "syllabus_revision": [
        "Data Structures",
        "Software Project Management",
        "Software Engineering",
        "Object Oriented Programming"
    ],
    "journal_papers_published": [
        "Investigative Protocol Design of Layer Optimized Image Compression in Telemedicine Environment”, Procedia Computer Science 167, 2617-2622",
        "ICTs role in building and understanding Indian Telemedicine Environment : A Study”, Information and Communication Technology for Competitive Strategies, Springer Publications, 2019. Scopus Indexed.",
        "A Dynamic MooM Dataset Processing under TelMED protocol design for QoS improvisation of telemedicine environment”, Journal of medical systems 43 (8), 257, 2019.",
        "Using an innovative stacked ensemble algorithm for the accurate prediction of preterm birth, Journal of the Turkish German Gynecological Association 20 (2), 70, 2019.",
        "An optimized RTSRV machine learning algorithm for biomedical signal transmission and regeneration for telemedicine environment, Procedia Computer Science 152, 140-149, 2019."
    ],
    "conference_papers_published": [
        "Optimized Multiwalk Algorithm for Test Case Reduction, International Conference on Intelligent Computing and Applications, Springer, 2019.",
        "Predicting Movie Success using Regression Techniques, International Conference on Intelligent Computing and Applications, Springer, 2019.",
        "Architecture to Minimize Energy Consumption in Cloud Datacenter, International Conference on Intelligent Computing and Applications, Springer, 2019.",
        "Chennai Water Crisis Data, International Conference on Intelligent Computing and Applications, Springer, 2019.",
        "Architecture to Minimize Energy Consumption in Cloud Datacenter”, International Conference on Intelligent Computing and Control System, pp.1044-1048, IEEE, 2019."
    ],
    "patents": [
        "A Method for Overcoming Cold Start Problem in Recommending Cloud Services. Application No: 201641025965 A (Published).",
        "A Method for Acquiring Quality of Service and Quality of Experience Parameter of PaaS Cloud Renderfarm Services. Application No: 201641025966 A, (Published)."
    ],
    "consultancies": [
        "Partially completed a consultancy project for Unwind labs for their project titled “Development of Auto BOTS for Integrated CR”",
        "Working on a consultancy project for Unwind Labs on Block chain technology"
    ],
    "research_guidance": True,
    "awards": [
        "Recipient of Innovative Technological Research & Dedicated, Excellent Professional Achievement Award organised by the Society of Innovative Educationalist & Scientic Research Professional Malayasia. App.No.201920R0624,FSIESRP, Oct 2020",
        "Recipient of Best Researcher Award  in the First International Scientific conference  organized by VD Good Chennai on 14th Sept 2019",
        "Recipient of “Bharat Shiksha Ratan Award” for recognizing outstanding achievements on the occasion of National Seminar “Individual Contribution for Social and Economic Growth” on 12th June 2014, New Delhi",
        "Recipient of “Best Teacher Award” from Lions Club of Red hills, Chennai.",
        "Recipient of Bharat Vibhushan Samman Puraskar award through the Economic and Human Resource Development Association on 20th December 2013."
    ],
    "charts": {
        "pass_percentage_data": [
            [
                "Compiler",
                56
            ],
            [
                "Green Design",
                78
            ],
            [
                "Operating System",
                94
            ],
            [
                "Cloud Computing",
                69
            ]
        ],
        "ques_quality_data": {
            "base_data": [
                {
                    "name": "compiler",
                    "y": 52.74,
                    "drilldown": "compiler"
                },
                {
                    "name": "Green Design",
                    "y": 72.74,
                    "drilldown": "Green Design"
                },
                {
                    "name": "Operating System",
                    "y": 62.74,
                    "drilldown": "Operating System"
                },
                {
                    "name": "Cloud Computing",
                    "y": 82.74,
                    "drilldown": "Cloud Computing"
                }
            ],
            "drilldown_data": [
                {
                    "name": "compiler",
                    "id": "compiler",
                    "data": [
                        [
                            "cat1",
                            47
                        ],
                        [
                            "cat2",
                            50
                        ],
                        [
                            "endsem",
                            75
                        ]
                    ]
                },
                {
                    "name": "Green Design",
                    "id": "Green Design",
                    "data": [
                        [
                            "cat1",
                            87
                        ],
                        [
                            "cat2",
                            90
                        ],
                        [
                            "endsem",
                            85
                        ]
                    ]
                },
                {
                    "name": "Operating System",
                    "id": "Operating System",
                    "data": [
                        [
                            "cat1",
                            87
                        ],
                        [
                            "cat2",
                            90
                        ],
                        [
                            "endsem",
                            85
                        ]
                    ]
                },
                {
                    "name": "Cloud Computing",
                    "id": "Cloud Computing",
                    "data": [
                        [
                            "cat1",
                            87
                        ],
                        [
                            "cat2",
                            90
                        ],
                        [
                            "endsem",
                            85
                        ]
                    ]
                }
            ]
        },
        "material_quality_data": [
            [
                "Compiler",
                66
            ],
            [
                "Green Design",
                18
            ],
            [
                "Operating System",
                98
            ],
            [
                "Cloud Computing",
                69
            ]
        ]
    }

}


@dashboard.route("/<string:username>", methods=["GET", "POST"])
def dashboard_data(username):

    # try:
    #     user_data = dashboard.find_one({"username": username})

    #     del user_data["_id"]

    #     return jsonify(user_data), 200

    # except Exception as e:

    #     print(e)

    #     return jsonify({"message": "Error Occured"}), 500

    return jsonify(dashboard_data_full), 200