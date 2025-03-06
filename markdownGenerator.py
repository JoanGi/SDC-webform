def generate_markdown(state):


###############################
## Start Summary
###############################
    html_str= f"""
# The Software diversity card of {state["master"]["title"]}
{state["master"]["desc"]} 

## :busts_in_silhouette: Teams Summary

<table>
<tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
    <th>Age Range</th>
    <th>Team Size</th>
    <th>Location</th>
</tr>"""
    
    ## Participants
    if 'participants' in state and isinstance(state['participants'], dict):
        for key, participant in state['participants'].items():
            if participant['name']:
                    description = participant['description'].replace('\\n', '')
                    html_str = html_str + f"""     
    <tr>
        <td><strong>{participant['name']}</strong></td>
        <td>{description}</td>
        """
            if 'type' in participant:
                html_str = html_str + f"""<td>{participant['type'][0]}</td>"""
            else:
                html_str = html_str + f"""<td> </td>"""

            html_str = html_str + f"""    
        <td>{participant['age'][0]}-{participant['age'][1]}</td>
        <td>{participant['size']}</td>
        <td>{participant['location']}</td>
    </tr>"""
        
    ## If target Communities add it
    if 'targetCommunity' in state['usageContext'] and isinstance(state['usageContext']['targetCommunity'], dict):
        for key, targetCommunity in state['usageContext']['targetCommunity'].items():
            if targetCommunity['name']:
                    description = targetCommunity['description'].replace('\\n', '')
                    html_str = html_str + f"""     
<tr>
<td><strong>{targetCommunity['name']}</strong></td>
    <td>{description}</td>
    <td> Targeted Community </td>
    <td>{targetCommunity['age'][0]}-{targetCommunity['age'][1]}</td>
    <td> many </td>
    <td>{targetCommunity['location']}</td>
</tr>"""
    ## If bodies add 
    if 'governance' in state:
        if 'bodies' in state['governance'] and isinstance(state['governance']['bodies'], dict):
            for key, body in state['governance']["bodies"].items():
                if body['name']:
                    description = body['description'].replace('\\n', '')
                    html_str = html_str + f"""     
        <tr>
        <td><strong>{body['name']}</strong></td>
        <td>{description}</td>"""
                if 'type' in body:
                    html_str = html_str + f"""<td>{body['type'][0]}</td>"""
                else:
                    html_str = html_str + f"""<td> </td>"""
                if 'organization' in body:
                    if body['organization']['name']:
                        html_str = html_str + f""" 
            <td>{body['organization']['age'][0]}-{body['organization']['age'][1]}</td>
            <td> - </td>
            <td>{body['organization']['location']}</td>
            </tr>"""    
                if 'participant' in body:
                    if body['participant']['name']:
                            html_str = html_str + f""" 
            <td>{body['participant']['age']}</td> 
            <td> - </td>
            <td>{body['participant']['location']}</td>
            </tr>"""
        
    ## End summary
    html_str = html_str + f"   </table>"

###############################
## Start Governance
###############################
    html_str = html_str + f"""

## 🏢 Governance
    
    """
    if 'governance' in state:
        if 'govProcesses' in state['governance'] and isinstance(state['governance']['govProcesses'], dict):
            for key, text in state['governance']["govProcesses"].items():
                  html_str = html_str + f"""
### Governance processes

**Process**: {text} 
"""
        if 'projectType' in state['governance']:
            html_str = html_str + f"""

**Type:** {pretty_list(state['governance']['projectType'])}
"""
            
      
        if 'bodies' in state['governance'] and isinstance(state['governance']['bodies'], dict):
            for key, body in state['governance']["bodies"].items():
                if body['name']:
                    description = body['description'].replace('\\n', '')
                    html_str = html_str + f"""     
   
#### **{body['name']}**

**Description:** {description}

"""
                if 'type' in body:
                    html_str = html_str + f"""
**Type:** {body['type'][0]} 

""" 
                if body['organization']['name']:
                    html_str = html_str + f""" 
**Organization:** {body['organization']['name']} 
"""
                if body['organization']['location']:
                    html_str = html_str + f""" 
**Location:** {body['organization']['location']} 

"""
                if body['organization']['age']:
                    html_str = html_str + f""" 
**Age range:** {body['organization']['age'][0]}-{body['organization']['age'][1]} 

"""
                if body['organization']['ethnicities']:
                    html_str = html_str + f""" 
**Ethnicities:** {body['organization']['ethnicities']} 
"""
                if body['organization']['genders']:
                    html_str = html_str + f""" 

**Genders:** {body['organization']['genders']} 

"""
                if 'languages' in body['organization']:
                       html_str = html_str + f""" 
**Languages:** {pretty_list(body['organization']['languages'])} 

"""

            
                if body['participant']['name']:
                         html_str = html_str + f""" 
**Organization:** {body['participant']['name']}
"""
                if body['participant']['location']:  
                     html_str = html_str + f""" 
**Location:** {body['participant']['location']}

"""
                if body['participant']['age']:  
                     html_str = html_str + f"""     
**Age range:** {body['participant']['age']}

"""
                if body['participant']['ethincity']:  
                     html_str = html_str + f""" 
**Ethnicities:** {body['participant']['ethincity']}

"""
                if body['participant']['gender']:  
                     html_str = html_str + f""" 
**Genders:** {body['participant']['gender']}

"""
                if 'languages' in body['participant']:
                    html_str = html_str + f""" 
** Languages: ** {pretty_list(body['participant']['languages'])}

"""
                    
###############################
## Start Usage Context
###############################
    if 'usageContext' in state:
        html_str = html_str + f"""

## :twisted_rightwards_arrows: Usage Context
    
"""
        if 'description' in state['usageContext']:
            html_str = html_str + f"""

**Description:** {state['usageContext']['description']}

"""
        if 'countries' in state['usageContext']:
             html_str = html_str + f"""
**Countries:** {pretty_list(state['usageContext']['countries'])}

"""
        if 'languages' in state['usageContext']:
            html_str = html_str + f"""
**Languages:** {pretty_list(state['usageContext']['languages'])}

"""
        if 'targetCommunity' in state['usageContext'] and isinstance(state['usageContext']['targetCommunity'], dict):        
            for key, targetCommunity in state['usageContext']['targetCommunity'].items():
            
              if 'name' in targetCommunity:
                html_str = html_str + f"""
#### Target Community: {targetCommunity['name']}

"""
              if 'description' in targetCommunity:
                html_str = html_str + f"""
**Description:** {targetCommunity['description']}

"""
              if 'age' in targetCommunity:
                 html_str = html_str + f""" 
**Age range:** {targetCommunity['age']}
"""
              if 'location' in targetCommunity:
                html_str = html_str + f""" 
**Location:** {targetCommunity['location']}

"""
        if 'adaptation' in state['usageContext'] and isinstance(state['usageContext']['adaptation'], dict):        
            for key, adaptation in state['usageContext']['adaptation'].items():
                if 'name' in adaptation:
                    html_str = html_str + f""" 
#### Adaptation: **{adaptation['name']}**

"""
                if 'description' in adaptation:
                    html_str = html_str + f""" 
{adaptation['description']}

"""
                    

###############################
## Start Participants
###############################
    if 'participants' in state:
        html_str = html_str + f"""

## :hammer_and_wrench: Participants     

"""
      ## Participants
        if isinstance(state['participants'], dict):
            for key, participant in state['participants'].items():
                if 'name' in participant:
                    html_str = html_str + f""" 
### {participant['name']}

"""
                if 'description' in participant:
                    html_str = html_str + f""" 
**Description:** {participant['description']}

"""
                if 'type' in participant:
                    html_str = html_str + f""" 
**Type:** {pretty_list(participant['type'])}

"""
                if 'size' in participant:
                    html_str = html_str + f""" 
**Size:** {participant['size']}

"""
                if 'location' in participant:
                    html_str = html_str + f""" 
**Location:** {participant['location']}

"""
                if 'workplace' in participant:
                    html_str = html_str + f""" 
**Workplace:** {participant['workplace']}

"""
                if 'ethnicitise' in participant:
                    html_str = html_str + f""" 
**Ethnicitise:** {participant['ethnicitise']}

"""
                if 'genders' in participant:
                    html_str = html_str + f""" 
**Genders:** {participant['genders']}

"""
                if 'countries' in participant:
                    html_str = html_str + f""" 
**Countries:** {pretty_list(participant['countries'])}

"""
                if 'edlevel' in participant:
                    html_str = html_str + f""" 
**Educational level:** {pretty_list(participant['edlevel'])}

"""
                if 'skills' in participant:
                    html_str = html_str + f""" 
**Skills level:** {pretty_list(participant['skills'])}

"""
                if 'languages' in participant:
                    html_str = html_str + f""" 
**Languages Spoken:** {pretty_list(participant['languages'])}

"""


    return html_str

def pretty_list(list):
    return ', '.join(list)