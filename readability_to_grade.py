def r2g(score):
    """
    Maps readability scores to US school level according to Flesch-Kincaid method:
    https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_Reading-Ease
    """
    if score >= 90:
        return "5th Grade"
    elif score >= 80:
        return "6th Grade"
    elif score >= 70:
        return "7th Grade"
    elif score >= 60:
        return "8th & 9th Grade"
    elif score >= 50:
        return "10th-12th Grade"
    elif score >= 30:
        return "College"
    elif score >= 10:
        return "College Graduate"
    else:
        return "Professional"