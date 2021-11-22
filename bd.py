import datetime
import shuijishu
import card2


def sd():
    year = datetime.datetime.today().year

    year = str(year)
    bday=card2.yujin()
    with open(file="birthday.ics", encoding="utf8", mode="w") as file_object:
        start_string = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:" \
                       + "农历生日" + "\nX-WR-TIMEZONE:Asia/Shanghai\n" \
                       + "X-WR-CALDESC:"+year+"农历生日\n"
        file_object.write(start_string)

        body_string = ("BEGIN:VEVENT\nDTSTAMP:20190912T184136Z\nUID:",
                       "END:VEVENT\n")

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + bday + "\nDTEND;VALUE=DATE:" + bday + "\n"
        beizhu = "DESCRIPTION:" + year+"农历生日" + "\n"
        body3 = "SUMMARY:" + year+"农历生日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        end_string = "END:VCALENDAR"
        file_object.write(end_string)


if __name__ == '__main__':
    a=sd()
    print(a)
