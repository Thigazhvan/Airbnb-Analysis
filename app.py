#Import Required Packages

import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option("display.max_column",None)
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


#Streamlit Part

st.set_page_config(layout="wide")
st.title(" :blue[AIRBNB DATA VISUALIZATION | By Thigazhvan]")
st.write("")

df = pd.read_csv("C:/Users/DELL-22/Desktop/Airbnb/Airbnb_dataset.csv")

#with st.select_slider:
tab1,tab2,tab3=st.tabs(["Home","About Project","🗃 Data Analaysis with Different Features"])
                     #styles={"nav-link": {"font-size": "18px", "text-align": "left", "margin": "-2px", "--hover-color": "#FF5A5F"},
                                #"nav-link-selected": {"background-color": "#6495ED"}}))
st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 100px;
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
        white-space: pre-wrap;
		background-color: #e8e8e8;
        color: #4f4f4f;
		border-radius: 4px 4px 0px 0px;
		gap: 10px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
        font-family: 'Courier New', Courier, monospace;
	}

</style>""", unsafe_allow_html=True)

#*********----------------------------*********


#Home Tab about Airbnb 
with tab1:
    st.title(":bar_chart:   About AirBnb-Analysis")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


    st.header("About Airbnb")
    st.image("C:/Users/DELL-22/Desktop/Airbnb/airbnb_banner.jpg")

    st.header("Introduction")
    st.write("""
    Airbnb is a global online marketplace that connects people looking for accommodations with hosts offering unique places to stay. Since its founding in 2008, Airbnb has revolutionized the travel and hospitality industry by enabling individuals to rent out their homes, apartments, or spare rooms to travelers. This peer-to-peer platform has grown to include millions of listings in over 220 countries and regions.
    """)

    st.header("How It Works")
    st.write("""
    Airbnb operates on a simple premise: hosts list their properties on the platform, and guests can book these properties for short-term stays. Here’s a step-by-step breakdown:

    1. **Hosts List Properties**: Hosts create listings for their properties, including details such as location, amenities, house rules, pricing, and availability. They can also upload photos and provide descriptions to attract potential guests.

    2. **Guests Search and Book**: Travelers search for accommodations based on their destination, travel dates, and preferences. They can filter results by price, property type, amenities, and more. Once they find a suitable listing, they can book it through the platform.

    3. **Payment and Confirmation**: Airbnb handles the payment process, collecting fees from guests at the time of booking and paying hosts after check-in. This secure payment system protects both parties and ensures a smooth transaction.

    4. **Check-in and Stay**: Guests communicate with hosts to arrange check-in details. During their stay, they can reach out to hosts for any assistance or local recommendations.

    5. **Review and Rating**: After the stay, both hosts and guests can leave reviews and ratings. This feedback system helps maintain trust and quality within the Airbnb community.
    """)

    st.header("Benefits of Using Airbnb")
    st.write("""
    - **Unique Accommodations**: Airbnb offers a wide range of lodging options, from cozy apartments and charming cottages to luxurious villas and quirky treehouses. This variety allows travelers to find accommodations that suit their tastes and budgets.

    - **Local Experiences**: Staying in an Airbnb often provides a more authentic travel experience, allowing guests to immerse themselves in local neighborhoods and cultures. Many hosts offer personalized recommendations and insider tips.

    - **Flexibility and Convenience**: With Airbnb, travelers can find accommodations for any length of stay, from one night to several months. The platform also offers flexible cancellation policies and 24/7 customer support.

    - **Cost-Effective**: Airbnb listings can often be more affordable than traditional hotels, especially for longer stays or larger groups. Additionally, guests have the option to cook their own meals, further reducing travel expenses.
    """)

    st.header("Challenges and Considerations")
    st.write("""
    - **Regulatory Issues**: Airbnb faces regulatory challenges in many cities, where local governments impose restrictions or require licenses for short-term rentals. These regulations can impact the availability and legality of Airbnb listings.

    - **Quality and Consistency**: Since Airbnb properties are individually owned and operated, the quality and consistency of accommodations can vary. It’s important for guests to read reviews and communicate with hosts to set clear expectations.

    - **Safety and Security**: While Airbnb implements measures to ensure safety, such as background checks and secure payments, guests and hosts should still exercise caution. It’s recommended to follow safety guidelines and verify the legitimacy of listings.
    """)

    st.header("Future of Airbnb")
    st.write("""
    Airbnb continues to innovate and expand its offerings. Recent initiatives include:

    - **Airbnb Experiences**: In addition to accommodations, Airbnb now offers experiences hosted by local experts. These activities range from cooking classes and guided tours to adventure sports and cultural workshops.

    - **Enhanced Cleaning Protocols**: In response to the COVID-19 pandemic, Airbnb introduced rigorous cleaning standards to ensure the safety and well-being of guests and hosts.

    - **Sustainability Efforts**: Airbnb is committed to promoting sustainable travel practices, including eco-friendly accommodations and supporting local communities.

    As the travel landscape evolves, Airbnb aims to adapt and provide meaningful, personalized experiences for its users around the world.
    """)

    st.header("Conclusion")
    st.write("""
    Airbnb has transformed the way people travel and experience new places. By leveraging technology and fostering a community-driven platform, Airbnb connects travelers with unique accommodations and local experiences, making travel more accessible, enjoyable, and diverse.
    """)

    st.markdown("Website link")
    st.button("link","https://www.airbnb.co.in/login-united-kingdom/stays")

#about the project
with tab2:
    st.title("Overview about Project")
    col1,col2 = st.columns(2,gap= 'medium')
    col1.markdown("#### :blue[Domain] : Travel Industry, Property Management and Tourism")
    col1.markdown("#### :blue[Technologies used] : Python, Pandas, Plotly, Streamlit, MongoDB")
    col1.markdown("#### :blue[Process Overview] : To analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. ")
    st.image("C:/Users/DELL-22/Desktop/Airbnb/0_bzvvyHggnVsjISds.jpg")
    
    with col2:
        st.image("C:/Users/DELL-22/Desktop/Airbnb/images.jpeg")


    st.markdown("## :violet[Work flow of Project]")

    st.subheader(" :blue[1. Data Collection:]")

    st.write("Establish a connection to the MongoDB Atlas database and retrieve the Airbnb dataset")
    
    st.subheader(" :blue[2. Data Cleaning and Preprocessing:]")

    st.write("Clean the Airbnb dataset by addressing missing values, eliminating duplicates, and adjusting data types as required. Prepare the dataset for Exploratory Data Analysis (EDA) and visualization tasks, ensuring data integrity and consistency throughout the process..")
    
    st.subheader(" :blue[3. Exploratory Data Analysis (EDA):]")

    st.write("Utilize the cleaned data to conduct an analysis and visualization of price variations across different locations, property types, and seasons. Develop dynamic plots and charts that empower users to explore trends in pricing, identify outliers, and discern correlations with other variables.")
   
    st.subheader(" :blue[4. Visualization:]")

    st.write("Leverage Tableau or Power BI to craft a comprehensive dashboard showcasing key insights derived from your analysis. Integrate various visualizations, including maps, charts, and tables, to offer a holistic perspective on the Airbnb dataset and its underlying patterns. Employ analysis techniques such as DAX (Data Analysis Expressions) to create new measures and add columns, enhancing the utility and depth of your analysis. This approach will enable a more nuanced exploration of the dataset, facilitating a richer understanding of trends and relationships within the Airbnb data.")
    
    st.subheader(" :blue[5. Geospatial Analysis:]")

    st.write("Utilize geospatial analysis to understand the geographical distribution of listings.Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations")

    st.subheader(" :blue[5. Final Output:]")
    
    st.write("The final output of my project aims to provide an easily accessible analysis of Airbnb data for clients and users, particularly those interested in tourism and hotel visits. This analysis includes features such as hotel types, average prices, minimum and maximum prices, types of rooms, available facilities, and a map for convenient exploration. By presenting this information in a user-friendly format, we aim to enhance the experience of individuals seeking accommodation, offering valuable insights into various aspects of Airbnb listings to facilitate informed decision-making for their travel plans.")

    st.markdown("Dataset link")
    st.button("link","https://docs.google.com/document/d/1SYlU0Wq4Ay-z_CTU3qviTwZd_eDp0vIB/edit")
    
#data analysis based on features
with tab3:
    st.title("Data Analaysis with Different Features")

    #setting option menu
    select = option_menu("Menu",["Price Analaysis","Geospatial Analysis","Availability Analysis","Top Insight Analysis"],
                         styles={"nav-link": {"font-size": "18px", "text-align": "left", "margin": "-2px", "--hover-color": "#FF5A5F"},
                                "nav-link-selected": {"background-color": "#6495ED"}})
    
    #Price Analysis
    #Average price Analysis
    if select=="Price Analaysis":

        st.title("Average Price Analaysis")
    
        col1,col2 = st.columns(2)
        #analysis based property types and review
        with col1:
            country = st.selectbox("select the country",sorted(df["country"].unique()))

            df1= df[df["country"]==country]
            df1.reset_index(drop=True,inplace = True)

            room_type = st.selectbox("select the RoomType",sorted(df["room_type"].unique()))

            df2= df1[df1["room_type"]==room_type]
            df2.reset_index(drop=True,inplace = True)

            df_bar = pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].mean().sort_values("price"))
            df_bar.reset_index(inplace=True)

            fig_bar = px.bar(df_bar,x="property_type",y="price",hover_data=["review_scores","number_of_reviews",],title="Property_type vs Price Analysis",color_discrete_sequence=px.colors.sequential.BuPu_r)       
            st.plotly_chart(fig_bar)

            st.write("##### :green[The chart shows the average price of different property types for a selected country and room type, along with hover data displaying average review scores and the number of reviews.]")
            st.write("##### :green[This helps identify which property types are most expensive and popular based on user ratings and review counts.]")
        
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            property_type = st.selectbox("select the Property_type",sorted(df["property_type"].unique()))

            df3= df[df["property_type"]==property_type]
            df3.reset_index(drop=True,inplace = True)

            df_pie = pd.DataFrame(df3.groupby("host_response_time")[["price","bedrooms","beds"]].mean().round(0).sort_values("price"))

            df_pie.reset_index(inplace=True)

            fig_bar = px.bar(df_pie,x="host_response_time",y="price",hover_data=["bedrooms","beds"],title="Host Response Time vs Price Analysis",color_discrete_sequence=px.colors.sequential.Agsunset_r)       
            st.plotly_chart(fig_bar)

            st.write("##### :green[The bar chart displays the average price of listings based on host response time for a selected property type, with hover data showing the average number of bedrooms and beds.]")
            st.write("##### :green[This helps identify how host response times correlate with pricing and the typical size of the properties]")
        
    

        df_do_bar= pd.DataFrame(df.groupby("cancellation_policy")[["price","beds","bedrooms"]].mean().round(0).sort_values("price"))
        df_do_bar.reset_index(inplace= True)

        fig_do_bar = px.bar(df_do_bar, x='cancellation_policy', y="price", 
                            title="Analysis based on cancellation policy", hover_data=['beds', 'bedrooms'],
        barmode='group',color_continuous_scale=px.colors.sequential.Agsunset_r)            
        st.plotly_chart(fig_do_bar)
        st.write("##### :red[The bar chart that visualizes the average price of listings based on different cancellation policies, with hover data displaying the number of beds and bedrooms.]")
        st.write("##### :red[This chart helps analyze how cancellation policies impact listing prices and provides insights into the relationship between cancellation flexibility and accommodation feature]")
    
       

        #Analysis based on Host Response Time
        col1,col2= st.columns(2)

    
        with col1:

            st.subheader("Analysis based on Host Response Time")
            hostresponsetime= st.selectbox("Select the host_response_time",df["host_response_time"].unique())

            df4= df[df["host_response_time"] == hostresponsetime]

            df_do_bar= pd.DataFrame(df4.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace= True)

            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
                                title="Maximum and Minimum nights", hover_data="price",
            barmode='group',color_continuous_scale=px.colors.sequential.Agsunset)            
            st.plotly_chart(fig_do_bar)

            st.write("#####  :violet[*This plot shows the sum of minimum and maximum nights required for different bed types.]") 
            st.write("")
            st.write("#####  :violet[*This can help to identify which bed types are associated with longer or shorter stays]")


        #Analysis based on Bed_type
        with col2:

            st.subheader("Analysis based on Bed_type")  
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

            df_do_bar_2= pd.DataFrame(df4.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())

            df_do_bar_2.reset_index(inplace= True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='Bedrooms and Bedtype accommodates',hover_data="price",
            barmode='group',color_continuous_scale=px.colors.sequential.Plasma)
           
            st.plotly_chart(fig_do_bar_2)

            st.write("##### :violet[*The bar chart displays the total number of bedrooms, beds, and accommodations for different bed types, with hover data showing the total price.]")
            st.write("##### :violet[*This helps identify how different bed types contribute to the overall capacity and pricing of the listings.]")
    

    #Geospatial Analysis
    if select=="Geospatial Analysis":
        st.title("Geospatial Analysis")
        st.write("")

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitute', color='city', size='accommodates',
                        color_continuous_scale= "rainbow",hover_name='host_neighbourhood',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
        fig_4.update_layout(width=2000,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)

        st.write("##### :blue[*The scatter map that visualizes the geospatial distribution of listings, with markers sized by accommodation capacity and colored by city, providing insights into the distribution of accommodations across different cities.]")
        
    #Availability Analysis
    if select == "Availability Analysis":
        st.title("Availability Analysis")
        
        col1,col2= st.columns(2)

        with col1:
            
            
            country= st.selectbox("Select the Country",df["country"].unique())

            df1_a= df[df["country"] == country]
            df1_a.reset_index(drop= True, inplace= True)

            property= st.selectbox("Select the Property Type",df["property_type"].unique())
            
            df2_a= df1_a[df1_a["property_type"] == property]
            df2_a.reset_index(drop= True, inplace= True)

            df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Agsunset_r)
            st.plotly_chart(df_a_sunb_30)
            
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

            df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sunb_60)

        col1,col2= st.columns(2)

        with col1:
            
            df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sunb_90)

        with col2:

            df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Inferno)
            st.plotly_chart(df_a_sunb_365)

        st.write("#### :green[The above Sunburst chart that visualizes the availability of listings for(30,60,90,365) a specific property type, further categorized by room type, bed type, and location accuracy.]")
    
        roomtype_a= st.selectbox("Select the Room Type_a", df2_a["room_type"].unique())

        df3_a= df2_a[df2_a["room_type"] == roomtype_a]

        df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df_mul_bar_a.reset_index(inplace= True)

        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='Availability based on host Response Time',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Viridis,width=1000)

        st.plotly_chart(fig_df_mul_bar_a)   

        st.write("#### :green[The grouped bar chart illustrating the availability of listings for different durations (30, 60, 90, and 365 days) based on host response time. This visualization allows for an analysis of how host response times correlate with listing availability over varying time frames, providing insights into booking trends and potential impacts on pricing strategies.]")
    
    
    #Top Insight Analysis
    if select == "Top Insight Analysis":
        Question=st.selectbox("select the Top Insight",["1.Top 10 Total Price Analysis based on Country",
                                                "2.Top 10 Total Price Analysis based on city",
                                                "3.Top 10 Total Price Analysis based on property_type",
                                                "4.Top 10 Total Price Analysis based on bed_type",
                                                "5.cancellation policy vs country",
                                                "6.Top 10 city availability_30",
                                                "7.Top 10 city availability_60",
                                                "8.Top 10 city availability_90",
                                                "9.Top 10 city availability_365",
                                                "10.Top 10 city host_response_rate",
                                                "11.Top 10 suburb weekly_price",
                                                "12.Top 10 suburb monthly_price",
                                                "13.Top 10 suburb review_scores",
                                                "14.Top 10 suburb cleaning_fee"])
        

        if Question=="1.Top 10 Total Price Analysis based on Country":
        
            df_1=pd.DataFrame(df.groupby("country")["price"].sum().reset_index().sort_values("price")).tail(10)
            df_1.reset_index(drop=True,inplace=True)

            fig_bar = px.bar(df_1,x="country",y="price",title="Country vs Totalprice")
            st.plotly_chart(fig_bar)

        elif Question=="2.Top 10 Total Price Analysis based on city":
        
            df_1=pd.DataFrame(df.groupby("city")["price"].sum().reset_index().sort_values("price")).tail(10)
            df_1.reset_index(drop=True,inplace=True)

            fig_bar = px.bar(df_1,x="city",y="price",title="city vs Totalprice")
            st.plotly_chart(fig_bar)

        elif Question=="3.Top 10 Total Price Analysis based on property_type":
        
            df_1=pd.DataFrame(df.groupby("property_type")["price"].sum().reset_index().sort_values("price")).tail(10)
            df_1.reset_index(drop=True,inplace=True)

            fig_bar = px.bar(df_1,x="property_type",y="price",title="property_type vs Totalprice",
                            barmode='group',color_discrete_sequence=px.colors.sequential.Viridis)
            st.plotly_chart(fig_bar)

        elif Question=="4.Top 10 Total Price Analysis based on bed_type":
        
            df_1=pd.DataFrame(df.groupby("bed_type")["price"].sum().reset_index().sort_values("price")).tail(10)
            df_1.reset_index(drop=True,inplace=True)

            fig_bar = px.bar(df_1,x="bed_type",y="price",title="bed_type vs Totalprice",
                            barmode='group',color_discrete_sequence=px.colors.sequential.Magma)
            st.plotly_chart(fig_bar)

        elif Question=="5.cancellation policy vs country":
        
            df_1=pd.DataFrame(df.groupby("cancellation_policy")[["country"]].value_counts().reset_index())
            df_1.reset_index(drop=True,inplace=True)
            

            fig_bar = px.bar(df_1,x="country",y="cancellation_policy",title="cancellation policy vs country",
                            hover_name='count',color_discrete_sequence=px.colors.sequential.Oranges_r)
            st.plotly_chart(fig_bar)    

        elif Question=="6.Top 10 city availability_30":
        
            df_1=pd.DataFrame(df.groupby("city")[["availability_30","availability_60","availability_90","availability_365"]].sum())
            df_1.reset_index(drop=True,inplace=True)
            df_2=pd.DataFrame(df.groupby("city")[["availability_30"]].sum().reset_index().sort_values("availability_30").tail(10))
            

            fig_bar = px.bar(df_2,x="city",y="availability_30",title="city vs availability_30",
                            color_discrete_sequence=px.colors.sequential.Reds_r)
            st.plotly_chart(fig_bar)

        elif Question=="7.Top 10 city availability_60":
        
            df_1=pd.DataFrame(df.groupby("city")[["availability_30","availability_60","availability_90","availability_365"]].sum())
            df_1.reset_index(drop=True,inplace=True)
            df_2=pd.DataFrame(df.groupby("city")[["availability_60"]].sum().reset_index().sort_values("availability_60").tail(10))
            

            fig_bar = px.bar(df_2,x="city",y="availability_60",title="city vs availability_60",
                            color_discrete_sequence=px.colors.sequential.Purples)
            st.plotly_chart(fig_bar)

        elif Question=="8.Top 10 city availability_90":
        
            df_1=pd.DataFrame(df.groupby("city")[["availability_30","availability_60","availability_90","availability_365"]].sum())
            df_1.reset_index(drop=True,inplace=True)
            df_2=pd.DataFrame(df.groupby("city")[["availability_90"]].sum().reset_index().sort_values("availability_90").tail(10))
            

            fig_bar = px.bar(df_2,x="city",y="availability_90",title="city vs availability_90",
                            color_discrete_sequence=px.colors.sequential.Purples_r)
            st.plotly_chart(fig_bar)

        elif Question=="9.Top 10 city availability_365":
        
            df_1=pd.DataFrame(df.groupby("city")[["availability_30","availability_60","availability_90","availability_365"]].sum())
            df_1.reset_index(drop=True,inplace=True)
            df_2=pd.DataFrame(df.groupby("city")[["availability_365"]].sum().reset_index().sort_values("availability_365").tail(10))
            

            fig_bar = px.bar(df_2,x="city",y="availability_365",title="city vs availability_365",
                            color_discrete_sequence=px.colors.sequential.Cividis)
            st.plotly_chart(fig_bar)

        elif Question=="10.Top 10 city host_response_rate":
        
            df_1=pd.DataFrame(df.groupby("city")[["host_response_rate","weekly_price","monthly_price","review_scores"]].sum())
            df_1.reset_index(drop=True,inplace=True)
            df_2=pd.DataFrame(df.groupby("city")[["host_response_rate"]].sum().reset_index().sort_values("host_response_rate").tail(10))
            

            fig_bar = px.bar(df_2,x="city",y="host_response_rate",title="city vs host_response_rate",
                            color_discrete_sequence=px.colors.sequential.Cividis_r)
            st.plotly_chart(fig_bar)

        elif Question=="11.Top 10 suburb weekly_price":
        
            df_1=pd.DataFrame(df.groupby("suburb")[["host_response_rate","weekly_price","monthly_price","review_scores"]].sum())
            df_1.reset_index(drop=True,inplace=True)
            df_2=pd.DataFrame(df.groupby("suburb")[["weekly_price"]].sum().reset_index().sort_values("weekly_price").tail(10))
            

            fig_bar = px.bar(df_2,x="suburb",y="weekly_price",title="suburb vs weekly_price",
                            color_discrete_sequence=px.colors.sequential.Viridis_r)
            st.plotly_chart(fig_bar)

        elif Question=="12.Top 10 suburb monthly_price":
        
            df_1=pd.DataFrame(df.groupby("suburb")[["host_response_rate","weekly_price","monthly_price","review_scores"]].sum())
            df_1.reset_index(drop=True,inplace=True)
            df_2=pd.DataFrame(df.groupby("suburb")[["monthly_price"]].sum().reset_index().sort_values("monthly_price").tail(10))
            

            fig_bar = px.bar(df_2,x="suburb",y="monthly_price",title="suburb vs monthly_price",
                            color_discrete_sequence=px.colors.sequential.Viridis)
            st.plotly_chart(fig_bar)

        elif Question=="13.Top 10 suburb review_scores":
        
            df_1=pd.DataFrame(df.groupby("suburb")[["host_response_rate","weekly_price","monthly_price","review_scores"]].sum())
            df_1.reset_index(drop=True,inplace=True)
            df_2=pd.DataFrame(df.groupby("suburb")[["review_scores"]].sum().reset_index().sort_values("review_scores").tail(10))
            

            fig_bar = px.bar(df_2,x="suburb",y="review_scores",title="suburb vs review_scores",
                            color_discrete_sequence=px.colors.sequential.Magma_r)
            st.plotly_chart(fig_bar)

        elif Question=="14.Top 10 suburb cleaning_fee":
        
            df_1=pd.DataFrame(df.groupby("suburb")[["cleaning_fee"]].sum().reset_index().sort_values("cleaning_fee").tail(10))
            df_1.reset_index(drop=True,inplace=True)
        
            fig_bar = px.bar(df_1,x="suburb",y="cleaning_fee",title="suburb vs cleaning_fee",
                            color_discrete_sequence=px.colors.sequential.Magma)
            st.plotly_chart(fig_bar)