import streamlit as st
from streamlit_option_menu import option_menu
import requests as r
import babel.numbers
from PIL import Image
from sklearn.impute import KNNImputer
from pycoingecko import CoinGeckoAPI
import streamlit.components.v1 as components
from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly_express as px
import statsmodels.api as sm
import webbrowser
import openpyxl as xls
import yfinance as yf
#_____________________________________________________________
st.set_page_config(layout="wide")
#_____________________________________________________________
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#_____________________________________________________________
#Insert navigation bar menu
Nav_Menu=option_menu(None,["Resume","GFC & Regulatory Compliance Analysis",
                           "Capital Markets Analysis","Stablecoins Analysis","Geography of Cryptocurrency Report",
                           "DeFi Liquidity Aggregator","SQL Business Analysis","System Architecture Analysis",
                           "Financial & Marketing Analysis","Business Ethics Analysis"],
                     icons=['house','briefcase-fill','bank', 'currency-bitcoin', 'pin-map-fill', 'droplet-half',
                            'bar-chart-fill','cpu-fill', 'activity', 'credit-card-2-back'],
                     default_index=0,
                     orientation="horizontal")

#insert condition of the navigation meny

if Nav_Menu == "Resume":
    Space_col1,Photo_col2,Space_col3=st.columns(3)

    with Space_col1:
        "\n"
        "\n"
        "\n"
        st.write("[LinkedIn](https://www.linkedin.com/in/guy-gnakpa/)", width="right")

    with Photo_col2:
        st.markdown("<h1 style='text-align: center; color: white;'>""Guy L. Gnakpa""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: white;'>"" ""</h1>", unsafe_allow_html=True)
        image0 = Image.open("IMG_2675.JPG")
        st.image(image0, width=400)
    with Space_col3:
        "\n"
        "\n"
        "\n"
        st.write("[Github](https://github.com/guygnakpa)")
    ###--------------------------------------------------------------###
    # Custom function for printing text
        def txt(a, b):
            col1, col2 = st.columns([4,1])
            with col1:
                st.markdown(a)
            with col2:
                st.markdown(b)
        def txt2(a, b):
            col1, col2 = st.columns([1,4])
            with col1:
                st.markdown(f'`{a}`')
            with col2:
                st.markdown(b)
        def txt3(a, b):
            col1, col2 = st.columns([1,2])
            with col1:
                st.markdown(a)
            with col2:
                st.markdown(b)
        def txt4(a, b, c):
            col1, col2, col3 = st.columns([1.5,2,2])
            with col1:
                st.markdown(f'`{a}`')
            with col2:
                st.markdown(b)
            with col3:
                st.markdown(c)

# ###--------------------------------------------------------------##
    st.markdown("## Profile", unsafe_allow_html=True)
    st.info("""A goal-oriented and collaborative professional with years of experience in financial services. 
    Hand on experience with fund management and administration for alternative assets in investment banking. Holds a 
    graduate-level education in management sciences and quantitative methods. Skilled at utilizing analytical tools to 
    better understand data for valuable insights with a focus on Data Analysis, ML Models, Data Visualization and Strategic 
    Reporting. Ability to adapt quickly, identify inefficiencies and communicate effectively with stakeholders. Passionate about 
    financial instruments, technology and the implication of decentralized ledger technology for decades to come. Seeking a challenging 
    opportunity with a renown and innovative culture where my experience, skills and education can add value for all stakeholders.""")

###--------------------------------------------------------------##
### Skills ###
    st.markdown("## Skills", unsafe_allow_html=True)
    st.info("""
    - Machine Learning Models (Regression, Time-series, Clustering, Decision Trees), Statistical Analysis (Exploratory, Predictive, Reporting)
    - Python (Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, Streamlit), Data Visualization/BI (Tableau) Data Wrangling (MySQL)
    - Microsoft Office (Word, Excel, PowerPoint, Visio, Project), Coaching and Mentoring – AICPA (06/21)
    - Blockchain (POW, POS, L1, L2), Defi Protocols (Dex, Asset Management, Lend/Borrow, Yield)
    """)

###--------------------------------------------------------------##
###Education###
    st.markdown("""## Education """,unsafe_allow_html=True)
    #Master of Science, Management Sciences and Quantitative Methods
    txt("**Master of Science**, *Management Sciences and Quantitative Methods*","****Jan 2021-Apr 2022****")
    st.markdown("""
    - Southern New Hampshire University, Manchester, NH
    - NECHE Accredited
    - GPA :  3.8/4.0
    """)
    #
    #Bachelor of Arts, Economics
    txt("**Bachelor of Arts**, *Economics*","****Sep 2017-Dec 2019****")
    st.markdown("""
    - Ramapo College of New Jersey, Mahwah, NJ
    - AACSB Accredited
    - GPA :  3.0/4.0
    """)
    ###--------------------------------------------------------------##
    ###EXPERIENCE###
    st.markdown("""## Experience
     """)
    txt("###### ****BNY Mellon, Woodland Park, NJ****", "****Jul 2020-Jan 2021****")
    st.text("Analyst, Fund Of Funds Custody (Full-Time)")
    st.markdown("""
    - Assisted in the daily custodial management for alternative asset investments. 
    - Utilized dashboards and management software tools to report on fund allocations. 
    - Daily communications with internal and external stakeholders led to quality monthly performance. 
    - Executed and monitored trade instructions; subscriptions, redemptions, proxies, and transfers. 
    - Conducted daily cash reconciliations for direct demand deposits on behalf of the clients. 
    - Employing AML/KYC procedures in funds distribution resulted in quality administrative duty and reporting. 
    - Authenticated trade instructions and facilitated inquiries in the interest of the client’s investments. 
    - Collaborated with Treasury and Operations teams in effort to execute on-demand wired transfers. 
    - Adapting management tools for monthly custody holding fees resulted in accurate and efficient reporting. 
  
    """)

    txt("###### ****Premium Merchant Funding, New York, NY****", "****Oct 2018-Sept 2019****")
    st.text("Analyst, Account Management (Full-Time)")
    st.markdown("""
    - Facilitated a funding team responsible for monthly capital investment allocation in SMEs. 
    - Exercised a leadership role by training interns on the offered financial products and services. 
    - Utilized Google Suite for communication management for all stakeholders. 
    - Presentation of products and services to new and existing clients resulted in a positive increase in capital investments.
    - Analyzed financial statements, credit history and contract documents to identify ambiguity between financial documents and prerequisites. 
    - Verified business account history to determine previous level of compliance with term structure. 
    - Recommendations of business strategy for future capital investment approval led to an increase of quality service demand. 
 
    """)

    txt(" ###### ****Lobster Life Systems, Lodi, NJ****", "****Aug 2016-Aug 2017****")
    st.text("Assistant Project Manager, Internship (Full-Time)")
    st.markdown("""
    - Conducted administrative duties for a manufacturing and wholesale business. 
    - Implemented management strategies for on demand resources. 
    - Onboarded new team members to maintain and supply the demand for services. 
    - Adapted administrative aides, hands on manufacturing production and inventory management. 
    - Assisted in the strategy of expansion and client acquisition in the northeast region of the country. 
    - Facilitated communication between internal and external project stakeholders to keep all parties well-informed.  
  
    """)

    # ###--------------------------------------------------------------###
    ###PROJECTS###
    st.markdown("## Projects", unsafe_allow_html=True)
    txt4("Global Financial Crimes & Regulatory Compliance Analysis",
                                     "An analysis on global financial crimes and regulatory compliance in banking."
                                     "The purpose of a compliance division in a bank and its core responsibilities are discussed. "
                                     "Financial regulators responsible for governing, monitoring and enforcing respective laws are highlighted  "
                                     "Risk factors associated with compliance in banking are mentioned as well as risk management systems ."
                                     "Data analysis of suspicious activity filings is conducted and reported through metric visualization  .",
                                    "FinCEN Data, Data manipulation and visual engineering all completed with excel, tableau and python libraries.")

    txt4("Capital Markets Analysis", "An analysis on capital markets focused on equity and bond securities. The primary and secondary "
                                    "markets are discussed. Economic factors which effect these markets are explored and illustrated through "
                                    "data visualisations. Time-series index analysis were conducted with satistical methologies. The market "
                                    "capitalization of selected Bond ETFs securities are calculated and visually displayed.",
                                    "API Requests, Data manipulation and visual engineering all completed with excel and python libraries.")
    txt4("Stablecoins Analysis", "An analytical research document describing stablecoins and their functions. The opportunities and risks "
                                 "are discused. Trend analysis and Machine learning modeling are utilised to convey existing relationship "
                                 "between Bitcoin and Stablecoins.",
                                 "Machine Learning with Python, Visual engineering with Python, Visualization Dashboard with Tableau.")
    txt4("Geography of Cryptocurrency Report", "An analysis on received and deposited funds based on-chain data. The analysis explores "
                                 "existing trends within geographic locations. Fundamental questiones are explored to produce insightful feedback. ",
                                "On-Chain Data, Data manipulation and Visual engineering with Python Libraries.")
    txt4('DeFi Liquidity Aggregator', "A DeFi liquidity aggregator interactive dashboard. Representation of decentralized application (dapp) as an "
                                      "insightful tool for fundamental understanding of liquidity allocation. Aggregates total value locked, market "
                                      "capitalization, daily volume, and other metrics for tracking DeFi activity.",
                                      "API Requests, Data manipulation and Visual Engineering all with Python libraries.")
    txt4('SQL Business Analysis', "An SQL query case study for a small business operation. Conducted 4 queries, "
                                              "asking 4 fundamental questions. Turning results of the questions and queries into an insightful "
                                              "feedback accompanied with recommendations for increasing revenue.",
                                              "SQL for Data Queries. Python and Streamlit for front-end execution.")
    txt4("System Architecture Analysis","A system architecture case study focused on system development for data management,"
                                         " service scheduling and daily reporting for a small business. A full analysis of developing an internal "
                                         "Electronic Data Interchange has been conducted and tested via reports.",
                                         "Microsoft Project, Microsoft Visio, Microsoft Excel, Microsoft Word, Discord, and Python were all utilized")
    txt4("Financial & Marketing Analysis","A case study higlighting the utilization of financial documents and reportings "
                                          "to evaluate how to strategically implement a product in a new market sector.","Completed with Google Suite")
    txt4("Business Ethics Analysis","Business Ethics case study evaluating ethical approaches to marketing, and corporate social responsibility.",
                                    "Completed with Google Suite")
    #Insert Resume for Download
    with open("GuyGnakpa_CV_1.0.pdf", "rb") as file:
        Button = st.download_button(
            label="Download Resume",
            data=file,
            file_name="GuyGnakpa_CV_1.0.pdf",
            mime="image/png"
        )

    st.write("")

    st.info("""
    DISCLAIMER: The production of these analyses are solely for educational purposes. The data used to explain certain events 
    is subject to change, and the analyses are not intended to be used as investment tools. 
    If these analyses are used for any other purposes than intended, the author is not liable.
    """)
########################################################################################################################
########################################################################################################################
########################################################################################################################
if Nav_Menu == "GFC & Regulatory Compliance Analysis":
    #insert title of Financial Crimes and Compliance Analysis
    st.markdown("<h1 style='text-align: center; color: white;'>""Global Financial Crimes & Regulatory Compliance in Banking ""</h1>", unsafe_allow_html=True)
    #Name on document
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Guy Gnakpa""</h1>", unsafe_allow_html=True)
    #Date of on documents
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" February, 2023""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>" "</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>" "</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>" "</h1>", unsafe_allow_html=True)
    #____________________________________Introduction of Compliance ________________________________________________________
    #insert summary title and body
    st.header("Summary")
    st.write("<div style='text-align:justify'> ""\n"
             "The global banking industry market has grown significantly over the past decades. As of Q3 2021, the industry had an estimated "
             "market capitalization of ~$8.36 trillion. The industry had an increase of 44.13% from its previous valuation in Q3 2020 (~$5.80 trillion), (Abby McCain, Zippia.com). "
             "The trend suggests the market will continue to show signs of positive growth over the coming years. The industry growth has led higher number of human capital "
             "to adequately satisfy the increasing number of clients. Digital transformation initiatives have been adopted to create efficiency within processes. "
             "Although the growth has positively effected earnings, global banking institutions face many challenges. The most evolving and important challenge is regulatory compliance "
             """due to a large number of risk factors. According to Mckinsey, "since 2009, regulatory fees have dramatically increase relative to bank's earnings"(Piotr Kaminski, mckinsey.com). """
             "This suggests the level of risk factors are continuously creating evolving challenges for the compliance department in many of the global banking institutions. "
             ,unsafe_allow_html=True)

    #insert expander for earnings vs fine and settlements.
    EarningsVSFees=Image.open("Earnings_VS_Fees.png")
    McKinseyButton=st.expander(label="Performance of 20 large US and EU Universal Banks vs. Fines Settlements")
    McKinseyButton.image(EarningsVSFees)
    #insert Purpose title and body
    st.header("Purpose")
    st.write("<div style='text-align:justify'> ""\n"
             "The objective of this documentation is to highlight the role of regulatory compliance and governance in banking, financial regulatory authorities, "
             "risk factors in banking, and relevant risk management systems. The subcategory of regulatory compliance in banking, Global Financial Crimes unit, will be mainly expolored. "
             "Further, an analysis of suspicious activity report(SAR) will be inclused to showcase "
             "and quantify challenges many financial institutions continuously face. "
             ,unsafe_allow_html=True)
    st.write("")
    st.write("---")
    #insert first point title and body
    st.subheader("Regulatory compliance and governance in banking")
    st.write("<div style='text-align:justify'> ""\n"
             "The compliance department hold a huge responsibility in the structure of a global bank. "
             "Although the compliance division consist of many functions, they all lead to a central goal; risk management. "
             "In the banking structure the compliance division is the second line of of defence for managing numerious diverse risk factors. "
             "The division must ensure the bank operates according to domestic and internal regulations. In addition, the divison is tasked to "
             "create, govern, monitor and revise compliance program and internal bank policy. Any suspicious fiancial activities are monitored and reported to financial regulators "
             "by the compliance department on behalf of the bank. Below are some of the core functions of the compliance(GFC) division but not limited to: "
             ,unsafe_allow_html=True)
    #insert core functions of the compliance division
    st.info("""
    - Anti-Corruption
        -
        - regulations and procedures in place to prevent corruption where the abuse of power or position is utilized for personal gain. Acitivities like embezzlement, bribery, use of secret informatin are all forms of unethical behavior that are subject to the Anti-corruption laws. The Anti-corruption procedures are meant to mitigate risks of fraud, promote transparency accountability and integrity wihtin banking.  
        - To prevent the risk of such activities the compliance division may implement policies, education, conduct internal and external audits.
        - Anti-corruption is governed by many authorities including; Department of Justice(DOJ), Securities and Exchange Commission(SEC), Financial Crime Enformance Network(FinCen), Federal Bureau of Investigation(FBI), Internal Revenue Services(IRS).
        - The Anti-corruption prevention is part of the American Anti-Corruption Act(AACA).
    - Anti-Money Laundering
        - 
        - regulations and procedures in place to prevent the efforts of concealing illicit funds as legitimate income. Regulators required transaction of $10,000 or more to be reported. Futher, it is required to conduct due diligence on customers through the process of Know Your Customer(KYC).
        - KYC enables for banks to better identity new clients, the nature of their activities, and clarification on the source of funds. KYC ensure customers are not part of a crimal organization, under economic sanctions by U.S regulators, nor politically affiliated.
        - Anti-money laundering and KYC procedures begin with the Bank Secrecy Act(1970), and are now part of The Anti-Money Laundering Act of 2020 in order to keep up with the increase of illicit activities. This law is engoreced by The Department of the Treasury, especifically the bureau of Financial Crimes Enforcement Network(FinCEN).  
    - Anti-Tax Evasion
        -
        - regulations and procedures in place to prevent, detect and monitor suspicious activities associated with tax evasion. The objective of these procedures is to prevent tax avoidance and promote integrity within the financial system.   
        - Banking institutions must comply with regulations set forth by Foreign Account Tax Compliance Act(FATCA), Common Reporting Standard(CRS), and the U.S. Internal Revenue Code. 
    - Anti-boycott
        -
        - regulations and procedures in place by U.S regulators prohibiting discrimination or the refusal of conducting business with countries or companies that are unsanctioned by the U.S government. Share information of unsanctioned boycotted countries and firms is also prohibited by the U.S.
        - Anti-Boycott Act of 2018 is part of the Export Control Reform Act of 2018 (ECRA). This law is enforced by the Bureau of Industry and Security(BIS).
    - Economic Sanctions - OFAC
        -
        - regulations and procedures in place to monitor and prevent economic transactions with individuals, entities or countries who are sanctions by U.S regulators. The policies in play help metigate risks associated with banking operations, national security and froeign policy.  
        - The Office of Foreign Assets Control(OFAC) division in the U.S. Treasury Department is responsible for enforcing this regulation. OFAC impose economic sanctions against specific countries, terrorist and crimical organizations.  
    - Political Contributions
        -
        - regulations and procedures in place to monitor and prevent corruption associated with financial donation in order to gain political influence.  
        - political contributions are subject to the Federal Election Campaign Act laws enforced by Federal Election Commission(FEC)
    """)
    #insert second point: description for regulatory bodies
    st.subheader("Financial regulatory authorities")
    st.write("<div style='text-align:justify'> ""\n"
             "Global financial institutions are regulated by many U.S and international agencies based on the banking structure. "
             "Below are a list of U.S. agencies who are responsible for the prevention of fraud and maintaining fairness, integrity, and accountibility in banking. "
             "Use the expand buttons below to see specific regulatory bodies responsible to enforce, govern and monitor the banking and security industry "
             ,unsafe_allow_html=True)
    st.write("")
    #insert expander button for each type of regulators
    Banking_Regulators=st.expander(label="Expand to see the relevant banking regulators ")
    Banking_Regulators.info("""
    - Consumer Financial Protection Bureau (CFPB) - consumer compliance
    - Federal Reserve System ("Fed")
    - Federal Deposit Insurance Corporation (FDIC)
    - Office of the Comptroller of the Currency (OCC)
    - National Credit Union Administration (NCUA)
    - Farm Credit Administration (FCA)
    - Federal Financial Institutions Examination Council (FFIEC) - main umbrella group for US Federal banking authorities
    - Conference of State Bank Supervisors (CSBS) [4] - main umbrella group representing US State and Territorial banking supervisors
    """)
    Securities_Regulators=st.expander(label="Expand to see the relevant securities regulators")
    Securities_Regulators.info("""
    - Securities & Exchange Commission (SEC)
    - Commodity Futures Trading Commission (CFTC)
    - Securities Investor Protection Corporation (SIPC)
    - Financial Industry Regulatory Authority (FINRA)
    - Municipal Securities Rulemaking Board (MSRB)
    - National Futures Association (NFA)[5]
    """)
    Other_Regulators=st.expander(label="Expand to see other relevant regulators")
    Other_Regulators.info("""
    - Financial Stability Oversight Board (FSOC) - systemic risk
    - Federal Housing Finance Agency (FHFA) - government sponsored housing finance
    - Financial Crimes Enforcement Network (FinCEN) - anti-money laundering
    - National Association of Insurance Commissioners (NAIC) - insurance
    - Each US state and territory generally has its own banking, insurance, and securities authorities
    """)
    st.write("---")
    #insert risk factors in banking
    st.subheader("Risk factors")
    st.write("<div style='text-align:justify'> ""\n"
             "More than ever banks are facing many challenges that are placing more pressure on compliance divisions to better operate "
             "with integrity and adhere to applicable laws, regulations and internal policies. Aside from the compliance department's core functions of "
             "enforcing Anti-Money Laundering(AML), Anti-Corruption, Anti-Tax Evasion, Economic Sanctions, and Political Contribution regulatory requirements, many other "
             "risk factors must be mitigated. Below are many other risk factors a compliance division may be faced with."
             ,unsafe_allow_html=True)
    st.info("""
    - Market risk
    - Financial Risk
    - Operation risk
    - Reputation Risk
    - Compliance Cost
    - Regulatory change
    - Digital transformation risk
    - Hybrid work environments risk 
    - Legal and regulatory penalties
    """)
    #insert relevant risk management systems for growing risk factors
    st.subheader("Risk management systems")
    st.info("""
    - Continue to implement adequate procedures to govern, monitor and report suspicious activity related to anti-money laundering, anti-tax evasion, anti-corruption, economic sanctions, and political contributions.   
    - Implement quality specialised training programs to better educate employees on relevant and evolving regulations.  
    - Continue to conduct internal audit, review and address compliance policies to identify inefficiencies that can lead to potencial risks.  
    - Implementing a more advance monitoring and reporting system to recognize and address risk factors associated with regulatory violation. 
    - Increase the use of data analysis to better understand trends associated with internal policies performance and financial activities. 
    - Increase reporting to senior management and the Board of Directors on compliance-related risks and the effectiveness of risk management measures. 
    - Improve relationships with regulatory agencies to stay informed on evolving laws and regulations. 
    """)
    st.write("---")
    #insert title and body of suspicious activity report
    st.subheader("Suspicious Activity Report(SAR) Analysis")
    st.info("""
    - The compliance division is the second line of defence against any illicit activities.
    - Per regulations, the division must monitor, and report any suspicious activities under the bank's supervision. 
    - The Global Financial Crimes sub-division of the compliance department is responsible for monitoring and reporting metrics associated with financial crimes. In addition, any found evidence of illicit activity must be filed with the respective regulatory agency. 
    - Blow is an analysis of Suspicious Activity Report(SAR) filed by entities in the Depository and Securities/Futures industry. 
    - The visualizations highlight key metrics within the data provided by Financial Crimes Enforcement Network(FinCEN)
    """)


    st.info("""
    - SAR: Filings of Depository Institution Industry
        - 
        - From 2014 to 2021 there is a positive trend in the number of SAR filings. 
        - More recently from 2020 to 2021 the number of SAR has increased by 17.78%.
        - When observing filings by specific categories from 2020 -2021, the data suggests Mortgage Fraud is down 22.41% and Terririst Financing is down by 15.18%.
        - Amongst the top 25 types of suspicious activity filed from 2014 - 2021, "Suspicion Concerning the Source of Funds" has the higher quatity.
        - When observing the distribution of filings per state and territory, New York (903,948), and California (1,463,306) have the highest quantity of SAR filings.      
        
    """)
    #insert Suspicious activity report analysis
    tableau_Col0,tableau_Col1=st.columns(2)
    with tableau_Col0:
        #st.info("description for the below visualization")
        SAR_Tableau_Dashboard="""
        <div class='tableauPlaceholder' id='viz1675876394378' style='position: relative'>
        <noscript>
        <a href='#'>
        <img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' />
        </a>
        </noscript>
        <object class='tableauViz'  style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
        <param name='embed_code_version' value='3' /> <param name='site_root' value='' />
        <param name='name' value='FinancialCrimes_Dashboard&#47;Dashboard1' />
        <param name='tabs' value='no' /><param name='toolbar' value='yes' />
        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard1&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        </object>
        </div>                
        <script type='text/javascript'>                    
        var divElement = document.getElementById('viz1675876394378');
        var vizElement = divElement.getElementsByTagName('object')[0];
            if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
             else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} 
             else { vizElement.style.width='100%';vizElement.style.height='1477px';}                     
             var scriptElement = document.createElement('script');                    
             scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
             vizElement.parentNode.insertBefore(scriptElement, vizElement);                
        </script>
        """
        components.html(SAR_Tableau_Dashboard, width=9000, height=799,scrolling=False)
    #insert second tableau visual
    with tableau_Col1:
        #st.info("description for the below visualization")
        SAR_ByStateFiling_Dash="""
        <div class='tableauPlaceholder' id='viz1675874378527' style='position: relative'>
        <noscript>
        <a href='#'>
        <img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard2&#47;1_rss.png' style='border: none' />
        </a>
        </noscript><object class='tableauViz'  style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
        <param name='embed_code_version' value='3' /> <param name='site_root' value='' />
        <param name='name' value='FinancialCrimes_Dashboard&#47;Dashboard2' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard2&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        <param name='filter' value='publish=yes' />
        </object>
        </div>                
        <script type='text/javascript'>                    
        var divElement = document.getElementById('viz1675874378527');                    
        var vizElement = divElement.getElementsByTagName('object')[0];                    
            if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
             else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
              else { vizElement.style.width='100%';vizElement.style.height='727px';}                     
              var scriptElement = document.createElement('script');                    
              scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
              vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        """
        components.html(SAR_ByStateFiling_Dash, width=9000, height=799,scrolling=False)

    #insert figure references button
    TableauDash_button=st.expander(label="Figure 2.0 references : Financial Crime Enforcement Network ")
    TableauDash_button.write("""
    Datasource: FinCEN
    
    Technologies: Excel, Tableau, PyCharm, Python; plotly express, pandas, streamlit""")

    #insert title and body of suspicious activity report
    st.info("""
    - SAR: Filings of Securities and Futures Industry
        - 
        - Within the Securities and Futures industry the top type of suspicious activity filing is "ACH". 
        - The overall filing value for ACH is 60,942, making up 8.92% of the overall distribution.
        - "Identity theft" is the second biggest type of suspicious activity within the securities and futures industry.
        - The overall filings for Identity theft is 54,968, making up 8.04% of the total distribution.
        - "Wire" fraud is responsible for 52,968 suspicious activity filings in the securities and futures industry. It is 7.72% of the total distribution.       
    """)
    Securities_Futures_DF=pd.read_csv("SAR_Securities_Futures_Industry.csv")
    Securities_Futures_DF=Securities_Futures_DF.drop(Securities_Futures_DF.index[-1])
    #st.dataframe(Securities_Futures_DF)

    SecuritiesFutures_Type_DF=pd.read_csv("SAR_SecuritiesFutures_Type.csv")
    #SecuritiesFutures_Type_DF=SecuritiesFutures_Type_DF.drop(Securities_Futures_DF.index[-1])
    st.dataframe(SecuritiesFutures_Type_DF)

    SecuritiesFutures_Type_fig=px.bar(SecuritiesFutures_Type_DF,
                                      x="Suspicious Activity Type",
                                      y="Filings (Overall)",
                                      title="Number of Filings by Type of Suspicious Activity from Securities/Futures Industry:January 1, 2014 - December 31, 2021")
    SecuritiesFutures_Type_fig.update_layout(legend_title="Features",width=1550,height=1050, plot_bgcolor='rgba(0,0,0,0)')
    SecuritiesFutures_Type_fig.update_xaxes(showgrid=False, title="Types of Securities/Futures")
    SecuritiesFutures_Type_fig.update_yaxes(showgrid=False, title="Overall Filings")
    st.plotly_chart(SecuritiesFutures_Type_fig)

    #insert figure references button
    Ploty_button=st.expander(label="Figure 3.0 references : Financial Crime Enforcement Network ")
    Ploty_button.write("""
    Datasource: FinCEN
    
    Technologies: Excel, Tableau, PyCharm, Python; plotly express, pandas, streamlit""")

    st.write("---")

    REFERENCES=st.expander(label="References")
    REFERENCES.write("""
    Data Source: Financial Crimes Enforcement Network (FinCEN)
    
    https://www.zippia.com/advice/financial-services-industry-statistics/#:~:text=Global%20Financial%20Services%20Industry%20Statistics&text=This%20data%20was%20published%20at,by%20the%20end%20of%202021.
    
    https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/a-best-practice-model-for-bank-compliance
    
    https://www.investopedia.com/terms/a/anti-boycott-regulations.asp#:~:text=Anti%2Dboycott%20regulations%20have%20provisions,about%20boycotted%20countries%20and%20firms.
    
    https://www.bis.doc.gov/index.php/enforcement/oac#:~:text=The%20antiboycott%20provisions%20of%20the%20EAR%20require%20U.S.%20persons%20to,their%20receipt%20of%20boycott%20requests.
    
    https://www.fincen.gov/history-anti-money-laundering-laws
    
    https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/types-contributions/
    
    https://en.wikipedia.org/wiki/List_of_financial_regulatory_authorities_by_country
    
    https://www.bankingsupervision.europa.eu/press/publications/newsletter/2020/html/ssm.nl200212_1.en.html#:~:text=Compliance%20functions%20are%20a%20key,laws%2C%20regulations%20and%20internal%20policies.
    
    """)
########################################################################################################################
########################################################################################################################
########################################################################################################################


if Nav_Menu == "Capital Markets Analysis":
    #____________________________________Title and author________________________________

    st.markdown("<h1 style='text-align: center; color: white;'>""Capital Markets: Equity and Bond Securities""</h1>", unsafe_allow_html=True)
    #Name on document
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Guy Gnakpa""</h1>", unsafe_allow_html=True)
    #Date of on documents
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" January, 2023""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>" "</h1>", unsafe_allow_html=True)

    #____________________________________Introduction of Capital Markets____________________________________________________
    #what is capital markets and its sub-categories
    st.header("Introduction")
    st.write("<div style='text-align:justify'> ""\n"
             "Capital markets play a vidal part in the US and global economy. These markets facilitate the free flow of capital in efforts "
             "to allocate funds towards the best ideas and companies. This financial system allows corporations, governments, and individual "
             "investors to raise capital by issuing and selling securities such as stocks(equity) and bonds(debt). All US participants benefit from healthy "
             "capital markets as funds can be utilized to grow businesses, improve technology, finance property investments, and fund infrastructure objectives. "
             "Many of these efforts lead to growth in the market place and influence the creation of jobs while improving national gross domestic product(GDP). "
             "Some fundamental economic functions of capital markets include: "
             ,unsafe_allow_html=True)
    st.info("""
    * Creates a link between investors and savers
    * Creates efficient capital utilization
    * Provides solution for trading securities
    * Provides a hedging(derivatives) solution against market risks
    * Improves the effectiveness of capital allocation thus impacting notional GDP
    """)

    # intro and functions of primary and secondary capital markets
    st.header("Sub-categories")
    st.subheader("Primary Market:")
    st.write("<div style='text-align:justify'> ""\n"
             "The primary market is where securities are issued and sold to the public for the first time, such as an initial "
             "public offering (IPO) of a company's stock. The primary market is where companies and governments raise long-term capital. "
             "Main functions of the primary market include:"
             ,unsafe_allow_html=True)
    st.info("""
    * Origination: focuses on the examination, evaluation and process of new proposals in the primary market.
    * Underwriting: investment banks determine the risk and price of particular soon to be issued securities.
    * Distribution: refers to brokers and dealers who have the ability to dispense new issued securities to institution and retail investors.
    """)
    st.subheader("""Secondary Market:""")
    st.write("<div style='text-align:justify'> ""\n"
             "The secondary market is where securities that have already been issued are bought and sold among investors. "
             "I.e the stock market, where investors can buy and sell stocks of publicly traded companies. The secondary market allows "
             "securities to be traded providing more leverage and liquidity for investors. "
             "Main functions of the secondary market include: "
             ,unsafe_allow_html=True)
    st.info("""
    * Advise the value of securities
    * Offers liquidity to investors for their respective assets
    * Provides a marketplace for financial instruments to be traded.
    """)
    #description of financial instruments in capital markets
    st.subheader("""Financial Instruments in Capital Markets:""")
    st.info("""
    * Equities(stocks): Investment share in a company's total capitalisation; making one a shareholder
    * Debt Securities(bonds): Financial assets that enables a stream of interest payments
    * Derivatives(futures): Financial instruments who's value are pegged to an underlying asset; i.e, commodities futures, credit default swaps
    * Exchange Traded Funds(ETFs-SPY): An instrument that replicated the performance of an underlying index. Funds that are traded on an exchange tracking stocks, bonds etc..
    * Foreign Exchange Instruments(FX-USD/EUR): These instruments consist of currencies and derivatives. Mainly currencies that are purchased and sold globally 
      based on their respective exchange rate. 
    """)
    st.write("___")
    st.info("""
    There are many factors that can effect capital markets when analysing performance, expected return and risk exposure.
    Gross Domestic Product(GDP) is an economic indicator to measure a nation's total productivity level through its products and services.
    Federal Fund Rate is one of the most important indicator as it determined the cost of capital for central banks to borrow.
    The cost of capital has a ripple effect throughout the rest of the market participants. The 30-year fixed mortgage is a significant indicator as
    it correlates with nominal GDP. The housing markets makes up 15-18% of the U.S. GDP. Further, a large volume of fixed-income mortgage securities 
    and respective derivatives are traded in capital markets. Lastly, the rate of unemployment determined the state of economic 
    conditions, potential exposure to risk for fixed-income and debt issuers. 
    
    Below, there is an interactive dashboard of economic factors that effect the strength of capital markets. In addition,
    the dashboard provides Time-Series analysis of equity indices and examples of tech stocks. Bonds make up a large portion 
    of capital markets. With that in mind, the dashboard also illustrates the market capitalization of some of largest Bond ETFs. 
    """)

    st.write("___")
    ########################################################################################################################
    #----------------------------Crearte Data Visualisation----------------------------
    #Import csv and excel files/prep dataframe
    #insert qrtly us gdp
    qrtly_us_GDP=pd.read_csv("QRLY_US_GDP.csv")
    #st.dataframe(qrtly_us_GDP)
    qrtly_us_GDP_fig=px.bar(qrtly_us_GDP, x="DATE", y=["GDP"], title="Gross Domestic Product(GDP): 1947 - 2022 | Billions of Dollars | Quarterly")
    qrtly_us_GDP_fig.update_layout(legend_title="Features",width=1300,height=450,title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
    qrtly_us_GDP_fig.update_xaxes(showgrid=False, title="Date")
    qrtly_us_GDP_fig.update_yaxes(showgrid=False, title="Billions of Dollars")
    st.plotly_chart(qrtly_us_GDP_fig)

    ColA,ColB=st.columns(2)
    with ColA:
        #column1
        #insert us funds rate
        US_FundsRate=pd.read_csv("FEDFUNDS.csv")
        #st.dataframe(US_FundsRate)
        US_FundsRate_fig=px.line(US_FundsRate, x="DATE", y=["FEDFUNDS"], title="Federal Funds Effective Rate(FEDFUNDS): 1954 - 2022 | Percent | Monthly")
        US_FundsRate_fig.update_layout(legend_title="Features",width=1100,height=450,title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
        US_FundsRate_fig.update_xaxes(showgrid=False, title="Date")
        US_FundsRate_fig.update_yaxes(showgrid=False, title="Percent")
        st.plotly_chart(US_FundsRate_fig)
    with ColB:
        #insert us 30-year-mortgage
        US_30yr_Mortgage=pd.read_csv("30yrs_US_Mortgage.csv")
        #st.dataframe(US_FundsRate)
        US_30yr_Mortgage_fig=px.line(US_30yr_Mortgage, x="DATE", y=["MORTGAGE_30YR_US"], title="US 30-Year Fixed Rate Mortgage Avg : 1971 - 2023 | Percent | Weekly")
        US_30yr_Mortgage_fig.update_layout(legend_title="Features",width=1100,height=450,title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
        US_30yr_Mortgage_fig.update_xaxes(showgrid=False, title="Date")
        US_30yr_Mortgage_fig.update_yaxes(showgrid=False, title="Percent")
        st.plotly_chart(US_30yr_Mortgage_fig)

    #insert table for Unemployment rate
    st.info("----------------------------------------------------------------------------------------------------------Unemployment Rate: 2012 - 2022---------------------------------------------------------------------------------------------------")
    UnemploymentRate=pd.read_csv("UnemploymentRate.csv")
    st.table(UnemploymentRate)

    st.write("___")
    ########################################################################################################################
    #----------------------------GSPC----------------------------
    #create a variable storing the strings of specific indicies
    #define a function:doownload all indicies of a specific timeframe/return the value
    Index_GSPC=["^GSPC"] #,"^IXIC","^DJI"
    @st.cache
    def GSPC_mining(Index_GSPC):
        IndexGSPC_data=yf.download(Index_GSPC, start ="1990-01-01", end = None)
        IndexGSPC_data.reset_index(inplace=True)
        IndexGSPC_data.rename(columns={"index": "Date"})
        IndexGSPC_data["Date"]=pd.to_datetime(IndexGSPC_data["Date"], unit="s").dt.date
        return IndexGSPC_data
    #using streamlit call and print the function/using plotly, plot line chart incling paremeters
    IndexGSPC_data0=GSPC_mining(Index_GSPC)
    def GSPC_chart(IndexGSPC_data0):
        fig_GSPC=px.line(IndexGSPC_data0, x="Date", y=["Adj Close","Open","Close","High","Low"], title="S&P500 Index: 1990 - Present | Thousands of Dollars | Yearly")
        fig_GSPC.update_layout(legend_title="Features",width=1300,height=450,title_x=0.5, title_y=.85,plot_bgcolor='rgba(0,0,0,0)')
        fig_GSPC.update_xaxes(showgrid=False, title="Date")
        fig_GSPC.update_yaxes(showgrid=True, title="Thousands of Dollars")
        return fig_GSPC
        #----------------------------IXIC----------------------------
    #define a function:doownload all indicies of a specific timeframe/return the value
    Index_IXIC=["^IXIC"]
    @st.cache
    def IXIC_mining(Index_IXIC):
        IndexIXIC_data=yf.download(Index_IXIC,start = "1990-01-01",end = None)
        IndexIXIC_data.reset_index(inplace=True)
        IndexIXIC_data.rename(columns={"index":"Date"})
        IndexIXIC_data["Date"]=pd.to_datetime(IndexIXIC_data["Date"], unit="s").dt.date
        return IndexIXIC_data
    #using streamlit call and print the function/using plotly, plot line chart incling paremeters
    IndexIXIC_data0=IXIC_mining(Index_IXIC)
    def IXIC_chart(IndexIXIC_data0):
        fig_IXIC=px.line(IndexIXIC_data0, x="Date", y=["Adj Close","Open","Close","High","Low"], title="Nasdaq Index: 1990 - Present | Thousands of Dollars | Yearly")
        fig_IXIC.update_layout(legend_title="Features", width=1300,height=450,title_x=0.5, title_y=.85,plot_bgcolor='rgba(0,0,0,0)')
        fig_IXIC.update_xaxes(showgrid=False, title="Date")
        fig_IXIC.update_yaxes(showgrid=True, title="Thousands of Dollars")
        return fig_IXIC
        #----------------------------DJI----------------------------
    #define a function:doownload all indicies of a specific timeframe/return the value
    Index_DJI=["^DJI"]
    @st.cache
    def DJI_mining(Index_DJI):
        IndexDJI_data=yf.download(Index_DJI,start = "1990-01-01",end = None)
        IndexDJI_data.reset_index(inplace=True)
        IndexDJI_data.rename(columns={"index":"Date"})
        IndexDJI_data["Date"]=pd.to_datetime(IndexDJI_data["Date"], unit="s").dt.date
        return IndexDJI_data
    #using streamlit call and print the function/using plotly, plot line chart incling paremeters
    IndexDJI_data0=DJI_mining(Index_DJI)
    def DJI_chart(IndexDJI_data0):
        fig_DJI=px.line(IndexDJI_data0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"], title="Dow Jones Index: 1990 - Present | Thousands of Dollars | Yearly")
        fig_DJI.update_layout(legend_title="Features",width=1300, height=450, title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
        fig_DJI.update_xaxes(showgrid=False, title="Date")
        fig_DJI.update_yaxes(showgrid=True, title="Thousands of Dollars")

        return fig_DJI
    #--------------------------------------------------------Create Top stocks chart----------------------------------------
    #----using yfinance mine the datas for the following tickers["AAPL","MSFT","GOOGL","AMZN","META","TSLA"]-----
    AAPL_Stock=["AAPL"]
    @st.cache
    def AAPL_mining(AAPL_Stock):
        Stock_AAPL_data=yf.download(AAPL_Stock, start ="2005-01-01", end = None)
        Stock_AAPL_data.reset_index(inplace=True)
        Stock_AAPL_data.rename(columns={"index": "Date"})
        Stock_AAPL_data["Date"]=pd.to_datetime(Stock_AAPL_data["Date"], unit="s").dt.date
        return Stock_AAPL_data
    #using streamlit call and print the function/using plotly, plot line chart incling paremeters
    Stock_AAPL_Stock0= AAPL_mining(AAPL_Stock)
    def AAPL_chart(Stock_AAPL_Stock0):
        fig_AAPL=px.line(Stock_AAPL_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"], title="Apple: 2005 - Present")
        fig_AAPL.update_layout(legend_title="Features",
                               width=1300, height=450,
                               title_x=0.5, title_y=.85,
                               plot_bgcolor='rgba(0,0,0,0)')
        return fig_AAPL
    #Stock_AAPL_Stock0=AAPL_chart(Stock_AAPL_Stock0)
    #------------------------------------Mining data for stock:MICROSOFT------------------------------------------
    #using yfinance mine the datas for the following tickers["AAPL","MSFT","GOOGL","AMZN","META","TSLA"]
    MSFT_Stock=["MSFT"]
    @st.cache
    def MSFT_mining(MSFT_Stock):
        Stock_MSFT_data=yf.download(MSFT_Stock, start ="2005-01-01", end = None)
        Stock_MSFT_data.reset_index(inplace=True)
        Stock_MSFT_data.rename(columns={"index": "Date"})
        Stock_MSFT_data["Date"]=pd.to_datetime(Stock_MSFT_data["Date"], unit="s").dt.date
        return Stock_MSFT_data
    #using streamlit call and print the function/using plotly, plot line chart incling paremeters
    Stock_MSFT_Stock0= MSFT_mining(MSFT_Stock)
    def MSFT_chart(Stock_MSFT_Stock0):
        fig_MSFT=px.line(Stock_MSFT_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"], title="Microsoft: 2005 - Present")
        fig_MSFT.update_layout(legend_title="Features",
                               width=1300, height=450,
                               title_x=0.5, title_y=.85,
                               plot_bgcolor='rgba(0,0,0,0)')
        return fig_MSFT
    #Stock_MSFT_Stock0=MSFT_chart(Stock_MSFT_Stock0)
    #------------------------------------Mining data for stock:GOOGLE------------------------------------------
    #using yfinance mine the datas for the following tickers["AAPL","MSFT","GOOGL","AMZN","META","TSLA"]
    GOOGL_Stock=["GOOGL"]
    @st.cache
    def GOOGL_mining(GOOGL_Stock):
        Stock_GOOGL_data=yf.download(GOOGL_Stock, start ="2005-01-01", end = None)
        Stock_GOOGL_data.reset_index(inplace=True)
        Stock_GOOGL_data.rename(columns={"index": "Date"})
        Stock_GOOGL_data["Date"]=pd.to_datetime(Stock_GOOGL_data["Date"], unit="s").dt.date
        return Stock_GOOGL_data
    #using streamlit call and print the function/using plotly, plot line chart incling paremeters
    Stock_GOOGL_Stock0=GOOGL_mining(GOOGL_Stock)
    def GOOGL_chart(Stock_GOOGL_Stock0):
        fig_GOOGL=px.line(Stock_GOOGL_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"], title="Google: 2005 - Present")
        fig_GOOGL.update_layout(legend_title="Features",
                                width=1300, height=450,
                                title_x=0.5, title_y=.85,
                                plot_bgcolor='rgba(0,0,0,0)')
        return fig_GOOGL
    #st.plotly_chart(GOOGL_chart(Stock_GOOGL_Stock0))
    #Stock_GOOGL_Stock0=GOOGL_chart(Stock_GOOGL_Stock0)
    #------------------------------------Mining data for stock:AMAZON------------------------------------------
    AMZN_Stock=["AMZN"]
    @st.cache
    def AMZN_mining(AMZN_Stock):
        Stock_AMZN_data=yf.download(AMZN_Stock, start ="2005-01-01", end = None)
        Stock_AMZN_data.reset_index(inplace=True)
        Stock_AMZN_data.rename(columns={"index": "Date"})
        Stock_AMZN_data["Date"]=pd.to_datetime(Stock_AMZN_data["Date"], unit="s").dt.date
        return Stock_AMZN_data
    #using streamlit call and print the function/using plotly, plot line chart incling paremeters
    Stock_AMZN_Stock0= AMZN_mining(AMZN_Stock)
    def AMZN_chart(Stock_AMZN_Stock0):
        fig_AMZN=px.line(Stock_AMZN_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"], title="Amazon: 2005 - Present")
        fig_AMZN.update_layout(legend_title="Features",
                               width=1300, height=450,
                               title_x=0.5, title_y=.85,
                               plot_bgcolor='rgba(0,0,0,0)')
        return fig_AMZN
    #Stock_AMZN_Stock0=AMZN_chart(Stock_AMZN_Stock0)
    #------------------------------------Mining data for stock:META------------------------------------------
    META_Stock=["META"]
    @st.cache
    def META_mining(META_Stock):
        Stock_META_data=yf.download(META_Stock, start ="2005-01-01", end = None)
        Stock_META_data.reset_index(inplace=True)
        Stock_META_data.rename(columns={"index": "Date"})
        Stock_META_data["Date"]=pd.to_datetime(Stock_META_data["Date"], unit="s").dt.date
        return Stock_META_data
    #using streamlit call and print the function/using plotly, plot line chart incling paremeters
    Stock_META_Stock0= META_mining(META_Stock)
    def META_chart(Stock_META_Stock0):
        fig_META=px.line(Stock_META_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"], title="Meta: 2005 - Present")
        fig_META.update_layout(legend_title="Features",
                               width=1300, height=450,
                               title_x=0.5, title_y=.85,
                               plot_bgcolor='rgba(0,0,0,0)')
        return fig_META
    #Stock_META_Stock0=META_chart(Stock_META_Stock0)
    #------------------------------------Mining data for stock:TSLA------------------------------------------
    TSLA_Stock=["TSLA"]
    @st.cache
    def TSLA_mining(TSLA_Stock):
        Stock_TSLA_data=yf.download(TSLA_Stock, start ="2005-01-01", end = None)
        Stock_TSLA_data.reset_index(inplace=True)
        Stock_TSLA_data.rename(columns={"index": "Date"})
        Stock_TSLA_data["Date"]=pd.to_datetime(Stock_TSLA_data["Date"], unit="s").dt.date
        return Stock_TSLA_data
    #using streamlit call and print the function/using plotly, plot line chart incling paremeters
    Stock_TSLA_Stock0=TSLA_mining(TSLA_Stock)
    def TSLA_chart(Stock_TSLA_Stock0):
        fig_TSLA=px.line(Stock_TSLA_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"], title="Tesla: 2005 - Present")
        fig_TSLA.update_layout(legend_title="Features",
                               width=1300, height=450,
                               title_x=0.5, title_y=.85,
                               plot_bgcolor='rgba(0,0,0,0)')
        return fig_TSLA
    #Stock_TSLA_Stock0=TSLA_chart(Stock_TSLA_Stock0)

    #----------------------------------Create Drop down Buttons for indecies/Index Analysis--------------------------------------------------
    #using streamlit module/def function create botton for each index
    index_category=["Dow Jones","S&P500","Nasdaq"]
    test0=st.multiselect("Equity Market: select 👇 for Time-series index analysis",index_category)
    #insert Dow Jones option
    if "Dow Jones" in test0:
        #prep dataframes for metrics
        DowCol_PreviousClosePrice,DowCol_OpenPrice,DowCol_Volume,DowCol_MrkCap=st.columns(4)
        PreviousDow_price=IndexDJI_data0["Adj Close"].tail(1)
        PreviousDow_price0=PreviousDow_price
        PreviousDow_price=babel.numbers.format_currency(float(PreviousDow_price),"USD",locale='en_US')
        OpenDow_price=IndexDJI_data0["Open"].tail(1)
        OpenDow_price0=OpenDow_price
        OpenDow_price=babel.numbers.format_currency(float(OpenDow_price),"USD",locale='en_US')
        VolumeDow=IndexDJI_data0["Volume"].tail(1)
        VolumeDow=babel.numbers.format_currency(float(VolumeDow),"USD",locale='en_US')
        DowMarketcap="$9.67T"

        #PerChngDow=(((PreviousDow_price0-OpenDow_price0)/PreviousDow_price0)*100)->format error

        #Output Metrics
        DowCol_PreviousClosePrice.metric("Previous Close:", PreviousDow_price)
        DowCol_OpenPrice.metric("Open Price:", OpenDow_price)
        DowCol_Volume.metric("Trading Volume:",VolumeDow)
        DowCol_MrkCap.metric("MarketCap as of 2022-31-12",DowMarketcap)
        #DowCol_PerChng.metric(label="∆ in Daily Price(%)",value=PerChngDow)->format error

        #print line chart/analysis
        st.plotly_chart(DJI_chart(IndexDJI_data0))

        st.write("Dow Jones Analysis:")
        #insert dow jones yearyly return
        Dow_Return=pd.read_csv("DowJones_YearlyReturn.csv")
        Dow_Return_fig=px.bar(Dow_Return, x="Year", y="Total Return", color="Total Return", title="Dow Jones Yearly Return : 1893 - 2023 | Percent | Yearly")
        Dow_Return_fig.update_layout(legend_title="Features",width=1250,height=450,title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
        Dow_Return_fig.update_xaxes(showgrid=False, title="Date")
        Dow_Return_fig.update_yaxes(showgrid=False, title="Percent")
        #insert dropdown for data table and stats
        Dow_dropdown_stats=st.expander(label="Dow Jones: Yearly Return and Index Statistics")
        Dow_dropdown_stats.plotly_chart(Dow_Return_fig)
        Dow_dropdown_stats.table(IndexDJI_data0.describe())

        #insert analysis description
        st.info("""
        The Dow Jones Industrial Average, also known as the Dow 30 is the second-oldest equity index in the U.S. The Dow constitutes of 30 
        public blue-chip companies traded on the New York Stock Exchange and the Nasdaq. The index was launched 
        in 1896 by Charles Dow and Edward Jones. The index is well known throughout the world and is utilized by 
        many investors to measure economic performance. The index includes a variety of top companies in numerous industries. 
        Some of the companies include: 
        * American Express 
        * Boeing
        * Cisco Systems
        * Goldman Sachs
        * Johnson & Johnson
        The chart above indicates the Dow Jones has been positively performing since its inception in capital markets.
        The lowest adjusted closing value of the index is 3,136.60 dollars on September 10, 1992. The highest adjusted closing 
        value of the index is 36,799.64 dollars on April 1, 1992. On average the index has an adjusted closing value of 13,644.91 dollars
        based on the available data. It is also important to note 75% of the adjusted closing values from 1992 to present are
        17,388.03 dollars or bellow. This metrics indicates the index has experienced a significant positive moving average since its lowest 
        adjusted value of 3,136.60 dollars in 1992. More specifically, the first dramatic pull-back of the index begin on October 9, 2007 with an 
        adjusted closing value of 14,164.53 dollars and continued until March 9, 2009 with an adjusted closing value of 6,547.05 dollars. From October 9, 2007 
        to March 9 2009, the index experienced a 53.77% retracement. On October 9, 2007, the equity markets, including Dow Jones rallied due to a Fed meeting 
        supporting interest rate cut by the end of the year. This bullish sentiment was short lived according to the data in the chart above. The overrall market conditions 
        during this time period were not favorable for institutions and retail investors. The Great Recession devalued capital markets during this time.
        In those three years, the average 30-years fixed-mortgage rate was approximately 5.80% with 2007 being the highest (6.34%). According to 
        Federal Reserve History, "the value of homes fell by approximately 30% on average from 2006 through mid-2009." Real GDP declined by 4.3% from its peak in 2007 to 
        2009. Lastly unemployment rose from 5% in december 2007 to 10% by October 2009. The Great Recession which started in late 2006, was the biggest influence for the 
        the Dow Jones's contraction from October 9, 2007 to March 9, 2009.
        """)
        #calculation for analysis above/stats
        current=6547.05
        previous=14164.53
        percent_change=float(current-previous)/abs(previous)*100
        #st.write(percent_change)
        Avg_30_fixed=(6.34+6.03+5.04)/3
        #st.write(Avg_30_fixed)

        #insert figure button
        DowJones_button=st.expander(label="Figure 1 : Dow Jones Index Time-series Analysis ")
        DowJones_button.write("""
        Datasource: Yahoo Finance
        Technologies: PyCharm, Python; plotly express, pandas, streamlit""")
    st.write("---")
    #insert S&P500 option
    if "S&P500" in test0:
        #create 4 columns
        SPCol_PreviousClosePrice,SPCol_OpenPrice,SPCol_Volume,SPCol_Mrkcap=st.columns(4)
        #prep dataframes for metrics
        PreviousSP_price=IndexGSPC_data0["Close"].tail(1)
        PreviousSP_price0=PreviousSP_price
        PreviousSP_price=babel.numbers.format_currency(float(PreviousSP_price),"USD",locale='en_US')
        OpenSP_price=IndexGSPC_data0["Open"].tail(1)
        OpenSP_price0=OpenSP_price
        OpenSP_price=babel.numbers.format_currency(float(OpenSP_price),"USD",locale='en_US')
        VolumeSP=IndexGSPC_data0["Volume"].tail(1)
        VolumeSP=babel.numbers.format_currency(float(VolumeSP),"USD",locale='en_US')
        SPmarketcap="$33.581T"
        #PerChngDow=(((PreviousDow_price0-OpenDow_price0)/PreviousDow_price0)*100)->format error

        #Output Metrics
        SPCol_PreviousClosePrice.metric("Previous Close:", PreviousSP_price)
        SPCol_OpenPrice.metric("Open Price:", OpenSP_price)
        SPCol_Volume.metric("Trading Volume:",VolumeSP)
        SPCol_Mrkcap.metric("MarketCap as of 2023-01-26:",SPmarketcap)
        #DowCol_PerChng.metric(label="∆ in Daily Price(%)",value=PerChngDow)->format error

        #print line chart/analysis
        st.plotly_chart(GSPC_chart(IndexGSPC_data0))
        #insert title
        st.write("S&P 500 Analysis:")
        #insert dow S&P 500 return
        SP500_Return=pd.read_csv("S&P500_YearlyReturn.csv")
        SP500_Return_fig=px.bar(SP500_Return, x="Year", y="Total Return", color="Total Return", title="S&P 500 Yearly Return : 1927 - 2023 | Percent | Yearly")
        SP500_Return_fig.update_layout(legend_title="Features",width=1250,height=450,title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
        SP500_Return_fig.update_xaxes(showgrid=False, title="Date")
        SP500_Return_fig.update_yaxes(showgrid=False, title="Percent")

        #insert dropdown for data table and stats
        SP500_dropdown_stats=st.expander(label="S&P 500: Yearly Return and Index Statistics")
        SP500_dropdown_stats.plotly_chart(SP500_Return_fig)
        SP500_dropdown_stats.table(IndexGSPC_data0.describe())
        #insert analysis description
        st.info("""
        The Standard and Poor's 500 also known as the S&P 500, is one of the most commonly followed equity indices.
        The S&P 500 is a market-capitalization-weighted index constituted of 500 large companies traded on the American stock exchanges.
        Originally the S&P 500 was The Composite Index 90; representing 90 leading companies in the United States. Later in 1957,
        the index grew to 500 companies. The market capitalization of the index is 33.587 trillion dollars as of 2023. Similar to 
        the Dow Jones, the value of the S&P 500 performance is one of the tools used to gauge U.S. economic conditions and performance. There are many requirements 
        to inter the index; including a market capitalization of 14.6 billion dollars and specified liquidity-based size. Some of the companies include:
        * Warner Bros. Discovery Inc. Series A
        * Carnival Corporation
        * NVIDIA Corporation 
        * United Airlines Holdings Inc.
        * Netflix   
        The chart above showcases the performance of the S&P 500 Index from 1990 to the present time. Similar to the Dow Jones, 
        the S&P 500 has been positively performing since 1957. The lowest adjusted closing value of the index is 295.46 dollars
        on October 11, 1990. The highest adjusted closing value of the index is 4,796.56 dollars on January 3rd, 2022. On average the 
        index has an adjusted closing value of 1,507.09 based on the extracted from yahoo finance. 75% of the adjusted closing prices from 
        1990 to year to day have a value of 1,957.16 dollars or lower. This metrics indicates the index has experienced a significant positive 
        moving average since its lowest adjusted value of 295.46 dollars on October 11, 1990. The line chart displays the most significant devaluation
        of the index from February 19, 2020 with an adjusted closing value of 3,386.15 dollars, to March 23, 2020 with an adjusted closing value of 2,237.40 dollars.
        From February 19, 2020 to March 23, 2020, the index experienced a 33.92% retracement. This significant dilution of the equity index
        was provoked by the Corona Virus crisis of 2019. Capital markets experienced a remarkable liquidity crunch due to lower gross domestic product(GDP) output. 
        The U.S. GDP dropped from 21.92 trillion dollars on February 29, 2020 to 20.74 trillion dollars on March 31st, 2020 and continued to plummet for a few more months.
        GDP fell by 5.33% while unemployment rose from 3.5% in February 2020 to 14.70% by April 2020. This had a significant impact on market conditions and economic output in the 
        United States. The implementation of monetary policy and quantitative easing was imperative for the recovery of capital markets during this health crisis. COVID19 was responsible 
        for the S&P 500's decline from February 19, 2020 to March 23, 2020.             
        """)
        #calculate % change during covid retracement
        current1=2237.40
        previous1=3386.15
        percent_change1=float(current1-previous1)/abs(previous1)*100
        #st.write(percent_change1)

        #insert figure references button
        SP500_button=st.expander(label="Figure 2.0 references : S&P500 Index Time-series Analysis ")
        SP500_button.write("""
        Datasource: Yahoo Finance
        Technologies: PyCharm, Python; plotly express, pandas, streamlit""")

    #insert NAsdaq option
    if "Nasdaq" in test0:
        #create 4 columns
        NasdaqCol_PreviousClosePrice,NasdaqCol_OpenPrice,NasdaqCol_Volume,NasdaqCol_Mrkcap=st.columns(4)
        #prep dataframes for metrics
        PreviousNasdaq_price=IndexIXIC_data0["Close"].tail(1)
        PreviousNasdaq_price0=PreviousNasdaq_price
        PreviousNasdaq_price=babel.numbers.format_currency(float(PreviousNasdaq_price),"USD",locale='en_US')
        OpenNasdaq_price=IndexIXIC_data0["Open"].tail(1)
        OpenNasdaq_price0=OpenNasdaq_price
        OpenNasdaq_price=babel.numbers.format_currency(float(OpenNasdaq_price),"USD",locale='en_US')
        VolumeNasdaq=IndexIXIC_data0["Volume"].tail(1)
        VolumeNasdaq=babel.numbers.format_currency(float(VolumeNasdaq),"USD",locale='en_US')
        Nasdaqmarketcap="$16.2T"
        #PerChngDow=(((PreviousDow_price0-OpenDow_price0)/PreviousDow_price0)*100)->format error

        #Output Metrics
        NasdaqCol_PreviousClosePrice.metric("Previous Close:", PreviousNasdaq_price)
        NasdaqCol_OpenPrice.metric("Open Price:", OpenNasdaq_price)
        NasdaqCol_Volume.metric("Trading Volume:",VolumeNasdaq)
        NasdaqCol_Mrkcap.metric("MarketCap as of 2022-01-26:",Nasdaqmarketcap)
        #DowCol_PerChng.metric(label="∆ in Daily Price(%)",value=PerChngDow)->format error
        #print line chart/analysis
        st.plotly_chart(IXIC_chart(IndexIXIC_data0))
        #insert title
        st.write("Nasdaq Analysis:")
        #insert dow S&P 500 return
        Nasda_Return=pd.read_csv("Nadsaq_YearlyReturn.csv")
        Nasda_Return_fig=px.bar(Nasda_Return, x="Year", y="Total Return", color="Total Return", title="Nasday Yearly Return : 1990 - 2023 | Percent | Yearly")
        Nasda_Return_fig.update_layout(legend_title="Features",width=1250,height=450,title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
        Nasda_Return_fig.update_xaxes(showgrid=False, title="Date")
        Nasda_Return_fig.update_yaxes(showgrid=False, title="Percent")


        #insert dropdown for data table and stats
        Nasdaq_dropdown_stats=st.expander(label="Nasdaq: Yearly Return and Index Statistics")
        Nasdaq_dropdown_stats.plotly_chart(Nasda_Return_fig)
        Nasdaq_dropdown_stats.table(IndexIXIC_data0.describe())
        st.info("""
        The Nasdaq Composite Index, also known as The Nasdaq includes 3,642 companies which are listed on the Nasdaq Stock market.
        The index was created in 1971 with a base value of 100. The do-com era boosted the index in terms of net return and increased its popularity.
        The Nasdaq composite tracks domestic and international companies making the index one of the most widely followed market indices.
        The index is heavily weighted towards information technology securities and has a market capitalization of 16.2 trillion dollars 
        as of December 2022. Some of the companies in the index include:
        * Apple
        * Microsoft
        * Amazon
        * Meta
        * Alphabet Class C (Google)
        * Tesla 
        The Chart above illustrates the performance of the Nasdaq Composite Index from 1990 to the present time. The index has 
        experienced a positive return since it's inception similar to the Dow Jones and the S&P 500. The lowest adjusted 
        closing value of the index is 325.40 dollars on October 16, 1990. The highest adjusted closing value of the index is 16,057.44
        dollars on November 19, 2021. The average adjusted closing value since its inception in the capital market is 3,565.03 dollars. 
        75% of the adjusted closing values from 1990 to year to day have a value of 4,564.75 dollars or lower. The Nasdaq has experienced
        several dramatic contraction periods influenced by market conditions of the the do-com bubble (1995-2021), 2008 financial crisis (2006-2009) and the COVID19 Pandemic (2019-2021).
        The effect of these events can be seen on the Time-series chart when zooming closing. During the do-com bubble, the index rallied
        from 1995 with a peak value of 5,048.62 dollars and fell to 1,114.11 dollars on October 9, 2022. Market conditions of the do-come bubble cause the 
        Nasdaq to fall by 77.93%. The next event which effected all capital markets world wide, especially the United States was the 2008 Financial 
        Crisis. The Nasdaq fell from a peak of 2,815.67 dollars on October 31, 2007 to 1,265.52 dollars on March 9, 2009 signifying a 55.05% capital loss of the index. 
        The Nasdaq soon recovered and experienced tremendous growth in price action and market capitalization. However, the COVID19 pandemic was another obstable 
        for capital markets and its respective participants. The Nasdaq Index fell dramatically from a value of 9,817.17 dollars on Feburary 
        19, 2020 to a value of 6,860.67 dollars on March 23, 2020. In 33 days the index fell by 33.11%, nearly one percent a day. Inflation rose 
        above 2% by the end of 2021. The labor market was unfavorable with the unemployment rate rising from 3.5% to 14.7%. The gross domestic product output 
        fell by 5.33% influencing capital loss and social challenges. In order to mitigate the economic downturn from worsening, the Federal Reserve employed monetary policies 
        to stimulate the economy. On March 2020, the federal funds rate decreased to a range of 0% - 0.25% enabling cheap capital and more spending. Interest rates remained 
        near 0 until unemployment rate was optimal for the economy. On March 15, 2020, The Fed announced the utilization of its QE tool to inject large some of liquity throught the purchased of 
        500 billion dollars in Treasury securities and 200 billion dollars in government-guaranteed mortgage-backed securities. The Fed's actions along with the containment of the health crisis 
        led to the recovery of Nasdaq Index and the rest of the equity market. From its last low value of 6,860.67 dollars on March 23, 2020, the index rallied to a peak of 16,057.44 dollars on November 19, 2021.
        The Nasdaq's increase of 134.05% towards value recovery after such economic downturn indicates large volume of Fed liquidity and investor confidence in the capital and equity markets.      
        """)
        #calculate % change during do-com bubble
        current2=1114.11
        previous2=5048.62
        percent_change2=float(current2-previous2)/abs(previous2)*100
        #st.write(percent_change2)
        #calculate % change during financial crisis
        current3=1265.52
        previous3=2815.67
        percent_change3=float(current3-previous3)/abs(previous3)*100
        #st.write(percent_change3)
        #calculate % change during COVID19 Pandemic
        current4=6860.67
        previous4=9817.17
        percent_change4=float(current4-previous4)/abs(previous4)*100
        #st.write(percent_change4)
        #calculate % change of rally after COVID19 Pandemic
        current5=16057.44
        previous5=6860.67
        percent_change5=float(current4-previous5)/abs(previous5)*100
        #st.write(percent_change4)

        #insert figure references button
        Nasdaq_button=st.expander(label="Figure 3.0 references : Nasdaq Index Time-series Analysis ")
        Nasdaq_button.write("""
        Datasource: Yahoo Finance
        Technologies: PyCharm, Python; plotly express, pandas, streamlit""")

    #--------------------------------Create Drop down Buttons for TopTechStock/Index Analysis--------------------------------------------------
    TopTechStock_Category=["Apple","Microsoft","Google","Amazon","Meta","Tesla"]
    test1=st.multiselect("Tech Stocks: Select 👇 for a comparison of Time-Series visualization",TopTechStock_Category)
    if "Apple" in test1:
        st.plotly_chart(AAPL_chart(Stock_AAPL_Stock0))
    if "Microsoft" in test1:
        st.plotly_chart(MSFT_chart(Stock_MSFT_Stock0))
    if "Google" in test1:
        st.plotly_chart(GOOGL_chart(Stock_GOOGL_Stock0))
    if "Amazon" in test1:
        st.plotly_chart(AMZN_chart(Stock_AMZN_Stock0))
    if "Meta" in test1:
        st.plotly_chart(META_chart(Stock_META_Stock0))
    if "Tesla" in test1:
        st.plotly_chart(TSLA_chart(Stock_TSLA_Stock0))

    st.write("---")
    #--------------------------------Create visualisation for Bond ETFs MrkCap-------------------------------
    #extract data and prep dataframe
    # Define the bond ticker symbol
    bond_etfs = ['AGG','HYG','LQD',"TLT","SHY","IEF"]
    market_cap=pdr.get_quote_yahoo(bond_etfs)["marketCap"]
    #st.dataframe(market_cap)
    #Create bar visualization from prepped dataframe
    Bond_MrkCap=pd.DataFrame(market_cap)
    Bond_MrkCap=Bond_MrkCap.sort_values(by="marketCap", ascending=False)
    Bond_MrkCap_fig=px.bar(Bond_MrkCap, x=Bond_MrkCap.index, y="marketCap", color=Bond_MrkCap.index, title=" Bond ETFs: Market Capitalization | ETFs")
    Bond_MrkCap_fig.update_layout(legend_title="Features",width=1350,height=450,title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
    Bond_MrkCap_fig.update_xaxes(showgrid=False, title="ETFs")
    Bond_MrkCap_fig.update_yaxes(showgrid=False, title="MarketCap")
    st.plotly_chart(Bond_MrkCap_fig)

    BOND_ETF_COLA,BOND_ETF_COLB=st.columns(2)
    with BOND_ETF_COLA:
        st.info("""
        ishares Core U.S. Aggregate Bond ETF(AGG)
        - Offers broad-based exposure to investment grade U.S. Bonds
        - Structured for long-term portfolio strategy
        - Includes hundreds of individual securities with the aim to mitigate illiquid challenges
        ishares iboxx $ Investment Grade Corporate Bond ETF(LQD)
        - Offers exposure to investment grade corporate bonds 
        - Structured for long-term portfolio strategy
        - Positive yield and low risk due to length of maturity
        ishares 1-3 Year Treasury Bond ETF(SHY)
        - Offers short-term maturity exposure 
        - Structured for low expected return
        - Offers exposure to securities 1-3 years to maturity
        """)
    with BOND_ETF_COLB:
        st.info("""
        ishares iboxx $ High Yield Corporate Bond ETF(HYG)
        - Offers exposure to U.S. dollar-denominated high yield liquid corporate bon market
        - High yield with high risk(higher potential for participants to default)
        - Majority of the securities are corporate bonds rated between B and BB
        ishares 7-10 Year Treasury Bond ETF(IEF)
        - Offers exposure to treasury bonds securities 7-10 years to maturity 
        - Offers higher return then short-term securities
        - Moderate levels of risk
        iShares 20+ Year Treasury Bond ETF(TLT)
        - Offers exposure to long-dated securities with low credit risk 
        - Offers higher liquidity exposure
        - Efficient and cost effective
        """)
    st.write("---")
    # #--------------------------------Create Drop down Buttons for TopTechStock/Index Analysis--------------------------------------------------
    # TopTechStock_Category=["Apple","Microsoft","Google","Amazon","Meta","Tesla"]
    # test1=st.multiselect("Tech Stocks: Select 👇 for a comparison of Time-Series visualization",TopTechStock_Category)
    # if "Apple" in test1:
    #     st.plotly_chart(AAPL_chart(Stock_AAPL_Stock0))
    # if "Microsoft" in test1:
    #     st.plotly_chart(MSFT_chart(Stock_MSFT_Stock0))
    # if "Google" in test1:
    #     st.plotly_chart(GOOGL_chart(Stock_GOOGL_Stock0))
    # if "Amazon" in test1:
    #     st.plotly_chart(AMZN_chart(Stock_AMZN_Stock0))
    # if "Meta" in test1:
    #     st.plotly_chart(META_chart(Stock_META_Stock0))
    # if "Tesla" in test1:
    #     st.plotly_chart(TSLA_chart(Stock_TSLA_Stock0))
    #insert figure button
    REFERENCES=st.expander(label="References")
    REFERENCES.write("""
        Datasource: Yahoo Finance, FRED
        
        Technologies: PyCharm, Python; plotly express, pandas, streamlit, Excel
        
        [https://data.oecd.org/unemp/unemployment-rate.htm](https://data.oecd.org/unemp/unemployment-rate.htm)
        
        [https://data.bls.gov/timeseries/LNS14000000](https://data.bls.gov/timeseries/LNS14000000)
        
        [https://ycharts.com/indicators/us_monthly_gdp](https://ycharts.com/indicators/us_monthly_gdp) 
        
        [https://www.macrotrends.net/2623/nasdaq-by-year-historical-annual-returns](https://www.macrotrends.net/2623/nasdaq-by-year-historical-annual-returns) 
        
        [https://www.slickcharts.com/dowjones/returns](https://www.slickcharts.com/dowjones/returns)
        
        [https://www.google.com/finance/quote/.INX:INDEXSP?hl=en](https://www.google.com/finance/quote/.INX:INDEXSP?hl=en)
        
        [https://www.federalreservehistory.org/essays/great-recession-of-200709#:~:text=The financial effects of the,its trough in March 2009](https://www.federalreservehistory.org/essays/great-recession-of-200709#:~:text=The%20financial%20effects%20of%20the,its%20trough%20in%20March%202009). 
        
        [https://fred.stlouisfed.org/series/MORTGAGE30US](https://fred.stlouisfed.org/series/MORTGAGE30US)
        
        [https://fred.stlouisfed.org/series/FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS)  
        
        [https://fred.stlouisfed.org/series/GDP](https://fred.stlouisfed.org/series/GDP)   
        
        [https://money.cnn.com/2007/10/09/markets/markets_0500/](https://money.cnn.com/2007/10/09/markets/markets_0500/)   
        
        [https://www.elearnmarkets.com/blog/5-instruments-of-capital-market/](https://www.elearnmarkets.com/blog/5-instruments-of-capital-market/)
        
        [https://en.wikipedia.org/wiki/Nasdaq#cite_note-2](https://en.wikipedia.org/wiki/Nasdaq#cite_note-2)    
        
        [https://focus.world-exchanges.org/issue/february-2023/market-statistics](https://focus.world-exchanges.org/issue/february-2023/market-statistics)  
        
        [https://indexes.nasdaqomx.com/Index/Overview/COMP](https://indexes.nasdaqomx.com/Index/Overview/COMP)  
        
        [https://indexes.nasdaqomx.com/Index/Weighting/COMP](https://indexes.nasdaqomx.com/Index/Weighting/COMP)   
        
        [https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average](https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average)  
        
        [https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/](https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/)
        
        [https://www.investopedia.com/terms/s/sp500.asp](https://www.investopedia.com/terms/s/sp500.asp)  
        
        [https://www.sifma.org/resources/research/fact-book/](https://www.sifma.org/resources/research/fact-book/)
            
        https://etfdb.com/etf/TLT/
        """)
    st.info("""
    DISCLAIMER: The production of this analysis is solely for educational purposes. The data used to explain certain events 
    is subject to change, and the analysis is not intended to be used as an investment tool. If this analysis is used for any other purpose, the author is not liable.
     
    """)



########################################################################################################################
########################################################################################################################
########################################################################################################################
if Nav_Menu == "Stablecoins Analysis":
    st.markdown("<h1 style='text-align: center; color: white;'>""Stablecoins: Key Roles in Blockchain & Traditional Banking""</h1>", unsafe_allow_html=True)
    #Name on document
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Guy L. Gnakpa""</h1>", unsafe_allow_html=True)
    #Date of on documents
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" May 2022""</h1>", unsafe_allow_html=True)
        #____________________________Insert Abstract and Introduction title/body text___________________________________________
    "\n"
    "\n"
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>""Abstract""</h1>", unsafe_allow_html=True)
    #subtitle "Abstract" using markdown function with html
    st.write("<div style='text-align:justify'> ""\n"
    "2020-2021 was a remarkable year for cryptocurrency and the blockchain industry"
    " as a whole. The market capitalization reaching $3 billion in November 2021 was a surprisingly incredible event. While many "
    "individuals couldn't have predicted this moment, others waited patiently to witness history in the making. Who would have thought "
    "decentralized networks with a peer-to-peer architecture would be so disruptive. The fundamental idea that anybody in the world can "
    "participate in the transaction of data in a secured and robust fashion is in fact revolutionary and disruptive. Among this technical "
    "revolution exist a class of cryptocurrency known as stablecoins. At a rudimentary level, stablecoins act as settlement agents because the "
    "value can represent the traditional dollar or a respective commodity. The stablecoin asset class grew over the course of 12 months surpassing "
    "$100 billion. The growth and adoption of stablecoins can have a significant influence on the cryptocurrency market and future of finance. "
    "This document will discuss the value proposition and types of stablecoins, the impact of stablecoins on blockchain adoption, and the impact on traditional "
    "fiat rails. A clear understanding of the value and multitudes of use-cases are essential as we examine it's effect on blockchain adoption and future financial "
    "applications. The document will take a technical approach as it attempt to analyze and explain the main points mentioned. Statistical methods and reliable data will be "
    "utilised to elucidate and visualize the objectives of this document. This analysis has been completed while considering the regulatory research of stablecoins "
    "for unified ruling as they may raise concerns and opportunities for traditional markets. Note, the report should serve as a sophisticated educational tool to further comprehend the evolution "
    "happening in the distributed ledger technology and financial markets.", unsafe_allow_html=True)
    #insert Introduction title and text
    st.subheader("Introduction")
    st.write("<div style='text-align:justify'>""\n"
    "The adoption growth of cryptocurrency, stablecoins in particular have wheeled\n"
    "the interest of many traditional market makers and market regulators worldwide. Federal Reserve Chairman, Jerome Powell said,"
    """ "One of the stronger argument for the U.S. central bank to set a digital currency is that it could undercut the need for private """
    """alternatives such as cryptocurrency and stablecoins", Reuters (Gary B. Gorton and Jeffery Y. Zhang, 2021). Federal Reserve Chairman, """
    "Jerome Powell is one of many officials who have commented on the adoption and influence of stablecoins. The demand of these digital assets "
    "has fostered an urgency for traditional markets and regulatory bodies to investigate the risks and opportunities that exist. The value proposition "
    "and utility will be defined by reporting on the various types of stablecoins. Further, a linear regression will be conducted to explore the relationship "
    "between the top stablecoin and Bitcoin. Lastly, the impact of stablecoins on centralized banking will be observed by assessing traditional institutions "
    "that are engaging with Central Bank Digital Currencies(CBDCs).", unsafe_allow_html=True)
    st.markdown("""---""")
#_______________________________I.A Insert Body text for Categorical Analysis:value proposition ________________________
#Descriptive analysis
    st.subheader("I. Descriptive Analysis")
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""A. Categorical Analysis: Value Proposition & Types of Stablecoins""</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>There are many components that are associated with the value proposition offered by "
    "stablecoins. Stablecoins were originally designed to serve as stabilizer agents for crypto trading settlements. More "
    "specifically, stablecoins minimize the volatility that is associated with the cryptocurrency market. The following are some examples "
    "of value proposition currently practiced.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
         "\n"
         "1. ***Hedging***: against volatility is one way stablecoins have created value for the"
         "   crypto market. Many cryptocurrencies or tokens are subject to market volatility. Stablecoins hold their value to a fixed price pegged"
         "   traditionally to the dollar, commodity or a respective native token. An investor who accumulated a significant amount of capital gain on"
         "   a given principle may not want to subject the funds to future market trends. The investor can use stablecoins as a vehicle to hedge for long"
         "   or short term move against volatility that’s in the market. Cryptocurrency miners can as well use stablecoins as a hedging instrument. During Bitcoin halving(s), miners who"
         "   are inclined to liquidate their crytocurrency assets for the purchase of equipments can leverage stablecoins without loosing significant value. This action prevents"
         "   miners from exposing their total portfolio to market volatility.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
         "\n"
         "2. ***Remittance***: transaction is an example in which stablecoins have infiltrated\n"
         "   the traditional banking system. Sending remittance via stablecoins can save significant upside for the parties involved."
         "   The reduction of time allocation and processing fees enable stablecoins to thrive in this specific financial sector. Traditional"
         "   rails like Western Union can often take 24 hours for domestic money transfer. Internationally, this process can take one to five business"
         "   days and be significantly expensive due to intermediaries. Processing such transactions utilizing USD Coin for example can take less than 10 minutes"
         "   with lower fees than Western Union. Additionally, the currency exchange rate between regions can reduce the original value when using traditional rails. Stablecoins allow for"
         "   fast transactions while removing intermediary bodies. Participants can transact without loosing a significant value on the total fund.\n",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
         "\n"
         "3. ***Capital gain***: settlement in stablecoins is a positive value transfer for investors. Traders can transfer in and out"
         "   of an asset without loosing sigificant value on trading fees. In addition, the porfolio can be protected from negative market trends.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
         "\n"
         "4. ***Reduction in trading cost***: is an added value stablecoins bring to the"
         "   digital asset and traditional markets. Stablecoins like Gemini Dollar(GUSD) and Binance USD(BUSD) enable cheaper transaction"
         "   fees than the traditional U.S. dollar during settlement of realized profits. Many stablecoins with such utility have helped increase"
         "   liquidity while creating optionality in the market." ,unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
         "\n"
         "5. ***Medium of exchange***: consistently takes place in the cryptocurrency market. Naturally,"
         "   the stablecoins infrastructure have created a simpler medium of exchange. Individuals utilize stablecoins to purchase other volatile"
         "   digital assets on exchanges that support stablecoins. Web 3 platforms like Travala and fintech firms like Stripe have added stablecoins as a"
         "   medium to purchase goods and services. This trend may continue as Stablecoins become more accepted." ,unsafe_allow_html=True)
    "\n"
    st.write("___")
#                   _______________________Stablecoins Categories__________________________
    st.write("<div style='text-align:justify'>""\n"
         "Majority of custodial stablecoins claim to be backed by traditional reserves like fiat, treasury bonds or other commodities. As of today, there exists four type of stablecoins."
         " Most stablecoins can be found on centralized and decentralized exchanges. The most common are fiat-backed stablecoins, which most participants have access to through markets "
         "like Coinbase and Uniswap. Below are the different categories available to the public.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
         "\n"
         "1. ***Fiat-backed stablecoins***: which are commonly known to be pegged one-to-one to the value held in reserve( dollars,euros, yen, yuan etc...)."
         "\n"
         "2. ***Commodity-backed stablecoins***: are often pegged to a tangible asset like oil, gold, silver, or other precious metals. The main attraction of these"
         "   stablecoins is that they are highly liquid while representing some illiquid traditional commodities.\n"
         "\n"
         "3. ***Crypto-backed stablecoins***: are pegged to fiat; however, the collateral is a digital crypto asset native to a respective network like; Bitcoin, Ethereum and many more."
         "\n"
         "4. ***Algorithmic-backed stablecoins***: maintain the price stability through smart contract conditions and algorithms that adjust supply based on market volatility.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""The figures below are examples of categorical stablecoins by market capitalization.",unsafe_allow_html=True)
#______________________________________________________________________________________________________________________#
#Using a def-function Pull Data from coingecko: Top 18 stablecoins \ provide currency \store and display in dataframe
    @st.cache
    def API_Data_Top():
        cg=CoinGeckoAPI() # call the coingecko API
        Top_Stablecoins_response=cg.get_coins_markets(
            ids=["tether", "usd-coin","binance-usd","terrausd","dai","frax","magic-internet-money","true-usd",
                 "pax-gold","neutrino","paxos-standard","fei-usd","liquity-usd","tether-gold","husd","mimatic",
                 "gemini-dollar","tether-eurt","alchemix-usd","usdx","xsgd","stasis-eurs","nusd"],
            vs_currency="usd")
        return Top_Stablecoins_response
    Top_Stablecoins_response=API_Data_Top()
    # store and display return of function as a dataframe \ clean: Drop columns \ print new dataframe
    Top_Stablecoins_df=pd.DataFrame(Top_Stablecoins_response)
    Top_Stablecoins_New_df=Top_Stablecoins_df.drop(
        columns=["id","image","symbol","market_cap_rank","fully_diluted_valuation","roi","ath_change_percentage",
                 "last_updated","atl","ath_date","atl_date","ath","atl_change_percentage","max_supply",
                 "price_change_percentage_24h","market_cap_change_24h","price_change_24h","market_cap_change_percentage_24h"
                 ],
        axis=0)
    st.dataframe(Top_Stablecoins_New_df)
    #insert figure button
    TopStablecoin_button=st.expander(label="figure 1.0 : Top Stablecoins Dataset")
    TopStablecoin_button.write("""
        Datasource: CoingeckoAPI
        
        Technologies: PyCharm, CoingeckoAPI functions, Python; pandas, streamlit """)
    #___________________________________________prep variabbles to be plotted_______________________________________________#

#__________________________Fiat-Backed Stablecoins___________________________#
    Fiat_Backed_Stablecoins_New_df=Top_Stablecoins_New_df[
        Top_Stablecoins_New_df["name"].isin(["Tether","USD Coin","Binance USD",
                                             "TrueUSD","HUSD","Gemini Dollar","Pax Dollar","Euro Tether","STASIS EURO","XSGD"])].sort_index(ascending=False)
    #st.dataframe(Fiat_Backed_Stablecoins_New_df)
    Fiat_MktCap=Fiat_Backed_Stablecoins_New_df["market_cap"].sum()
    #st.write(Fiat_MktCap)
#__________________________Commodity-Backed Stablecoins___________________________#
    Commodity_Backed_Stablecoins_New_df=Top_Stablecoins_New_df[
        Top_Stablecoins_New_df["name"].isin(["PAX Gold","Tether Gold"])].sort_index(ascending=False)
    #st.dataframe(Commodity_Backed_Stablecoins_New_df)
    Commodity_MktCap=Commodity_Backed_Stablecoins_New_df["market_cap"].sum()
    #st.write(Commodity_MktCap)
#__________________________Crypto-backed Stablecoins___________________________#
    Crypto_Backed_Stablecoins_New_df=Top_Stablecoins_New_df[
        Top_Stablecoins_New_df["name"].isin(["Dai","Magic Internet Money","Liquity USD",
                                             "Alchemix USD","Neutrino USD","USDX","sUSD"])].sort_index(ascending=False)
    #st.dataframe(Crypto_Backed_Stablecoins_New_df)
    Crypto_MktCap=Crypto_Backed_Stablecoins_New_df["market_cap"].sum()
    #st.write(Crypto_MktCap)
#__________________________Algo-backed Stablecoins___________________________#
    Algo_Backed_New_df=Top_Stablecoins_New_df[
        Top_Stablecoins_New_df["name"].isin(["TerraUSD","Frax","Fei USD","MAI",])].sort_index(ascending=False)
    #st.dataframe(Algo_Backed_New_df)
    Algo_MktCap=Algo_Backed_New_df["market_cap"].sum()
    #st.write(Algo_MktCap)

#____________________Create a Dataframe for the Calculated MarketCap _____________#
    Category_MarketCap={"StablecoinCategory":["Fiat-backed Stablecoins","Commodity-backed Stablecoins",
                                              "Crypto-backed Stablecoins","Algorithmic-backed Stablecoins"],
                        "MarketCapitalization":[Fiat_MktCap,Algo_MktCap,Crypto_MktCap,Commodity_MktCap]}
    Category_MarketCap_df=pd.DataFrame(Category_MarketCap) #.sort_index(ascending=False)
    #st.dataframe(Category_MarketCap_df)
#________________________________________________Using plotly display bar charts______________________________________#
    st.markdown("<h1 style='text-align: center; font-size: 100%'>Stablecoins Categories</h1>", unsafe_allow_html=True)
    #Initiate figure with subplot
    fig=make_subplots(rows=2, cols=2, subplot_titles=(
        "Fiat-backed Stablecoins",
        "Commodity-backed Stablecoins",
        "Crypto-backed Stablecoins",
        "Algorithmic-backed Stablecoins"),
                      vertical_spacing=0.35,
                      horizontal_spacing=0.25)
#Add Needed Traces
    fig.add_trace(go.Bar(x=Fiat_Backed_Stablecoins_New_df["name"], y=Fiat_Backed_Stablecoins_New_df["market_cap"]),row=1, col=1,)
    fig.add_trace(go.Bar(x=Commodity_Backed_Stablecoins_New_df["name"],y=Commodity_Backed_Stablecoins_New_df["market_cap"]),row=1, col=2)
    fig.add_trace(go.Bar(x=Crypto_Backed_Stablecoins_New_df["name"],y=Crypto_Backed_Stablecoins_New_df["market_cap"]),row=2, col=1)
    fig.add_trace(go.Bar(x=Algo_Backed_New_df["name"], y=Algo_Backed_New_df["market_cap"]),row=2, col=2)
    fig.update_layout(width=1350, height=700, plot_bgcolor='rgba(0,0,0,0)')
    #Update xaxis properties
    fig.update_layout(showlegend=False)
    fig.update_xaxes( showgrid=False, tickangle=90, row=1, col=1)
    fig.update_xaxes( showgrid=False, tickangle=90, row=1, col=2)
    fig.update_xaxes(title_text="Stablecoins", showgrid=False, tickangle=90, row=2, col=1)
    fig.update_xaxes(title_text="Stablecoins", showgrid=False, tickangle=-90, row=2, col=2)
    #Update yaxis properties
    fig.update_yaxes(title_text="Market Capitalization($)", showgrid=False, row=1, col=1)
    fig.update_yaxes(title_text="Market Capitalization($)", showgrid=False, row=1, col=2)
    fig.update_yaxes(title_text="Market Capitalization($)", showgrid=False, row=2, col=1)
    fig.update_yaxes(title_text="Market Capitalization($)", showgrid=False, row=2, col=2)
    #fig.show()
    st.plotly_chart(fig)

    #insert figure button
    Stablecoin_Categ_button=st.expander(label="Figure 1.1A - 1.1D : Stablecoins by Categories")
    Stablecoin_Categ_button.write("""
    1.1A: Fiat Stablecoin
        
    1.1B: Commodity-backed Stablecoins
        
    1.1C: Crypto-backed Stablecoins
        
    1.1D: Algorithmic-backed Stablecoins
        
    Datasource: CoingeckoAPI
        
    Technologies: PyCharm, Python; plotly subplots, pandas, streamlit, """)

#Display the various stablecoins category and  marketcaps
    Categ_Visual1=px.bar( data_frame=Category_MarketCap_df,x=["MarketCapitalization","StablecoinCategory"],y="StablecoinCategory",
                          color="StablecoinCategory",orientation="h",barmode="stack",width=1290, height=250,)
    #Update xaxis properties
    Categ_Visual1.update_xaxes(title_text="Market Capitalization($)", showgrid=True)
    #Update yaxis properties
    Categ_Visual1.update_yaxes(title_text="Categories")
    Categ_Visual1.update_layout(legend_title="Stablecoin Categories",plot_bgcolor='rgba(0,0,0,0)' )
    st.plotly_chart(Categ_Visual1)
    #insert figure button
    Categ_Visual1_button=st.expander(label="Figure 1.2 : Stablecoins Categories by Market capitalization ")
    Categ_Visual1_button.write("""
    Datasource: CoingeckoAPI
    
    Technologies: PyCharm, Python; plotly express, pandas, streamlit""")
#___________________#Bar charts Body Text description_________________________________#
    st.write("<div style='text-align:justify'>""\n"
             "Looking at the examples provided above, the data suggests the Fiat-backed category is the most valuable category representing"
             " more than $140 billion based on the market capitalization. Within the Fiat-backed category, the token Tether occupies most"
             " of the market shares with a market capitalization of roughly $75 billions. Although the Commodity-backed categogy has only two"
             " tokens, Pax Gold has a high market capitalization of more than $601 million versus Tether Gold hovering around $458 million."
             " There exists large domiance when observing the Crypto-backed stablecoins category. Within the five examples given, the Dai token by far has"
             " the largest market capitalization of approximately $6 billion. The token sUSD hold the smallest market capitalization of about $91"
             " million. Lastly, the Algorithmic-backed stablecoins category also displays a large dominance effect. Frax proves to hold the largest"
             " market capitalization of about $1.5 billion, while MAI holds the smallest market capitalization of roughly $269.5 million. It is important "
             "to note the market capitalizations expressed for these categories are not fixed and suggest to change based on the market demand. The interpretation of the"
             " numerical values and ranking of each token correlates to the time in which the document is written (live data).\n",unsafe_allow_html=True)
    #___________________________________I.B Trend Analysis: Bitcoin vs. Tether______________________________________________
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""B. Trend Analysis: Bitcoin vs Tether ""</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Bitcoin has been the most dominant cryptocurrency since its inception. Despite the fluctuation of percentage dominance"
             " due to market volatility, Bitcoin has held a significant percentage of the total liquidity available on the market for years."
             " More than often the cryptocurrency market follows the bitcoin trend. The above categorical analysis indicates Tether is the most"
             " liquid among all stablecoins. A time series analysis between the total volumes of Bitcoin and Tether can be conducted to explore"
             " any existing relationships. Exploring the volume as opposed to the price can better demonstrate the trend of supply and demand.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "Figure 1.3 below, is a line graph expressing the trend between the total volumes of Bitcoin and Tether from January 2, 2020 to April 3,"
             " 2022. At a fundamental level, both Bitcoin and Tether display some characteristics of seasonality. Further, the graph indicates Tether has"
             " more volume than Bitcoin at a consistent level for the chosen time period. The figure shows one event when the daily Bitcoin volume is greater"
             " than Tether's volume. On September 6th 2020, the total volume for Bitcoin was $56.43 billion, while Tether's volume was $53.09 billion."
             " From the given data, the daily Bitcoin volume surpassed Tether's volume by $3.34 billion. Aside from Bitcoin's one event of daily volume significance,"
             " Tether's daily volume has dominated for the given time period. From November 16, 2020 to May 27 2021, Tether's volume indicates a positive trend. Whithin"
             " that time period, there were five all-time high peaks, whithout a pull-back to the daily volume of November 16, 2020. On November 27 2020, the daily volume was"
             " $81.12 billion. The next all-time high of daily volume is $116.09 billion on January 9, 2021. Followed by a peak on February 10, 2021 with a significant"
             " volume of $120.39 billion. The trend continues on April 13, 2021 with a daily volume of $123.52 billion dollars. Lastly, on April 27th 2021, the all-time high surpasses"
             " the previous with a daily volume of $124.92 billion before a significant pullback.\n", unsafe_allow_html=True)
    #_____________________________________Import GoingeckoAPIexcel file_____________________________________________________
    #import data
    BTC_USDT_DF=pd.read_excel("Stablecoins.xlsx")
#______________________________________CLean Data for Trend and Regression Analysis____________________________________
#check data before outlier -> NUll
    Null_check=BTC_USDT_DF.isnull().sum()

    #                           ________#Define a function to treat columns simultaneously_________
    #first ID the outlier that are behond the UL and LL limits
    @st.cache
    def Outlier_limits(col):
        Q3,Q1=np.nanpercentile(col, [75,25])
        IQR=Q3-Q1
        Upper_limit=Q3+1.3*IQR
        Lower_limit=Q1-1.3*IQR
        return Upper_limit, Lower_limit
    #st.write(Outlier_limits)
    #                               _____________Convert the Outlier to Missing values_________
    for column in BTC_USDT_DF.columns:
        if BTC_USDT_DF[column].dtype != "object":
            Upper_limit, Lower_limit=Outlier_limits(BTC_USDT_DF[column])
            BTC_USDT_DF[column]=np.where((BTC_USDT_DF[column]>Upper_limit)|(BTC_USDT_DF[column]<Lower_limit),
                                         np.nan, BTC_USDT_DF[column])

    #                      _______Check for missing Values|There are zero missing values_______
    #check data after outlier -> NUll
    SL_Null_check2=BTC_USDT_DF.isnull().sum()
    #st.write(Null_check2)
    #       ______Conduct Treatment of missing(outliers) values via KNNImputerAlgo___________
    #Create a copy of the original df and apply KNN method
    BTC_USDT_DF_KNN=BTC_USDT_DF.copy()
    knn=KNNImputer()
    BTC_USDT_DF_KNN.iloc[:, :]=knn.fit_transform(BTC_USDT_DF_KNN)
    #check for Null after KNN treatment
    Null_check3=BTC_USDT_DF_KNN.isnull().sum()
    #st.write(Null_check3)
#_________________________________________Plot Line Chart for Trend Analysis____________________________________________
#change unix format into datetime format
    BTC_USDT_DF_KNN["Timestamp"]=pd.to_datetime(BTC_USDT_DF_KNN["Timestamp"], unit="ms").dt.date
    #Plot the data above
    x2=pd.DataFrame(BTC_USDT_DF_KNN)
    BTC_USDT_Plot=px.line(x2, x="Timestamp", y=["Bitcoin Total Volumes","Tether Total Volumes","USD Coin Total Volumes","Pax Gold Total Volumes"],
                          title="BTC and USDT Total Volumes From Jan 2020-April 2022")
    BTC_USDT_Plot.update_layout( legend_title="Digital Assets", width=1300, height=450, title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
    BTC_USDT_Plot.update_xaxes(showgrid=False, title="Date")
    BTC_USDT_Plot.update_yaxes(showgrid=True,title="Daily Volume($)")
    st.plotly_chart(BTC_USDT_Plot)
    #      ____________Insert Body Text for Metric Visuals of Daily Volume % Growth between Nov2020-May2021________
    st.write("<div style='text-align:justify'>""\n"
             "The metrics highlighted below, show a significant increase in the daily trading volume of Tether. From November 16th 2020 to April 27th 2021, Tether's daily volume"
             " increased by approximately 54%. In a matter of 5 months, the daily trading volume grew incredibly. After a significant correction, the market ajusted to a much lower volume"
             " of $32.36 billion as displayed on the line chart above.\n", unsafe_allow_html=True)
    #      ____________Insert Metric visuals of Daily Volume % Growth between Nov2020-May2021_______________
    "\n"
    col1=81.12
    col2=124.92
    col3=format((col2-col1), ".2f")
    Nov_2020_Col, May_2021_col2, N_months, DailyVolume_PercentChange_col3 = st.columns(4)
    Nov_2020_Col.metric("Nov 16,  2020 Daily Volume($)", "81.12B")
    May_2021_col2.metric("April 27, 2021 Daily Volume($)", "124.92B")
    N_months.metric("Number of Months", "5")
    DailyVolume_PercentChange_col3.metric(label="∆ in Daily Volume(%)", value="43.8B", delta=format(((col2-col1)/(col1)*100),".2f"))
    #insert figure button
    BTC_USDT_Plot_button=st.expander(label="figure 1.3 : BTC and USDT line Graph")
    BTC_USDT_Plot_button.write("""
    Datasource: CoingeckoAPI
    
    Disclaimer: Data was treated for outliers using KNNImputer Algorithm
    
    Technologies: PyCharm, API functions, Python; plotly express, pandas, numpy sklearn.Impute, streamlit """)
    st.write("___")
#___________________________________II. Predictive Analysis: Bitcoin vs. Stablecoins _________________________________________
# Insert Title/Body Text
    st.subheader("II. Predictive Analysis: Bitcoin vs. Stablecoins ")
    st.write("<div style='text-align:justify'>""\n"
             " The demand for stablecoins have increased its supply and volume in the past several months. With that in mind, the questions remains, "
             " does the trading volume of Stablecoins influence the volume of Bitcoin and to what degree of significance? "
             " The question can be observed through a first principle framework by utilizing the technique of simple linear regression."
             " Although figure 2.0 displays many variables, the daily volume for Bitcoin and Tether are the two variables needed to conduct the "
             "regression. Bitcoin will be the dependent variable (response) while Tether will act as the independent variable (predictor). Figure 2.0 "
             "shows the dataset extracted from CoingeckoApi for the regressions.",unsafe_allow_html=True)
    "\n"
#insert the respective dataset
    st.dataframe(BTC_USDT_DF_KNN)
    #              ______________Insert summary statistics Body Text & Graphs_______________
    st.write("<div style='text-align:justify'>""\n"
             "The table below is a summary statistics derived from the original dataset. All the variables have "
             " the same number of data ; 821 observations. Among the observations, the variable with the largest mean value is Tether; $59.46 "
             "billion. TerraUSD holds the minimum value of $16.19 billion, while Tether representing the largest median value at $54.35 billion. "
             "Lasly, Tether holds the largest maximum value of $124.92 billion. As illustrated, Tether's daily total volume dominate in every "
             "level (except minimum value) compared to the rest of the variables.",unsafe_allow_html=True)

    #insert descriptive summary
    Desc_BTC_USDT_DF=BTC_USDT_DF_KNN.describe()
    "\n"
    st.table(Desc_BTC_USDT_DF)
    #insert figure button
    Dataset_button=st.expander(label="Figure 2.0 - 2.1 : Stablecoins Regression Dataset & Summary Statistics")
    Dataset_button.write("""
    Figure 2.0: Stablecoins Regression Dataset
    
    Figure 2.1 : Summary Statistics
    
    Datasource: CoingeckoAPI
    
    Disclaimer: Data was treated for outliers using KNNImputer Algorithm
    
    Technologies: PyCharm, CoingeckoApi, Python; KNNImputer, pandas, streamlit""")

    #                   ____________#insert Simple Linear Regression title&Body Text________________
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""A. Simple Linear Regression: Bitcoin vs Tether""</h1>", unsafe_allow_html=True)
    #Insert Histogram Plot Body Text
    st.write("<div style='text-align:justify'>""\n"
             "Before the model implementation, let's first observe the data's frequency distribution through a histogram. Figure 2.1A"
             " below, is a histogram showcasing value distribution of both variables. Tether's values are represented in the blue color,"
             " while Bitcoin's values are represented in red. The x-axes holds both the BTC and USDT values. The y-axes represents the "
             "frequency. The histogram appears to be asymmetrical due to the right-skewed distribution (positive skewed distribution). "
             "More specifically, the Bitcoin's distribution shows left truncation. This distribution indicates the mean, median and mode are much different."
             " Unlike a normal distribution with equal mean, median and mode, the positive skewed distribution tend to be less predictable. The dataset skews "
             "to the right much more for Tether because the lower bounds are much smaller values relative to the complete dataset. With better understanding of the data frequency distribution,"
             " the next graphs can be plotted.",unsafe_allow_html=True)
    #                           __________________Insert all respect plots___________________
    SL_Reg=BTC_USDT_DF_KNN
    #Plot Histogram
    Reg_BTC_USDT_Hist_DF=px.histogram(SL_Reg[["Tether Total Volumes","Bitcoin Total Volumes"]], title="Histogram of BTC and USDT Volume", range_x=[-10,350000000000])
    Reg_BTC_USDT_Hist_DF.update_layout(legend_title="Digital Assets", width=1300, height=450, title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
    Reg_BTC_USDT_Hist_DF.update_xaxes(showgrid=False, title="BTC and USDT Volume($)")
    Reg_BTC_USDT_Hist_DF.update_yaxes(showgrid=True,title="Frequency")
    st.plotly_chart(Reg_BTC_USDT_Hist_DF)
    #Insert Scatter Plot Body Text
    st.write("<div style='text-align:justify'>""\n"
             "Figure 2.1B is a scatter plot illustrating the daily volume distribution between Bitcoin and Tether. Bitcoin's values are "
             "represented on the y-axes in billions. Tether's daily trading volumes are represented on the x-axes in billions as well. "
             "The plot shows significant characteristics of a positive correlation between the two digital assets. It is clear both variables "
             "are rising and moving to the right in a positive direction. Lastly, the distribution does not demonstrate data points far beyond "
             "majority of the cluster, thus lowering the risks of outliers. The next plot will confirm if any outliers exist.", unsafe_allow_html=True)
    #Plot Scatter plot(Bitcoin)
    Reg_BTC_USDT_Scatter_DF=px.scatter(SL_Reg, x="Tether Total Volumes", y="Bitcoin Total Volumes", title="Scatter Plot of BTC and USDT Volume")  #trendline="ols"
    Reg_BTC_USDT_Scatter_DF.update_layout(width=1300, height=450, title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')#width=1000, height=450,
    Reg_BTC_USDT_Scatter_DF.update_xaxes(showgrid=False, title="Tether Volume($)")
    Reg_BTC_USDT_Scatter_DF.update_yaxes(showgrid=False,title="Bitcoin Volume($)")
    st.plotly_chart(Reg_BTC_USDT_Scatter_DF)
    #Insert BoxPlot Body Text
    st.write("<div style='text-align:justify'>""\n"
             "Figure 2.1C is a boxplot to better visualize the potential existing outliers. In the both distributions, the plot shows "
             "the median of the data is slightly closer to 25th quantile as also indicated in the histogram. This event signifies the data is slightly skewed and not symmetrical."
             " The distribution has no data points within or beyond either whiskers. Essentially, there are no outliers based on the boxplot.",unsafe_allow_html=True)
    #Insert a Outlier Boxplot
    Reg_BTC_USDT_BoxPlot_DF=px.box(SL_Reg, y=["Bitcoin Total Volumes","Tether Total Volumes",], title="Box Plot of BTC and USDT Volume", notched=True) #color="Tether Total Volumes",
    Reg_BTC_USDT_BoxPlot_DF.update_layout(width=1300, height=450, title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')#width=1000, height=450,
    Reg_BTC_USDT_BoxPlot_DF.update_xaxes(showgrid=False, title="Digital Assets")
    Reg_BTC_USDT_BoxPlot_DF.update_yaxes(showgrid=False,title="Volume($)")
    st.plotly_chart(Reg_BTC_USDT_BoxPlot_DF)
    #insert model implementation info
    st.info("The model below is implementated using Ordinary Least Squared to attempt to quantify the level of significance between the relationship of the BTC volume and USDT volume. ")
    #Inser Simple Linear Regression formula
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" ŷ= Bitcoin Total Volume, b0 = y-intercept , x1 =Tether Total Volume, e =  Error Term  ""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" Bitcoin Total Volume = Y-Intercept + Tether Total Volume + Error Term ""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" ŷ  = b0 + b1x1 + e  ""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" ŷ  = 7.8221e+09 + 0.47489 Tether Total Volume ""</h1>", unsafe_allow_html=True)

    #                             ______________Conduct Simple Regression & Body Text________________
    SL_Reg2=SL_Reg.copy()
    x_variable=SL_Reg2["Tether Total Volumes"]
    y_variable=SL_Reg2["Bitcoin Total Volumes"]
    x_variable=sm.add_constant(x_variable)
    Model_1=sm.OLS(y_variable, x_variable).fit()
    st.write(
        #Model_1.params,
        #Model_1.summary()
    )
    SLRegression_imge = Image.open("SLRegression1.png")
    #Create/Insert col for Reg output and interpretation
    SL_col1, SL_col2, = st.columns(2)
    with SL_col1:
        st.image(SLRegression_imge, width=700)
    with SL_col2:
        st.info("""
    ***Result Overview***: The results of the OLS linear regression model is on the left in figure 2.1D. The data was tested for outliers through clear logic. Existing outliers were transformed to null values. All null values were treated using an KNNImputer algorithm.
    The Data was tested for multicollinearity using a VIF method. A result of 5 indicated moderate level and no treatment was necessary.
    
    ***Key Metrics***: The R-squared and Standard Error of Regression (S) are important metrics to observe and interpret when conducting a regression. The R-Squared explains the variation in y = (Bitcoin volume).
    S explains the distance the data falls from the regression line as displayed below. Figure 2.1E shows the predictive trend line and the equation.
    
    ***Result Interpretation***: The coefficient of determination(R-Squared) is .72. Tether's volume explains 72% of the total variation in the Bitcoin volume.
    The S value and predictive regression line below indicate a significant number of data points fall on the regression line and near it.
    Each additional added volume of Tether is correlated with an average increase of 0.4748(coefficient) in Bitcoin volume based on the slope. Further, the t-stat associated
    with the respective p-value remains at 0. In conclusion, the standard error of the regression slope is smaller than the coefficient making Tether's volume
    statistically significant in relation to Bitcoin's volume.""")

    #                   ______________Insert Scatter PLot & Trend line For SL_Reg_____________
    #Plot Scatter plot(Tether)
    Reg_BTC_USDT_Scatter_DF=px.scatter(SL_Reg2, x="Tether Total Volumes", y="Bitcoin Total Volumes", trendline="ols", title="Scatter Plot of BTC and USDT(Trend Line)",trendline_color_override='white',color="Tether Total Volumes", )
    Reg_BTC_USDT_Scatter_DF.update_layout(width=1300, height=450, title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')#width=1000, height=450,
    Reg_BTC_USDT_Scatter_DF.update_xaxes(showgrid=False, title="Tether Volume($)")
    Reg_BTC_USDT_Scatter_DF.update_yaxes(showgrid=False,title="Bitcoin Volume($)")
    st.plotly_chart(Reg_BTC_USDT_Scatter_DF)
    # insert a correlation matrix table
    corrMatrix_0=pd.DataFrame(BTC_USDT_DF_KNN, columns=["Bitcoin Total Volumes","Tether Total Volumes","USD Coin Total Volumes", "Pax Gold Total Volumes", "Dai Total Volumes", "TerraUSD Total Volumes" ])
    corrMatrix=corrMatrix_0.corr()
    Corr_fig=px.imshow(corrMatrix)
    Corr_fig.update_layout(width=1230, height=450)
    st.plotly_chart(Corr_fig)

    #insert figure button
    SLReg_button=st.expander(label="Figure 2.1A - 2.1F : Visual Plots & OLS Regression Results")
    SLReg_button.write("""
    Figure 2.1A: Histogram of BTC and USDT Volume
    
    Figure 2.1B: Scatter Plot of BTC and USDT Volume
    
    Figure 2.1C: Box Plot of BTC and USDT Volume
    
    Figure 2.1D: OLS Regression Results
    
    Figure 2.1E: Scatter Plot of BTC and USDT Volume(Trend Line)
    
    Figure 2.1E: Heatmap of Digital Assets
    
    Datasource: CoingeckoAPI
    
    Disclaimer: Data was treated for outliers using KNNImputer Algorithm
    
    Technologies: PyCharm, CoingeckoApi, Python; statsmodels.api, KNNImputer, plotly express, pandas, streamlit""")

    # insert a correlation matrix table
    st.write("___")
    #_______________________________________III. Stablecoins & Fiat rails  _________________________________________________
    #Insert Title & Body text
    st.subheader("III. S.W.O.T Analysis: Central Bank Digital Currencies")

    st.write("<div style='text-align:justify'>""\n"
             "Distributed Ledger Technology has given rise to a multitude of digital asset applications particularly in the financial sector. "
             "Blockchain, derived from DLT, solved the doubled-spending problem enabling the prevention of data minipulation and payment authentication. "
             "The most powerful aspect of the technology is the transparency of the digital ledger, aka, data record. Any participant who is part of the "
             "network can view any public transactions stored on the network. The implication of the technology is disruptive for many intermediary institutions "
             "like brokers, settlement agencies and independent third-party verification. When mentioning stablecoins, it is without thinking of Central Bank Digital Currencies. "
             "The efficiency and immutability for a central bank-issued digital cash has proppeled nations worldwide to seriously investigate the opportunities and risk exposure if fully adopted. "
             "For years now, many nations and regulatory bodies have began research or implemented a pilot version of a government-issue stablecoin. Conducting a S.W.O.T analysis can "
             "help deepen the understanding of the risks and opportunities associated with the use of CBDCs.",unsafe_allow_html=True)

    #Insert Strength title & body text
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""A. Strengths</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Central bank stablecoins, CBDCs, can have a significant influence on the market as they serve as legal tender being they are already pegged "
             "to the existing central bank notes. When compared to traditional private bank deposits, CBDCs are a risk free alternative. This without a doubt is "
             "a competitive advantage compared to other forms of stablecoins. The issuance of CBDCs by a central bank can expand financial inclusion. Many regions in "
             "the U.S and in emerging nations lack access to financial banking vehicles. Accompanied with financial inclusion, participants can experience better efficiency in the "
             "payment system as opposed to the legacy system. For decades, the cost of conventional digital payment options like credit and debit card has been expensive with little innovation. "
             "CBDCs can be credit risk free for participants as they are directly coming from central bank. The reduction of a multitude of intermediary bodies can cut transaction fees and create "
             "more savings for the individual. Faster and better cross border payments would be an added strength to CBDCs. A study conducted by many financial institutions like Central Bank of Canada, "
             "Singapore and the UK has concluded CBDCs have the potential to reduce counterparty credit risk regarding cross-border payments. In that specific regard, countries that previously couldn't "
             "trade with other nations would then have access to new trade avenues while reducing the friction of foreign currency exchange rates. In totality, risks associated with the collapse of commercial bank "
             "and national hyperinflation can be eliminated. Although many strengths of CBDCs have been mentioned, many more will surface as more research and experimemts are completed by regulatory bodies. "
             "The figure 3.0, displays the types of Central Bank Digital Currencies. ",unsafe_allow_html=True)
    "\n"
    "\n"
    #insert CBDCs Architecture
    CBDC_col1,CBDC_col2,=st.columns(2)
    with CBDC_col1:
        CBDC_image0 = Image.open("CBDC Architecture3.png")
        st.image(CBDC_image0,width=645)
    with CBDC_col2:
        st.info("""
        Figure 3.0: CBDC Models. Expand picture for better visual. 
            
        ***Wholesale CBDCs***: facilitate payment and settling transactions between financial institutions for the purchase of
        assets and services. Ideally Wholesale CBDCs could replace the Real-Time Gross Settlement systems. Some are restricted to the regional
        issuer while others can be interoperable.
            
        ***Retail CBDCs***: focuses on day-to-day transactions for good and services by non-enterprise. Retail CBDCs can even be a vehicle 
        for public capital distribution during economic uncertainty.Retail CBDCs can be distributed directly to the consumer,
        though intermediary parties or a mixture of both techniques.""")

    #Insert Weaknesses title & body text
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""B. Weaknesses</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Well constructed CBDCs will have to iron key issues that are raising many concerns today. Primarily, Central Banks will have full control over CBDCs. "
             "With a centralized framework, central banks can restrict or influence the types of transactions permitted. In a long term this can be unsettling for all participants and  "
             "reduce confidence in the CBDC and its issuer. Further, central powers will have enormous data through the ledger. A clear ethical framework of data collection and data governance by central powers "
             "will have to be addressed to mitigate privacy concerns. Knowing education often fosters adoption, many individuals who do not have adequate resources may fall behind the DLT adoption curve. Central powers may need to "
             "take on the responsibility of educating the masses and promoting financial inclusion. The benefit of utilizing CBDCs are inherently great; however, many intermediary agencies like; small commercial banks, lenders and brokers "
             "could be significantly affected by the transition. Beyond the examples mentioned, there are many other weaknesses or concerns to be addressed by central banks in the years to come.",unsafe_allow_html=True)

    #Insert Opportunity title & body text
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""C. Opportunities</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "The demand for blockchain technology and digital assets has open a space for many opportunities. CBDCs have the chance to modernize the legacy banking system."
             "As previously expressed fast, cheaper, and more secure transactions would be the standard for payments and financial services if CBDCs are adopted throughout different markets. This would be a clear opportunity to shift to a cashless system."
             """Further, it is important to consider the vast number of unbanked individuals who still wish to participate in the financial market. According to Global Findex Database, "Globally about 1.7 billion adult remains """
             """unbanked--without an account at a financial institution or through a mobile money provider. In 2014 that number was 2 billion." At a local level, "5.4 percent of U.S. households (~ 7.1 million) were unbanked in 2019, meaning"""
             """ no one in the household had a checking or savings account at a bank or credit union" (FDIC, 2021,"How America Bank: Household Use of Banking and Financial Services)." There, lies an opportunity for CBDCs to onboard billions of people into """
             "a modern financial system. In return, the economy can increase in saving deposits. Once disposable income increases, individuals have more optionality for quality of living and spending. Emerging nations like Haiti, Zimbabwe, Nigeria, Ecuador and Ghana are regions "
             "that can benefit greatly from CBDCs as their native currencies often fall victim to hyperinflation and geopolitical events. An inclusive and efficient CBDC that has proper governance can certainly change the lives of billion individuals. Many nations have considered "
             "adopting to their own CBDC. Figure 3.1A shows an interactive dashboard of countries who have shown interest or begun testing CBDCs.",unsafe_allow_html=True)

    #Insert Threats body text
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""D. Threats</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Beyond all opportunities, there exists a large number of threats for central digital currencies. First and formost, decentralized ledger technologies have proven a significant level of security depending on the consensus protocol. "
             "While that holds to be true, cybersecurity remains the largest threat of CBDCs. Any database or digital payment system falls prey to cybersecurity attacks like; data breaches, account theft, and counterfeiting. There has already been "
             "numerous events of digital currencies experiencing large liquidation due to a weakness in the network. CBDCs will have to be constructed in a robust way to instill confidence in its security. Next, users with privileged rolls can be a thread to CBDCs. "
             "In the current payment system, central authorities have the privilege to authorize or deny transactions as part of compliance. The same behavior or action can take place with CBDCs compliance. Based on the consensus, central authorities or third parties whom have privileged actions "
             "must prevent internal bias or malicious action. Lastly, too many intermediary enterprises can increase the level of risk if not properly vetted. As there are many versions of CBDCs (figure 3.0), indirect retail CBDCs controlled by multitude of payment service providers will have to implement sound "
             "cybersecurity risk management for the benefit of all stakeholders. At last, there are many other significant threats to CBDCs; however, cybersecurity holds supreme. Figure, 3.1A below shows an interactive dashboard of nations interested in CBDCs. ", unsafe_allow_html=True)
    "\n"
    st.info(" ")

    #                               _________#Insert Tableau Dashboard__________
    Tableau_embedded_value="""
    <div class='tableauPlaceholder' id='viz1653292527042' style='position: relative'>
        <noscript>
            <a href='#'>
            <img alt='Central Bank Digital Currencies Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;te&#47;test_16530957433120&#47;Dashboard1&#47;1_rss.png' style='border: none' />
            </a>
            </noscript>
            <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
            <param name='embed_code_version' value='3' /> 
            <param name='site_root' value='' />
            <param name='name' value='test_16530957433120&#47;Dashboard1' />
            <param name='tabs' value='no' /><param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;te&#47;test_16530957433120&#47;Dashboard1&#47;1.png' /> 
            <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                
            <script type='text/javascript'> 
            var divElement = document.getElementById('viz1653292527042');var vizElement = divElement.getElementsByTagName('object')[0]; 
                if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='727px';} 
                    else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='727px';} 
                        else { vizElement.style.width='100%';vizElement.style.height='1177px';} 
                        var scriptElement = document.createElement('script'); 
                        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; 
                        vizElement.parentNode.insertBefore(scriptElement, vizElement); 
            </script>"""
    components.html(Tableau_embedded_value, width=9000, height=700)

    #insert figure button
    SLReg_button=st.expander(label="Figure 3.0 - 3.1A : CBDC Models & CBDCs Dashboard")
    SLReg_button.write("""
    Figure 3.0: CBDCs Models Architecture
    
    Figure 3.1A: Central Bank Digital Currencies Interactive Dashboard
    
    Datasource: CoingeckoAPI, cbdctracker.org
        
    Technologies: PyCharm, CoingeckoApi, Tableau, Miro Visual Whiteboard, Streamlit""")

    # insert a correlation matrix table
    st.write("___")
    #_________________________________________________IV. Conclusion________________________________________________________
    #Insert Stablecoins risks: Title and body text
    st.subheader("IV. Conclusion: Risk Analysis")
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""A. Stablecoin Risks: Lack of Reserves </h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Traditional stablecoins have shown lots of promises for the near future. The capibility for stablecoins to become mainstream has raised a primary concern for its reverse mechanism. Many individuals fear "
             "stablecoins are not fully backed by reserve currencies they claim. A stablecoin that is not sufficiently backed by cash, bank deposits, treasury bills, commodities or corporate bonds can experience detrimental liquidation events. "
             "This is a critical risk that can affect the greater crypto market. Algorithmic-backed stablecoins are the most susceptable to such vulnerability. A clear example of this concern has been examplified by the stablecoin TerraUSD. "
             "TerraUSD by Terrafor Labs is an algorithmic-backed stablecoin that collapsed with a loss of approximately $45 billion, including Terra Luna (native token), in less than seven days. The lack of reserves, risky stabilizer protocol and fixed high yield of its governance token(LUNA) led to de-risking pressure. "
             " A domino-effect of selling pressure caused many investors to lose life savings. This event is considered to be one of the most catastrophic in the history of cryptocurrency. In figures 5.0 and 5.1A, one graph shows the volume collapse of TerraUSD while the other shows the price collapse of its governance token Terra Luna. "
             " A correlation between the stablecoins's volume and governance token is evident. On May 6th, 2022 theres a massive retracement on both graphs. There seem to be an injection of liquidity in TerraUSD on May 7th, 10th and 12th, however; "
             " the sell off continued and Terra Luna kept dumping. The $1 stablecoin has been de-pegged from the US dollar since May 9th, 2022 and is currently trading below $0.10. The governance token, Terra Luna, was once trading at $116.29, today the same token is trading bellow $0.003. "
             "This collapse could very well be a foreshadowing for many Algorithmic-backed stablecoins if the system is not well constructed and has inadequate reserves.",unsafe_allow_html=True)
    #                              _________Call API for TerraUSD and Terra Luna___________
    #CallAPI/Select the needed columns

    def API_TerraUSD():
        cg=CoinGeckoAPI() # call the coingecko API
        TerraUSD_history=cg.get_coin_market_chart_by_id(id="terrausd", vs_currency="usd", days=365)
        TerraUSD_history_DF=pd.DataFrame(TerraUSD_history["total_volumes"])
        TerraUSD_history_DF=TerraUSD_history_DF.rename(columns={0:"Timestamp",1:"TerraUSD Volume"})
        return TerraUSD_history_DF
    TerraUSD_history_DF=API_TerraUSD()

    def API_TerraLuna():
        cg=CoinGeckoAPI() # call the coingecko API
        TerraLuna_history=cg.get_coin_market_chart_by_id(id="terra-luna", vs_currency="usd", days=365)
        TerraLuna_history_DF=pd.DataFrame(TerraLuna_history["prices"])
        TerraLuna_history_DF=TerraLuna_history_DF.rename(columns={0:"Timestamp",1:"Terra Luna Price"})
        return TerraLuna_history_DF
    TerraLuna_history_DF=API_TerraLuna()

    #Combine Tables
    UST_LUNA_DF=TerraUSD_history_DF
    UST_LUNA_DF["Terra Luna Price"]=TerraLuna_history_DF[["Terra Luna Price"]]
    UST_LUNA_DF["Timestamp"]=pd.to_datetime(UST_LUNA_DF["Timestamp"], unit="ms").dt.date

    #                              _____________Insert line graph of TerraUST/Luna___________
    UST_DF_PLOT=px.line(UST_LUNA_DF, x="Timestamp", y=["TerraUSD Volume"],
                        title="TerraUSD Volume")
    UST_DF_PLOT.update_layout( legend_title="Digital Asset", width=1300, height=450, title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
    UST_DF_PLOT.update_xaxes(showgrid=False, title="Date")
    UST_DF_PLOT.update_yaxes(showgrid=True,title="Daily Volume($)")
    st.plotly_chart(UST_DF_PLOT)

    LUNA_DF_PLOT2=px.line(UST_LUNA_DF, x="Timestamp", y=["Terra Luna Price"],
                          title="Terra Luna Price")
    LUNA_DF_PLOT2.update_layout( legend_title="Digital Asset", width=1300, height=450, title_x=0.5, title_y=.85, plot_bgcolor='rgba(0,0,0,0)')
    LUNA_DF_PLOT2.update_xaxes(showgrid=False, title="Date")
    LUNA_DF_PLOT2.update_yaxes(showgrid=True,title="Daily Price($)")
    st.plotly_chart(LUNA_DF_PLOT2)

    #                           _________Insert Stablecoins risks: Title and body text__________
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""A. CBDC Risks: Mass surveillance </h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "The S.W.O.T analysis has highlighted many threats with CBDCs. The risk of mass surveillance is a critical risk associated with the adoption of CBDCs. Based on the model and design, these "
             "government issued digital cash can have a massive implication on human rights. Government agencies will have the ability to monitor every move of every participant as all transactions are forever "
             "on the ledger. Individual's activity could potentially be targeted based on their credit history, politican ties, race or ethnicity. Transactions can very well be restricted or permitted by central bank authorities. "
             "Aside from control of funds, if applied CBDC issuers will have full access to digital identity of individuals. This also reigns massive implication on human rights. Participants will need confidence that their digital identity isn't misused. "
             "The best way to mitigate these concerns is to adopt CBDC solutions which place these risks at the forefront and eliminates them entirely. Central bank digital currencies will need to address a number of important risks and concerns in a short "
             "amount of time if authorities wish to include this technology in the fabric of traditional finance and banking.",unsafe_allow_html=True)

    #Insert Stablecoins risks: Title and body text
    st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""C. Bottom line </h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Distributed Ledger technologies have given rise to blockchains. Many of these chains have grown enormously in the past four years sparking pockets of economic value. "
             "Nations worldwide have recognized the future opportunities with their own version of stablecoins; CBDCs (digital cash). With so much innovations ahead for programmable money, there are many risks and concerns. Market makers, national authorities and "
             "international regulatory bodies will have to work extremly hard for an equilibrium between innovation and ethical implementation framework. In the months and years to come, the evolution of blockchain will be an exciting dance to watch between regulators and all stakeholders! ",unsafe_allow_html=True)
    "\n"
    #insert figure button
    SLReg_button=st.expander(label="Figure 5.0 - 5.1A : TerraUSD Volume & Terra Luna Volume")
    SLReg_button.write("""
    Figure 5.0: TerraUSD Volume
    
    Figure 5.1A: Terra Luna Volume
    
    Datasource: CoingeckoAPI
    
    Technologies: PyCharm, CoingeckoApi, Python; plotly express, pandas, streamlit""")

    st.info("REFERENCES")

    #insert References button
    SLReg_button=st.expander(label=" Expand for references")
    SLReg_button.write("""
    
    [bcg.com, Kay Burchardi, igor Mikhalev, Bihao Song, and Steven Alexander Kok (2020), "Get ready for the Future of Money"]
        (https://www.bcg.com/publications/2020/get-ready-for-the-future-of-money) 

    [bis.org, Hyun Song Shin, Benoit Coeure (2021), "Bis Annual Economic Report"]
        (https://www.bis.org/publ/arpdf/ar2021e3.htm)
    
    ["big.org, Condruta Boar and Andreas Wehrli (2021), "Ready, Steady, go? --Results of the Third BIS Survey on Central Bank Digital Currency]
        (https://www.bis.org/publ/bppdf/bispap114.pdf)
    
    [consensys.net, Matthieu Saint Olive (2020), "What is Retail Central Bank Digital Currency"]
        (https://consensys.net/blog/enterprise-blockchain/what-is-retail-central-bank-digital-currency/)
    
    [globalfindex.worldbank.org, "The Unbanked"]
        (https://globalfindex.worldbank.org/sites/globalfindex/files/chapters/2017%20Findex%20full%20report_chapter2.pdf)
    
    [FDIC.gov, Federal Deposite Insurance Corporation (2021), "How American Banks: Households Use of Banking and Financial Services"]
        (https://www.fdic.gov/analysis/household-survey/index.html)
        
    [nytimes.com, David Yaffe-Bellany and Erin Griffith (2022), "How a Trash-Talking Crypto Founder Caused a $40 Billion Crash "]
        (https://www.nytimes.com/2022/05/18/technology/terra-luna-cryptocurrency-do-kwon.html)
    
    [ecb.europa.eu, Mitsutoshi Adachi, Alexandra Born, Isabella Gschossmann and Anton Van Der Kraaij (2021), "The Expanding Functions and Uses of Stablecoins"]
        (https://www.ecb.europa.eu/pub/financial-stability/fsr/focus/2021/html/ecb.fsrbox202111_04~45293c08fc.en.html)
    
    [ieeexplore.ieee.org, Clemens Jeger, Bruno Rodrigues, Eder Scheid, and Burkhard Stiller (2020), "Analysis of Stablecoins During the Global COVID-19 Pandemic"]
        (https://ieeexplore.ieee.org/abstract/document/9274450?figureId=fig1#fig1)
    
    [libertystreeteconomics.newyorkfed.org, Rod Garratt, Michael Lee, Antoine Martin, and Joseph Torregrossa (2022), "The Future of payments Is Not Stablecoins"]
        (https://libertystreeteconomics.newyorkfed.org/2022/02/the-future-of-payments-is-not-stablecoins/)
    
    [finra.org, Finra (2020), "3 Things to Know About Stablecoins"]
        (https://www.finra.org/investors/insights/3-things-stablecoins
    
    [coindesk.com, Alexander Lipton (2020), "Stablecoins Are the Bridge From Central Banks to Consumer Payments."]
        (https://www.coindesk.com/markets/2020/05/30/stablecoins-are-the-bridge-from-central-banks-to-consumer-payments/)

    [coindesk.com, Kay Burchardi and Igor Mikhalev (2020), "Central Bank Digital Currencies Need Decentralization"]
        (https://www.coindesk.com/policy/2020/05/23/central-bank-digital-currencies-need-decentralization/)
   
    [101blockchains.com, Qwyneth Iredale (2021), "Advantages of Central Bank Digital Currencies (CBDCs)"]
        (https://101blockchains.com/advantages-of-central-bank-digital-currencies/)
    
    [weforum.com, Sebastian Banescu, Ben Borodach, and Ashley Lannquist (2021), "4 Key Cybersecurity threats to new central bank digital currencies"]
        (https://www.weforum.org/agenda/2021/11/4-key-threats-central-bank-digital-currencies/#:~:text=Yet%20like%20any%20digital%20payment,be%20confident%20in%20its%20security).
    
    [finextra.com, Jeremy Light (2022), "The Risks to Society of central Bank Digital Currencies"]
        (https://www.finextra.com/blogposting/21584/the-risks-to-society-of-central-bank-digital-currencies)
        
    [bloomberg.com, Hannah Miller (2022), "Terra $45 Billion Face Plant Creates Crowd of Crypto Losers"]
        (https://www.bloomberg.com/news/articles/2022-05-14/terra-s-45-billion-face-plant-creates-a-crowd-of-crypto-losers)
    
    [Coingecko API ]
        (https://www.coingecko.com/en/api/documentation)
    
    [CBDCs Tracker]
        (https://cbdctracker.org/)
    """)
    st.write("---")
########################################################################################################################
##########################################################################################################################
########################################################################################################################
if Nav_Menu == "Geography of Cryptocurrency Report":
    #_________________________________Import/Config Chainalysis logos_______________________________________________________
    # #insert background logo
    # Space_col1,Photo_col2,Space_col3=st.columns(3)
    # with Space_col1:
    #     "\n"
    # with Photo_col2:
    #     ChainalysisLogo1=Image.open("Chainalysis_Logo.png")
    #     st.image(ChainalysisLogo1, width=290)
    # with Space_col3:
    #     "\n"
    #insert background logo
    ChainalysisLogo2=Image.open("Logo0.png")
    st.image(ChainalysisLogo2, use_column_width="always")
    "\n"
    #_________________________________Introduction Body Text _______________________________________________________________
    st.subheader("Introduction")
    st.write("<div style='text-align:justify'> ""\n"
             "Satoshi Nakamoto once said, “A lot of people automatically dismiss e-currency as a lost cause because of all the "
             "companies that failed since the 1990’s. I hope it’s obvious it was only the centrally controlled nature of those "
             "systems that doomed them. I think this is the first time we’re trying a decentralized, non-trust-based system.”"
             " This vision of Satoshi Nakamoto was apparent more than ever soon after the 2019 Bitcoin halving. More specifically, "
             "2020-2021 showcased the possibility of cryptocurrency and its adoption for multitudes of use cases. The utilization of decentralized "
             "ledger technology ( DLT) can be observed throughout the world; from the small sub-region of Micronesia to the sub-region of North America. "
             "With the help of on-chain data, transactions from any respective blockchain ledger can be studies and interpreted to aid enterprise functions. "
             "To emphasize this point, this analysis report answers fundamental questions associated with received and deposited transactions throughout the world. "
             "The questions below are analyzed to better understand the geographic distribution of cryptocurrency funds. Further, compelling evidence affiliated with "
             "the volume of these transactions based on a specific time period is discussed. The overarching goal of this report is the investigation of cruptocurrency transactions and "
             "inform the reader about its utilization worldwide through statistical methods, and data visualization.",unsafe_allow_html=True)
    "\n"
    #_________________________________Import Statistical Questions _________________________________________________________
    st.info("""
        * Which top 5 sub-regions have received and deposited the most funds during 2019 – 2022? 
        * Within the top 5 sub-regions, which top nation are these transactions originating from?  
        * Within the top 5 sub-regions, which sub-region display most distributed volume of received transactions and what may be the reason(s) for it?
        * Which top 2 sub-regions show the lowest volume of deposits and which countries contribute to this output?
        * For the selected top 5 sub-regions, when are majority of the transactions (received and deposits) taking place?  
        * What are the catalysts that contributed to the enormous growth of cryptocurrency activity during 2020-2021? 
        """)
    st.write("____")
    #_________________________________Import/Dispaly data___________________________________________________________________
    "\n"
    #interpredation bodytext
    st.subheader("On-chain Cryptocurrency Value Received and Deposits From 2019 - 2022")
    df=pd.read_csv("Geography_Analyst_Data_Assignment.csv")
    st.dataframe(df)
    st.write("<div style='text-align:justify'> ""\n"
             "The table above expresses received and deposit transactions from around the world. The table is interactive and "
             "can be filtered via each respect attribute. The ranking of each sub-regions and countries can be identified by sorting "
             "received or deposited transactions."
             ,unsafe_allow_html=True)
    st.write("____")
    #_________________________________Visulization histogram charts_________________________________________________________
    #sub-regions
    st.subheader("Top 5 Sub-regions with Most Transaction Volume During  2019 - 2022")
    SubRegion_TotalTransac_plot0=px.histogram(df,x="final_sub_region",y=["final_received_usd","final_deposits"],
                                              title="Sub-Region: Received Funds vs. Deposits | Mar '19 - Apr '22",width=1360, height=500)
    SubRegion_TotalTransac_plot0.update_layout(legend_title="Transaction Type",plot_bgcolor='rgba(0,0,0,0)',xaxis={'categoryorder':'total descending'})
    SubRegion_TotalTransac_plot0.update_yaxes(title="Sum of Transactions ($)")
    SubRegion_TotalTransac_plot0.update_xaxes(title="Sub-Region")
    #SubRegion_TotalTransac_plot0.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(SubRegion_TotalTransac_plot0)
    #sub-regions
    st.subheader("Top Country with the Most Total Value Received During  2019 - 2022")
    Country_TotalTransac_plot0=px.histogram(df,x="final_country",y=["final_received_usd","final_deposits"],
                                            title="Country: Received Funds vs. Deposits | Mar '19 - Apr '22",width=1360, height=700)
    Country_TotalTransac_plot0.update_layout(legend_title="Transaction Type",plot_bgcolor='rgba(0,0,0,0)',xaxis={'categoryorder':'total descending'})
    Country_TotalTransac_plot0.update_yaxes(title="Sum of Transactions ($)")
    Country_TotalTransac_plot0.update_xaxes(title="Country")
    st.plotly_chart(Country_TotalTransac_plot0)
    "\n"
    "\n"
    #_____________________calculation/display metrics_______________
    #calculate the sum of both final_received_usd and final_deposits
    SUM_Received_funds=df["final_received_usd"].sum()
    SUM_Deposited_funds=df["final_deposits"].sum()
    #calculate the sum of each respective region for metric formation
    A=df.loc[df["final_sub_region"]=="Eastern Asia"].sum()
    B=df.loc[df["final_sub_region"]=="Northern America"].sum()
    C=df.loc[df["final_sub_region"]=="Eastern Europe"].sum()
    D=df.loc[df["final_sub_region"]=="Western Europe"].sum()
    E=df.loc[df["final_sub_region"]=="Latin America and the Caribbean"].sum()
    #calculate total Received and Deposited transactions against top 5 regions for metric output
    TotalReceived_Top5Regions=A["final_received_usd"]+B["final_received_usd"]+C["final_received_usd"]+D["final_received_usd"]+E["final_received_usd"]
    TotalDeposits_Top5Regions=A["final_deposits"]+B["final_deposits"]+C["final_deposits"]+D["final_deposits"]+E["final_deposits"]
    TotalReceived_Top5Regions_USDConversion=babel.numbers.format_currency(float(TotalReceived_Top5Regions), "USD", locale='en_US')
    TotalDeposits_Top5Regions_USDConversion=babel.numbers.format_currency(float(TotalDeposits_Top5Regions), "USD", locale='en_US')
    #Calculate percentage of total received and deposited transactions for top 5 regions
    Top5_VS_TotalReceived=(TotalReceived_Top5Regions/SUM_Received_funds)
    Top5_VS_TotalDeposits=format((TotalDeposits_Top5Regions/SUM_Deposited_funds)*100,".2f")
    #insert metric columns
    metric_col0,metric_col1,metric2=st.columns(3)
    metric_col0.metric("Top Sub-regions", "5")
    metric_col1.metric("Total Cryptocurrency Value Received", TotalReceived_Top5Regions_USDConversion)
    with metric2:
        percent_metric="{:.0%}".format(Top5_VS_TotalReceived)
        st.metric(" Market Share of Total Worldwide Value Received", percent_metric)
    #interpredation bodytext
    st.write("<div style='text-align:justify'> ""\n"
             "Eastern Asia, Northern America, Eastern Europe, Latin America and the Caribbean as well as Western Europe make "
             "up the top 5 sub-regions with the largest total received value. Together they make up $17,575,237,887,498.85, which "
             "is 59.43% of the total received funds from all sub-regions. The United States ranks 1st for the nation with largest volume"
             " of cryptocurrency value received. The transactions in the United States accrue to approximately $3.07 trillion."
             ,unsafe_allow_html=True)
    "\n"
    #_____________________insert figure button_______________
    PlotA_button=st.expander(label="figures 1.0 - 1.B : Sub-region, Country Total Received and Deposits Transactions")
    PlotA_button.write("""
        Note: Chart is interactive, select transaction type for comparison, Zoom in for low volume data points
        
        figures 1.0 : Data transactions  
        
        figures 1.A : Sub-region total Received and Deposits 
        
        figures 1.B : Country total Received and Deposits 
        
        Datasource: Chainalysis
        
        Technologies: PyCharm, Python; plotly express, pandas, streamlit """)
    st.write("____")
    #recieved
    st.subheader("The Sub-region in the Top 5 with Most Distributed Value Received per Country During  2019 - 2022")
    received_TotalTransac_plot0=px.histogram(df,x="final_sub_region" ,y="final_received_usd", color="final_country",
                                             title="Received Funds vs. Sub-Region per Country | Mar '19 - Apr '22",width=1360, height=500)
    received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)',xaxis={'categoryorder':'total descending'})
    received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)")
    received_TotalTransac_plot0.update_xaxes(title="Sub-Region")
    st.plotly_chart(received_TotalTransac_plot0)
    #deposits
    "\n"
    #interpredation bodytext
    st.write("<div style='text-align:justify'> ""\n"
             "The sub-region of Latin America and the Caribbean is the 4th largest sub-region based on its volume of value received "
             "More importantly, the sub-region displays a volume that is more evenly distributed among all countries compare to other sub-regions "
             "in the selected top 5. Among all 30+ nations, Argentina and Brazil are responsible for majority of the value received in the region, "
             "which accounts for a total of approximately 1.53 trillion dollars. It is no surprise Latin America ranks 4th as many of these nations "
             "utilize cryptocurrency to transact internationally for remittance and other commercial use cases. Aside from El Salvador adopting Bitcoin "
             "as a legal tender, the sub-region accounts for $134 billion in remittance according to Statista."
             ,unsafe_allow_html=True)
    "\n"
    "\n"
    #deposite
    st.subheader("Top 2 Sub-regions with the Least Deposits per Country During  2019 - 2022")
    deposits_TotalTransac_plot0=px.histogram(df,x="final_sub_region" ,y="final_deposits", color="final_country",
                                             title="Deposits vs. Sub-Region per Country | Mar '19 - Apr '22",width=1360, height=500)
    deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)',xaxis={'categoryorder':'total ascending'})
    deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposit Transactions ($)")
    deposits_TotalTransac_plot0.update_xaxes(title="Sub-Region")
    st.plotly_chart(deposits_TotalTransac_plot0)
    "\n"
    #interpredation bodytext
    st.write("<div style='text-align:justify'> ""\n"
             "Although North America leads in most value deposits, Micronesia and Polynesia ranks as top two sub-region with least cryptocurrency value deposits "
             "French Polynesia and Guam together accumulate for approximately $611,924 in deposits."
             ,unsafe_allow_html=True)
    "\n"
    #_____________________insert figure button_______________
    PlotB_button=st.expander(label="figures 2.0 - 2.A : Sub-region Total Received and Deposits Transactions per country")
    PlotB_button.write("""
        Note: Chart is interactive, select country for comparison, Zoom in for low volume data points
        
        figures 2.0 : Received Funds vs. Sub-region per country 
        
        figures 1.A : Deposits Funds vs. Sub-region per country   
        
        Datasource: Chainalysis
        
        Technologies: PyCharm, Python; plotly express, pandas, streamlit """)
    st.write("___")
    #_________________________________Create/Display DF for Eastern Asia_____________________________________________________
    Eastern_Asia_Df=df.loc[df["final_sub_region"]=="Eastern Asia"]
    #st.dataframe(Eastern_Asia_Df)
    #_________________________________Visulization line charts______________________________________________________________
    st.subheader("2020 - 2021 Led to an Increase of Cryptocurrency Value Received")
    #EasternAsia_Recieved
    EasternAsia_Received_TotalTransac_plot0=px.line(Eastern_Asia_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                                    title="Eastern Asia: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
    EasternAsia_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    EasternAsia_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
    EasternAsia_Received_TotalTransac_plot0.update_xaxes(showgrid=False,title="Date")
    st.plotly_chart(EasternAsia_Received_TotalTransac_plot0)
    #EasternAsia_Deposits
    EasternAsia_Deposits_TotalTransac_plot0=px.line(Eastern_Asia_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                    title="Eastern Asia: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
    EasternAsia_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    EasternAsia_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
    EasternAsia_Deposits_TotalTransac_plot0.update_xaxes(showgrid=False,title="Date")
    #st.plotly_chart(EasternAsia_Deposits_TotalTransac_plot0)
    #_________________________________Create/Display DF for North America_____________________________________________________
    Northern_America_Df=df.loc[df["final_sub_region"]=="Northern America"]
    #Northern_America_Df
    #_________________________________Visulization line charts______________________________________________________________
    #NorthAmerica_Recieved
    NorthAmerica_Received_TotalTransac_plot0=px.line(Northern_America_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                                     title="North America: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
    NorthAmerica_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    NorthAmerica_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
    NorthAmerica_Received_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
    st.plotly_chart(NorthAmerica_Received_TotalTransac_plot0)
    #NorthAmerica_Deposits
    NorthAmerica_Deposits_TotalTransac_plot0=px.line(Northern_America_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                     title="North America: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
    NorthAmerica_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    NorthAmerica_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
    NorthAmerica_Deposits_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
    #st.plotly_chart(NorthAmerica_Deposits_TotalTransac_plot0)
    #interpredation bodytext
    st.write("<div style='text-align:justify'> ""\n"
             "When looking at the biggest sub-region for value received, China appears to be the country with the largest volume of "
             "received transactions over the given time period. Evidence of seasonality can be observed as the volume of transactions increases right before and "
             "during the Bitcoin Halving. Between March, 2019 and Oct 2020, China shows a relatively constant trend. "
             "We see a significant positive trend during Oct 2020 and May 2021, resulting to an 8.2 multiple. The volume of received transactions "
             "jumped from 30.53 billion dollars to 251.43 billion dollars. Soon after, we see a tremendous bull-back as low as 20.32 billion dollars. "
             "The Republic of Korea, Japan, Taiwon followed the China trend with a much lower volume.",unsafe_allow_html=True)
    "\n"
    #interpredation bodytext
    st.write("<div style='text-align:justify'> ""\n"
             "United States leads in volume of value received within North America in the given time period. The volume remains "
             "predictably constant for most of the time period until Oct 2020, where the volume increases from 29.55 billion dollars to 337.84 billions dollars in May 2021."
             "The total received funds increased by a multiple of 11.43. This is a significant increase in less than 12 months. Canada mimics the trend of the United States "
             "with a lower volume. Bermuda remained constant with no noticeable improvement in value received.",unsafe_allow_html=True)
    "\n"
    #_____________________insert figure button_______________
    PlotC_button=st.expander(label="figures 3.0 - 3.A : Eastern Asia and Northern America Monthly Value Received per Country")
    PlotC_button.write("""
        Note: Chart is interactive, select country for comparison, Zoom in for low volume data points
        
        figures 3.0 : Eastern Asia: Monthly Value Received Per Country
        
        figures 3.A : Northern America: Monthly Value Received Per Country   
        
        Datasource: Chainalysis
        
        Technologies: PyCharm, Python; plotly express, pandas, streamlit """)
    st.write("___")

    #_________________________________Create/Display DF for Eastern Europe_____________________________________________________
    Eastern_Europe_Df=df.loc[df["final_sub_region"]=="Eastern Europe"]
    #Eastern_Europe_Df
    #_________________________________Visulization line charts______________________________________________________________
    #EasternEurope_Recieved
    EasternEurope_Received_TotalTransac_plot0=px.line(Eastern_Europe_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                                      title="Eastern Europe: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
    EasternEurope_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    EasternEurope_Received_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
    EasternEurope_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
    #st.plotly_chart(EasternEurope_Received_TotalTransac_plot0)
    #EasternEurope_Deposits
    EasternEurope_Deposits_TotalTransac_plot0=px.line(Eastern_Europe_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                      title="Eastern Europe: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
    EasternEurope_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    EasternEurope_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
    EasternEurope_Deposits_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
    #st.plotly_chart(EasternEurope_Deposits_TotalTransac_plot0)
    "\n"
    "\n"
    st.write("___")
    #_________________________________Create/Display DF for LatinAmerica & Caribbean_____________________________________________________
    LatinAmerica_Caribbean_Df=df.loc[df["final_sub_region"]=="Latin America and the Caribbean"]
    #LatinAmerica_Caribbean_Df
    #_________________________________Visulization line charts______________________________________________________________
    #WesternEurope_Recieved
    st.subheader("2020 - 2021 Led to an Increase of Cryptocurrency Deposits")
    LatinAmerica_Caribbean_Received_TotalTransac_plot0=px.line(LatinAmerica_Caribbean_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                                               title="Latin America and the Caribbean: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
    LatinAmerica_Caribbean_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    LatinAmerica_Caribbean_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
    LatinAmerica_Caribbean_Received_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
    #st.plotly_chart(LatinAmerica_Caribbean_Received_TotalTransac_plot0)
    #WesternEurope_Deposits
    LatinAmerica_Caribbean_Deposits_TotalTransac_plot0=px.line(LatinAmerica_Caribbean_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                               title="Latin America and the Caribbean: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
    LatinAmerica_Caribbean_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    LatinAmerica_Caribbean_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
    LatinAmerica_Caribbean_Deposits_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
    st.plotly_chart(LatinAmerica_Caribbean_Deposits_TotalTransac_plot0)
    #_________________________________Create/Display DF for Western Europe_____________________________________________________
    Western_Europe_Df=df.loc[df["final_sub_region"]=="Western Europe"]
    #Western_Europe_Df
    #_________________________________Visulization line charts______________________________________________________________
    #WesternEurope_Recieved
    WesternEurope_Received_TotalTransac_plot0=px.line(Western_Europe_Df,x="month_year" ,y="final_received_usd", color="final_country",
                                                      title="Western Europe: Monthly Value Received Per Country | Mar '19 - Apr '22",width=1360, height=500)
    WesternEurope_Received_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    WesternEurope_Received_TotalTransac_plot0.update_yaxes(title="Sum of Received Transactions ($)",showgrid=True)
    WesternEurope_Received_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
    #st.plotly_chart(WesternEurope_Received_TotalTransac_plot0)
    #WesternEurope_Deposits
    WesternEurope_Deposits_TotalTransac_plot0=px.line(Western_Europe_Df,x="month_year" ,y="final_deposits", color="final_country",
                                                      title="Western Europe: Monthly Deposits Per Country | Mar '19 - Apr '22",width=1360, height=500)
    WesternEurope_Deposits_TotalTransac_plot0.update_layout(legend_title="Country",plot_bgcolor='rgba(0,0,0,0)')
    WesternEurope_Deposits_TotalTransac_plot0.update_yaxes(title="Sum of Deposits ($)",showgrid=True)
    WesternEurope_Deposits_TotalTransac_plot0.update_xaxes(title="Date",showgrid=False)
    st.plotly_chart(WesternEurope_Deposits_TotalTransac_plot0)
    #interpredation bodytext
    st.write("<div style='text-align:justify'> ""\n"
             "The charts above express seasonality of the cryptocurrency nature led by the 2020 Bitcoin Halving. "
             "The sub-region of the Latin America and the Caribbean show significant volume distribution among all the respective "
             "countries when it comes to value received and deposits. Unlike previous value received charts, the activity level noticeable "
             "since March 1, 2019, especially in Brazil. Drastic increase in deposits begin on July 2020. Brazil, the leading country, shows significant increase from 1.11 million dollars to 4.59 million dollars. "
             "This increase is a 4.13x from its volume on July 1, 2020. Similarly, most of the countries in the sub-region experience an enormous increase in deposits. During this bull-run, some countries with"
             "increasing deposit activity are; Argentina(3.35 million dollars), Venezuela (1.51 million dollars), Mexico (1.50 million dollars), Columbia (1.11 million dollars), Chile "
             "(954.13 thousand dollars), Peru (693.92 thousand dollars), Dominican Republic (454.73 thousand dollars). A deeper look of the data of all "
             "the countries in the sub-region illustrates a widespread of the total cryptocurrency value deposits",unsafe_allow_html=True)
    "\n"
    "\n"
    st.write("<div style='text-align:justify'> ""\n"
             "In the sub-region of Western Europe, more fluctuation in the total volume of deposits is apparent from March 1, 2019 to May 1, 2021. "
             "Many peaks and valleys can be identified from December 1, 2019 to present time. May 1, 2021 and Jan 1, 2022 appears to be the peaks with the highest deposit volume "
             "for Germany as the leader. The volume rose from 555.05 thousand dollars to 4.23 million dollars in deposits. With a similar trend, Germany, France and the Netherlands "
             "are the leading nations in the sub-region of Western Europe. Luxembourg, Monaco and Liechtenstein show very little asctivity in compare to the leading countries. "
             ,unsafe_allow_html=True)
    "\n"
    #_____________________insert figure button_______________
    PlotD_button=st.expander(label="figures 4.0 - 4.A : Latin America and the Caribbean and Western Europe Monthly Deposits per Country")
    PlotD_button.write("""
        Note: Chart is interactive, select country for comparison, Zoom in for low volume data points
        
        figures 4.0 : Latin America and the Caribbean: Monthly Deposits Per Country
        
        figures 4.A : Western Europe: Monthly Deposits Per Country   
        
        Datasource: Chainalysis
        
        Technologies: PyCharm, Python; plotly express, pandas, streamlit """)
    st.write("___")
    #_____________________insert figure button_______________
    st.subheader("Catalysts Associated with the 2020 - 2021 Increase of Cryptocurrency Activity ")
    st.info("""
        * 2020 Bitcoin Halving
            * Institutional Defi activity
            * Peer-to-peer Platforms 
        * COVID-19 Pandemic 
        * Quantitative Easing (QE)
        """)
    st.write("____")
    #insert button for references
    References=st.expander(label="REFERENCES")
    References.write("""
        
        [Chainalysis ]
            (on-chain data)
        
        [Value of remittances received in selected countries in Latin America in 2021]
            (https://www.statista.com/statistics/439126/value-of-remittances-received-latin-america-by-country/#:~:text=In%202021%2C%20Mexico%20received%20nearly,amounting%20to%2015.3%20billion%20dollars.)
       
        ["Quantitative easing in the U.S. - statistics & facts"]
            (https://www.statista.com/statistics/439126/value-of-remittances-received-latin-america-by-country/#:~:text=In%202021%2C%20Mexico%20received%20nearly,amounting%20to%2015.3%20billion%20dollars.)
        
        [chainalysis.com, Chainalysis Research Team (2021), "2021 Geography of Cryptocurrency Report"]
            (https://go.chainalysis.com/2021-geography-of-crypto.html)
        
        """)
    st.write("____")
########################################################################################################################
##########################################################################################################################
########################################################################################################################
if Nav_Menu == "DeFi Liquidity Aggregator":
    #______________________________________________#insert logo/title_______________________________________________________
    st.markdown("<h1 style='text-align: center; color: white; font-size: 500%'>""LarocheNomics☕""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 200%'>""DeFi💧Aggregator ""</h1>", unsafe_allow_html=True)
    st.info("-----------------------------------------------------------------------------------------------------------------💧------------------------------------------------------------------------------------------------------------------------------------")
    #_________________________________________Call API & Set Dataframes_____________________________________________________

    def defi_His_API():
        Chart_response=r.get("https://api.llama.fi/charts")
        Defi_His_DF=Chart_response.json()
        Defi_His_DF=pd.DataFrame(Defi_His_DF)
        return Defi_His_DF
    Defi_His_DF=defi_His_API()
    Defi_His_DF["date"]=pd.to_datetime(Defi_His_DF["date"], unit="s").dt.date

    def defi_API():
        Chains_response=r.get("https://api.llama.fi/chains")
        Defi_Chains_Df=Chains_response.json()
        Defi_Chains_Df=pd.DataFrame(Defi_Chains_Df)
        return Defi_Chains_Df
    Defi_Chains_Df=defi_API()
    ETH_Ratio=Defi_Chains_Df[["name","tvl"]]
    ETH_Ratio=ETH_Ratio.loc[ETH_Ratio["name"]=="Ethereum"]

    Defi_Agr_Data0=pd.DataFrame(Defi_Chains_Df)
    Defi_Agr_Data1=Defi_Agr_Data0.loc[[0,1,3,4,5,9,23],["name","tvl"]]

    def Protocol_API():
        Protocol_response=r.get("https://api.llama.fi/protocols")
        Protocol_response_Df=Protocol_response.json()
        Protocol_response_Df=Protocol_response_Df[0:100]
        Protocol_response_Df2=pd.json_normalize(Protocol_response_Df)
        Protocol_response_Df2=pd.DataFrame(Protocol_response_Df2[["name","chain","category","tvl","change_1h","change_1d","change_7d","mcap","chains"]])
        return Protocol_response_Df2
    Protocol_response_Df2=Protocol_API()

    def Categories_API():
        cg=CoinGeckoAPI()
        DeFi_Categ=cg.get_coins_categories()
        DeFi_Categ0=pd.DataFrame(DeFi_Categ)
        return DeFi_Categ0
    DeFi_categ0=Categories_API()
    Defi_MrkCap=pd.DataFrame(DeFi_categ0[["name","market_cap","market_cap_change_24h","volume_24h"]])
    Defi_Metric=Defi_MrkCap.loc[[13],:]

    def Defi_Categories_API():
        DeFi_Categ_response=r.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-finance-defi&order=market_cap_desc&per_page=200&page=1&sparkline=false")
        DeFi_Categ3=DeFi_Categ_response.json()
        DeFi_Categ3_Norm=pd.json_normalize(DeFi_Categ3)
        DeFi_Categ3_Norm=pd.DataFrame(DeFi_Categ3)
        DeFi_Categ3_Norm=DeFi_Categ3_Norm.drop(columns=["id","symbol","image","roi","last_updated"])
        return DeFi_Categ3_Norm
    DeFi_Categ3_Norm=Defi_Categories_API()
    #___________________________________Insert Hist TVL lineChart___________________________________________________________
    Defi_His_LinePlot=px.line(Defi_His_DF, x="date", y="totalLiquidityUSD")
    Defi_His_LinePlot.update_layout( legend_title="Digital Assets", width=1300, height=550, plot_bgcolor='rgba(0,0,0,0)')
    Defi_His_LinePlot.update_xaxes(showgrid=False)
    Defi_His_LinePlot.update_yaxes(showgrid=True)
    #________________________________________________LineChart and buttin title_____________________________________________
    TVL_col0,TVL_col2=st.columns(2)
    with TVL_col0:
        Press=st.button("Total TVL (USD)")
    with TVL_col2:
        st.write("")
    st.plotly_chart(Defi_His_LinePlot)
    st.write("---")
    #________________________________________Insert Metrics in three Columns _____________________________________________________
    TVL_Metric=Defi_Chains_Df[["tvl"]].sum()
    TVL_MetricUSD=babel.numbers.format_currency(float(TVL_Metric), "USD", locale='en_US')
    Defi_MRKCAP_Metric=Defi_Metric[["market_cap"]].sum()
    Defi_MRKCAP_MetricUSD=babel.numbers.format_currency(float(Defi_MRKCAP_Metric), "USD", locale="en_US")
    ETH_Ratio_Metric=ETH_Ratio[["tvl"]].sum()

    TVL_col2, HR24_Change_col,ChainDominance_col1,Defi_ETH_Ratio_col=st.columns(4)
    with TVL_col2:
        TVL_col2.metric("TOTAL VALUE LOCKED OF ALL CHAINS (USD)", TVL_MetricUSD )
    with HR24_Change_col:
        st.metric("DeFi TOTAL MARKETCAP",Defi_MRKCAP_MetricUSD)
    with ChainDominance_col1:
        ratio_metric=format((Defi_MRKCAP_Metric[0]/TVL_Metric[0] ), ".2f")
        st.metric("MARKETCAP / TVL (ratio)",ratio_metric)
    with Defi_ETH_Ratio_col:
        ETH_Ratio_Metric=(ETH_Ratio_Metric[0]/TVL_Metric[0])
        ETH_Ratio_Metric="{:.0%}".format(ETH_Ratio_Metric)
        st.metric("ETHEREUM TVL DOMINANCE", ETH_Ratio_Metric)
    st.info("--------------------------------------------------------------------The liquidity charts below are interactive. Selected or unselect features for comparisons----------------------------------------------------------------")
    #__________________________________________________Insert Category VS. Networks_________________________________________
    AlgoStable_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Algo-Stables"]
    Bridge_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Bridge"]
    CDP_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="CDP"]
    Chain_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Chain"]
    CrossChain_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Cross Chain"]
    Derivatives_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Derivatives"]
    Dexes_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Dexes"]
    Insurance_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Insurance"]
    Lending_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Lending"]
    LiquidStaking_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Liquid Staking"]
    Options_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Options"]
    Payment_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Payment_output"]
    Privacy_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Privacy"]
    ReserveCurrency_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Reserve Currency"]
    Services_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Services"]
    Synthetics_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Synthetics"]
    Yield_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Yield"]
    YieldAggregator_output=Protocol_response_Df2.loc[Protocol_response_Df2["category"]=="Yield Aggregator"]
    #_________________________________________network output________________________________________________________________
    Algo_Plot=px.bar(data_frame=AlgoStable_output, x="name", y=["tvl","mcap"], title="Algorithmic Stablecoins Category: TVL vs. MarktCap",)
    Algo_Plot.update_layout( legend_title="Features",  plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Algo_Plot.update_xaxes(showgrid=False, title="Protocols")
    Algo_Plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Algo_Plot)
    Bridge_Plot=px.bar(data_frame=Bridge_output, x="name", y=["tvl","mcap"],title="Bridge Category: TVL vs. MarktCap")
    Bridge_Plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Bridge_Plot.update_xaxes(showgrid=False, title="Protocols")
    Bridge_Plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Bridge_Plot)
    CDP_Plot=px.bar(data_frame=CDP_output, x="name", y=["tvl","mcap"],title="Collateralized Debt Position Category: TVL vs. MarktCap",)
    CDP_Plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    CDP_Plot.update_xaxes(showgrid=False, title="Protocols")
    CDP_Plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(CDP_Plot)
    Chain_plot=px.bar(data_frame=Chain_output, x="name", y=["tvl","mcap"],title="Chain Category: TVL vs. MarktCap",)
    Chain_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Chain_plot.update_xaxes(showgrid=False, title="Protocols")
    Chain_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Chain_plot)
    CrossChain_plot=px.bar(data_frame=CrossChain_output, x="name", y=["tvl","mcap"],title="Cross Chain Category: TVL vs. MarktCap",)
    CrossChain_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    CrossChain_plot.update_xaxes(showgrid=False, title="Protocols")
    CrossChain_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(CrossChain_plot)
    Derivatives_plot=px.bar(data_frame=Derivatives_output, x="name", y=["tvl","mcap"],title="Derivatives Category: TVL vs. MarktCap",)
    Derivatives_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Derivatives_plot.update_xaxes(showgrid=False, title="Protocols")
    Derivatives_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Derivatives_plot)
    Dexes_plot=px.bar(data_frame=Dexes_output, x="name", y=["tvl","mcap"],title="Dexes Category: TVL vs. MarktCap",)
    Dexes_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Dexes_plot.update_xaxes(showgrid=False, title="Protocols")
    Dexes_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Dexes_plot)
    Insurance_plot=px.bar(data_frame=Insurance_output, x="name", y=["tvl","mcap"],title="Insurance Category: TVL vs. MarktCap",)
    Insurance_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Insurance_plot.update_xaxes(showgrid=False, title="Protocols")
    Insurance_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Insurance_plot)
    Lending_plot=px.bar(data_frame=Lending_output, x="name", y=["tvl","mcap"],title="Lending Category: TVL vs. MarktCap",)
    Lending_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Lending_plot.update_xaxes(showgrid=False, title="Protocols")
    Lending_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Lending_plot)
    LiquidStaking_plot=px.bar(data_frame=LiquidStaking_output, x="name", y=["tvl","mcap"],title="Liquid Staking Category: TVL vs. MarktCap",)
    LiquidStaking_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    LiquidStaking_plot.update_xaxes(showgrid=False, title="Protocols")
    LiquidStaking_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(LiquidStaking_plot)
    Options_plot=px.bar(data_frame=Options_output, x="name", y=["tvl","mcap"],title="Options Category: TVL vs. MarktCap",)
    Options_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Options_plot.update_xaxes(showgrid=False, title="Protocols")
    Options_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Options_plot)
    Payment_plot=px.bar(data_frame=Payment_output, x="name", y=["tvl","mcap"],title="Payment Category: TVL vs. MarktCap",)
    Payment_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Payment_plot.update_xaxes(showgrid=False, title="Protocols")
    Payment_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Payment_plot)
    Privacy_plot=px.bar(data_frame=Privacy_output, x="name", y=["tvl","mcap"],title="Privacy Category: TVL vs. MarktCap",)
    Privacy_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Privacy_plot.update_xaxes(showgrid=False, title="Protocols")
    Privacy_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Privacy_plot)
    ReserveCurrency_plot=px.bar(data_frame=ReserveCurrency_output, x="name", y=["tvl","mcap"],title="Reserve Currency Category: TVL vs. MarktCap",)
    ReserveCurrency_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    ReserveCurrency_plot.update_xaxes(showgrid=False, title="Protocols")
    ReserveCurrency_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(ReserveCurrency_plot)
    Services_plot=px.bar(data_frame=Services_output, x="name", y=["tvl","mcap"],title="Services Category: TVL vs. MarktCap",)
    Services_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Services_plot.update_xaxes(showgrid=False, title="Protocols")
    Services_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Services_plot)
    Synthetics_plot=px.bar(data_frame=Synthetics_output, x="name", y=["tvl","mcap"],title="Synthetics Category: TVL vs. MarktCap",)
    Synthetics_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Synthetics_plot.update_xaxes(showgrid=False, title="Protocols")
    Synthetics_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Synthetics_plot)
    Yield_plot=px.bar(data_frame=Yield_output, x="name", y=["tvl","mcap"],title="Yield Category: TVL vs. MarktCap",)
    Yield_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    Yield_plot.update_xaxes(showgrid=False, title="Protocols")
    Yield_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(Yield_plot)
    YieldAggregator_plot=px.bar(data_frame=YieldAggregator_output, x="name", y=["tvl","mcap"],title="Yield Aggregator Category: TVL vs. MarktCap",)
    YieldAggregator_plot.update_layout( legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    YieldAggregator_plot.update_xaxes(showgrid=False, title="Protocols")
    YieldAggregator_plot.update_yaxes(showgrid=False,title="MarktCap/TVL (USD)")
    #categRes=st.plotly_chart(YieldAggregator_plot)

    #_________________________________________ETHEREUM VS OTHER ECOSYSTEMS__________________________________________________
    ETH_plot=px.bar(data_frame=Defi_MrkCap, x="name", y=["market_cap","volume_24h"],title="ETHEREUM & OTHER ECOSYSTEMS: MARKTCAP vs. VOLUME_24HR",)
    ETH_plot.update_layout( legend_title="Features", width=1300, height=600, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    ETH_plot.update_xaxes(showgrid=False, title="Ecosystems")
    ETH_plot.update_yaxes(showgrid=False,title="MarktCap/Volume 24hr (USD)")
    st.plotly_chart(ETH_plot)

    DeFi_Categ3_plot=px.line(data_frame=DeFi_Categ3_Norm, x="name", y=["current_price","market_cap","total_volume","circulating_supply","total_supply"],title="DeFi TOKENS: LIQUIDITY vs. SUPPLY",)
    DeFi_Categ3_plot.update_layout( legend_title="Features", width=1300, height=600, plot_bgcolor='rgba(0,0,0,0)') # width=1300, height=450, title_x=0.5, title_y=.85,
    DeFi_Categ3_plot.update_xaxes(showgrid=False, title="DeFi Tokens")
    DeFi_Categ3_plot.update_yaxes(showgrid=False,title="Value in (USD)")
    st.plotly_chart(DeFi_Categ3_plot)
    "\n"
    "\n"
    st.info("-----------------------------------------------------------------Select one or multiple categories for charts to be displayed. Categorical liquidity comparisons-----------------------------------------------------------")

    "\n"
    "\n"
    #___________________________________________#Category Dropdown________________________________________________________
    Categories=["Algorithmic Stablecoins","Bridge","Collateralized Debt Position(CDP)","Chain","Cross Chain","Derivatives","Dexes","Insurance",
                "Lending","Liquid Staking","Options","Payments","Privacy","Reserve Currency","Services","Synthetics","Yield","Yield Aggregator"]

    test0=st.multiselect("DeFi CATEGORIES 👇",Categories)
    if "Algorithmic Stablecoins" in test0:
        st.plotly_chart(Algo_Plot)
    if "Bridge" in test0:
        st.plotly_chart(Bridge_Plot)
    if "Collateralized Debt Position(CDP)" in test0:
        st.plotly_chart(CDP_Plot)
    if "Chain"in test0:
        st.plotly_chart(Chain_plot)
    if "Cross Chain" in test0:
        st.plotly_chart(CrossChain_plot)
    if "Derivatives" in test0:
        st.plotly_chart(Derivatives_plot)
    if "Dexes" in test0:
        st.plotly_chart(Dexes_plot)
    if "Insurance" in test0:
        st.plotly_chart(Insurance_plot)
    if "Lending" in test0:
        st.plotly_chart(Lending_plot)
    if "Liquid Staking" in test0:
        st.plotly_chart(LiquidStaking_plot)
    if "Options" in test0:
        st.plotly_chart(Options_plot)
    if "Payments"in test0:
        st.plotly_chart(Payment_plot)
    if "Privacy" in test0:
        st.plotly_chart(Privacy_plot)
    if "Reserve Currency" in test0:
        st.plotly_chart(ReserveCurrency_plot)
    if "Services" in test0:
        st.plotly_chart(Services_plot)
    if "Synthetics" in test0:
        st.plotly_chart(Synthetics_plot)
    if "Yield" in test0:
        st.write(Yield_plot)
    if "Yield Aggregator" in test0:
        st.plotly_chart(YieldAggregator_plot)
    "\n"
    "\n"
    st.info("---------------------------------------------------------------------------------------------------------------TOP 100 PROTOCOLS--------------------------------------------------------------------------------------------------------------")
    #insert TOP 100 Protocols
    Protocol_response_Df2
    st.info("---------------------------------------------------------------------------------------------------------------------DeFi Tokens--------------------------------------------------------------------------------------------------------------------")

    DeFi_Categ3_Norm
    st.info("-------------------------------------------------------------------------------------------------DECENTRALIZED ARCHITECTURE MODELS----------------------------------------------------------------------------------------------")
    #insert Data for Web3 Model
    Model0 = Image.open("Comp of Decen sys.png")
    Model0_Expander=st.expander(label="COMPONENTS OF DECENTRALIZED SYSTEMS")
    Model0_Expander.image(Model0, use_column_width="always")

    Model1 = Image.open("CentrTODecentr.png")
    Model1_Expander=st.expander(label="FROM CENTRALIZATION TO FULL DECENTRALIZATION")
    Model1_Expander.image(Model1, use_column_width="always")

    Model2 = Image.open("web3OpenDecen.png")
    Model2_Expander=st.expander(label="WEB3 MODEL OF OPEN DECENTRALIZATION")
    Model2_Expander.image(Model2, use_column_width="always")

    Model3 = Image.open("WEB3andIntProp.png")
    Model3_Expander=st.expander(label="WEB3 MODEL OF OPEN DECENTRALIZATION UTILIZING INTELLECTUAL PROPERTY")
    Model3_Expander.image(Model3, use_column_width="always")

    Model4 = Image.open("WEB3OpenDecenNFT.png")
    Model4_Expander=st.expander(label="WEB3 MODEL OF OPEN DECENTRALIZATION FOR NFT")
    Model4_Expander.image(Model4, use_column_width="always")

    Model5 = Image.open("WEB3DecenTPro.png")
    Model5_Expander=st.expander(label="WEB3 MODEL OF DECENTRALIZATION FOR TOKENIZATION PROTOCOLS")
    Model5_Expander.image(Model5, use_column_width="always")
    st.info("---------------------------------------------------------------------------------------------------------------------------💧-------------------------------------------------------------------------------------------------------------------------")
    #insert figure button
    Defi_button=st.expander(label="REFERENCES")
    Defi_button.write("""
    
    [Coingecko API ]
        (https://www.coingecko.com/en/api/documentation)
    
    [Defi Llama API]
        (https://defillama.com/docs/api)
    
    [future.com, Miles Jennings (2022), "Decentralization for Web3 Builders: Principles, Models, How"]
        (https://future.com/web3-decentralization-models-framework-principles-how-to/)
    
    Technologies: Pycharm, CoingeckoAPI, DefiLlama API, Python;plotly express, pandas, numpy, streamlit
    """)
    st.write("___")

########################################################################################################################
########################################################################################################################
########################################################################################################################
if Nav_Menu == "SQL Business Analysis":
    # insert date and participants to of the document
    st.markdown("<h1 style='text-align: center; color: white;'>""SQL Business Analysis: LargeCo's Strategic Revenue Improvement Report""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Applied Data Structure and Database""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Guy Gnakpa ""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""April 21, 2022""</h1>", unsafe_allow_html=True)
    "\n"
    "\n"
    "\n"
    #_________________________________________Insert Report Body Text_______________________________________________________
    st.write("<div style='text-align:justify'>""\n"
             "LargeCo is a retail store based out of downtown Los Angeles California. LargeCo was established in 2017 by two founders: "
             "Robert Marshall and Louise Rise. The two founders met back in college during their senior year. After connecting for a year "
             "and finally graduating, the two newly graduates decided to team up and create a retail store that can service the local people of "
             "Los Angeles. The object was to create a paint supply retail store. This was a long difficult journey due to brand establishment and "
             "competition in the local area. After tremendous amount of work and dedication, LargeCo finally established its presence in the industry "
             "at a local level. The business model began to generate revenue and increase the number of employees. Today LargeCo has 363 employees, "
             "1362 customers and generates $673,685.60 a year. LargeCo is certainly happy with what it has accomplished thus far, however; Robert Marshall "
             "and Louise Rise would like to improve their business and increase the bottle line. The founders have decided to onboard a data scientist who "
             "can help ask the proper questions, source the data and give insightful feedback for a better strategic objective. ",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "First and foremost, it is important to understand where most of the revenue is coming from. More specific, which top 5 "
             "employees are performing the best. After some statistical enquiry, the result indicates 5 employees are responsible for "
             "$123,399.74 out of 363 employees. These top employees bring a significant amount of value to the company. Their combined "
             "efforts can help transform the LargeCo’s performance culture. With such insightful feedback, LargeCo can utilize the sales "
             "results as a standard performance metric. Lastly, LargeCo incentivize top performers to double their output in order to generate "
             "twice the value. Statistical knowledge of the top producers accompanied with one of the recommendations can help guide new metrics "
             "for a stronger bottom line. ",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "Secondly, it is important to understand which vendors are performing the least. This data can allow the company to reconsider "
             "the chosen products and it’s “shelf-life”. Statistical enquiry was completed for the top 5 vendors with the least numbers of "
             "products sold. Knowing the product is already on the shelf, a recommendation would be to put these products on sale. Another "
             "option would be to bundle these products and offer a bulk discount. This strategy would allow the shelf-life of these products "
             "to reduce. LargeCo can use this data to renegotiate the purchase structure with these respective vendors. For future inventory, "
             "perhaps LargeCo can purchase the same products at a lower price due to the response of the market. Lastly, the company can choose "
             "to pivot away from those selective vendors and acquire new vendor relationships that can reduce wholesale cost thus strengthening "
             "the bottom line. ",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "Third, it is important to understand which customers are buying the least. More specifically, who are the top 10 customers "
             "purchasing the least. Utilizing this insight, the sales team can be more attentive to these select few in order to "
             "increase the purchase order. Statistical inquiry was completed to further understand this premise. Total sales of all 10 "
             "customers with the least purchases is $27,233.84. This number is relatively low for 10 clients. A recommendation to improve "
             "the total sales of these 10 customers would be to retarget these individuals more often. Cross-sales would be a great tool to "
             "utilize in this case. To exemplify this method, a client can be offered a paint brush at a 10% discount if he or she purchased 4 "
             "gallons of paint as oppose to 2 gallons. Another recommendation would be to establish a “Membership Credit Option (MCO)” with a "
             "monthly cap for these individuals. In the inception of the program, the customer can be allowed to purchase up to $1000 worth of "
             "products if they pay 90% of the credit before day 21 of that specific month. This would include zero fees and unlimited return of "
             "products purchased in the respective month. The monthly cap can increase based on the consistency of the payback and tier of membership. "
             "MCO can be a great incentive for client retention while increasing purchases. " ,unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "Lastly, it is important to understand what methods can be implemented to increase the bottom line. Specific inquiries have "
             "resulted the following knowledge; LargfeCo has 363 employees who generate total sales of $673,685.60 from 1362 customer. "
             "Based on these figures, the first recommendations would be customer acquisition. With so many employees, LargeCo’s marketing "
             "team can allocate some efforts towards social media content marketing. This tactic can simply be short video about LargeCo and "
             "the value it brings to the Los Angeles community. Search engine optimization (SEO) would be another great way to expand their presence. "
             "Other than email marketing, a referral program can certainly help spread their services from pier to pier. Another recommendation related "
             "to the internal structure of the business, would be to standardize the sales performance metric to match the top producers. The final recommendation "
             "would be to support the new sales performance standard with more industry grade education. LargeCo can invest more in their employees by offering "
             "sales and marketing to vouches for conferences, seminars, courses and high education. These methods can help deepen the industry education of "
             "each employee, boost professional morel, create support, increase professional competition and performance standard. If many of these implimentation do not "
             "improve the revenue metric, then sourcing better talent would be the optimal decision and perhaps less expensive. Many of these tools "
             "can be utilized to improve quarterly revenue thus obtaining the yearly objective. " ,unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "LargeCo is a paint retail store that has already established a lot and made a name for itself. In such little time it has grown tremendously. "
             "The future of the company is bright. After exploring my analysis, it is with great optimism I offer the recommendations to the management team. "
             "Undoubtedly the proper questions have been asked, data has been sourced and insightful feedback has been recommended for a better strategic objective.",unsafe_allow_html=True)
    st.write("---")
    st.info("----------------------------------------------------------------------Below are the technical steps taken that resulted in the report described above--------------------------------------------------------------------------")
    "\n"
    #____________________________________________________Insert ERD_________________________________________________________
    st.write("<div style='text-align:justify'>""\n"
    "The queries began with constructing an Entity Relationship Diagram (ERD) to better visualise the databases and the given data.",unsafe_allow_html=True)
    ERD = Image.open("ERD_SQL.png")
    ERD_Expander=st.expander(label="Entity Relationship Diagram")
    ERD_Expander.image(ERD, use_column_width="always")
    #______________________________________________Insert 1st Query_________________________________________________________
    st.info("1. Who are the top 5 employee producers at LargeCo ?")
    st.info("""
    * Select TOP 5 sum(INV_TOTAL) as "Total Revenue Generated
    * From LGINVOICE inv inner join LGEMPLOYEE emp ON emp.EMP_NUM = inv.EMPLOYEE_ID
    * Group By inv.EMPLOYEE_ID
    * Order By "Total Revenue Generated" DESC;
    """)

    st.write("<div style='text-align:justify'>""\n"
             "\n"
             "a. I made a decision to fetch those 5 employees whose generated most Revenue for the company due to their interactions with the customers."
             "   It means their behaviors and attitude towards customers was excellent leading to customer retention and acquisition. Thus generated most revenue"
             "   for the company. Based on this, I decided to fetch 5 top employees who generated most revenue for the company.",unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "\n"
             "b.    This query is the best used case because it is exact fulfilling the requirements that was asked to help the company to find 5 employees. By"
             " evaluating that scenario, we see where most of the value is coming from and why. This process can be repeated quarterly to help achieve the company’s objective goal.",unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "c.	The result of the query can be seen in the table below. The table contains Employee ID with the most generated revenue parallel to each employee.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "d.    Based on the result, the company should pay close attention to the top 5 employees who are "
             "generating the most revenue. Their methods and relationship with the customers should be adopted throughout the company so "
             "that the rest of the employees can perform as well as the top producers. Such application can improve the quarterly performance of the company.",unsafe_allow_html=True)

    Q1 = Image.open("Q1.png")
    Q1_Expander=st.expander(label="Top 5 Employee Producers Query Result")
    Q1_Expander.image(Q1, use_column_width="always")
    #______________________________________________Insert 2st Query_________________________________________________________
    st.info("2. Which vendors should LargeCo reconsider working with?")
    st.info("""
    * Select TOP 5 count(line.PROD_SKU) as "Min Product from vendors", Ven.VEND_ID
    * From LGLINE line INNER JOIN LGPRODUCT pro ON line.PROD_SKU = pro.PROD_SKU
    * INNER JOIN LGSUPPLIES sup ON sup.PROD_SKU = pro.PROD_SKU
    * INNER JOIN LGVENDOR ven ON ven.VEND_ID = sup.VEND_ID
    * Group by Ven.VEND_ID
    * Order By "Min Product from vendors" ASC
    """)
    st.write("<div style='text-align:justify'>""\n"
             "a.	To establish which vendors the LargeCo should reconsider working with, I filtered the vendors who sold out the least "
             "number of products and generated less revenue for the company. The table below illustrates the vendors with the product "
             "count that have been sold and that are the lowest.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "b.	This query best answers the posed question because it highlights the vendors whose product contributes the least when "
             "it comes the bottle line. The generated insightful feedback that the company can leverage in regard to the vendors.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "c.	The screenshot below displays a table that includes the Vendor ID from the least to the most number of products sold.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "d.	Feedback can help the LargeCo better understand which vendors are performing the least. This allows flexibility "
             "for the company to restructure their wholesale contract with certain vendors or pivot towards new vendors.",unsafe_allow_html=True)
    Q2 = Image.open("Q2.png")
    Q2_Expander=st.expander(label="Vendor(s) with Least Sold Products Query Result")
    Q2_Expander.image(Q2, use_column_width="always")
    #______________________________________________Insert 3rd Query_________________________________________________________
    st.info("3. Who are the 10 customers the sales team should flag to retarget?")
    st.info("""
    * Select TOP 10 sum(INV_TOTAL) as "Most Sales Total to Customer", cus.CUST_CODE
    * From LGINVOICE inv INNER JOIN LGCUSTOMER cus ON cus.CUST_CODE = inv.CUST_CODE
    * Group by cus.CUST_CODE
    * Order By "Most Sales Total to Customer" DESC
    """)
    st.write("<div style='text-align:justify'>""\n"
             "a.	As the question indicates to select the top 10 contacts the sales department should retarget. I fetched customers based "
             "on the sales sum that are produced with each customer. That result was then filtered by customer whose sales were more than others, "
             "thus indicating who to contact next.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "b.	This query best answers the question simply because one can see the relationship between a customer and the respective total sale.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "c.	The screenshot below displays a table that contains the customer code(id) as well as total sales per customer.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "d.	Given the result, the sales team should contact these 10 customers and give them "
             "incentives to purchase more. Email marketing and promotion deals can certainly help incentivize these top 10 customers.",unsafe_allow_html=True)
    Q3 = Image.open("Q3.png")
    Q3_Expander=st.expander(label="Top 10 Customers with Low Purchase Order Query Result")
    Q3_Expander.image(Q3, use_column_width="always")
    #______________________________________________Insert 3rd Query_________________________________________________________
    st.info("4. What is your top suggestion for increasing revenues for the company?")
    st.info("""
    * Select count(*) as "Number Of Employee" from LGEMPLOYEE;
    * Select sum(INV_TOTAL) as "Total Sale generated" From LGINVOICE;
    * Select count(*) as "Total Number of customer" From LGCUSTOMER;
    """)
    st.write("<div style='text-align:justify'>""\n"
             "a.	For an impactful suggestion, I conducted 3 queries to take a look at the total number of employees, the total number of "
             "sales generated and the total number of customers. It’s clear that there are 363 employees in the company while the total number "
             "of customers is only 1362. That is most 4 customers for every employee, which is low.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "b.	These queries were chosen to best answer the question because they bring everything to a fundamental level. "
             "Understanding the total numbers of the selected attributes can allow the company to revisit the current standard performance metric.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "c.	The screenshot below displays a table that contains the total number of employees, the total amount of sales generated and the total number of customers.",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "d.	The results suggests the optimal decision for LargeCorp is to increase sales with the top employees while decreasing the total number of employees if the performance remains low.",unsafe_allow_html=True)
    Q4 = Image.open("Q4.png")
    Q4_Expander=st.expander(label="Suggestion for Increased Revenue Query Result")
    Q4_Expander.image(Q4, use_column_width="always")

    #insert figure button
    SQL_button=st.expander(label="REFERENCES")
    SQL_button.write("""
    
    Case Study: LargeCo Retail Business 
    
    Datasource: Provided by Dr. Henley
    
    Technologies: Pycharm, MySQLWorkbench, Python, Miro Visual Whiteboard, streamlit
    """)

########################################################################################################################
########################################################################################################################
########################################################################################################################
if Nav_Menu == "System Architecture Analysis":
    # insert date and participants to of the document
    st.markdown("<h1 style='text-align: center; color: white;'>""System Architecture and Design Analysis: Hudson Kayak Adventures""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Oumar Cisse, Sushmita Shrestha, Guy Gnakpa ""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Advanced Info Technology""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""May 26, 2022""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style= color: white; font-size: 95%;'>""</h1>", unsafe_allow_html=True)
    #insert background title and body text
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Background</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Hudson Kayak Adventures, a kayak rental that rents out, instructs individuals on how to use it and guided tours about "
             "the facility and along the river, was built by the Lanes family. Linda, who is a web designer, oversees the technical aspect "
             "of the business such as making sure that the website is up to date or creating a database to log all the information about customers "
             "that are renting a kayak. And Steve makes sure that the business is running smoothly. Reservations are entered in a loose-leaf binder, "
             "with separate tabs for each business activity. Linda uses an inexpensive accounting package to keep HKA's financial records. For quick "
             "reference, she displays kayak availability on a wall-mounted board with color-coded magnets. HKA’s inventory includes 16 rental kayaks of "
             "several types, lengths, and capacities, eight car-top carriers, and a large assortment of accessories and safety equipment. And they are "
             "thinking of adding more informational videos to make it accessible to the customers. Although the current business is working fine for now, "
             "they want to create an automated reservation process and record useful data to make good predictions or change business plan.",unsafe_allow_html=True)

    #insert problem statement title and body text
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Problem Statement</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Currently, HKA does not have a centralized repository for storing, organizing, accessing, or disseminating information. "
             "Whether it is client information, process information, company policy and procedure, or helpful reminders, the Lanes have "
             "a unique system for storing and accessing the various types of information which is printing out a list that wall-mounted "
             "on a board. Due to the various ways in which information is currently being stored and referenced throughout the office, "
             "it can take employees longer to locate the information that they need to do their job than it does to complete a task. "
             "They are some occasionally conflict where the Lanes must be at two places at one. Linda, who manages the database, has "
             "some trouble keeping up with the daily update of information. Additionally, there is not a universal method for integrating "
             "new clients or for managing cases from an administrative perspective, and, despite recent efforts to improve these mechanisms, "
             "the Lanes must rely on those old-fashioned ways to get work done. They want a system that gives daily reports, shows trends in "
             "the market and kayak management tools.",unsafe_allow_html=True)

    #insert Audience title and body text
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Audience</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "This proposal's target audience includes the company's owners, employees, and customers. An owner has full access to the "
             "detailed history of every data in this system. It compiles reservation data, kayak type data, and client data into a single "
             "data set that is sorted by reservation date. Telephone inquiries and table reservations are handled by employees. Customers "
             "enter their personal information to make a reservation and access the system's services. Both the administration and the "
             "users can see if the table is available. One of the owners, Linda, updates the data or makes improvements to the system. ",unsafe_allow_html=True)
    #_________________________insert project plan text and corresponding png____________________________#
    #insert Project Plan title and body text
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Project Plan</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "This plan shows the project timeline. The tasks are listed and the end date of each of them.",unsafe_allow_html=True)
    "\n"
    #________phase1___________#
    image1 = Image.open("systemdesign1.png")
    st.image(image1, use_column_width="always")
    st.write("""***Figure 1: phase 1*** """)
    #________phase2___________#
    image2 = Image.open("systemdesign2.png")
    st.image(image2, use_column_width="always")
    st.write("""***Figure 2: phase 2*** """)
    #________phase 3___________#
    image3=Image.open("systemdesign3.png")
    st.image(image3, use_column_width="always")
    st.write("""***Figure 3: phase 3***""")
    #________phase 4___________#
    image4=Image.open("systemdesign4.png")
    st.image(image4, use_column_width="always")
    st.write("""***Figure 4: phase 4***""")
    "\n"
    #_________________________insert Requirements Modelling ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Requirements Modeling</h1>", unsafe_allow_html=True)
    #________Outputs___________#
    st.write("**Outputs:**")
    st.info("""
    -	Employees get daily reservations 
    -	Owners get profit or losses for the business annually
    -	Customers get email notifications for upcoming appointment with HKA
    -	Owners get a quarterly report that identify changes in ordering pattern and trends
    -	Customers get the list of kayaks on hand and time when they are available for booking
    -	Owners have a daily activity report with a listing of all service transactions for the day
     """)
    #________Intputs___________#
    st.write("**Inputs:**")
    st.info("""
    -	Customers perform a payment
    -	Customers can book online appointments
    -	Employees must be able to change customer appointments
    -	Employees must enter customers’ booking when making phone call appointment
    -	Employees must be able to update information about kayak availabilities and videos
     """)
    #________Process___________#
    st.write("**Process:**")
    st.info("""
    -	System must perform a daily back up
    -	Update the financial details into the accounting software
    -	System must calculate employee salaries, bonuses and taxes related to IRS
    -	System must update available slot based on employee availabilities and kayaks
    -	System must calculate discount to customers that have been using HKA services multiple times
     """)
    #________Performance___________#
    st.write("**Performance:**")
    st.info("""
    -	Website response time must not exceed four seconds
    -	The website must support up to 20 users simultaneously
    -	Kayak and employee must be ready to welcome customers within 10 minutes of their appointment
    -	Cancel appointment by customer must be available to other customers within 10 seconds of the cancellation
     """)
    #________Controls___________#
    st.write("**Controls:**")
    st.info("""
    -	All transactions must be audit trailed
    -	Website must have a strong logon security
    -	System must have a secure electronic payment 
    -	The employee or customer can have ability to modify appointments
    -	System must be able to back-up file every week for security purposes
    -	Appointment cannot be made online unless first payment has been made
     """)
    #_________________________Insert Data Flow body text and Diagram  ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Data Flow Diagram</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Hudson Kayak Adventure's data diagram can be seen below in figure 5. The figure illustrates the inflows and outflows of "
             "the electronic data interchange (EDI). There are five entities highlighted in the illustration. The Electronic Data Interchange "
             "is the main operating system which is the circle-shaped object located at the center of the diagram. The rest of the entities are "
             "represented in rectangle-shaped objects interacting with the EDI.Depicted in distinct colors, the system is composed of five outputs "
             "seen in the green color. There are 3 inputs, which are represented in the blues arrows. ", unsafe_allow_html=True)
    "\n"
    #________DataFlowDiagram___________#
    image5=Image.open("DataFlowDiagram1.png")
    st.image(image5, use_column_width="always") #output_format="auto"
    st.write("""***Figure 5: Data Flow Diagram***""")
    "\n"
    #_________________________Insert Data Dictionary body text and Diagrams  ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Data Dictionary</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "The data dictionary of the internal system process of Hudson Kayak Adventure can be seen in figure 6 below. The data dictionary "
             "specifically focuses on the entity and process of the EDI in relation to the rest of the external entities. The entity table is "
             "subdivided into four attributes: entity name, description, inputs, and outputs. Each respective entity from the flow diagram is "
             "included in the data dictionary table. The description and function of each entity are also illustrated in the table before. "
             "Lastly, the data flow of each entity in respect to their relation can be seen in the table below. The process table in figure "
             "6.1 illustrates the process of the system as well as their description and order number. The relation between each entity and "
             "its function can be clearly identified in the process table.", unsafe_allow_html=True)
    "\n"
    #________DataDictionary Diagrams(entities)___________#
    image6=Image.open("DataDictionaryDiagram1.png")
    st.image(image6, use_column_width="always") #output_format="auto"
    st.write("""***Figure 6: Data Dictionary, Entities***""")
    #________(Process)___________#
    image7=Image.open("DataDictionaryDiagram2.png") #output_format="auto"
    st.image(image7, use_column_width="always")
    st.write("""***Figure 6.1: Data Dictionary, Process***""")
    #________(Database)___________#
    image8=Image.open("DataDictionaryDiagram3.png")
    st.image(image8, use_column_width="always") #output_format="auto"
    image8_1=Image.open("DataDictionaryDiagram4.png")
    st.image(image8_1, use_column_width="always") #output_format="auto"
    st.write("""***Figure 6.2: Data Dictionary, Tables for Database***""")
    "\n"
    #_________________________Insert Use Case body text and Diagrams  ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Use Case Diagram</h1>", unsafe_allow_html=True)
    st.write("<div style='text-align:justify'>""\n"
             "Below in figure 7, the use case diagram shows the relationship between customers, staff(employee), and administration. "
             "All personnel entities are represented in the green stick figure objects while their function is represented in the respective arrows. "
             "The function of employees and admin can overlap while the function of customers does not. The function and process of the system is "
             "represented in the circular objects and located at the center of the respective arrows.", unsafe_allow_html=True)
    "\n"
    #________(insert use case diagram)___________#
    image9=Image.open("UseCaseDiagram.png")
    st.image(image9, use_column_width="always") #output_format="auto"
    st.write("""***Figure 7: Use Case Diagram***""")
    #_________________________Insert Specifications body text and Diagrams  ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Specifications</h1>", unsafe_allow_html=True)
    #________insert body text ___________#
    st.write("<div style='text-align:justify'>""\n"
             "\n"
             "***Management Summary***: Hudson Kayak Adventures is going to benefit from a completely new website where customers can make "
             "reservations to rent kayaks. The project cost will not be significant as Linda is a web designer and will be helping with "
             "the construction of the new website. With Linda and the two developers, the timeline for this project should take three months."
             "\n"
             "\n"
             "***System Components***: The user interface will be colorful, user-friendly, and contain photos of what kind of services we provide. "
             "We will use Microsoft Azure to buy licenses for Microsoft Teams and Outlook so that the employees and the owners can communicate freely. "
             "Also, create an Azure database that Linda will update. Files will be stored on the local computer that only an authorized person will have access to. "
             "That will be ideal for now because the company is small. The website will perform a weekly backup of all data. Linda will perform backup for files stored "
             "on the computer at the workplace. We will get a license for QuickBooks so that the company has an audit trail for tax and payroll purposes. "
             "\n"
             "\n"
             "***System Environment***: New hardware will be needed as we will have a desktop for employees that will take orders and modify them. "
             "Security will not be an issue as we will have a different log-in of each employee and act accordingly if something goes wrong. "
             "All money transactions records will be available in QuickBooks where the appropriate person will access it. "
             "\n"
             "\n"
             "***Implementation Requirements***: As the company grows, we will have to design a training document for new hires to use as a guide. "
             "We will move all the existing data over to the new database. Linda will give training to the employees on how to use the website "
             "and complete the daily tasks that they are going to achieve. "
             "\n"
             "\n"
             """***Time and Cost Estimates***: The first month will be dedicated to the building of the website and the database. This will """
             "most likely be hard to achieve but feasible. Into the second month, we will move all require data and train employees on how "
             "to use the website. The third month will most likely be an observation month where developers will fix bugs and implement new "
             "important features. Since the company is small and has a low budget, continuous delivery will be costly as it can take many months "
             "to get a product to market. Our website will be hosted on Azure to limit the headache of a crash or hack from an outside party.", unsafe_allow_html=True)
    "\n"
    #________specification diagram___________#
    image10=Image.open("SpecificationDiagram.png")
    st.image(image10, use_column_width="always")
    st.write("""***Figure 8: Specifications***""")
    #_________________________Insert Data Design Diagrams  ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Data Design</h1>", unsafe_allow_html=True)
    image11=Image.open("DataDesign1.png")
    st.image(image11, use_column_width="always")
    image12=Image.open("DataDesign2.png")
    st.image(image12, use_column_width="always")
    image13=Image.open("DataDesign3.png")
    st.image(image13, use_column_width="always")
    st.write("""***Figure 9: 3NF Chart***""")
    #_________________________Insert Description and Entity Relationship Diagram  ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Entity Relationship Diagram</h1>", unsafe_allow_html=True)
    #________description___________#
    st.write("<div style='text-align:justify'>""\n"
             "In figure 10 below, there is an entity relationship diagram. The diagram includes 9 entities that are connected to other "
             "respective entities based on their function and relationship. The primary key and foreign key for each entity has been illustrated. "
             "The connecting arrows help illustrate the flow of data within the system.", unsafe_allow_html=True)
    "\n"
    #________ERD Diagram___________#
    image14=Image.open("ERD.png")
    st.image(image14, use_column_width="always")
    st.write("""***Figure 10: Entity Relationship Diagram***""")
    #_________________________Insert Description and User Interface Diagram  ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>User Interface Diagram</h1>", unsafe_allow_html=True)
    #________Description___________#
    st.write("<div style='text-align:justify'>""\n"
             "The user interface diagram of kayaks for online applications is shown in Figure 11, which comprises sign-in, profile, "
             "booking, payment history, notification, account settings, and log out. The main sections of the Kayaks web application "
             "include reservations, kayaks, instructors, and customer service.", unsafe_allow_html=True)
    st.info("""
    -	Kayaks depict the size and type of individuals.
    -	Customers are guided and kayak lessons are given by instructors.
    -	Customer service provides HKA email and phone details to customers.
    -	The availability of a day and time to reserve the available slots is shown in the reservation.
     """)
    #________UID Diagram___________#
    image15=Image.open("UserInterfaceDiagram.png")
    st.image(image15, use_column_width="always")
    st.write("""***Figure 11: User Interface Diagram***""")
    #_________________________Insert Body text for System Architecture ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>System Architecture</h1>", unsafe_allow_html=True)
    #________Body Text___________#
    st.write("<div style='text-align:justify'>""\n"
             "A study of day-to-day business functions, talking to users at all levels, and focusing on operational feasibility issues "
             "is the key answer to how to describe the culture of the organization. The Lanes love outdoor activities and rely on mouth-to-mouth "
             "advertisements for years. They are doing good in terms of making money and customers happy, but they just have an issue with the "
             "technical part of the business which we will provide for them. As the database and software were designed, it was made sure that "
             "there is room for scalability in case the company expands in the upcoming years. No data will be able to be lost and the records "
             "will be kept for future implementation. The integration will not be challenging as Linda has enough technical knowledge to ensure "
             "that all employees are getting their questions answered to make the transition smoother. Training will also be provided. Every "
             "employee will have an ID number and their passwords for desktop login and website. That way, we will track every employee if "
             "something goes missing. The employee will be told to never share their info with other employees.", unsafe_allow_html=True)
    #_________________________Insert Body text for Project Monitoring and Control Plan____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Project Monitoring and Control Plan</h1>", unsafe_allow_html=True)
    #________Body Text___________#
    st.write("<div style='text-align:justify'>""\n"
             "The changes made to the project towards the end of the semester played in our favor. Originally, we were given a short period of time "
             "to deliver the project proposal by the semester and we were racing against the clock to meet it. Between correcting our mistakes from "
             "the past deliveries and planning to work on the next, the workload was a little big and there was no time to entirely grasp the fundamentals "
             "of the lessons taught. With the change of schedule, we were allowed to make mistakes and correct those mistakes before moving onto the next chapter. "
             "The quality of the proposal looked so much better as we were dedicating a large amount of our time to this project as we will use those skills in our future jobs. "
             "The risk of failure was significantly reduced to a minimum as the team were preparing the best version of HKA proposal to present at the end of the semester. "
             "The risk of success was significantly up by those changes and the team felt really good about it.", unsafe_allow_html=True)
    #_________________________Insert Body text and Diagram for System Mockup: Related Tables, Data Types, Relationships____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>System Mockup: Related Tables, Data Types, Relationships</h1>", unsafe_allow_html=True)
    #________Body Text___________#
    st.write("<div style='text-align:justify'>""\n"
             "\n"
             "\n"
             "In ***figures 12 – 13***, Access was utilized to create a prototype for the new information system. As illustrated, the prototype "
             "matches the logical design models as well as the supporting details in the data dictionary. Access does a great showcasing "
             "the relationship between the different entities. In figure 15, the Employee entity has two foreign keys, Title_ID and Address_ID. "
             "Similarly, the Address entity has two foreign keys, City_ID and Stat_ID. The Customer entity has a foreign key as Address_ID while "
             "the Reserve entity has Customer_ID and Inventory_ID. Lastly, the Payment entity has Reservation_ID as its foreign key. "
             "\n"
             "\n"
             "***Figure 13*** displays the related tables and data types. Each table represents an entity with its respective primary key and "
             "foreign key. Each table also includes some sample data and functionality. In the tables, the entities are represented in "
             "the red highlight while the primary keys are represented in yellow. For a logical flow of the entities and data, please "
             "follow the relationship diagram (figure 12) rather than figure 13.", unsafe_allow_html=True)
    "\n"
    #________System Mockup Relationship Diagram___________#
    image16=Image.open("SystemMockupRelationships.png")
    st.image(image16, use_column_width="always")
    st.write("""***Figure 12: System Mockup Relationships***""")
    #________System Mockup Table and Data___________#
    image16=Image.open("SystemMockupRelationships2.png")
    st.image(image16, use_column_width="always")
    image17=Image.open("SystemMockupRelationships3.png")
    st.image(image17, use_column_width="always")
    st.write("""***Figure 13: System Mockup Related Tables & Data Type***""")
    #_________________________Insert Body text and Diagram for System Mockup: Six Queries Utilizing Relating Tables ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>System Mockup: Six Queries Utilizing Relating Tables</h1>", unsafe_allow_html=True)
    #________Body Text___________#
    st.write("<div style='text-align:justify'>""\n"
             "We have made 6 queries from our database. The above image shows the different queries that we have conducted. "
             "The first query is related to the list of employees that were employed before 2018. The second one is the query of all employees "
             "that the last name is “Walker”. As of right now, we only have one result to show for. The third one is the list of inventories "
             "that can fit more than 2 people. As of right now, the query shows that we only have 4 on hands. The fourth image shows the "
             "query of all customers that last name is “Smith”. The reservation query is sorted by descending according to the Reservation_ID. "
             "The last query is related to all the payments that amount is greater than $300.", unsafe_allow_html=True)
    "\n"
    #________System Mockup Queries___________#
    image18=Image.open("SystemMockupQueries1.png")
    st.image(image18, use_column_width="always")
    image19=Image.open("SystemMockupQueries2.png")
    st.image(image19, use_column_width="always")
    st.write("""***Figure 14: System Mockup Six Queries***""")
    #_________________________Insert Body text and Diagram for System Mockup: Four Forms ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>System Mockup: Four Forms</h1>", unsafe_allow_html=True)
    #________Body text___________#
    st.write("<div style='text-align:justify'>""\n"
             "From our database design, we have made four forms. The customer will be able to enter their information when creating a "
             "profile as the figure below shows it. A manager will be able to create an account for an employee and create a reservation "
             "for a customer. The design was made for either customer and employee to have an easy and simple UI to make the daily activities easier.", unsafe_allow_html=True)
    "\n"
    #________Four Form Diagram___________#
    image20=Image.open("SystemMockup4Form1.png")
    st.image(image20, use_column_width="always")
    image21=Image.open("SystemMockup4Form2.png")
    st.image(image21, use_column_width="always")
    st.write("""***Figure 15: System Mockup Four Forms***""")
    #_________________________Insert Body text and Diagram for System Mockup: Four Reports ____________________________#
    st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>System Mockup: Four Reports</h1>", unsafe_allow_html=True)
    #________Body text___________#
    st.write("<div style='text-align:justify'>""\n"
             "Figure 16 shows the reports for the following: customer employee, reservation and payment. As displayed the customer report "
             "represents a small portion of Hudson Kayak Adventure’s clientele. The customers are stored in the internal database. "
             "The information for each customer is specific and associated with their respective Customer_ID. The employee report "
             "represents the staff who work for Hudson Kayak Adventure. Some of the employees' responsibilities are to service the "
             "customers by making reservations, updating reservations and cancelling reservations. Like the customer report, the "
             "employee’s information is stored in the internal database. The information for each employee is specific and associated "
             "with their respective Emloyee_ID. Reservation report shows the internal database of the reservations initiated by the "
             "employee that is correlated to the respective customer. Each reservation is associated to the Customer_ID and Reservation_ID. "
             "The payment report shows each capital settlement based on the reservation. As illustrated, the payments are associated "
             "to the Reservation_ID. The report also shows an aggregate value of all the payments of $21,300. ", unsafe_allow_html=True)
    "\n"
    #________Four Reports Diagram___________#
    image22=Image.open("SystemMockup4Reports1.png")
    st.image(image22, use_column_width="always")
    image23=Image.open("SystemMockup4Reports2.png")
    st.image(image23, use_column_width="always")
    st.write("""***Figure 16: System Mockup Four Reports***""")
    #_________________________Insert expander Button for References ____________________________#
    references_expander=st.expander(label="Expand for References")
    references_expander.write("""
    Case Study: Hudson Kayak Adventures
    
    Data Source: Arbitrary strings and integers
    
    Author(s): Streamlit Project: Guy Gnakpa | case: Guy Gnakpa & other mentioned in the title
    
    Technologies: Microsoft Project, Microsoft Visio, Microsoft Excel, Microsoft Word, Discord, Streamlit library
    """)
########################################################################################################################
########################################################################################################################
########################################################################################################################
if Nav_Menu == "Financial & Marketing Analysis":
    # insert title
    st.markdown("<h1 style='text-align: center; color: white;'>""ABC Corp: Sales and Marketing Initiative to Increase Loyalty Membership Card in Low-Income Communities.""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Human Behavior Organization ""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Guy Gnakpa ""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""June 16, 2022""</h1>", unsafe_allow_html=True)
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    #______________________________________________# insert subheaders _______________________________________________
    col1, col2, col3=st.columns(3)
    with col1:
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Date:""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""To:""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""From:""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Subject:""</h1>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""June 16, 2022""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Sr. Manager of Sales and Marketing ""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Guy Gnakpa, Sales and Marketing Associate""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Financial Analysis report of Sales and Marketing Initiative to Increase "
                    "Loyalty Membership card in Low-income Communities ""</h1>", unsafe_allow_html=True)
    #________________________________________________# insert Body text ________________________________________________________
    "\n"
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "ABC Corp is changing! The evolution of markets and regulation has changed the landscape of business. ABC Corp has recognized the "
             "opportunity in remodeling the business to prioritize people, planet and profit in that respective order. The company’s efforts to pivot "
             "its resources to adapt a triple bottle line will benefit the overall vision. More specificity, ABC Corp’s sales and marketing team is launching "
             "an initiative to increase loyalty memberships card in low-income markets. The low-income communities represent a larger untapped market for the company’s "
             "goods and services. An analysis report has been conducted to illustrate the proposal of this initiative. Consolidated balance sheet, consolidated income statement,"
             "KPI & TBL balance scorecard, executive summary cash flow statement and a swot analysis have been utilized to complete this analysis. First and foremost, it is important "
             "to highlight the problem the sales and marketing team aims to solve. On the other hand, it is also important to mention the strategies put in place to solve the problem. "
             "According to Forbes, statistics show 13.4% of US national population live below the poverty line. ABC Corp has directed its campaign to increase market shares in low-income "
             "regions that are 100-200% of the national average poverty line in the 48 contiguous states (Sale & Marketing Team, Executive Summary).  ", unsafe_allow_html=True)
    "\n"
    # insert financial statements & body text
    image1 = Image.open("povertyguideline.png")
    st.image(image1, use_column_width="always")
    st.write("""***Figure 1: poverty guideline chart*** """)
    image2 = Image.open("povertychart.png")
    st.image(image2, use_column_width="always")
    st.write("""***Figure 2: poverty line chart*** """)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "The above chart illustrates the median average income per the following percentile: 1(100%), 2(133%), 3(138%), 4(150%), 5(200%). "
             "The income represented in the line chart was obtained by calculating the median income earned within the data pool of each percentile, "
             "ex; 100% pool has a median income of $28,440 for a household of 4 (Sale & Marketing Team, Executive Summary).  The line graph indicates a "
             "positive moving average in salary as the percentile increases. The proposal to create strategies that are ethical, creative, and mutually beneficial "
             "is important for the corporate’s initiative and customer retention. ABC Corp can market its membership card at each average income level starting with $28,440. "
             "The goal is to reduce barrier of entry for the loyalty membership card. Although a current average reward member has an income of $85,000, ABC Corp understands the "
             "corporate responsibility it must hold. Their efforts to solve this problem includes, targeting the unbanked, individuals with no internet access or smart phones. The "
             "mentioned limitations have urged ABC Corp to utilize a combination of direct marketing, indirect marketing, social media influencers, school and commercial partnerships "
             "to make it more inclusive for low-income communities. This will allow ABC Corp to give back and increase market shares while accomplishing its corporate responsibility to the "
             "people, planet profit. Secondly, new processes of the vision with measurable indicators have been put in place. Supporting documents such as financial reports, KPI scorecard and "
             "executive documentation are the specific tools that demonstrates the changes ABC Corp has commenced under its proposal. The company’s financial statement from 2016 to 2018, indicate "
             "a positive growth average for gross income profit and net profit year after year (Sale & Marketing Team, Executive Summary). ", unsafe_allow_html=True)
    "\n"
    # insert financial statements & body text
    image3 = Image.open("Sale&MrktBarChart.png")
    st.image(image3, use_column_width="always")
    st.write("""***Figure 3: Gross Income & Net Profit*** """)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "A bar chart has been provided for further support. A positive correlation exists between gross income per year and net "
             "profit per year. As the year increase so does the value of gross income. Similar behavior is evident in the relationship "
             "of net profit and year. Aside from profit, operating expenditure has also increased by 11% from 2017 to 2018 (Sale & Marketing "
             "Team, Executive Summary). The increase in operating cost can be attributed to an increase in salary and advertising expense. ABC Corp. "
             "hired more individuals to support the TTL efforts and objectives. As proposed, members of specific communities have been onboarded to collaborate "
             "and execute direct and indirect marketing strategies. Further, incentives like business conference vouchers and a hybrid system have been introduced "
             "to the organization body. Such efforts have helped mitigate the company’s risk of high turnover of the sales team while opening opportunities in new market "
             "segments (Sale & Marketing Team, SWOT Analysis). The new hiring initiative has increased employee diversity and strengthen the company culture. Advertising "
             "expense is another important variable when evaluating ABC Corp’s initiative. Advertising expense grew only by 1.066 percent from $7500 to $8000 between 2017 "
             "and 2018 (Sale & Marketing Team, Income Statement). The capital invested was properly allocated with the attention to increase marketing in low-income regions "
             "through fliers, newspapers and social media influencers. The use of these new marketing avenues has helped strengthened previous weaknesses of the company. ABC "
             "Corp struggled with low engagement of customers through social media and low brand image of loyalty program with new targeted leads (Sale & Marketing Team, SWOT "
             "Analysis). The ongoing efforts is to eliminate these weaknesses. Nevertheless, ABC Corp can also rely on its core strengths. The sales and marketing team have "
             "maintained the high referral rate from existing customers to their loved ones. Furthermore, the company has high retention of existing customers and membership. "
             "Another variable to observe is the total expenditure in charitable donations. For the past three years, the budget has only increased by 1.111 percent (Sale & Marketing "
             "Team, Income Statement). Looking at the data, the charitable donations expense is low in comparison to the support from those communities. More capital should be allocated "
             "towards the donation pool in the budget. Two charts are provided, one chart exemplifies the current percent growth in charitable donations. The second chart shows the yearly "
             "volume if 1.15% were to be allocated towards the budget rather than 1.11%. The larger percentage is more compatible with the support for those communities. These efforts are in "
             "place to focus on the people aspect of the initiative. ", unsafe_allow_html=True)
    "\n"
    # insert financial statements & body text
    image4 = Image.open("Sale&MrktBarChart2.png")
    st.image(image4, use_column_width="always")
    st.write("""***Figure 4: Current vs. Future Charity Donations*** """)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "Next, paying attention to the cash flow statement can help understand the financial status of ABC Corp. The company "
             "exemplifies positive cash flow in year after year. Amongst all three years, the most attractive net cash flow is evident "
             "in 2018. The cash flow grew by $4470 from 2017 to 2018 (Sale & Marketing Team, Cash Flow Statement). This growth can be "
             "attributed to strategic partnerships with schools and local retail stores to improve loyalty points redemption options. "
             "Another reason for the high increase in cash flow is the combination of client retention; high-quality customer service, "
             "and satisfaction. To further solidify its presence in the community, ABC Corp has invested in schools, foodbanks and local "
             "retail stores (Sale & Marketing Team, Executive Summary).  Similarly, there are many indicators of the triple bottom line "
             "progress in the data provided in the balance sheet. Looking at ABC Corp’s assets, liabilities and equity, one can highlight "
             "whether or not the company is fulfilling its social corporate responsibility. ABC Corp has increased its assets and collecting "
             "its account receivables. The line chart below indicates the positive trend in accounts and other receivables while the pie chart "
             "showcases the increase of total assets after expenses on a yearly base.", unsafe_allow_html=True)
    "\n"
    # insert financial statements & body text
    image5 = Image.open("AssetsAccRec.png")
    st.image(image5, use_column_width="always")
    st.write("""***Figure 5: Account Receivables & Total Assets*** """)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "Based on the balance sheet we can also conduct an analysis that promotes an increase in non-current assets. The total property, "
             "building and equipment budget has seen a tremendous capital allocation from 2017 to 2018 (Sale & Marketing Team, Balance Sheet). "
             "The budget grew by $5,974 due to new hired employees, equipment and a more efficient building utilization. The increased budget gives "
             "flexibility to the sales and marketing team to explore new opportunities with packaging suppliers who are sustainability-centric. Sustainable "
             "packaging along with pro-rata coupon accounting have significantly reduced the dependency of paper-based marketing campaigns. These key performance "
             "indicators are geared to benefit the people and planet in the short term then profit in the long run. ABC Corp’s total liability has increased year after "
             "year; however, the long-term debt has subsided from 2017 to 2018 (Sale & Marketing Team, Balance Sheet). The savings in long-term liability can be associated "
             "with the company’s partnership with schools, brick-and-mortar and recreation facilities. Many of these partnerships have helped facilitate the growth of the marketing "
             "campaigns and reduced operating hours for the headquarter. Knowing the grand corporate social responsibility, the company needed to improve its limited diversity of market segments. "
             "ABC Corp has been reinvesting the retained profit back into its triple bottom line initiative. Lastly, the KPI and triple bottom line balanced scorecard is included below to illustrate "
             "the goal the sales and marketing team has planned for the coming year.", unsafe_allow_html=True)
    "\n"
    # insert KPI/TPL card & body text
    image6 = Image.open("KPI TPL card.png")
    st.image(image6, use_column_width="always")
    st.write("""***Figure 6: KPI and Triple Bottom Line(TBL) balanced scorecard*** """)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "ABC Corp’s efforts to further achieve its corporate responsibility can be seen in the representation above. The goals "
             "for 2021 under each respective P’s of the triple bottom line is clear in the chart (Sale & Marketing Team, KPI and etc..). "
             "Under the category of people, ABC Corp should increase its partnerships with young social media influencers. With an increase of "
             "10 influencers by 2021, this will positively impact the marketing endeavors while giving back to young individuals in the community. "
             "The outcome can be measured monthly or quarterly based on the number of inquiries for brand ambassador. Next, eliminating paper-based "
             "marketing should be a priority for 2021. The goal is to bring the usage of paper-based marketing to a zero percent capacity. The progress "
             "of this goal can be measured by calculating the over-all expenses related to paper-based marketing. The lower the expense, the less likely the "
             "paper-based marketing is utilized. This major change will first benefit the planet due to sustainability practices. In addition, this course of "
             "action will reduce expenses and potentially increase net income. Lastly, ABC Corp plans on doubling its yearly retention of the loyalty membership "
             "card. Its membership program should increase by 100% (Sale & Marketing Team, KPI and etc..). The progress can be measured by calculating the reoccurring "
             "customers with membership. By doubling the members, the sales and marketing team in turns doubles its membership revenue. All three examples showcase ABC "
             "Corp’s vision for the upcoming year in continuing its corporate social responsibility. By identifying a problem, analyzing financial reports, and strategizing "
             "for solutions, ABC has a better direction with its commitment to the corporate social responsibility initiative. The focus on people, planet and profit benefits "
             "both, the moral responsibility and the economic opportunity of the business.", unsafe_allow_html=True)
    "\n"
    # insert conclusion body text
    st.write("""Sale & Marketing Team, Southern New Hampshire University 
    MBA 500 Project Two, Consolidate Balance Sheet from
    Sales and Marketing Department, ABC Corp.
    Consolidated Balance Sheet
    Sale & Marketing Team, Southern New Hampshire University
    MBA 500 Project Two. Consolidated Cash Flow statement 
    from Sales and Marketing Department, ABC Corp. 
    Consolidated Cash Flow Statement
    Sale & Marketing Team, Southern New Hampshire University 
    MBA 500 Project Two, Consolidated Income statement,
    from Sales and Marketing Department, ABC Corp.
    Consolidated Income Satement
    Sale & Marketing Team, Southern New Hampshire University 
    MBA 500 Project Two, KPI and Triple Bottom Line Balance 
    scorecard, from Sales and Marketing Department, ABC Corp.
    KPI and Triple Bottom Line balance Scorecard 
    Sale & Marketing Team, Southern New Hampshire University 
    MBA 500 Project Two, Marketing and Sales Executive Summary, from Sales and 
    Marketing Department, ABC Corp. """)

    #insert financial statements
    Fin_State_Model0 = Image.open("balance sheet.png")
    Fin_State_Model0_Expander=st.expander(label="Consolidated Balance Sheet")
    Fin_State_Model0_Expander.image(Fin_State_Model0, use_column_width="always")

    Fin_State_Model1 = Image.open("cash flow statement.png")
    Fin_State_Model1_Expander=st.expander(label="Consolidated Cash Flow Statement")
    Fin_State_Model1_Expander.image(Fin_State_Model1, use_column_width="always")

    Fin_State_Model0 = Image.open("income statemetments.png")
    Fin_State_Model0_Expander=st.expander(label="Consolidated Income Statemetment")
    Fin_State_Model0_Expander.image(Fin_State_Model0, use_column_width="always")
    st.write("___")

    #insert reference button
    Fina_Ana_button=st.expander(label="Case Study References")
    Fina_Ana_button.write("""
    Case Study: ABC Copr Business
    
    Sale & Marketing Team, Southern New Hampshire University 
        MBA 500 Project Two, Consolidate Balance Sheet from
        Sales and Marketing Department, ABC Corp.
        Consolidated Balance Sheet
        
    Sale & Marketing Team, Southern New Hampshire University
        MBA 500 Project Two. Consolidated Cash Flow statement 
        from Sales and Marketing Department, ABC Corp. 
        Consolidated Cash Flow Statement
        
    Sale & Marketing Team, Southern New Hampshire University 
         MBA 500 Project Two, Consolidated Income statement,
        from Sales and Marketing Department, ABC Corp.
        Consolidated Income Satement
        
    Sale & Marketing Team, Southern New Hampshire University 
        MBA 500 Project Two, KPI and Triple Bottom Line Balance 
        scorecard, from Sales and Marketing Department, ABC Corp.
        KPI and Triple Bottom Line balance Scorecard 
        
    Sale & Marketing Team, Southern New Hampshire University 
        MBA 500 Project Two, Marketing and Sales Executive Summary, from Sales and 
        Marketing Department, ABC Corp. 

    Technologies: Pycharm, Microsoft Office, Miro Visual Whiteboard, Python, streamlit
    """)
########################################################################################################################
########################################################################################################################
########################################################################################################################
if Nav_Menu == "Business Ethics Analysis":
    # insert header & subheaders
    st.markdown("<h1 style='text-align: center; color: white;'>""ABC Corp: Legal and Ethical Concerns Regarding Proposal to Increase Loyalty Membership Card in Low Income Markets.""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Human Behavior Organization ""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Guy Gnakpa ""</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""June 24, 2022""</h1>", unsafe_allow_html=True)
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    #__________________________________________________insert subheaders_____________________________________________
    col1, col2, col3=st.columns(3)
    with col1:
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Date:""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""To:""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""From:""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Subject:""</h1>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""June 24, 2022""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Legal Team ""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Guy Gnakpa, Sales and Marketing Associate""</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: left; color: white; font-size: 150%'>""Legal and Ethical Concerns Regarding Proposal to Increase Membership in Low Income Markets.""</h1>", unsafe_allow_html=True)
    #_____________________________________________________Insert intro and main body texts_____________________________________________________
    "\n"
    "\n"
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "A business must learn to be flexible and adapt to changes based on the direction of the market (Hernandez, 2021, CSR Initiative Letter, p. 1). "
             "As consumer behavior evolves, supply and demand must also adjust. Furthermore, despite the size, a business must adhere to its corporate social responsibility. "
             "(Daniel G. Bachrach, John R. Schermerhorn, 2021, Ethics and Social Responsibility p.48). ABC Corp aims to demonstrate just that, by committing to its strategic initiative. "
             "The increase of membership in low-income markets is a large task; however, attainable. The initiative will highlight effective methods on how to achieve both moral responsibility "
             "and economic opportunity (Hernandez, 2021, CSR Initiative Letter, p. 1). It is often impossible to model such a business strategy without considering the legal and ethical impact "
             "on all stakeholders (Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 2). Understanding the importance of this matter has led to identifying a specific legal "
             "requirement and an ethical concern that needs to be addressed before the proposal is approved. The legal requirement will be to advertise “the truth” to the new consumers followed "
             "by reviewing the collection and use of consumer data (Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 2). Both matters will be addressed and accompanied by a "
             "recommendation to help ABC Corp achieve the vision. First, the team has recognized the proposal mentions specific claims about the benefits of the membership and the collection of "
             "personal data (Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 1). The responsibility of exercising truth in advertising will be addressed by the following: ", unsafe_allow_html=True)
    st.info("""
    •	The law 
    
    •	Why adhere to truth in advertising 
    
    •	A recommendation
    """)
    st.write("<div style='text-align:justify'>""\n"
             "The U.S Federal Trade Commission requires that all advertising be truthful and be supported by evidence.” (Hernandez, 2021, "
             "Concerns about the Marketing and Sales Proposal p. 1). The law specifies anytime an ad is on the radio, television, newspaper, "
             "or the internet, it must be truthful and not misleading. The law also indicates the content of the advertisement must be supported by "
             "facts and science. Specific to ABC Corp, advertising is the main tool for the growth of the initiative, therefore the company must adhere "
             "to the specified law. The potential advertisement headlines for the marketing team included the following language (Hernandez, 2021, CSR Initiative Letter, p. 3).:", unsafe_allow_html=True)
    st.info("""
    •	Membership pays for itself. 
    
    •	The more you buy, the more you give to your school, community, and charities.
    
    •	There is no better way to give.
    
    •	The best way to help your neighbor is to help yourself to our loyalty membership. 
    """)
    st.write("<div style='text-align:justify'>""\n"
             "Looking at the above-mentioned language, many of them can be restructured to align better with an ethical advertising "
             "practice. Knowing ABC Corp has subscribed to a “moral rights view,” the chosen slogans must mimic a more positive and "
             "transparent objective (Daniel G. Bachrach, John R. Schermerhorn, 2021, Ethics and Social Responsibility p.48). Often the "
             "communities targeted represent individuals with low education, low income and vulnerable. The significance of ethical marketing "
             "approach enables the program to behave culturally, economically, and socially appropriate for the respective communities "
             "(Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 3). The recommended slogans that would display transparency "
             "in the language and ethical framework are the following:", unsafe_allow_html=True)
    st.info("""
    •	Membership with rewards opportunity
    
    •	When using your card, a portion goes to local schools, communities, and charities.
    
    •	There are many ways to give back, the loyalty membership card is one of them.
    
    •	You can help yourself and neighbors with the loyalty membership rewards card. 
    """)
    st.write("<div style='text-align:justify'>""\n"
             "The above recommendation is well orientated with ABC Corp’s “moral rights view” and its corporate social responsibility. "
             "The change of language in the slogans address the required precision when making statements about the program’s benefits "
             "(Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 3). Each line promotes the fundamental truth of the reward opportunities. "
             "In addition, there needs to be a focus on educating the audience and consumer on reading the fine print in efforts to mitigate misinformation "
             "and promote due diligence. Focusing on non-deceptive commercial speech is another requirement that is addressed through the adjusted slogans "
             "(Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 3). Knowing the financial vulnerability of the targeted population, "
             "ABC Corp’s approach is to add value to the lives of the community. Transparency is mandatory in every form of promotion of the membership. "
             "Campaigns will be prepared with the removal of any predatory marketing practice (Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 3). "
             "The Sales and marketing team must be able to support direct or implied claims. An example of ABC Corp’s support for the first two slogans can be found in "
             "the data produced by the marketing team. In the middle-and upper-income, 27.8% of the loyalty members do not redeem their points. Many individuals benefit "
             "the most from the discount on purchases. 67% of the folks that do not redeem their points do not maximize their utility.12% of the non-redeeming member who "
             "renew end up not purchasing enough to benefit from the reward (Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 3). "
             "This data is no surprise because the team’s strengths are in annual brand analysis and research (Hernandez, 2021, SWOT analysis p. 1). "
             "Knowing this fact, the sales and marketing team has planned to prevent the “under-redemption” and “under-use” actions from being practiced "
             "in the low-income communities. Low disposable income in these selected markets already limits access to the membership program. "
             "It is in the best interest of ABC Corp to threat all the stakeholders with moral rights and ethics (Daniel G. Bachrach, John R. "
             "Schermerhorn, 2021, Ethics and Social Responsibility p.60).",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "Second, the sales and marketing team has identified ethical concern that should be addressed. The collection and use of "
             "consumer data are important ethical concerns the team has been tackling (Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 2). "
             "The responsibility of exercising ethical data collection will be addressed by looking at the following:" ,unsafe_allow_html=True)
    st.info("""
    •	The Law
    
    •	Why adhere to ethical data collection and privacy
    
    •	A recommendation
    """)
    st.write("<div style='text-align:justify'>""\n"
             "When discussing the laws of the marketplace, The Sarbanes-Oxley Act of 2020 must not be neglected. This bill came in "
             "response to the substantial number of financial scandals during the 2000’s. Many of these scandals were attempted by "
             "publicly traded companies like Enron Corporation, Tyco International and many more (Will Kenton. Sarbanes-Oxley(SOX) Act of 2002, p.1). "
             "The goal of the new regulations was to help keep investors safe from fraudulent financial practices. The act imposed strict new rules for "
             "accountants, auditors, and corporate organizations. This specific law also added new penalties for violating the securities laws (Will Kenton. "
             "Sarbanes-Oxley(SOX) Act of 2002, p.1). Although this law reigns, the more important law regarding ABC Corp’s objective is the California Consumer "
             "Privacy Act of 2018 (CCPA). This law includes a list of clauses in favor of the consumer. Some of these clauses are, “the right to know about the "
             "personal information a business collects about them and how it is shared and used, the right to delete personal information collected from them.  "
             "The right to opt-out of the sale of their personal information, and the right to non‐discrimination for exercising their privacy rights” (Will Kenton. "
             "Sarbanes-Oxley(SOX) Act of 2002, p.1). Many of these laws are in the mind of the team when constructing a viable marketing strategy. More reasons to adhere "
             "to ethical data collection and privacy is it builds trust and transparency while creating a bond between the community and corporation. Practicing ethical "
             "strategies in this arena is super important because of the economic vulnerability the demography already experiences. The company’s mortal ethical view gives "
             "it no choice but to adhere to the respective responsibilities (Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 2). A recommendation of an "
             "ethical practice is collecting only the needed data for the purpose of contacting the consumer and shipping the respective product. Furthermore, because behavioral "
             "profiling is a familiar key issue related to low-income communities, the team must use its strength in high customer satisfaction and great customer service to address "
             "this vulnerability (Hernandez, 2021, Concerns about the Marketing and Sales Proposal p. 3-4). To further assist the community, the team has decided to use culturally "
             "and linguistically curated marketing messaging respective to the socioeconomics restrictions. The objective of the initiative has led the company to focus on the "
             "following: people, planet, profit (Hernandez, 2021, CSR Initiative Letter, p. 1). ",unsafe_allow_html=True)
    "\n"
    st.write("<div style='text-align:justify'>""\n"
             "Lastly, ABC Corporate’s concerns have been identified and addressed. The sales and marketing team identified the legal "
             "requirement, truth in advertising. The team highlighted the law, its importance, and respective recommendations. Next, the "
             "team identified an ethical concern and addressed it. The collection and use of consumer data were thoroughly demonstrated through law, "
             "level of importance, and recommendations. ABC Corp is in a positive direction to complete its corporate social responsibility. More significantly, "
             "the Company will impact many communities while satisfying the bottom line (Hernandez, 2021, CSR Initiative Letter, p. 2).",unsafe_allow_html=True)

    #insert reference button
    References_button=st.expander(label="Case Study References")
    References_button.write("""
    ABC Corp. (2012). Concerns about the Marketing and Sales Proposal. Sales and Marketing Department. 
    Concerns about the Marketing and Sales Proposal Hernandez. (2021). CRS Initiative Letter. ABC Corporation. Sales and Marketing
    Department. Marketing and Sales Executive Summary
    
        
    Sale & Marketing Team, Southern New Hampshire University
    MBA 500 Project Two. Consolidated Cash Flow statement 
    from Sales and Marketing Department, ABC Corp. 
    Consolidated Cash Flow Statement
        
    Management, Daniel G. Bachrach, John R. Schermerhorn. (Acquisitions Editors) (2021). 
    Management: Ethics and Social Responsibility. Wiley Plus.
        
    Investopedia, Will Kenton (2021). Sarbanes-Oxley(SOX) Act of 2002. Sarbanes-Oxley (SOX) Act of 	2002  
        
    FTC.gov, Federal Trade commission (2021). Truth in Advertising. Truth in Advertising
    Hernandez. (2021). SWOT Analysis. ABC Corporation. Sales and Marketing
    Department. SWOT Analysis From Sales and Marketing
    
    Technologies: Pycharm, Microsoft Office, Miro Visual Whiteboard, Python, streamlit
      """)
########################################################################################################################
########################################################################################################################
########################################################################################################################
