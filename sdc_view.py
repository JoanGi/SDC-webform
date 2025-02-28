import streamlit as st
from dataModel import AST
from eventHanlder import handle_value_change
import json



def render_sdc():


    country_options = [
        "USA", "Canada", "Mexico", "UK", "Germany",
        "France", "Italy", "Spain", "Australia", "Japan"
    ]
    EducationalLevelType = ['earlyChildhood','primary','lowerSecondary','upperSecondary','postSecondaryNonTertiary','shortCycleTertiary','bachelorEquivalent','masterEquivalent','doctorateEquivalent']
    SESType = ['upperClass' ,'upperMiddleClass' ,'middleClass' , 'lowerMiddleClass' , 'lowerClass']
    SkillLevelType = ['expert' , 'proficient' , 'advanced' , 'competent' , 'beginner']
    ISO3166 = ['Andorra', 'UnitedArabEmirates', 'Afghanistan', 'AntiguaandBarbuda', 'Anguilla', 'Albania', 'Armenia', 'Angola', 'Antarctica', 'Argentina', 'AmericanSamoa', 'Austria', 'Australia', 'Aruba', 'ÅlandIslands', 'Azerbaijan', 'BosniaandHerzegovina', 'Barbados', 'Bangladesh', 'Belgium', 'BurkinaFaso', 'Bulgaria', 'Bahrain', 'Burundi', 'Benin', 'SaintBarthélemy', 'Bermuda', 'BruneiDarussalam', 'Bolivia,PlurinationalStateof', 'Bonaire,SintEustatiusandSaba', 'Brazil', 'Bahamas', 'Bhutan', 'BouvetIsland', 'Botswana', 'Belarus', 'Belize', 'Canada', 'Cocos(Keeling)Islands', 'Congo,DemocraticRepublicofthe', 'CentralAfricanRepublic', 'Congo', 'Switzerland', 'CôtedIvoire', 'CookIslands', 'Chile', 'Cameroon', 'China', 'Colombia', 'CostaRica', 'Cuba', 'CaboVerde', 'Curaçao', 'ChristmasIsland', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Denmark', 'Dominica', 'DominicanRepublic', 'Algeria', 'Ecuador', 'Estonia', 'Egypt', 'WesternSahara', 'Eritrea', 'Spain', 'Ethiopia', 'Finland', 'Fiji', 'FalklandIslands(Malvinas)', 'Micronesia,FederatedStatesof', 'FaroeIslands', 'France', 'Gabon', 'UnitedKingdomofGreatBritainandNorthernIreland', 'Grenada', 'Georgia', 'FrenchGuiana', 'Guernsey', 'Ghana', 'Gibraltar', 'Greenland', 'Gambia', 'Guinea', 'Guadeloupe', 'EquatorialGuinea', 'Greece', 'SouthGeorgiaandtheSouthSandwichIslands', 'Guatemala', 'Guam', 'Guinea-Bissau', 'Guyana', 'HongKong', 'HeardIslandandMcDonaldIslands', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Ireland', 'Israel', 'IsleofMan', 'India', 'BritishIndianOceanTerritory', 'Iraq', 'Iran,IslamicRepublicof', 'Iceland', 'Italy', 'Jersey', 'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Comoros', 'SaintKittsandNevis', 'Korea,DemocraticPeoplesRepublicof', 'Korea,Republicof', 'Kuwait', 'CaymanIslands', 'Kazakhstan', 'LaoPeoplesDemocraticRepublic', 'Lebanon', 'SaintLucia', 'Liechtenstein', 'SriLanka', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Libya', 'Morocco', 'Monaco', 'Moldova,Republicof', 'Montenegro', 'SaintMartin(Frenchpart)', 'Madagascar', 'MarshallIslands', 'NorthMacedonia', 'Mali', 'Myanmar', 'Mongolia', 'Macao', 'NorthernMarianaIslands', 'Martinique', 'Mauritania', 'Montserrat', 'Malta', 'Mauritius', 'Maldives', 'Malawi', 'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'NewCaledonia', 'Niger', 'NorfolkIsland', 'Nigeria', 'Nicaragua', 'Netherlands,Kingdomofthe', 'Norway', 'Nepal', 'Nauru', 'Niue', 'NewZealand', 'Oman', 'Panama', 'Peru', 'FrenchPolynesia', 'PapuaNewGuinea', 'Philippines', 'Pakistan', 'Poland', 'SaintPierreandMiquelon', 'Pitcairn', 'PuertoRico', 'Palestine,Stateof', 'Portugal', 'Palau', 'Paraguay', 'Qatar', 'Réunion', 'Romania', 'Serbia', 'RussianFederation', 'Rwanda', 'SaudiArabia', 'SolomonIslands', 'Seychelles', 'Sudan', 'Sweden', 'Singapore', 'SaintHelena,AscensionandTristandaCunha', 'Slovenia', 'SvalbardandJanMayen', 'Slovakia', 'SierraLeone', 'SanMarino', 'Senegal', 'Somalia', 'Suriname', 'SouthSudan', 'SaoTomeandPrincipe', 'ElSalvador', 'SintMaarten(Dutchpart)', 'SyrianArabRepublic', 'Eswatini', 'TurksandCaicosIslands', 'Chad', 'FrenchSouthernTerritories', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau', 'Timor-Leste', 'Turkmenistan', 'Tunisia', 'Tonga', 'Türkiye', 'TrinidadandTobago', 'Tuvalu', 'Taiwan,ProvinceofChina', 'Tanzania,UnitedRepublicof', 'Ukraine', 'Uganda', 'UnitedStatesMinorOutlyingIslands', 'UnitedStatesofAmerica', 'Uruguay', 'Uzbekistan', 'HolySee', 'SaintVincentandtheGrenadines', 'Venezuela,BolivarianRepublicof', 'VirginIslands(British)', 'VirginIslands(U.S.)', 'VietNam', 'Vanuatu', 'WallisandFutuna', 'Samoa', 'Yemen', 'Mayotte', 'SouthAfrica', 'Zambia', 'Zimbabwe']
    ISO639 = ['Afar' , 'Abkhazian', 'Avestan' , 'Afrikaans' , 'Akan' , 'Amharic' , 'Aragonese','Arabic','Assamese','Avaric','Aymara','Azerbaijani','Bashkir','Belarusian','Bulgarian','Bislama','Bambara','Bengali','Tibetan','Breton','Bosnian','Catalan-Valencian','Chechen','Chamorro','Corsican','Cree','Czech','ChurchSlavonic-OldSlavonic-OldChurchSlavonic','Chuvash','Welsh','Danish','German','Divehi-Dhivehi-Maldivian','Dzongkha','Ewe','GreekModern','English','Esperanto','Spanish-Castilian','Estonian','Basque','Persian','Fulah','Finnish','Fijian','Faroese','French','WesternFrisian','Irish','Gaelic-ScottishGaelic','Galician','Guarani','Gujarati','Manx','Hausa','Hebrew','Hindi','HiriMotu','Croatian','Haitian-HaitianCreole','Hungarian','Armenian','Herero','Interlingua','Indonesian','Interlingue-Occidental','Igbo','SichuanYi-Nuosu','Inupiaq','Ido','Icelandic','Italian','Inuktitut','Japanese','Javanese','Georgian','Kongo','Kikuyu-Gikuyu','Kuanyama-Kwanyama','Kazakh','Kalaallisut-Greenlandic','CentralKhmer','Kannada','Korean','Kanuri','Kashmiri','Kurdish','Komi','Cornish','Kyrgyz-Kirghiz','Latin','Luxembourgish-Letzeburgesch','Ganda','Limburgan-Limburger-Limburgish','Lingala','Lao','Lithuanian','Luba-Katanga','Latvian','Malagasy','Marshallese','Maori','Macedonian','Malayalam','Mongolian','Marathi','Malay','Maltese','Burmese','Nauru','NorwegianBokmål','NorthNdebele','Nepali','Ndonga','Dutch-Flemish','NorwegianNynorsk','Norwegian','SouthNdebele','Navajo-Navaho','Chichewa-Chewa-Nyanja','Occitan','Ojibwa','Oromo','Oriya','Ossetian-Ossetic','Punjabi-Panjabi','Pali','Polish','Pashto-Pushto','Portuguese','Quechua','Romansh','Rundi','Romanian-Moldavian-Moldovan','Russian','Kinyarwanda','Sanskrit','Sardinian','Sindhi','NorthernSami','Sango','Sinhala-Sinhalese','Slovak','Slovenian','Samoan','Shona','Somali','Albanian','Serbian','Swati','SouthernSotho','Sundanese','Swedish','Swahili','Tamil','Telugu','Tajik','Thai','Tigrinya','Turkmen','Tagalog','Tswana','Tonga','Turkish','Tsonga','Tatar','Twi','Tahitian','Uighur-Uyghur','Ukrainian','Urdu','Uzbek','Venda','Vietnamese','Volapük','Walloon','Wolof','Xhosa','Yiddish','Yoruba','Zhuang-Chuang','Chinese','Zulu']
  
  # Example of how to filter and serialize session state
    def serialize_session_state():
        # Filter out only serializable items (i.e., strings, numbers, lists, dicts)
        serializable_state = {key: value for key, value in st.session_state["form_data"].items() if isinstance(value, (str, int, float, list, dict))}
        
        # Serialize the filtered session state to JSON
        return json.dumps(serializable_state, indent=4)
    
  
  # Function to load cached data (initializes only once)
    @st.cache_data
    def load_cached_data():
        return {}

    # Initialize session state with cached data
    if "form_data" not in st.session_state:
        st.session_state.form_data = load_cached_data()

    # Function to save to cache when any input changes
    def save_to_cache():
        st.cache_data.clear()
        st.cache_data(lambda: st.session_state.form_data)  # Save updated form data

    # Function to save input into cache
    def save_to_cache():
        st.cache_data.clear()  # Clear old cache before saving
        st.cache_data(lambda: st.session_state)  # Save updated state

    # Function to create a text area with caching
    def cached_text_area(label, key, placeholder=""):
        if key not in st.session_state.form_data:
            st.session_state.form_data[key] = ""  # Initialize dynamically
    
        st.text_area(
            label=label,
            placeholder=placeholder,
            key=key,
            value=st.session_state.form_data.get(key, ""),  # Load from session state
            on_change=lambda: (st.session_state.form_data.update({key: st.session_state[key]}), save_to_cache())[1],
    )
        
        # Function to create a text area with caching
    def cached_text_input(label, key, placeholder=""):
        if key not in st.session_state.form_data:
            st.session_state.form_data[key] = ""  # Initialize dynamically
    
        st.text_input(
            label=label,
            placeholder=placeholder,
            key=key,
            value=st.session_state.form_data.get(key, ""),  # Load from session state
            on_change=lambda: (st.session_state.form_data.update({key: st.session_state[key]}), save_to_cache())[1],
    )
        # Function to create a text area with caching
    def cached_radio_input(label, options, key, help=""):
        if key not in st.session_state.form_data:
            st.session_state.form_data[key] = ""  # Initialize dynamically
    
        st.radio(
            label=label,
            options=options,
            key=key,
            help=help,
            #value=st.session_state.form_data.get(key, ""),  # Load from session state
            on_change=lambda: (st.session_state.form_data.update({key: st.session_state[key]}), save_to_cache())[1],
            horizontal=True
        )

    def cached_multiple_radio(key,options,label):

        # Initialize session state for selected countries if needed
        if key not in st.session_state:
            st.session_state[key] = []
        # Display the multiselect widget
        st.multiselect(
            label,
            options=options,
            key=key,
            on_change=lambda: (st.session_state.form_data.update({key: st.session_state[key]}), save_to_cache())[1]
        )
        
        # Function to create a text area with caching
    def participant(key):
        colr, coll = st.columns([1, 1])
        with colr:
            cached_text_input("Name", f"{key}_name", "Name or identifier of the participants")
            # Initialize session state for the number input if it doesn't exist
            agekey = f"{key}_age"
            if  agekey not in st.session_state:
                st.session_state[agekey] = 0  # default value
            # Display a number input widget
            st.number_input(
                label="The age of the participant:",
                key=agekey,
                on_change=lambda: (st.session_state.form_data.update({key: st.session_state[key]}), save_to_cache())[1]
            )
            cached_text_input("Location", f"{key}_location", "The title of the card")
            cached_radio_input("WorkplaceType", ["Presential", "Hybrid", "Remote"],  f"{key}_workdplace", "The title of the card")
            cached_text_input("Ethnicity", f"{key}_ethincity", "The title of the card")
            cached_text_input("Gender", f"{key}_gender", "The title of the card")
            cached_text_input("Disabilities", f"{key}_disabilities", "The title of the card")
            cached_text_input("Sexual Orientation", f"{key}_sexualOrientation", "The title of the card")
            cached_text_input("Religion", f"{key}_religion", "The title of the card")
        with coll:
  
            cached_multiple_radio(f"{key}_countries",ISO3166,"Select one or several countries:")
            cached_multiple_radio(f"{key}_edlevel",EducationalLevelType,"Educational Level")
            cached_multiple_radio( f"{key}_sociostati", SESType,"Socioeconomic Status")
            cached_multiple_radio( f"{key}_skills", SkillLevelType,"Skill Level")
            cached_multiple_radio( f"{key}_languages", ISO3166, "Select one or several langauges spoken by the participant:")
          
            # Initialize session state for the number input if it doesn't exist
            tenkey = f"{key}_tenure"
            if  tenkey not in st.session_state:
                st.session_state[tenkey] = 0  # default value

            # Display a number input widget
            st.number_input(
                label="The professioanl tenure of the participant in years",
                key=tenkey,
                on_change=lambda: (st.session_state.form_data.update({key: st.session_state[tenkey]}), save_to_cache())[1]
            )

    def organization(key):
        cached_text_input("Organization name", f"{key}_name", "Name or identifier of the organization")
        group(key)

    def group(key):
        colr, coll = st.columns([1, 1])
        with colr: 
            agekey = f"{key}_age"
            if  agekey not in st.session_state:
                st.session_state[agekey] = 0  # default value
            # Display a number input widget
            st.slider(
                label="The age of the participant:",
                value=60,
                min_value=0,
                max_value=120,
                key=agekey,
                on_change=lambda: (st.session_state.form_data.update({key: st.session_state[agekey]}), save_to_cache())[1]
            )
            cached_text_input("Location", f"{key}_location", "Location of the organization")
            cached_radio_input("WorkplaceType", ["Presential", "Hybrid", "Remote"],  f"{key}_workplace", "The kind of organization")
            cached_text_input("Ethnicities", f"{key}_ethnicities", "Ethinicities present in the organization, comma sepparated ")
            cached_text_input("Genders", f"{key}_genders", "Distribution and presence of gender presence, domma sepparated ")
            cached_text_input("Disabilities", f"{key}_disabilities", "Disabilities present in the organization, comma sepparated ")
            cached_text_input("Religious Beliefs", f"{key}_religious", "Disabilities present in the organization, comma sepparated ")
        with coll:    
            cached_multiple_radio(f"{key}_countries",ISO3166,"Select one or several countries:")
            cached_multiple_radio(f"{key}_edlevel",EducationalLevelType,"Educational Level")
            cached_multiple_radio( f"{key}_sociostati", SESType,"Socioeconomic Status")
            cached_multiple_radio( f"{key}_skills", SkillLevelType,"Skill Level")
            cached_multiple_radio( f"{key}_languages", ISO3166, "Select one or several langauges spoken by the participant:")
                    # Initialize session state for the number input if it doesn't exist
            agekey = f"{key}_tenure"
            if  agekey not in st.session_state:
                st.session_state[agekey] = 0  # default value

            # Display a number input widget
            st.number_input(
                label="The professioanl tenure of the participant in years",
                key=agekey,
                on_change=lambda: (st.session_state.form_data.update({key: st.session_state[key]}), save_to_cache())[1]
            )

    def init_state(key):
        if key not in st.session_state:
            st.session_state[key] = []

    def add_text_area(key):
        init_state(key)
        st.session_state[key].append("")

    def remove_text_area(index,key):
        if key in st.session_state and 0 <= index < len(st.session_state[key]):
            st.session_state[key].pop(index)
            st.rerun() # Rerun to update the interface
    ##
    ## Title
    ##
    st.title("The Software Diversity Card :woman_and_man_holding_hands: :memo:")

    st.markdown("""\
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        """)

    ##
    ## Master info
    ##
    cached_text_input("The name of the software project", "master_title", "The title of the card")
    cached_text_area("A description of the software project", "master_desc", "The title of the card")


    with st.expander("**Document the teams and crowds in your software**", expanded=True):
        governance, usageContext, participants = st.tabs([
            "Governance",
            "Usage context",
            "Participants"
        ])

        with governance:
            col1, col2 = st.columns([1, 2])
            with col1:
                cached_text_input("Project Type", "governance_projectType", "Specify the type of software project (private, public funded, non-profit, driven by an open-source community, etc.)")
            
            with col2:
                # Multiple value
                key = "governance_govProcesses"
                init_state(key)
                if st.button("Add governament processes"):
                    add_text_area(key)
                # Loop over the array and create a text area with a remove button for each element
                for idx, text in enumerate(st.session_state[key]):
                    # Create two columns: one for the text area, one for the remove button
                    col1, col2 = st.columns([6, 1])
                    with col1:
                        cached_text_area(f"Governament process {idx + 1}", f"governance_govProcesses{idx}", "Specific the governance rules of the software project. For instance, the funders, or the role and the relation between the different bodies that governs the software.")
                    with col2:
                        if st.button("Remove", key=f"{key}_remove_{idx}"):
                            remove_text_area(idx,key)

            # BODIES
            key = "governance_bodies"
            init_state(key)
            if st.button("Add governament bodies"):
                add_text_area(key)
            # Loop over the array and create a text area with a remove button for each element
          
            for idx, text in enumerate(st.session_state[key]):
                # Create two columns: one for the text area, one for the remove button
                with st.container(border=True):
                    col1, col2 = st.columns([2, 2])
                    with col1:
                        cached_text_input("Body name", f"{key}_{idx}_name", "The name of id of the body")
                        cached_text_area("Body description", f"{key}_{idx}_description", "A description of the body")
                    

                    with col2:
                        if st.button("Remove", key=f"{key}_remove_{idx}"):
                          remove_text_area(idx,key)
                        cached_radio_input(f"Body type", ['funders', 'directors', 'administrators', 'other'],  f"{key}_{idx}_type")

                    st.text("If participants in the body are individuals please use the individuals tab. If not, leave it blank.")
                # Button to add a new text area
                    org, individual = st.tabs([
                            "Organization",
                            "Individual",
                        ])
                    with individual:
                        participant(f"{key}_{idx}_participant")
                    with org:
                        organization(f"{key}_{idx}_organization")
              

        with usageContext:
            ##
            ## Age
            ##
            age_checkbox = st.radio("Do you want to specifiy the age of your students?", ["No", "Yes"])
            if age_checkbox == "Yes":
                age_input = st.slider("Age: (**required**)", min_value=0, max_value=100, step=1)

     
        
        with participants:
           st.write("the participants")
          


    ## Showing the generated card and the generated JSON
    st.divider()
    promptTab, impTab = st.tabs(["**Compiled card in markdown**", "**Generated JSON**" ])
    with promptTab:
            html_str= f"""
                    # The Software diversity card of {st.session_state["master_title"]}
                     {st.session_state["master_desc"]} 
                    ## 🏢 Teams Summary

                    <table>
                    <tr>
                        <th>Name</th>
                        <th>Type</th>
                        <th>Age Range</th>
                        <th>Ethnicities</th>
                        <th>Genders</th>
                        <th>Team Size</th>
                        <th>Average Tenure</th>
                        <th>Start Date</th>
                        <th>Location</th>
                    </tr>
                    <tr>
                        <td><strong>DevelopmentTeam</strong></td>
                        <td>DevelopmentTeam</td>
                        <td>25-30</td>
                        <td>Colombian, Brazilian, Argentinian, French, Spanish, Pakistani, Serbian, Iranian, Moroccan, Italian</td>
                        <td>Male 80%, Female 20%</td>
                        <td>15</td>
                        <td>4.3</td>
                        <td>11-08-2022</td>
                        <td>Luxembourg</td>
                    </tr>
                    <tr>
                        <td><strong>Usability Testers</strong></td>
                        <td>Tester Team</td>
                        <td>22-24</td>
                        <td>French</td>
                        <td>Non-disclosed</td>
                        <td>18</td>
                        <td>0.5</td>
                        <td>17-10-2023</td>
                        <td>University of Luxembourg</td>
                    </tr>
                    <tr>
                        <td><strong>Computer Science Students</strong></td>
                        <td>Target Community</td>
                        <td>18-100</td>
                        <td>Non-disclosed</td>
                        <td>Non-disclosed</td>
                        <td>-</td>
                        <td>0</td>
                        <td>-</td>
                        <td>France & Luxembourg</td>
                    </tr>
                    <tr>
                        <td><strong>Climate Public Servants</strong></td>
                        <td>Target Community</td>
                        <td>20-100</td>
                        <td>Non-disclosed</td>
                        <td>Non-disclosed</td>
                        <td>-</td>
                        <td>3-5</td>
                        <td>-</td>
                        <td>Luxembourg</td>
                    </tr>
                    </table>

                    ---
                  """
            # Provide a download button
            st.download_button(
                label="Download Markdown",
                data=html_str,
                file_name="SoftareDiveristyCard.md",
                mime="text/markdown"
            )
            st.markdown(html_str, unsafe_allow_html=True)
    with impTab:

            # Convert the session state to a JSON string
            session_state_json = json.dumps(serialize_session_state(), indent=4)
            st.download_button(
                label="Download JSON",
                data=session_state_json,
                file_name="SoftareDiveristyCard.json",
                mime="application/json"
            )
            # Display the session state as pretty JSON
            st.json(serialize_session_state())
         