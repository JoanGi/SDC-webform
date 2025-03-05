def generate_markdown(state):
    print(state)
    html_str= f"""
# The Software diversity card of {state["master"]["title"]}
{state["master"]["desc"]} 
## 🏢 Teams Summary

<table>
<tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
    <th>Age Range</th>
    <th>Ethnicities</th>
    <th>Genders</th>
    <th>Team Size</th>
    <th>Location</th>
</tr>"""
    ## If development team addit
    if 'participants' in state:
        for key, participant in state['participants'].items():
            if participant['name']:
                    html_str = html_str + f"""     
    <tr>
        <td><strong>{participant['name']}</strong></td>
        <td>{participant['description'].replace('\n', '')}</td>
        """
            if 'type' in body:
                html_str = html_str + f"""<td>{body['type'][0]}</td>"""
            else:
                html_str = html_str + f"""<td> </td>"""

            html_str = html_str + f"""    
        <td>{participant['age'][0]}-{participant['age'][1]}</td>
        <td>{participant['ethnicities']}</td>
        <td>{participant['genders']}</td>
        <td>{participant['size']}</td>
        <td>{participant['location']}</td>
    </tr>"""
        ## If target Communities add it
    if state['socialContext']['targetCommunity']['name']:
                        html_str = html_str + f"""     
<tr>
<td><strong>{state['socialContext']['targetCommunity']['name']}</strong></td>
    <td>{state['socialContext']['targetCommunity']['description'].replace('\n', '')}</td>
    <td> Targeted Community </td>
    <td>{state['socialContext']['targetCommunity']['age'][0]}-{state['socialContext']['targetCommunity']['age'][1]}</td>
    <td>{state['socialContext']['targetCommunity']['ethnicities']}</td>
    <td>{state['socialContext']['targetCommunity']['genders']}</td>
    <td> many </td>
    <td>{state['socialContext']['targetCommunity']['location']}</td>
</tr>"""
    ## If bodies add 
    if 'governance' in state:
        if 'bodies' in state['governance']:
            for key, body in state['governance']["bodies"].items():
                if body['name']:
                    html_str = html_str + f"""     
        <tr>
        <td><strong>{body['name'].replace('\n', '')}</strong></td>
        <td>{body['description'].replace('\n', '')}</td>"""
                if 'type' in body:
                    html_str = html_str + f"""<td>{body['type'][0]}</td>"""
                else:
                    html_str = html_str + f"""<td> </td>"""
                if body['organization']['name']:
                    html_str = html_str + f""" 
        <td>{body['organization']['age'][0]}-{body['organization']['age'][1]}</td>
        <td>{body['organization']['ethnicities']}</td>
        <td>{body['organization']['genders']}</td>
        <td> - </td>
        <td>{body['organization']['location']}</td>
        </tr>"""    
            
                    if body['participant']['name']:
                        html_str = html_str + f""" 
        <td>45</td> 
        <td>{body['participant']['ethincity']}</td>
        <td>{body['participant']['gender']}</td>
        <td> - </td>
        <td>{body['participant']['location']}</td>
        </tr>"""
        
    ## End summary
    html_str = html_str + f"   </table>"

                   
    return html_str