from flask import Flask, render_template, request
from datetime import datetime, date

HIJRI_MONTH_NAMES = ["Muharram", "Safar", "Rabi' al-Awwal", "Rabi' al-Thani",
                      "Jumada al-Awwal", "Jumada al-Thani", "Rajab", "Sha'ban",
                      "Ramadan", "Shawwal", "Dhu al-Qi'dah", "Dhu al-Hijjah"]

def gregorian_to_jd(year, month, day):
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    return day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045

def jd_to_hijri(jd):
    jd = int(jd)
    l = jd - 1948440 + 10632
    n = (l - 1) // 10631
    l = l - 10631 * n + 354
    j = ((10985 - l) // 5316) * ((50 * l) // 17719) + (l // 5670) * ((43 * l) // 15238)
    l = l - ((30 - j) // 15) * ((17719 * j) // 50) - (j // 16) * ((15238 * j) // 43) + 29
    month = (24 * l) // 709
    day = l - (709 * month) // 24
    year = 30 * n + j - 30
    return year, month, day

def format_hijri(g_date):
    y, m, d = jd_to_hijri(gregorian_to_jd(g_date.year, g_date.month, g_date.day))
    m = max(1, min(12, m))
    return f"{d} {HIJRI_MONTH_NAMES[m - 1]} {y} AH"

app = Flask(__name__)

def get_zodiac_sign(day, month):
    zodiacs = [
        (1, 20, "Capricorn ♑", "Aquarius ♒"),
        (2, 19, "Aquarius ♒", "Pisces ♓"),
        (3, 21, "Pisces ♓", "Aries ♈"),
        (4, 20, "Aries ♈", "Taurus ♉"),
        (5, 21, "Taurus ♉", "Gemini ♊"),
        (6, 21, "Gemini ♊", "Cancer ♋"),
        (7, 23, "Cancer ♋", "Leo ♌"),
        (8, 23, "Leo ♌", "Virgo ♍"),
        (9, 23, "Virgo ♍", "Libra ♎"),
        (10, 23, "Libra ♎", "Scorpio ♏"),
        (11, 22, "Scorpio ♏", "Sagittarius ♐"),
        (12, 22, "Sagittarius ♐", "Capricorn ♑")
    ]
    for m, d, sign1, sign2 in zodiacs:
        if month == m:
            return sign1 if day < d else sign2
    return "Unknown"


def get_generation(year):
    """Return the generational label for a given birth year."""
    if year <= 1927:
        return "Greatest Generation"
    elif year <= 1945:
        return "Silent Generation"
    elif year <= 1964:
        return "Baby Boomer"
    elif year <= 1980:
        return "Generation X"
    elif year <= 1996:
        return "Millennial"
    elif year <= 2012:
        return "Generation Z"
    elif year <= 2025:
        return "Generation Alpha"
    else:
        return "Generation Beta"


@app.route('/', methods=['GET', 'POST'])
def home():
    results = None
    dob_val = ""  # Default empty so browser shows mm/dd/yyyy
    target_val = date.today().strftime("%Y-%m-%d")

    if request.method == 'POST':
        try:
            dob_str = request.form.get('dob')
            target_str = request.form.get('target_date')
            
            dob_val = dob_str
            target_val = target_str

            if not dob_str:
                return render_template('index.html', error="Please select a valid Date of Birth.", dob=dob_val, target=target_val)

            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
            target_date = datetime.strptime(target_str, "%Y-%m-%d").date()

            if dob > target_date:
                return render_template('index.html', error="Date of birth cannot be in the future!", dob=dob_val, target=target_val)

            # Age Calculation Logic
            years = target_date.year - dob.year
            months = target_date.month - dob.month
            days = target_date.day - dob.day

            if days < 0:
                months -= 1
                prev_month = target_date.month - 1 if target_date.month > 1 else 12
                prev_year = target_date.year if target_date.month > 1 else target_date.year - 1
                days_in_prev_month = (date(prev_year, prev_month % 12 + 1, 1) - date(prev_year, prev_month, 1)).days if prev_month != 12 else 31
                days += days_in_prev_month

            if months < 0:
                years -= 1
                months += 12

            # Conversions
            diff = target_date - dob
            total_days = diff.days
            total_weeks = total_days // 7
            rem_days_weeks = total_days % 7
            total_hours = total_days * 24
            total_minutes = total_hours * 60
            total_seconds = total_minutes * 60
            total_months = (years * 12) + months

            # Next Birthday
            next_birthday_year = target_date.year
            if (target_date.month, target_date.day) > (dob.month, dob.day):
                next_birthday_year += 1
            
            try:
                next_birthday = date(next_birthday_year, dob.month, dob.day)
            except ValueError:
                next_birthday = date(next_birthday_year, 2, 28)
                
            days_to_next_bday = (next_birthday - target_date).days
            bday_day_name = next_birthday.strftime("%A")

            results = {
                'years': years, 'months': months, 'days': days,
                'total_months': total_months, 'total_weeks': total_weeks, 'rem_days_weeks': rem_days_weeks,
                'total_days': f"{total_days:,}", 'total_hours': f"{total_hours:,}",
                'total_minutes': f"{total_minutes:,}", 'total_seconds': f"{total_seconds:,}",
                'born_day': dob.strftime("%A"),
                'zodiac': get_zodiac_sign(dob.day, dob.month),
                'generation': get_generation(dob.year),
                'next_bday_days': days_to_next_bday,
                'next_bday_day_name': bday_day_name,
                'is_today': target_str == date.today().strftime("%Y-%m-%d"),
                'raw_total_days': total_days,
                'raw_total_hours': total_hours,
                'raw_total_minutes': total_minutes,
                'raw_total_seconds': total_seconds,
            }

        except Exception as e:
            return render_template('index.html', error="Invalid date format provided.", dob=dob_val, target=target_val)

    return render_template('index.html', results=results, dob=dob_val, target=target_val)

if __name__ == '__main__':
    app.run(debug=True)