import numpy as np
import pickle

pipeline = pickle.load(open('./model.pkl', 'rb'))

example = {'income': 0,
 'educ': 0,
 'oftvote': 0,
 'age': 50,
 'retired': 0,
 'student': 0,
 'employed': 0,
 'sav': 0,
 'econ_ineq': 0,
 'int_con_1': 0,
 'local_1': 0,
 'glob_econ_1': 0,
 'econ_unf_1': 0,
 'pol_comp_1': 0,
 'clear_sol_1': 0,
 'sex_1': 0,
 'white': 0,
 'wlack': 0,
 'asian': 0,
 'race_other': 0,
 'native': 0,
 'protestant': 0,
 'roman Catholic': 0,
 'mormon': 0,
 'orth Chr': 0,
 'jewish': 0,
 'muslim': 0,
 'buddhist': 0,
 'hindu': 0,
 'atheist': 0,
 'agnostic': 0,
 'relig_Other': 0,
 'nothing': 0,
 'christian': 0,
 'unitarian': 0,
 'republican': 0,
 'democrat': 0,
 'independent': 0,
 'party_none': 0,
 'party_other': 0}


def make_prediction(features):
    X = np.array([features[key] for key in features.keys()]).reshape(1,-1)
    prob_engaged = pipeline.predict_proba(X)[0, 1]

    result = {
        'prediction': int(prob_engaged > 0.5),
        'prob_engaged': round(prob_engaged, 2)
    }
    return result

if __name__ == '__main__':
    print(make_prediction(example))
