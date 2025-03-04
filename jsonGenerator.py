def generate_json(form_state):

 

    dataModel = {
        "name": None,
        "description": None,
         "organizations": [],
        "targetCommunities": [],
         "bodies": [],
         "governance": [],
         "socialContexts":[],
         "adaptations":[],
         "participants":[],
         "teams":[]
    }

    targetCommunities =  {
                "id": None,
                "startingAgeRange": None,
                "endingAgeRange": None,
                "ethnicities": [],
                "genders": [],
                "spokenLanguages": [
                    {"language": None, "proficiency": None}
                ],
                "socioEconomicStati": [],
                "skillLevels": [],
                "averageTenure": None
            }
    bodies = {

    }
    dataModel = {
        "name": None,
        "description": None,
        "organizations": [],
        "targetCommunities": [
            {
                "id": None,
                "startingAgeRange": None,
                "endingAgeRange": None,
                "ethnicities": [],
                "genders": [],
                "spokenLanguages": [
                    {"language": None, "proficiency": None}
                ],
                "socioEconomicStati": [],
                "skillLevels": [],
                "averageTenure": None
            },
            {
                "id": None,
                "startingAgeRange": None,
                "endingAgeRange": None,
                "ethnicities": [],
                "genders": [],
                "spokenLanguages": [
                    {"language": None, "proficiency": None}
                ],
                "socioEconomicStati": [],
                "skillLevels": [],
                "averageTenure": None
            }
        ],
        "bodies": [
            {
                "id": None,
                "description": None,
                "type": None
            },
            {
                "id": None,
                "description": None,
                "type": None
            }
        ],
        "governances": [
            {
                "id": None,
                "projectType": None
            }
        ],
        "socialContexts": [],
        "useCases": [],
        "adaptations": [
            {
                "id": None,
                "description": None,
                "useCases": [],
                "targetCommunities": [],
                "relatedTeams": []
            },
            {
                "id": None,
                "description": None,
                "useCases": [],
                "targetCommunities": [],
                "relatedTeams": []
            }
        ],
        "participants": [
            {
                "id": None,
                "age": None,
                "location": None,
                "workplaceType": None,
                "ethnicity": None,
                "gender": None,
                "disabilities": [],
                "sexualOrientation": None,
                "religion": None,
                "country": None,
                "spokenLanguages": [
                    {"language": None, "proficiency": None}
                ],
                "socioEconomicStatus": None,
                "skillLevel": None,
                "tenure": None
            }
        ],
        "teams": [
            {
                "id": None,
                "type": None,
                "description": None,
                "startingAgeRange": None,
                "endingAgeRange": None,
                "locations": [],
                "workplaceType": None,
                "ethnicities": [],
                "genders": [],
                "disabilities": [],
                "sexualOrientations": [],
                "religiousBeliefs": [],
                "countries": [],
                "educationalLevels": [],
                "spokenLanguages": [
                    {"language": None, "proficiency": None}
                ],
                "socioEconomicStati": [],
                "skillLevels": [],
                "averageTenure": None,
                "startDate": None,
                "endDate": None,
                "teamSize": None,
                "iterations": None,
                "participants": []
            },
            {
                "id": None,
                "type": None,
                "description": None,
                "startingAgeRange": None,
                "endingAgeRange": None,
                "locations": [],
                "workplaceType": None,
                "ethnicities": [],
                "genders": [],
                "disabilities": [],
                "sexualOrientations": [],
            }
        ]
    }
 


    return dataModel


def unflatten(flat_dict):
    nested = {}
    for flat_key, value in flat_dict.items():
        keys = flat_key.split('_')
        current = nested
        for i, key in enumerate(keys):
            # For intermediate keys, ensure the container is a dict.
            if i < len(keys) - 1:
                if key in current:
                    # If current[key] exists but isn't a dict, replace it.
                    if not isinstance(current[key], dict):
                        current[key] = {}
                else:
                    current[key] = {}
                current = current[key]
            else:
                # Last key: assign the value.
                current[key] = value
    return nested

