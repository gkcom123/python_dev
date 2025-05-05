def life_in_weeks(age):
    life_in_week = (90 - age) * 52
    print(f"you have {life_in_week} weeks left.")


life_in_weeks(40)


def calculate_love_score(first_name, sec_name):
    final_letter = first_name.lower() + sec_name.lower()
    first_letter = 'true'
    second_letter = 'love'
    first_total_score = 0
    sec_tot_score = 0
    for let_1 in first_letter:
        first_total_score += final_letter.count(let_1.lower())
    for let_2 in second_letter:
        sec_tot_score += final_letter.count(let_2.lower())

    print(str(first_total_score) + "" + str(sec_tot_score))


calculate_love_score("Kanye West", "Kim Kardashian")
