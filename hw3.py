from collections.abc import Iterable
from itertools import count

from county_demographics import *
from data import CountyDemographics

# Part 1

# Answer for population_total
def population_total(county_demographics: list[CountyDemographics]) -> float:
    if  county_demographics is None:
        return 0
    total = 0
    for county_demographic in county_demographics:
        total += county_demographic.population["2014 Population"]
    return total


#Fill out the following functions:

# Part 2

# returns a new list that has all the demographics in a given list that are from a given state
def filter_by_state(demographics: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    list_state = []
    for demographic in demographics:
        if demographic.state == state:
            list_state.append(demographic)
    return list_state




# Part 3

# returns the total population in a given list of demographics, which has at least a given education
def population_by_education(demographics: list[CountyDemographics],education_key: str ) -> float:
    return

# returns the total population fo a given ethnicity in a given list of demographics
def population_by_ethnicity(demographics: list[CountyDemographics],ethnicity_key: str ) -> float:
    return

# Part 4

# returns the percent of a population of given demographics which has at least a given education level
def percent_by_education(demographics: list[CountyDemographics], education_key: str) -> float:
    return

# returns the percent a population of given demographics which is below the poverty level
def percent_below_poverty_level(demographics: list[CountyDemographics]) -> float:
    return