# Answers


answers = {
           '001': '233168',
           '002': '4613732',
           '003': '6857',
           '004': '906609',
           '006': '25164150',
           '007': '104743',
           '008': '40824',
           '009': '31875000',
           '010': '142913828922',
           '011': '70600674',
           '016': '1366',
           '020': '648',
           '025': '4782',
           '040': '210'
           }


def get(prob_num):
    """
    Returns expected answer for PE problem
    Throws KeyError for missing answers
    """
    return answers[str(prob_num)]


if __name__ == '__main__':
    pass
