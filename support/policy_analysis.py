# policy_analysis.py
# Data pre-processing for policy analysis visualization.

import altair as alt
import pandas as pd
import streamlit as st


def create_stacked_bar():
    # read in data as csv
    COUNTRY_VOTES = pd.read_csv("data/CountryVotesonAI.csv")
    # combine totally agree/tend agree to one agree column for user clarity
    COUNTRY_VOTES["Agree"] = (
        COUNTRY_VOTES["Tend_Agree"] + COUNTRY_VOTES["Totally_Agree"]
    )
    # combine totally disagree/tend disagree to one disagree column for user clarity
    COUNTRY_VOTES["Disagree"] = (
        COUNTRY_VOTES["Tend_Disagree"] + COUNTRY_VOTES["Totally_Disagree"]
    )
    COUNTRY_VOTES = COUNTRY_VOTES.rename(
        columns={
            "Totally_Agree": "Totally Agree",
            "Tend_Agree": "Tend Agree",
            "Tend_Disagree": "Tend Disagree",
            "Totally_Disagree": "Totally Disagree",
        }
    )

    country_selector = alt.selection_multi(
        fields=["Country"], init=[{"Country": "Hungary"}]
    )

    # transform fold is conducted so that we can utilize the stacked bar approach
    # and analyze the huge discrepanacy between what world powers think
    st.title("World Power Belief on AI Safety and Regulation")

    all_country_data = (
        alt.Chart(COUNTRY_VOTES)
        .mark_bar()
        .encode(
            x=alt.X(
                "Agree:Q",
                title="Percent Representatives that Want AI Regulation",
                scale=alt.Scale(domain=[0, 100]),
            ),
            y=alt.Y("Country:N", title="Country"),
            color=alt.condition(
                country_selector, alt.value("#714141"), alt.value("#d9d9d9")
            ),
        )
        .add_selection(country_selector)
        .interactive()
    )

    by_country2 = (
        alt.Chart(COUNTRY_VOTES)
        .transform_fold(["Agree", "Disagree"], as_=["Sentiment", "Agree/Disagree"])
        .mark_bar()
        .encode(
            x=alt.X("Country:N", title="Country"),
            y=alt.Y(
                "Agree/Disagree:Q",
                title="Is AI Regulation Needed?",
                scale=alt.Scale(domain=[0, 100]),
            ),
            tooltip=[alt.Tooltip("Country:N", title="Country")],
            color=alt.Color(
                "Sentiment:N",
                scale=alt.Scale(
                    domain=["Agree", "Disagree"], range=["#714141", "#d9d9de"]
                ),
            ),
        )
        .transform_filter(country_selector)
        .interactive()
    )

    joint_chart = all_country_data | by_country2

    st.write(joint_chart)
    st.write(
        "From the chart above we can see that nearly every major world power agrees"
        + " that AI imposes enough risk that it should be regulated. There is not one outlier nation "
        + "that does not think that AI and Robotics are begning to play in increasingly "
        + "dangerous or volatile role."
    )


create_stacked_bar()
